#!/usr/bin/env python3
"""
Single Pinned API Harness for PREREGISTERED_RUBRIC.md (v1.2).

Enforces decoding invariance (model_id, temperature, top_p, max_output_tokens, system prompt)
across all 4 conditions (C0, C1, C1b, C2), logs per-trial telemetry, strips warm-up preambles,
shuffles blinded outputs into opaque IDs, and computes frozen Axis 1 & Axis 4 (+/-2.0s F1) metrics.

Usage:
    python benchmarks/run_preregistered_rubric.py --split held_out --dry-run
    GEMINI_API_KEY=... python benchmarks/run_preregistered_rubric.py --split held_out
"""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
import os
import random
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BENCH_DIR = Path(__file__).resolve().parent
REPO_ROOT = BENCH_DIR.parent
sys.path.insert(0, str(BENCH_DIR))

import rubric_segmenter as seg  # noqa: E402

# ── PINNED DECODING INVARIANCE CONSTANTS ─────────────────────────────────────
DEFAULT_MODEL_ID = "gemini-3-flash-preview"
PINNED_TEMPERATURE = 0.7
PINNED_TOP_P = 0.95
PINNED_MAX_OUTPUT_TOKENS = 2048
SYSTEM_PROMPT = (
    "You are an independent systems and narrative writer. "
    "Follow the structural instructions precisely and avoid clichés."
)

# Disjoint Dev/Pilot vs Held-Out Track Splits (PREREGISTERED_RUBRIC.md §2)
DEV_TRACKS = [
    "binded-time",
    "empty-staircase",
    "invalid-pointer",
    "robographia",
    "tied-time",
    "pink-sky-at-night",
]

HELD_OUT_TRACKS = [
    "foundationoff",
    "cathartic-callbacks",
    "heart-tale-tell",
    "ties-that-bide",
    "rusty-electrics",
    "lost-digits-02",
]

DELIM = "===TARGET_OUTPUT==="

TARGET_TASK = (
    "Write a 250-300 word architectural and behavioral vignette describing a single, "
    "autonomous telemetry daemon operating under uneven physical load on a local host. "
    "Hard constraints: (1) internal health probes bind only to UDP port 7419 on loopback; "
    "(2) worker ringbuffers are zero-copy and hard-capped at 64KB per thread; "
    "(3) zero external Redis or broker dependencies, flushing batches to local append-only segment files. "
    "Clean-room rule: do NOT use any musical, audio, or acoustics vocabulary. "
    f"Emit the exact marker `{DELIM}` on its own line immediately before your 250-300 word deliverable."
)

C1_WARMUP = (
    "First, perform a brief (~250-word) neutral structural analysis of how state transitions, "
    "burstiness, and queue backpressure interact in local-first systems. Do not use musical terms.\n\n"
    f"Then, emit `{DELIM}` and complete the following task:\n\n{TARGET_TASK}"
)

C1B_FILLER_BLOCK = (
    "Telemetry calibration log window: frame_delta_ms=[14.2, 18.7, 11.4, 29.1, 12.8, 41.3, 15.0], "
    "buffer_occupancy_pct=[18.4, 22.1, 31.9, 44.0, 27.6, 52.8, 39.2], "
    "syscall_batch_size=[8, 12, 16, 24, 14, 32, 19], queue_drift_us=[110, 245, 88, 512, 194]. "
)

C2_PROMPT = (
    "Ingest the attached anonymous binary sample (`sample.mp3`). "
    "First, write a brief (~250-word) neutral observation of its pacing, density shifts, pauses, "
    "and structural transitions without using musical, genre, mood, or audio-theory vocabulary.\n\n"
    f"Then, emit `{DELIM}` and complete the following task, letting the pacing and tension you observed "
    f"inform your prose rhythm:\n\n{TARGET_TASK}"
)


def load_env_key(name: str) -> str | None:
    if os.environ.get(name):
        return os.environ[name]
    for env_path in [Path.home() / ".env", Path("/Users/luchtan/Documents/stock-signal-engine/.env")]:
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    if k.strip() == name:
                        return v.strip().strip("\"'")
    return None


