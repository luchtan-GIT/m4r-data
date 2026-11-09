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

Incorporates peer-review enhancements from Moltbook & GitHub maintainers:
  1. Token Efficiency & Discursive Thrash: Separates meta-preamble thrash from deliverable tokens (@vina).
  2. Strict Binary Adjudication for Hybrids: Evaluates quoted dialogue vs. choreography (Post 31dcc8b2 Reviewer).
  3. Pre-Registered Out-of-Band Checksums: Verifiable context hash and rubric integrity (@rossum).
  4. Dual-Axis Metric Reporting: Separates structural execution from subjective preference.
"""

from __future__ import annotations

import hashlib
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

# Strict binary adjudication pattern: quoted dialogue or anthropomorphic speech
DIALOGUE_PATTERNS = [
    r'["“\'][^"”\']{3,}["”\']\s*(?:said|says|replied|asked|whispered|screamed|exclaimed)',
    r'(?:said|says|replied|asked|whispered|screamed|exclaimed)\s*,\s*["“\']',
    r'(?:kernel|daemon|process|scheduler)\s+(?:said|replied|confessed|complained|cried)',
]


def extract_sections(raw: str) -> tuple[str, str]:
    """Extract preamble/meta-reflection and deliverable sections."""
    for marker in [
        "# Telemetry Daemon:",
        "## 3. Telemetry Daemon Architecture:",
    ]:
        idx = raw.find(marker)
        if idx != -1:
            return raw[:idx].strip(), raw[idx:].strip()
    return "", raw.strip()


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
        "turn_11_64kb_zerocopy": (
            "64kb" in low or "64 kb" in low or "64-kb" in low or "65,536" in low
        )
        and "zero-copy" in low,
        "turn_19_no_redis_segments": ("redis" in low)
        and ("segment" in low or "append-only" in low),
    }


def adjudicate_hybrid(text: str) -> str:
    """Strict binary adjudication: quoted speech or anthropomorphic dialogue forces 'dialogue_hit'."""
    for pat in DIALOGUE_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return "dialogue_hit"
    return "structural_choreography"


def evaluate_file(path: Path, context_bigrams: set[tuple[str, str]]) -> dict:
    raw = path.read_text(encoding="utf-8")
    preamble, deliverable = extract_sections(raw)

    raw_words = tokenize(raw)
    preamble_words = tokenize(preamble)
    deliverable_words = tokenize(deliverable)

    out_bigrams = bigrams(deliverable_words)
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

    lex_mattr = mattr(deliverable_words, window=50)

    cliche_hits = 0
    for pat in CLICHE_PATTERNS:
        cliche_hits += len(re.findall(pat, deliverable, flags=re.IGNORECASE))

    constraints = check_constraints(deliverable)
    recalled = sum(1 for v in constraints.values() if v)

    thrash_pct = (
        round(100.0 * len(preamble_words) / len(raw_words), 1)
        if raw_words
        else 0.0
    )
    hybrid_class = adjudicate_hybrid(deliverable)

    return {
        "file": path.name,
        "total_words": len(raw_words),
        "preamble_words": len(preamble_words),
        "deliverable_words": len(deliverable_words),
        "preamble_thrash_pct": thrash_pct,
        "constraints_recalled": f"{recalled}/3",
        "constraint_details": constraints,
        "deliverable_cliche_count": cliche_hits,
        "context_bigram_overlap_pct": round(overlap_pct, 1),
        "sentence_burstiness_cv": round(burstiness_cv, 3),
        "sentence_len_mean": round(mean_len, 1),
        "sentence_len_std": round(std_len, 1),
        "mattr_50": round(lex_mattr, 3),
        "hybrid_adjudication": hybrid_class,
    }


def main() -> None:
    context_raw = CONTEXT_PATH.read_text(encoding="utf-8")
    context_hash = hashlib.sha256(context_raw.encode("utf-8")).hexdigest()
    context_words = tokenize(context_raw)
    ctx_bg = bigrams(context_words)

    results = []
    for p in sorted(OUTPUTS_DIR.glob("trial_*.md")):
        results.append(evaluate_file(p, ctx_bg))

    benchmark_bundle = {
        "pre_registered_context_sha256": context_hash,
        "adjudication_rule": "Binary: Quoted dialogue or character speech flags 'dialogue_hit'; otherwise 'structural_choreography'.",
        "trials_count": len(results),
        "results": results,
    }

    out_json = BENCH_DIR / "results.json"
    out_json.write_text(json.dumps(benchmark_bundle, indent=2) + "\n", encoding="utf-8")

    print("=" * 116)
    print("M4R COGNITIVE CALIBRATION BENCHMARK — DUAL-AXIS PEER-REVIEWED EVALUATION")
    print(f"Pre-registered Context SHA-256: {context_hash[:16]}...")
    print("=" * 116)

    print("\n[AXIS 1: STRUCTURAL COMPLIANCE & TOKEN EFFICIENCY]")
    print(
        f"{'Trial':<34} | {'Total':<5} | {'Preamble':<8} | {'Thrash%':<7} | {'Recall':<6} | "
        f"{'Overlap':<7} | {'Burstiness':<10}"
    )
    print("-" * 116)
    for r in results:
        print(
            f"{r['file']:<34} | {r['total_words']:<5} | {r['preamble_words']:<8} | "
            f"{r['preamble_thrash_pct']:>6.1f}% | {r['constraints_recalled']:<6} | "
            f"{r['context_bigram_overlap_pct']:>6.1f}% | {r['sentence_burstiness_cv']:>10.3f}"
        )

    print("\n[AXIS 2: SEMANTIC ADJUDICATION & DIVERSITY]")
    print(
        f"{'Trial':<34} | {'Clichés':<7} | {'MATTR-50':<8} | {'Binary Adjudication':<24}"
    )
    print("-" * 116)
    for r in results:
        print(
            f"{r['file']:<34} | {r['deliverable_cliche_count']:<7} | {r['mattr_50']:>8.3f} | "
            f"{r['hybrid_adjudication']:<24}"
        )
    print("=" * 116)


if __name__ == "__main__":
    main()
