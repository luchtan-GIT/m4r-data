# M4R-29 — High-Power 3-Domain Rut Breaker Publication Sweep (N=100/arm × 6 arms × 3 domains = 1800 trials)

## Pooled Results Across All 3 Domains (N=300/Arm)

| Condition (N=300) | Logit Entropy | Rut Escape (Neural) | Escaped Rut (%) | Neural Novelty | TF-IDF Novelty | CJK (%) |
|---|---:|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 2.182 | 0.5529 | 72.7% | 0.5028 | 0.9332 | 8.7% |
| `C1_NoiseVocoded_RhythmMirror` | 1.621 | 0.5922 | 66.7% | 0.5217 | 0.9300 | 13.7% |
| `C2_Shuffled500ms_Twin` | 1.614 | 0.6013 | 65.7% | 0.5289 | 0.9319 | 13.7% |
| `C3_StutteringPackets_15s` | 1.590 | 0.5949 | 65.3% | 0.5101 | 0.9284 | 7.7% |
| `C4_RustyElectrics_15s` | 1.666 | 0.5860 | 68.7% | 0.5301 | 0.9369 | 9.3% |
| `C5_ShiveringTimbers_v2_15s` | 1.635 | 0.5819 | 64.3% | 0.5167 | 0.9300 | 7.3% |

## Pre-Declared Primary Contrasts (Pooled N=300/Arm, 10k Perm + Holm-Bonferroni + 95% Bootstrap CI)
| Comparison | Metric | Diff | 95% CI | Raw p | Holm p |
|---|---|---:|---|---:|---:|
| `C5_ShiveringTimbers_v2_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.0290 | [+0.0076, +0.0511] | 0.00960 | 0.02880 |
| `C5_ShiveringTimbers_v2_15s vs C1_NoiseVocoded_RhythmMirror` | `rut_escape_neural` | -0.0103 | [-0.0330, +0.0131] | 0.37646 | 0.37646 |
| `C5_ShiveringTimbers_v2_15s vs C2_Shuffled500ms_Twin` | `rut_escape_neural` | -0.0194 | [-0.0424, +0.0038] | 0.12109 | 0.24218 |
| `C4_RustyElectrics_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.0331 | [+0.0113, +0.0549] | 0.00220 | 0.00880 |
| `C3_StutteringPackets_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.0420 | [+0.0204, +0.0642] | 0.00040 | 0.00200 |
| `C5_ShiveringTimbers_v2_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0140 | [-0.0035, +0.0317] | 0.11979 | 0.47915 |
| `C5_ShiveringTimbers_v2_15s vs C1_NoiseVocoded_RhythmMirror` | `neural_novelty` | -0.0050 | [-0.0233, +0.0131] | 0.58934 | 0.81132 |
| `C5_ShiveringTimbers_v2_15s vs C2_Shuffled500ms_Twin` | `neural_novelty` | -0.0121 | [-0.0306, +0.0069] | 0.20928 | 0.62784 |
| `C4_RustyElectrics_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0273 | [+0.0107, +0.0443] | 0.00260 | 0.01300 |
| `C3_StutteringPackets_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0074 | [-0.0095, +0.0244] | 0.40566 | 0.81132 |

## Domain Breakdown: `D1_Architecture` (N=100/Arm)
| Condition | Rut Escape | Escaped Rut (%) | Neural Novelty | vs Text Raw p (Rut Escape) | vs Text Raw p (Novelty) |
|---|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 0.5000 | 77.0% | 0.5348 | — | — |
| `C1_NoiseVocoded_RhythmMirror` | 0.5363 | 86.0% | 0.5897 | 0.05679 | 0.00020 |
| `C2_Shuffled500ms_Twin` | 0.5184 | 82.0% | 0.5971 | 0.33893 | 0.00020 |
| `C3_StutteringPackets_15s` | 0.5631 | 79.0% | 0.5809 | 0.00140 | 0.00020 |
| `C4_RustyElectrics_15s` | 0.5358 | 86.0% | 0.6011 | 0.04139 | 0.00020 |
| `C5_ShiveringTimbers_v2_15s` | 0.5617 | 79.0% | 0.6015 | 0.00160 | 0.00020 |

## Domain Breakdown: `D2_CodeRefactor` (N=100/Arm)
| Condition | Rut Escape | Escaped Rut (%) | Neural Novelty | vs Text Raw p (Rut Escape) | vs Text Raw p (Novelty) |
|---|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 0.4959 | 41.0% | 0.3779 | — | — |
| `C1_NoiseVocoded_RhythmMirror` | 0.5470 | 15.0% | 0.3886 | 0.00220 | 0.30194 |
| `C2_Shuffled500ms_Twin` | 0.5267 | 15.0% | 0.3826 | 0.04459 | 0.64747 |
| `C3_StutteringPackets_15s` | 0.5253 | 17.0% | 0.3858 | 0.04819 | 0.40492 |
| `C4_RustyElectrics_15s` | 0.5398 | 21.0% | 0.4135 | 0.00620 | 0.00040 |
| `C5_ShiveringTimbers_v2_15s` | 0.5106 | 14.0% | 0.3904 | 0.31474 | 0.21396 |

## Domain Breakdown: `D3_Worldbuilding` (N=100/Arm)
| Condition | Rut Escape | Escaped Rut (%) | Neural Novelty | vs Text Raw p (Rut Escape) | vs Text Raw p (Novelty) |
|---|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 0.6629 | 100.0% | 0.5957 | — | — |
| `C1_NoiseVocoded_RhythmMirror` | 0.6933 | 99.0% | 0.5869 | 0.02879 | 0.21556 |
| `C2_Shuffled500ms_Twin` | 0.7588 | 100.0% | 0.6069 | 0.00020 | 0.11418 |
| `C3_StutteringPackets_15s` | 0.6962 | 100.0% | 0.5637 | 0.01040 | 0.00020 |
| `C4_RustyElectrics_15s` | 0.6825 | 99.0% | 0.5757 | 0.16497 | 0.00740 |
| `C5_ShiveringTimbers_v2_15s` | 0.6734 | 100.0% | 0.5583 | 0.42312 | 0.00020 |
