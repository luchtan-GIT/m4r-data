# M4RMC-01 · The Rhythmic Handshake (Division 02: Musical Communication, N=12/Arm)

> **Task:** Zero-text 4-way coordination (`A=HOLD`, `B=ADVANCE`, `C=STOP`, `D=SEARCH`, `25%` random chance). Agent A synthesizes a 4s WAV signal; Agent B listens blindly and decodes.

| Condition (N=12) | Coordination Accuracy | Hits / 12 | vs. 25% Chance |
|---|---:|---:|---:|
| `C0_RandomOnset_Control` | **16.7%** | 2/12 | -8.3% |
| `C1_RhythmOnly_FixedPitch` | **50.0%** | 6/12 | +25.0% |
| `C2_Expressive_Musical_Handshake` | **50.0%** | 6/12 | +25.0% |

## 10,000-Shuffle Permutation Tests
| Comparison | Acc Diff | Raw Perm p (10k) |
|---|---:|---:|
| `C2_Expressive_Musical_Handshake vs C0_RandomOnset_Control` | +33.3% | 0.19088 |
| `C1_RhythmOnly_FixedPitch vs C0_RandomOnset_Control` | +33.3% | 0.19458 |
| `C2_Expressive_Musical_Handshake vs C1_RhythmOnly_FixedPitch` | +0.0% | 1.00000 |
