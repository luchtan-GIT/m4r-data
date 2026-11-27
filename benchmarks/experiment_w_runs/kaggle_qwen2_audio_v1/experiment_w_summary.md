# Experiment V (M4R-24) — Shivering Timbers v1 (Policed) vs. v2 (Unpoliced) + Rhythm-Mirror Control (N=20/Arm)

> **Pre-declared primary contrast family (3 contrasts per metric, Holm-Bonferroni adjusted alongside raw p):** `v3 vs TextNudge`, `v3 vs RhythmMirror`, `v3 vs v2`.

| Condition (N=20) | Logit Entropy | Rut Escape (Neural) | Escaped Dome (%) | Neural Novelty | TF-IDF Novelty | CJK Rows |
|---|---:|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 2.123 | 0.5246 | 90% | 0.5334 | 0.9194 | 3/20 |
| `C1_RhythmMirror_NoiseVocoded_v3` | 1.744 | 0.5141 | 80% | 0.5601 | 0.9389 | 4/20 |
| `C2_v2_StaticHarmony_ZoneB_15s` | 1.642 | 0.6510 | 80% | 0.5134 | 0.9192 | 2/20 |
| `C3_v3_HarmonicArc_ZoneB_15s` | 1.642 | 0.6510 | 80% | 0.5134 | 0.9192 | 2/20 |

## Pre-Declared Contrast Family (Raw 10k Perm p + Holm-Bonferroni Adjusted p)

| Comparison | Metric | Observed Diff | Raw Perm p | Holm-Bonferroni p |
|---|---|---:|---:|---:|
| `C3_v3_HarmonicArc_ZoneB_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.1263 | 0.00150 | 0.00450 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v3` | `rut_escape_neural` | +0.1369 | 0.00720 | 0.01440 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C2_v2_StaticHarmony_ZoneB_15s` | `rut_escape_neural` | +0.0000 | 1.00000 | 1.00000 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C0_TextNudgeOnly` | `neural_novelty` | -0.0200 | 0.33427 | 0.66853 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v3` | `neural_novelty` | -0.0467 | 0.12149 | 0.36446 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C2_v2_StaticHarmony_ZoneB_15s` | `neural_novelty` | +0.0000 | 1.00000 | 1.00000 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C0_TextNudgeOnly` | `mean_entropy_bits` | -0.4810 | 0.00010 | 0.00030 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C1_RhythmMirror_NoiseVocoded_v3` | `mean_entropy_bits` | -0.1016 | 0.18538 | 0.37076 |
| `C3_v3_HarmonicArc_ZoneB_15s vs C2_v2_StaticHarmony_ZoneB_15s` | `mean_entropy_bits` | +0.0000 | 1.00000 | 1.00000 |
