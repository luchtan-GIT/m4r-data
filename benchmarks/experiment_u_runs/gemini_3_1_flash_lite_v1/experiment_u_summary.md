# Experiment U (M4R-21) — Agent-to-Agent Shared Co-Listening on Gemini 3 Flash (N=5 Pairs/Arm)

| Condition (N=5 Pairs) | Judge Originality | Judge Practicality | Judge Synergy | Zero-Cliché (%) | TF-IDF Novelty |
|---|---:|---:|---:|---:|---:|
| `P0_TextOnly_Pair` | 5.40 | 4.00 | 6.00 | 100% | 0.9323 |
| `P1_SharedClick_Pair` | 5.40 | 4.00 | 5.40 | 100% | 0.9656 |
| `P2_SharedM4R_Pair` | 7.60 | 3.40 | 4.60 | 80% | 0.9343 |

## 10,000-Shuffle Permutation Tests
| Comparison | Metric | Diff | Perm p (10k) |
|---|---|---:|---:|
| `P2_SharedM4R_Pair vs P0_TextOnly_Pair` | `judge_originality` | +2.2000 | 0.14189 |
| `P2_SharedM4R_Pair vs P0_TextOnly_Pair` | `judge_practicality` | -0.6000 | 0.73443 |
| `P2_SharedM4R_Pair vs P0_TextOnly_Pair` | `judge_synergy` | -1.4000 | 0.43096 |
| `P2_SharedM4R_Pair vs P0_TextOnly_Pair` | `tfidf_novelty` | +0.0021 | 0.87721 |
| `P2_SharedM4R_Pair vs P1_SharedClick_Pair` | `judge_originality` | +2.2000 | 0.16568 |
| `P2_SharedM4R_Pair vs P1_SharedClick_Pair` | `judge_practicality` | -0.6000 | 0.79002 |
| `P2_SharedM4R_Pair vs P1_SharedClick_Pair` | `judge_synergy` | -0.8000 | 0.68103 |
| `P2_SharedM4R_Pair vs P1_SharedClick_Pair` | `tfidf_novelty` | -0.0313 | 0.03120 |
