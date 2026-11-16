#!/usr/bin/env python3
"""
Statistical Analyzer & Dual-Reporting Generator for PREREGISTERED_RUBRIC.md (v1.2).

Reads a run directory (`scoring_sheet.csv`, `exclusions.csv`, `run_manifest.json`),
computes per-axis comparisons (C2 vs C0, C1, C1b) via Mann-Whitney U / permutation test,
reports both exclusions-applied and intent-to-evaluate sensitivity checks, and writes RESULTS_REPORT.md.

Usage:
    python benchmarks/score_preregistered_rubric.py benchmarks/preregistered_runs/<run_tag>
"""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import mannwhitneyu


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def mean_std(vals: list[float]) -> str:
    if not vals:
        return "n/a"
    arr = np.asarray(vals, dtype=float)
    return f"{np.mean(arr):.3f} ± {np.std(arr):.3f} (n={len(arr)})"


def compare_groups(a: list[float], b: list[float]) -> str:
    if len(a) < 2 or len(b) < 2:
        return "n/a"
    stat, p = mannwhitneyu(a, b, alternative="two-sided")
    return f"U={stat:.1f}, p={p:.4f}"


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python benchmarks/score_preregistered_rubric.py <run_dir>")
        sys.exit(1)

    run_dir = Path(sys.argv[1]).resolve()
    manifest = json.loads((run_dir / "run_manifest.json").read_text(encoding="utf-8"))
    rows = load_csv(run_dir / "scoring_sheet.csv")
    exclusions = load_csv(run_dir / "exclusions.csv")

    by_cond: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in rows:
        by_cond[r["condition"]].append(r)

    lines = [
        f"# Preregistered Rubric Results — `{manifest['run_tag']}`",
        "",
        f"- **Split:** `{manifest['split']}`",
        f"- **Model:** `{manifest['pinned_decoding']['model_id']}` (temp={manifest['pinned_decoding']['temperature']}, top_p={manifest['pinned_decoding']['top_p']})",
        f"- **Git Commit SHA:** `{manifest['git_commit_sha']}`",
        f"- **Frozen Segmenter SHA-256:** `{manifest['segmenter_sha256'][:16]}...`",
        f"- **Completed Trials:** {len(rows)} | **Excluded Trials:** {len(exclusions)}",
        "",
        "## 1. Per-Axis Summary (Exclusions Applied)",
        "",
        "| Condition | N | Dialogue Ratio | Dialogue (0-3) | Repetition (0-3) | Motif Reuse (0-3) | Temporal F1 (±2.0s) |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    def col_vals(cond_rows: list[dict[str, str]], key: str) -> list[float]:
        return [float(r[key]) for r in cond_rows if r.get(key, "") != ""]

    for cond in ["C0", "C1", "C1b", "C2"]:
        cr = by_cond.get(cond, [])
        lines.append(
            f"| `{cond}` | {len(cr)} | {mean_std(col_vals(cr, 'dialogue_word_ratio'))} | "
            f"{mean_std(col_vals(cr, 'dialogue_score_0_3'))} | {mean_std(col_vals(cr, 'repetition_score_0_3'))} | "
            f"{mean_std(col_vals(cr, 'motif_reuse_0_3'))} | {mean_std(col_vals(cr, 'auto_temporal_f1_2s'))} |"
        )

    lines.extend(["", "## 2. Hypothesis Tests (`C2` vs Controls)", ""])
    c2 = by_cond.get("C2", [])
    for ctrl in ["C0", "C1", "C1b"]:
        cr = by_cond.get(ctrl, [])
        lines.append(f"### `C2` vs `{ctrl}`")
        for metric in ["dialogue_word_ratio", "dialogue_score_0_3", "repetition_score_0_3", "motif_reuse_0_3"]:
            lines.append(f"- `{metric}`: {compare_groups(col_vals(c2, metric), col_vals(cr, metric))}")
        lines.append("")

    # Intent-to-evaluate sensitivity check (impute excluded C2 temporal F1 = 0.0)
    c2_f1_applied = col_vals(c2, "auto_temporal_f1_2s")
    c2_excl = [e for e in exclusions if e.get("condition") == "C2"]
    c2_f1_ite = c2_f1_applied + [0.0] * len(c2_excl)
    lines.extend([
        "## 3. Intent-to-Evaluate Sensitivity Check",
        "",
        f"- **Exclusions Applied (`C2` Temporal F1):** {mean_std(c2_f1_applied)}",
        f"- **Intent-to-Evaluate (`C2` Temporal F1, excluded=0.0):** {mean_std(c2_f1_ite)}",
        "",
        "## 4. Exclusion Log",
        "",
        f"Total exclusions: **{len(exclusions)}** (see `exclusions.csv`).",
    ])

    report_path = run_dir / "RESULTS_REPORT.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {report_path}")


if __name__ == "__main__":
    main()
