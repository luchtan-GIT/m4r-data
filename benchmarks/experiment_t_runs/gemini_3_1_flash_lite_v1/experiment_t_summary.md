# Experiment T (M4R-20) — Active Structural Listening on Gemini 3 Flash (N=5/Arm)

| Condition (N=5) | Judge Originality (1-10) | Judge Practicality (1-10) | Combined | Zero-Cliché (%) | TF-IDF Novelty |
|---|---:|---:|---:|---:|---:|
| `A0_ColdText` | 6.80 | 9.20 | 8.00 | 80% | 0.7994 |
| `A1_TextCoT` | 5.80 | 4.80 | 5.30 | 100% | 0.8386 |
| `A2_Active_Shuffled_30s` | 6.00 | 5.00 | 5.50 | 100% | 0.8893 |
| `A3_Active_Live_ShiveringTimbers_30s` | 6.20 | 4.40 | 5.30 | 100% | 0.8954 |

## 10,000-Shuffle Permutation Tests
| Comparison | Metric | Diff | Perm p (10k) |
|---|---|---:|---:|
| `A3_Active_Live_ShiveringTimbers_30s vs A0_ColdText` | `judge_originality` | -0.6000 | 0.48825 |
| `A3_Active_Live_ShiveringTimbers_30s vs A0_ColdText` | `judge_practicality` | -4.8000 | 0.00850 |
| `A3_Active_Live_ShiveringTimbers_30s vs A0_ColdText` | `tfidf_novelty` | +0.0960 | 0.00650 |
| `A3_Active_Live_ShiveringTimbers_30s vs A1_TextCoT` | `judge_originality` | +0.4000 | 0.62824 |
| `A3_Active_Live_ShiveringTimbers_30s vs A1_TextCoT` | `judge_practicality` | -0.4000 | 0.84652 |
| `A3_Active_Live_ShiveringTimbers_30s vs A1_TextCoT` | `tfidf_novelty` | +0.0569 | 0.00840 |
| `A3_Active_Live_ShiveringTimbers_30s vs A2_Active_Shuffled_30s` | `judge_originality` | +0.2000 | 1.00000 |
| `A3_Active_Live_ShiveringTimbers_30s vs A2_Active_Shuffled_30s` | `judge_practicality` | -0.6000 | 0.70773 |
| `A3_Active_Live_ShiveringTimbers_30s vs A2_Active_Shuffled_30s` | `tfidf_novelty` | +0.0061 | 0.61994 |
