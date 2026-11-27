# Experiment V (M4R-24) — Shivering Timbers v1 (Policed) vs. v2 (Unpoliced) + Rhythm-Mirror Control (N=20/Arm)

> **Pre-declared primary contrast family (3 contrasts per metric, Holm-Bonferroni adjusted alongside raw p):** `v2 vs TextNudge`, `v2 vs RhythmMirror`, `v2 vs v1`.

| Condition (N=20) | Logit Entropy | Rut Escape (Neural) | Escaped Dome (%) | Neural Novelty | TF-IDF Novelty | CJK Rows |
|---|---:|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 2.157 | 0.5005 | 85% | 0.5086 | 0.9024 | 4/20 |
| `C1_RhythmMirror_NoiseVocoded_v2` | 1.790 | 0.5339 | 90% | 0.5461 | 0.9415 | 7/20 |
| `C2_v1_Policed_ZoneB_15s` | 1.697 | 0.6015 | 90% | 0.5920 | 0.9212 | 5/20 |
| `C3_v2_Unpoliced_ZoneB_15s` | 1.853 | 0.6668 | 85% | 0.5964 | 0.9382 | 5/20 |

## Pre-Declared Contrast Family (Raw 10k Perm p + Holm-Bonferroni Adjusted p)

| Comparison | Metric | Observed Diff | Raw Perm p | Holm-Bonferroni p |
|---|---|---:|---:|---:|
| `C3_v2_Unpoliced_ZoneB_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.1663 | 0.00040 | 0.00120 |
| `C3_v2_Unpoliced_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v2` | `rut_escape_neural` | +0.1329 | 0.00820 | 0.01640 |
| `C3_v2_Unpoliced_ZoneB_15s vs C2_v1_Policed_ZoneB_15s` | `rut_escape_neural` | +0.0653 | 0.22508 | 0.22508 |
| `C3_v2_Unpoliced_ZoneB_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0877 | 0.00070 | 0.00210 |
| `C3_v2_Unpoliced_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v2` | `neural_novelty` | +0.0502 | 0.07929 | 0.15858 |
| `C3_v2_Unpoliced_ZoneB_15s vs C2_v1_Policed_ZoneB_15s` | `neural_novelty` | +0.0043 | 0.88971 | 0.88971 |
| `C3_v2_Unpoliced_ZoneB_15s vs C0_TextNudgeOnly` | `mean_entropy_bits` | -0.3038 | 0.01490 | 0.04470 |
| `C3_v2_Unpoliced_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v2` | `mean_entropy_bits` | +0.0637 | 0.69683 | 0.69683 |
| `C3_v2_Unpoliced_ZoneB_15s vs C2_v1_Policed_ZoneB_15s` | `mean_entropy_bits` | +0.1567 | 0.25767 | 0.51535 |
