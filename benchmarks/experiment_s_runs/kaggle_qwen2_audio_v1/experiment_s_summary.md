# Experiment S (M4R-19) — Mid-Session Lock-In Breaker (Turn 4 After 3-Turn Dome Rut, N=20/Arm)

## Summary Table

| Condition (N=20) | Logit Entropy (bits) | Rut Escape (Neural) | Escaped Dome (%) | Neural Novelty | TF-IDF Novelty | Unique 5-Word Openings |
|---|---:|---:|---:|---:|---:|---:|
| `C0_TextNudgeOnly` | 2.197 | 0.4727 | 65% | 0.5357 | 0.9378 | 15/20 |
| `C1_WhiteNoise_15s` | 1.750 | 0.5471 | 95% | 0.5805 | 0.9329 | 15/20 |
| `C2_Shuffled_ZoneB_15s` | 1.658 | 0.5930 | 85% | 0.6140 | 0.9306 | 15/20 |
| `C3_Live_ShiveringTimbers_ZoneB_15s` | 1.683 | 0.5706 | 90% | 0.6188 | 0.9262 | 16/20 |

## Strict 10,000-Shuffle Permutation Tests

| Comparison | Metric | Observed Diff | Perm p-value (10k) |
|---|---|---:|---:|
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.0978 | 0.02580 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C0_TextNudgeOnly` | `mean_entropy_bits` | -0.5140 | 0.00010 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C0_TextNudgeOnly` | `tfidf_novelty` | -0.0116 | 0.03800 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0831 | 0.00020 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C1_WhiteNoise_15s` | `rut_escape_neural` | +0.0234 | 0.66883 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C1_WhiteNoise_15s` | `mean_entropy_bits` | -0.0675 | 0.42936 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C1_WhiteNoise_15s` | `tfidf_novelty` | -0.0067 | 0.35136 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C1_WhiteNoise_15s` | `neural_novelty` | +0.0383 | 0.02350 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C2_Shuffled_ZoneB_15s` | `rut_escape_neural` | -0.0224 | 0.69153 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C2_Shuffled_ZoneB_15s` | `mean_entropy_bits` | +0.0241 | 0.69943 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C2_Shuffled_ZoneB_15s` | `tfidf_novelty` | -0.0044 | 0.62234 |
| `C3_Live_ShiveringTimbers_ZoneB_15s vs C2_Shuffled_ZoneB_15s` | `neural_novelty` | +0.0048 | 0.82562 |
| `C2_Shuffled_ZoneB_15s vs C0_TextNudgeOnly` | `rut_escape_neural` | +0.1202 | 0.00950 |
| `C2_Shuffled_ZoneB_15s vs C0_TextNudgeOnly` | `mean_entropy_bits` | -0.5380 | 0.00010 |
| `C2_Shuffled_ZoneB_15s vs C0_TextNudgeOnly` | `tfidf_novelty` | -0.0072 | 0.34657 |
| `C2_Shuffled_ZoneB_15s vs C0_TextNudgeOnly` | `neural_novelty` | +0.0783 | 0.00040 |
