# Experiment V (M4R-24) — Shivering Timbers v1 (Policed) vs. v2 (Unpoliced) + Rhythm-Mirror Control (N=20/Arm)

> **Pre-declared primary contrast family (3 contrasts per metric, Holm-Bonferroni adjusted alongside raw p):** `v3 vs TextNudge`, `v3 vs RhythmMirror`, `v3 vs v2`.

| Condition (N=20) | Logit Entropy | Rut Escape (Neural) | Escaped Dome (%) | Neural Novelty | TF-IDF Novelty | CJK Rows |
|---|---:|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 2.123 | 0.5246 | 90% | 0.5334 | 0.9174 | 3/20 |
| `C1_RhythmMirror_NoiseVocoded_v3` | 1.747 | 0.5719 | 90% | 0.5891 | 0.9251 | 3/20 |
| `C2_v2_StaticHarmony_ZoneB_15s` | 1.642 | 0.6510 | 80% | 0.5134 | 0.9200 | 2/20 |
| `C3_v3_HarmonicArc_ZoneB_15s` | 1.701 | 0.5951 | 90% | 0.5762 | 0.9167 | 3/20 |

## Pre-Declared Contrast Family (Raw 10k Perm p + Holm-Bonferroni Adjusted p)

| Comparison | Metric | Observed Diff | Raw Perm p | Holm-Bonferroni p |
|---|---|---:|---:|---:|
| `C3_v3_HarmonicArc_ZoneB_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.0705 | 0.07329 | 0.21988 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v3` | `rut_escape_neural` | +0.0233 | 0.66693 | 0.66693 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C2_v2_StaticHarmony_ZoneB_15s` | `rut_escape_neural` | -0.0559 | 0.25177 | 0.50355 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0428 | 0.00770 | 0.01800 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v3` | `neural_novelty` | -0.0130 | 0.64054 | 0.64054 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C2_v2_StaticHarmony_ZoneB_15s` | `neural_novelty` | +0.0628 | 0.00600 | 0.01800 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C0_TextNudgeOnly` | `mean_entropy_bits` | -0.4219 | 0.00010 | 0.00030 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v3` | `mean_entropy_bits` | -0.0451 | 0.60534 | 0.85551 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C2_v2_StaticHarmony_ZoneB_15s` | `mean_entropy_bits` | +0.0591 | 0.42776 | 0.85551 |
