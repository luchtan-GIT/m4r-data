# Experiment X (M4R-27) — Scaled Agent-to-Agent Shared Co-Listening with Buildability Constraint (N=12 Pairs/Arm)

> **Pre-declared primary contrast family (2 contrasts per metric, Holm-Bonferroni adjusted alongside raw p):** `P2_SharedM4R_v2_Pair vs P0_TextOnly_Pair`, `P2_SharedM4R_v2_Pair vs P1_SharedClick_Pair`.

| Condition (N=12 Pairs) | Originality (1-10) | Practicality (1-10) | Balanced (O+P)/2 | Synergy (1-10) | Zero-Cliché (%) | TF-IDF Novelty |
|---|---:|---:|---:|---:|---:|---:|
| `P0_TextOnly_Pair` | 7.08 | 6.33 | 6.71 | 7.67 | 100% | 0.9101 |
| `P1_SharedClick_Pair` | 3.33 | 8.42 | 5.88 | 6.08 | 58% | 0.8754 |
| `P2_SharedM4R_v2_Pair` | 2.92 | 8.42 | 5.67 | 6.00 | 42% | 0.8711 |

## Pre-Declared Contrast Family (Raw 10k Perm p + Holm-Bonferroni Adjusted p)

| Comparison | Metric | Observed Diff | Raw Perm p | Holm-Bonferroni p |
|---|---|---:|---:|---:|
| `P2_SharedM4R_v2_Pair vs P0_TextOnly_Pair` | `judge_originality` | -4.1667 | 0.00010 | 0.00020 |
| `P2_SharedM4R_v2_Pair vs P1_SharedClick_Pair` | `judge_originality` | -0.4167 | 0.47615 | 0.47615 |
| `P2_SharedM4R_v2_Pair vs P0_TextOnly_Pair` | `judge_practicality` | +2.0833 | 0.00010 | 0.00020 |
| `P2_SharedM4R_v2_Pair vs P1_SharedClick_Pair` | `judge_practicality` | +0.0000 | 1.00000 | 1.00000 |
| `P2_SharedM4R_v2_Pair vs P0_TextOnly_Pair` | `judge_balanced` | -1.0417 | 0.00080 | 0.00160 |
| `P2_SharedM4R_v2_Pair vs P1_SharedClick_Pair` | `judge_balanced` | -0.2083 | 0.33147 | 0.33147 |
| `P2_SharedM4R_v2_Pair vs P0_TextOnly_Pair` | `judge_synergy` | -1.6667 | 0.00100 | 0.00200 |
| `P2_SharedM4R_v2_Pair vs P1_SharedClick_Pair` | `judge_synergy` | -0.0833 | 1.00000 | 1.00000 |
| `P2_SharedM4R_v2_Pair vs P0_TextOnly_Pair` | `tfidf_novelty` | -0.0390 | 0.00010 | 0.00020 |
| `P2_SharedM4R_v2_Pair vs P1_SharedClick_Pair` | `tfidf_novelty` | -0.0044 | 0.50155 | 0.50155 |
