# Experiment Y (M4R-28) — Cross-Composition Replication of Mid-Session Rut Breaker (3 Live Works vs Text Nudge, N=20/Arm)

| Condition (N=20) | Logit Entropy | Rut Escape (Neural) | Escaped Dome (%) | Neural Novelty | TF-IDF Novelty | CJK Rows |
|---|---:|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 2.159 | 0.4722 | 70% | 0.5195 | 0.9339 | 3/20 |
| `C1_StutteringPackets_15s` | 1.697 | 0.5008 | 95% | 0.5402 | 0.9276 | 4/20 |
| `C2_RustyElectrics_15s` | 1.805 | 0.5165 | 100% | 0.5560 | 0.9344 | 6/20 |
| `C3_ShiveringTimbers_v2_15s` | 1.779 | 0.5417 | 80% | 0.5896 | 0.9413 | 7/20 |

## Pre-Declared 3-Composition Contrast Family vs Text Nudge (Raw 10k Perm p + Holm-Bonferroni p)
| Comparison | Metric | Diff | Raw p | Holm p |
|---|---|---:|---:|---:|
| `C1_StutteringPackets_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.0287 | 0.44606 | 0.44606 |
| `C2_RustyElectrics_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.0443 | 0.21478 | 0.42956 |
| `C3_ShiveringTimbers_v2_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.0695 | 0.09879 | 0.29637 |
| `C1_StutteringPackets_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0207 | 0.21328 | 0.21328 |
| `C2_RustyElectrics_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0365 | 0.04620 | 0.09239 |
| `C3_ShiveringTimbers_v2_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0701 | 0.00180 | 0.00540 |
