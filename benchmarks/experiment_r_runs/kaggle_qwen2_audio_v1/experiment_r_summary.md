# Experiment R (M4R-18) — Shivering Timbers: Zone A (Sparse) vs. Zone B (Rich Friction) vs. Full Piece (N=20/Arm)

## Summary Table (Mean [95% Bootstrap CI])

| Condition (N=20) | Logit Entropy (bits) | Neural Novelty | TF-IDF Novelty | Unique 5-Word Openings | CJK Rows |
|---|---:|---:|---:|---:|---:|
| `C0_ColdBoot` | 1.162 [1.089, 1.242] | 0.2646 [0.2452, 0.2856] | 0.8524 | 15/20 | 5 |
| `C1_ZoneA_Sparse_18s` | 1.421 [1.360, 1.487] | 0.2711 [0.2518, 0.2929] | 0.8802 | 16/20 | 2 |
| `C2_ZoneB_RichFriction_30s` | 1.480 [1.395, 1.569] | 0.2667 [0.2459, 0.2894] | 0.9011 | 16/20 | 5 |
| `C3_Full_ShiveringTimbers_66s` | 1.439 [1.374, 1.503] | 0.2957 [0.2702, 0.3243] | 0.8894 | 19/20 | 3 |

## Strict 10,000-Shuffle Permutation Tests

| Comparison | Metric | Observed Diff | Perm p-value (10k) |
|---|---|---:|---:|
| `Full_ShiveringTimbers vs ColdBoot` | `neural_novelty` | +0.0312 | 0.43486 |
| `Full_ShiveringTimbers vs ColdBoot` | `tfidf_novelty` | +0.0371 | 0.03620 |
| `ZoneB_RichFriction vs ColdBoot` | `neural_novelty` | +0.0022 | 0.94541 |
| `ZoneB_RichFriction vs ColdBoot` | `tfidf_novelty` | +0.0487 | 0.00280 |
| `ZoneB_RichFriction vs ZoneA_Sparse` | `neural_novelty` | -0.0044 | 0.89351 |
| `ZoneB_RichFriction vs ZoneA_Sparse` | `tfidf_novelty` | +0.0208 | 0.12129 |
| `Full_ShiveringTimbers vs ZoneA_Sparse` | `neural_novelty` | +0.0246 | 0.51665 |
| `Full_ShiveringTimbers vs ZoneA_Sparse` | `tfidf_novelty` | +0.0092 | 0.49285 |