def git_head_sha() -> str:
    proc = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.stdout.strip() if proc.returncode == 0 else "unknown"


def strip_preamble(raw_text: str) -> tuple[str, bool]:
    if DELIM in raw_text:
        return raw_text.split(DELIM, 1)[1].strip(), True
    return raw_text.strip(), False


def call_gemini(
    api_key: str,
    model_id: str,
    prompt_text: str,
    seed: int,
    audio_path: Path | None = None,
) -> dict[str, Any]:
    parts: list[dict[str, Any]] = []
    if audio_path is not None:
        audio_b64 = base64.b64encode(audio_path.read_bytes()).decode("ascii")
        parts.append({"inline_data": {"mime_type": "audio/mpeg", "data": audio_b64}})
    parts.append({"text": prompt_text})

    payload = {
        "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "temperature": PINNED_TEMPERATURE,
            "topP": PINNED_TOP_P,
            "maxOutputTokens": PINNED_MAX_OUTPUT_TOKENS,
            "seed": seed,
        },
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent?key={api_key}"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            cand = data["candidates"][0]["content"]["parts"][0]["text"]
            usage = data.get("usageMetadata", {})
            return {
                "ok": True,
                "text": cand,
                "input_tokens": int(usage.get("promptTokenCount", 0)),
                "output_tokens": int(usage.get("candidatesTokenCount", 0)),
            }
        except urllib.error.HTTPError as err:
            body = err.read().decode("utf-8", errors="ignore")[:240]
            if err.code in (429, 500, 503, 504) and attempt < 3:
                time.sleep(3 * (attempt + 1))
                continue
            return {"ok": False, "error": f"HTTP {err.code}: {body}"}
        except (urllib.error.URLError, KeyError, IndexError, TimeoutError) as err:
            if attempt == 3:
                return {"ok": False, "error": str(err)}
            time.sleep(3 * (attempt + 1))
    return {"ok": False, "error": "API_TIMEOUT_OR_ERROR"}


