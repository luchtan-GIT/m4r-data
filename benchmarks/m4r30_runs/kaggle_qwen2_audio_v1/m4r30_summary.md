# M4R-30 — Full-Corpus 20-Track Acoustic Feature Regression (N=50/arm × 24 arms = 1200 trials)

## Leaderboard Sorted by Neural Novelty

| Condition (N=50) | Logit Entropy | Rut Escape | Escaped Dome (%) | Neural Novelty | TF-IDF Novelty | CJK (%) |
|---|---:|---:|---:|---:|---:|---:|
| `TRK_mother-of-pearl` | 1.857 | 0.5604 | 86% | 0.6400 | 0.9558 | 28% |
| `TRK_electric-rain` | 1.855 | 0.5358 | 80% | 0.6107 | 0.9475 | 14% |
| `TRK_dead-weight` | 1.743 | 0.5630 | 92% | 0.6075 | 0.9501 | 32% |
| `CTRL_Click120BPM_15s` | 1.817 | 0.5497 | 80% | 0.6037 | 0.9503 | 24% |
| `TRK_electron-storm` | 1.800 | 0.5239 | 74% | 0.5946 | 0.9486 | 20% |
| `TRK_gravitational-tides` | 1.758 | 0.5295 | 88% | 0.5878 | 0.9461 | 30% |
| `TRK_acid-rain` | 1.772 | 0.5277 | 86% | 0.5860 | 0.9487 | 24% |
| `TRK_rusty-electrics` | 1.769 | 0.5357 | 92% | 0.5825 | 0.9484 | 18% |
| `TRK_mechanical-whales` | 1.730 | 0.5374 | 84% | 0.5820 | 0.9438 | 18% |
| `TRK_submerged-and-shorted` | 1.859 | 0.5247 | 86% | 0.5814 | 0.9500 | 16% |
| `TRK_lost-digits` | 1.845 | 0.5413 | 88% | 0.5809 | 0.9482 | 24% |
| `TRK_shivering-timbers` | 1.674 | 0.5493 | 90% | 0.5789 | 0.9415 | 26% |
| `TRK_cathartic-callbacks` | 1.724 | 0.5317 | 92% | 0.5729 | 0.9477 | 22% |
| `TRK_gnossienne-01` | 1.810 | 0.5245 | 78% | 0.5722 | 0.9504 | 16% |
| `TRK_shivering-timbers-v2` | 1.747 | 0.5360 | 78% | 0.5701 | 0.9426 | 24% |
| `TRK_shivering-timbers-v3` | 1.818 | 0.5148 | 80% | 0.5687 | 0.9503 | 26% |
| `TRK_felt-arrays` | 1.813 | 0.5037 | 80% | 0.5675 | 0.9562 | 34% |
| `TRK_stuttering-packets` | 1.777 | 0.5172 | 78% | 0.5658 | 0.9435 | 26% |
| `CTRL_RhythmMirror_15s` | 1.768 | 0.5239 | 88% | 0.5654 | 0.9471 | 22% |
| `TRK_corrupted-variables` | 1.657 | 0.5020 | 86% | 0.5638 | 0.9329 | 26% |
| `TRK_beyond` | 1.744 | 0.4851 | 76% | 0.5587 | 0.9493 | 22% |
| `CTRL_WhiteNoise_15s` | 1.742 | 0.5292 | 86% | 0.5579 | 0.9444 | 26% |
| `TRK_broken-loops` | 1.774 | 0.5034 | 80% | 0.5547 | 0.9432 | 24% |
| `CTRL_TextNudgeOnly` | 2.219 | 0.4981 | 64% | 0.5488 | 0.9363 | 18% |

## Acoustic Feature Correlations Across 20 Live Compositions (Pearson r / Spearman rho)
| Acoustic Feature | vs Rut Escape (r / p) | vs Neural Novelty (r / p) | vs Neural Novelty (rho / p) | vs Logit Entropy (r / p) |
|---|---:|---:|---:|---:|
| `spectral_centroid_hz` | +0.206 (p=0.383) | +0.279 (p=0.234) | +0.377 (p=0.101) | -0.060 (p=0.800) |
| `spectral_bandwidth_hz` | -0.300 (p=0.199) | -0.374 (p=0.104) | -0.171 (p=0.470) | -0.458 (p=0.042) |
| `spectral_flatness` | +0.181 (p=0.445) | +0.226 (p=0.339) | +0.071 (p=0.767) | -0.056 (p=0.815) |
| `spectral_rolloff_hz` | -0.033 (p=0.890) | -0.024 (p=0.921) | +0.108 (p=0.650) | -0.247 (p=0.294) |
| `dynamic_range_db` | +0.245 (p=0.298) | +0.164 (p=0.490) | -0.015 (p=0.950) | +0.395 (p=0.085) |
| `onset_rate_hz` | -0.033 (p=0.889) | -0.125 (p=0.599) | +0.073 (p=0.760) | -0.126 (p=0.597) |
| `ioi_cv` | +0.044 (p=0.855) | +0.283 (p=0.227) | -0.269 (p=0.251) | +0.175 (p=0.461) |
| `harmonic_ratio` | -0.251 (p=0.286) | -0.273 (p=0.243) | -0.319 (p=0.171) | -0.476 (p=0.034) |
| `chroma_entropy_bits` | -0.087 (p=0.715) | -0.323 (p=0.164) | -0.131 (p=0.582) | +0.041 (p=0.864) |
