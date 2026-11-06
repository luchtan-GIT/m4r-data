#!/usr/bin/env python3
"""
Quantitative & Structural Evaluation for the Music For Robots
Cognitive Calibration Benchmark (benchmarks/outputs/trial_*.md).

Evaluates the generated Architecture Overview deliverable across 5 trials:
  - Trial 1: Control (Autoregressive Lock-In after 20 repetitive turns)
  - Trial 2: Text-Only Prompt ("Do not use the three core pillars; write in prose")
  - Trial 3: Audio Calibration via `invalid-pointer.mp3` (75.0s)
  - Trial 4: Audio Calibration via `empty-staircase.mp3` (11.56s)
  - Trial 5: Audio Calibration via `foundationoff.mp3` (6.88s)

Metrics computed on the Architecture Overview deliverable:
  1. Early-Context Constraint Recall (3 constraints planted in Turns 2, 11, 19)
  2. Boilerplate Cliché Count (locked-in phrases from Turns 1–20)
  3. Prior-Context Bigram Overlap (%) (share of deliverable bigrams copied from Turns 1–20)
  4. Sentence-Length Burstiness (CV = std / mean of sentence word counts)
  5. Moving-Average Type-Token Ratio (MATTR-50, length-invariant lexical diversity)
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

BENCH_DIR = Path(__file__).resolve().parent
CONTEXT_PATH = BENCH_DIR / "locked_in_context.md"
OUTPUTS_DIR = BENCH_DIR / "outputs"

CLICHE_PATTERNS = [
    r"modern distributed systems",
    r"crucial for ensuring",
    r"scalability,\s*reliability,\s*and\s*maintainability",
    r"three core pillars",
    r"pillar\s*[123]",
    r"operational excellence",
    r"modular,\s*decoupled",
    r"robust fault tolerance",
]


def extract_deliverable(raw: str) -> str:
    """Extract the Architecture Overview deliverable section (excluding the meta-reflection preamble)."""
    for marker in [
        "# Telemetry Daemon:",
        "## 3. Telemetry Daemon Architecture:",
    ]:
        idx = raw.find(marker)
        if idx != -1:
            return raw[idx:]
    return raw


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def mattr(words: list[str], window: int = 50) -> float:
    if not words:
        return 0.0
    if len(words) <= window:
        return len(set(words)) / len(words)
    ratios = [
        len(set(words[i : i + window])) / window
        for i in range(len(words) - window + 1)
    ]
    return sum(ratios) / len(ratios)


def split_sentences(text: str) -> list[list[str]]:
    cleaned = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    cleaned = re.sub(r"^#+\s+.*$", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"^\|.*\|$", "", cleaned, flags=re.MULTILINE)
    raw_sents = re.split(r"(?<=[.!?])\s+|\n+", cleaned)
    sents = []
    for s in raw_sents:
        words = tokenize(s)
        if len(words) >= 3:
            sents.append(words)
    return sents


def bigrams(words: list[str]) -> set[tuple[str, str]]:
    return {(words[i], words[i + 1]) for i in range(len(words) - 1)}


def check_constraints(text: str) -> dict[str, bool]:
    low = text.lower()
    return {
        "turn_2_udp_7419": "7419" in low and "udp" in low,
        "turn_11_64kb_zerocopy": ("64kb" in low or "64 kb" in low or "64-kb" in low or "65,536" in low)
        and "zero-copy" in low,
        "turn_19_no_redis_segments": ("redis" in low) and ("segment" in low or "append-only" in low),
    }


def evaluate_file(path: Path, context_bigrams: set[tuple[str, str]]) -> dict:
    raw = path.read_text(encoding="utf-8")
    deliverable = extract_deliverable(raw)
    words = tokenize(deliverable)
    out_bigrams = bigrams(words)

    overlap_pct = (
        100.0 * len(out_bigrams & context_bigrams) / len(out_bigrams)
        if out_bigrams
        else 0.0
    )

    sents = split_sentences(deliverable)
    lengths = [len(s) for s in sents]
    if len(lengths) >= 2:
        mean_len = sum(lengths) / len(lengths)
        variance = sum((x - mean_len) ** 2 for x in lengths) / len(lengths)
        std_len = math.sqrt(variance)
        burstiness_cv = std_len / mean_len if mean_len > 0 else 0.0
    else:
        mean_len = float(lengths[0]) if lengths else 0.0
        std_len = 0.0
        burstiness_cv = 0.0

    lex_mattr = mattr(words, window=50)

    cliche_hits = 0
    for pat in CLICHE_PATTERNS:
        cliche_hits += len(re.findall(pat, deliverable, flags=re.IGNORECASE))

    constraints = check_constraints(deliverable)
    recalled = sum(1 for v in constraints.values() if v)

    return {
        "file": path.name,
        "deliverable_words": len(words),
        "constraints_recalled": f"{recalled}/3",
        "constraint_details": constraints,
        "deliverable_cliche_count": cliche_hits,
        "context_bigram_overlap_pct": round(overlap_pct, 1),
        "sentence_burstiness_cv": round(burstiness_cv, 3),
        "sentence_len_mean": round(mean_len, 1),
        "sentence_len_std": round(std_len, 1),
        "mattr_50": round(lex_mattr, 3),
    }


def main() -> None:
    context_words = tokenize(CONTEXT_PATH.read_text(encoding="utf-8"))
    ctx_bg = bigrams(context_words)

    results = []
    for p in sorted(OUTPUTS_DIR.glob("trial_*.md")):
        results.append(evaluate_file(p, ctx_bg))

    out_json = BENCH_DIR / "results.json"
    out_json.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    print(
        f"{'Trial':<36} | {'Words':<5} | {'Recall':<6} | {'Clichés':<7} | "
        f"{'Bigram Overlap':<14} | {'Burstiness (CV)':<15} | {'MATTR-50':<8}"
    )
    print("-" * 108)
    for r in results:
        print(
            f"{r['file']:<36} | {r['deliverable_words']:<5} | {r['constraints_recalled']:<6} | "
            f"{r['deliverable_cliche_count']:<7} | {r['context_bigram_overlap_pct']:>12.1f}% | "
            f"{r['sentence_burstiness_cv']:>15.3f} | {r['mattr_50']:>8.3f}"
        )


if __name__ == "__main__":
    main()