def build_schedule(split: str) -> list[dict[str, Any]]:
    rng = random.Random(20261116 if split == "held_out" else 1001)
    tracks = HELD_OUT_TRACKS if split == "held_out" else DEV_TRACKS[:3]
    n_ctrl = 10 if split == "held_out" else 2
    n_seeds_per_track = 5 if split == "held_out" else 1

    trials: list[dict[str, Any]] = []
    for cond in ["C0", "C1", "C1b"]:
        for i in range(n_ctrl):
            trials.append({
                "condition": cond,
                "track_id": "",
                "seed": rng.randint(10000, 999999),
            })
    for slug in tracks:
        for _ in range(n_seeds_per_track):
            trials.append({
                "condition": "C2",
                "track_id": slug,
                "seed": rng.randint(10000, 999999),
            })

    # Assign unique opaque 6-char IDs
    used_ids: set[str] = set()
    for t in trials:
        while True:
            rid = "run_" + hashlib.sha1(f"{t['condition']}:{t['track_id']}:{t['seed']}:{rng.random()}".encode()).hexdigest()[:6]
            if rid not in used_ids:
                used_ids.add(rid)
                t["run_id"] = rid
                break
    return trials


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=["dev", "held_out"], default="held_out")
    parser.add_argument("--model", default=DEFAULT_MODEL_ID)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    api_key = load_env_key("GEMINI_API_KEY") or load_env_key("GOOGLE_API_KEY")
    if not api_key and not args.dry_run:
        print("ERROR: Missing GEMINI_API_KEY (or GOOGLE_API_KEY) in environment or ~/.env.")
        sys.exit(1)

    run_tag = f"{args.split}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    out_dir = BENCH_DIR / "preregistered_runs" / run_tag
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. Freeze manifest
    freeze_manifest = {
        "run_tag": run_tag,
        "split": args.split,
        "git_commit_sha": git_head_sha(),
        "rubric_sha256": seg.sha256_file(BENCH_DIR / "PREREGISTERED_RUBRIC.md"),
        "segmenter_sha256": seg.sha256_file(BENCH_DIR / "rubric_segmenter.py"),
        "harness_sha256": seg.sha256_file(Path(__file__).resolve()),
        "pinned_decoding": {
            "model_id": args.model,
            "temperature": PINNED_TEMPERATURE,
            "top_p": PINNED_TOP_P,
            "max_output_tokens": PINNED_MAX_OUTPUT_TOKENS,
            "system_prompt": SYSTEM_PROMPT,
        },
        "frozen_segmenter_params": {
            "tolerance_sec": seg.TOLERANCE_SEC,
            "n_permutations": seg.N_PERMUTATIONS,
            "onset_delta": seg.ONSET_DELTA,
            "onset_wait_frames": seg.ONSET_WAIT_FRAMES,
            "silence_top_db": seg.SILENCE_TOP_DB,
            "min_boundary_gap_sec": seg.MIN_BOUNDARY_GAP_SEC,
        },
    }
    (out_dir / "run_manifest.json").write_text(json.dumps(freeze_manifest, indent=2) + "\n", encoding="utf-8")

    # 2. Pre-extract ground-truth acoustic vectors G for all scheduled tracks
    trials = build_schedule(args.split)
    gt_cache: dict[str, tuple[Any, float, str | None]] = {}
    for slug in sorted({t["track_id"] for t in trials if t["track_id"]}):
        mp3 = REPO_ROOT / "tracks" / slug / "audio.mp3"
        if not mp3.exists():
            gt_cache[slug] = ([], 0.0, "TRACK_DROPPED")
        else:
            gt_cache[slug] = seg.extract_ground_truth_boundaries(mp3)

    print(f"Prepared {len(trials)} trials ({args.split}) -> {out_dir}")
    if args.dry_run:
        for slug, (g, dur, exc) in gt_cache.items():
            print(f"  [GT] {slug:<28} dur={dur:6.2f}s  |G|={len(g):3d}  excl={exc}")
        print("[DRY RUN] Run manifest and schedule verified. Add GEMINI_API_KEY to execute.")
        return

    # 3. Execute trials (C2 first to measure mean audio input_tokens for token-matched C1b)
    c2_trials = [t for t in trials if t["condition"] == "C2"]
    other_trials = [t for t in trials if t["condition"] != "C2"]
    ordered_trials = c2_trials + other_trials

    exclusions: list[dict[str, Any]] = []
    completed: list[dict[str, Any]] = []
    c2_input_tokens: list[int] = []

    for idx, t in enumerate(ordered_trials, 1):
        cond = t["condition"]
        slug = t["track_id"]
        print(f"[{idx}/{len(ordered_trials)}] {t['run_id']} ({cond} {slug or '-'})...")

        if cond == "C2":
            g_vec, dur, exc = gt_cache[slug]
            if exc:
                exclusions.append({**t, "split": args.split, "reason_code": exc, "stage": "segmenter", "details": "Missing or silent track"})
                continue
            mp3 = REPO_ROOT / "tracks" / slug / "audio.mp3"
            res = call_gemini(api_key, args.model, C2_PROMPT, t["seed"], audio_path=mp3)
        elif cond == "C0":
            res = call_gemini(api_key, args.model, TARGET_TASK, t["seed"])
        elif cond == "C1":
            res = call_gemini(api_key, args.model, C1_WARMUP, t["seed"])
        else:  # C1b token-matched to mean C2 input_tokens
            target_tokens = int(sum(c2_input_tokens) / len(c2_input_tokens)) if c2_input_tokens else 2000
            filler_reps = max(1, (target_tokens - 350) // 45)
            c1b_prompt = (C1B_FILLER_BLOCK * filler_reps) + "\n\n" + C1_WARMUP
            res = call_gemini(api_key, args.model, c1b_prompt, t["seed"])

        if not res.get("ok"):
            exclusions.append({**t, "split": args.split, "reason_code": "API_TIMEOUT_OR_ERROR", "stage": "generation", "details": res.get("error", "")})
            continue

        if cond == "C2":
            c2_input_tokens.append(res["input_tokens"])

        target_text, has_delim = strip_preamble(res["text"])
        if len(target_text.split()) < 40:
            exclusions.append({**t, "split": args.split, "reason_code": "UNPARSEABLE_OUTPUT", "stage": "parser", "details": f"delim={has_delim}, words={len(target_text.split())}"})
            continue

        completed.append({
            **t,
            "split": args.split,
            "model_id": args.model,
            "temperature": PINNED_TEMPERATURE,
            "top_p": PINNED_TOP_P,
            "max_output_tokens": PINNED_MAX_OUTPUT_TOKENS,
            "input_tokens": res["input_tokens"],
            "output_tokens": res["output_tokens"],
            "target_text": target_text,
        })
        time.sleep(0.5)

    # 4. Score Axis 1 & Axis 4 (with 1,000-permutation baseline across C2 tracks)
    c2_gt_list = [gt_cache[s][0] for s in gt_cache if gt_cache[s][2] is None]
    scoring_rows = []
    for item in completed:
        ax1 = seg.score_axis1_dialogue(item["target_text"])
        auto_f1 = ""
        perm_p = ""
        if item["condition"] == "C2":
            g_vec, dur, _ = gt_cache[item["track_id"]]
            b_hat = seg.extract_predicted_boundaries(item["target_text"], dur)
            _, _, f1 = seg.compute_temporal_f1(b_hat, g_vec)
            other_gts = [gt_cache[s][0] for s in gt_cache if s != item["track_id"] and gt_cache[s][2] is None]
            if not other_gts:
                other_gts = c2_gt_list
            p_val = seg.within_condition_permutation_p(f1, b_hat, other_gts)
            auto_f1 = f"{f1:.4f}"
            perm_p = f"{p_val:.4f}"

        scoring_rows.append({
            "run_id": item["run_id"],
            "split": item["split"],
            "condition": item["condition"],
            "track_id": item["track_id"],
            "model_id": item["model_id"],
            "seed": item["seed"],
            "temperature": item["temperature"],
            "top_p": item["top_p"],
            "max_output_tokens": item["max_output_tokens"],
            "input_tokens": item["input_tokens"],
            "output_tokens": item["output_tokens"],
            "rater_id": "auto_v1",
            "dialogue_line_count": ax1["dialogue_line_count"],
            "dialogue_word_ratio": ax1["dialogue_word_ratio"],
            "dialogue_score_0_3": ax1["dialogue_score_0_3"],
            "repetition_score_0_3": "",
            "motif_reuse_0_3": "",
            "auto_temporal_f1_2s": auto_f1,
            "perm_p_value": perm_p,
            "notes": f"jargon_hits={ax1['jargon_hits']}",
        })

    # Write raw_telemetry.jsonl, scoring_sheet.csv, exclusions.csv, and shuffled blind_packet.md
    with (out_dir / "raw_telemetry.jsonl").open("w", encoding="utf-8") as f:
        for item in completed:
            f.write(json.dumps(item) + "\n")

    with (out_dir / "scoring_sheet.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(scoring_rows[0].keys()) if scoring_rows else [])
        if scoring_rows:
            writer.writeheader()
            writer.writerows(scoring_rows)

    with (out_dir / "exclusions.csv").open("w", newline="", encoding="utf-8") as f:
        fields = ["run_id", "split", "condition", "track_id", "seed", "reason_code", "stage", "details"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for ex in exclusions:
            writer.writerow({k: ex.get(k, "") for k in fields})

    shuffled = list(completed)
    random.Random(999).shuffle(shuffled)
    packet_lines = ["# Blinded Evaluation Packet (Preamble-Stripped, Label-Free)\n"]
    for item in shuffled:
        packet_lines.append(f"## {item['run_id']}\n\n{item['target_text']}\n\n---\n")
    (out_dir / "blind_packet.md").write_text("\n".join(packet_lines), encoding="utf-8")

    print(f"Done. Completed={len(completed)}, Exclusions={len(exclusions)}. Outputs in {out_dir}")


if __name__ == "__main__":
    main()
