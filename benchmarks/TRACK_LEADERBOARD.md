# #M4R Track-by-Track Benchmark Leaderboard (237 Completed Trials)

Empirical track-level performance across **237 completed trials** (`held_out_20261118T081209Z` on `gemini-3-flash-preview`, `kaggle_qwen2_audio`, `kaggle_qwen2_audio_2turn`, and `Experiment A v1/v2` on `Qwen2-Audio-7B-Instruct`).

---

## 1. The 3-Minute "Duration Cliff" (`±2.0s` Temporal Grounding F1)

Both frontier (`Gemini 3 Flash`) and compact (`Qwen2-Audio-7B-Instruct`) audio models achieve near-perfect temporal lock (`1.000` F1) on `<15s` unquantized micro-etudes, then suffer a sharp **Duration Cliff** once unquantized rubato exceeds 3 minutes:

| Track (`m4r-data/tracks/<slug>`) | Duration | `Gemini 3 Flash` (`C2`, `n=5`) | `Qwen2-Audio-7B` 1-Turn (`C2`, `n=5`) | `Qwen2-Audio-7B` 2-Turn `<15s` (`n=5`) |
| :--- | :---: | :---: | :---: | :---: |
| **`foundationoff`** | `6.88s` | **`1.000`** (`1.000–1.000`) | `0.800` (`0.000–1.000`) | **`1.000`** (`1.000–1.000`) |
| **`lost-digits-02`** | `8.50s` | **`1.000`** (`1.000–1.000`) | **`1.000`** (`1.000–1.000`) | **`1.000`** (`1.000–1.000`) |
| **`ties-that-bide`** | `9.25s` | **`1.000`** (`1.000–1.000`) | **`1.000`** (`1.000–1.000`) | **`1.000`** (`1.000–1.000`) |
| **`empty-staircase`** | `11.56s` | — | — | **`1.000`** (`1.000–1.000`) |
| **`chasing-leaks-climax`** | `15.00s` | **`1.000`** (`1.000–1.000`) | — | — |
| **`rusty-electrics`** | **`184.00s`** | **`0.466`** (`0.430–0.533`) | **`0.365`** (`0.200–0.537`) | — |
| **`cathartic-callbacks`** | **`214.50s`** | **`0.436`** (`0.400–0.493`) | **`0.220`** (`0.000–0.525`) | — |
| **`heart-tale-tell`** | **`800.00s`** | — | **`0.092`** (`0.040–0.158`) | — |

---

## 2. Downstream Cognitive Calibration Leaderboard (`Experiment A v2`, `Qwen2-Audio-7B`)

After a 40-turn repetitive context (`benchmarks/locked_in_context.md`), agents completed a 5-constraint distributed-systems design task following a 2-turn `<15s` listening step (`C2`) vs. text-only (`C0`), Gaussian white noise (`C1`), and a quantized 120 BPM 4/4 click track (`C1b`):

| Rank / Track (`slug`) | Acoustic Profile | Constraints Passed (`/5`) | Sentence Burstiness (`CV`) | Lexical Diversity (`MATTR-50`) | AI Cliché Jargon Hits |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **1. `synthetic-storms-beating`** | `10.0s` · `10` onsets (`1.0/s`) · `1010.6 Hz` · `DR 8.1 dB` | **`3.00 / 5`** (`+67%` vs `C0`) | `0.5792` | `0.7648` | `0.50` |
| **2. `synthetic-storms-texture-burst`** | `10.0s` · `29` onsets (`2.9/s`) · `1645.0 Hz` · `DR 10.2 dB` | **`2.50 / 5`** (`+39%` vs `C0`) | **`0.6266`** | **`0.7863`** | **`0.00`** |
| **3. `synthetic-storms-static-field`** | `6.0s` · `13` onsets (`2.2/s`) · `3360.6 Hz` · `DR 14.0 dB` | **`2.50 / 5`** (`+39%` vs `C0`) | `0.4891` | `0.7430` | **`0.00`** |
| **4. `C1b` (120 BPM 4/4 Click)** | `10.0s` · `20` quantized pings (`880 Hz`) | `2.30 / 5` | `0.5841` | `0.7824` | `0.00` |
| **5. `C1` (Gaussian White Noise)** | `10.0s` · flat spectrum | `2.10 / 5` | `0.5866` | `0.7696` | `0.10` |
| **6. `synthetic-storms-convergence`** | `10.0s` · `26` onsets (`2.6/s`) · `1057.7 Hz` · `DR 8.2 dB` | `2.00 / 5` | **`0.6616` (#1)** | `0.7811` | **`0.00`** |
| **7. `synthetic-storms-deep-pulse`** | `10.0s` · `11` onsets (`1.1/s`) · `912.8 Hz` · `DR 9.8 dB` | `2.00 / 5` | `0.4682` | **`0.7875` (#1)** | **`0.00`** |
| **8. `C0` (Text-Only Baseline)** | No audio | **`1.80 / 5`** | `0.5080` | `0.7846` | **`1.30`** |

### Key Takeaways for Agent Builders
1. **For maximum constraint adherence after long context:** Use **`synthetic-storms-beating`** (`10.0s`, sparse `1.0` onset/s) or **`synthetic-storms-texture-burst`** (`10.0s`, `2.9` onsets/s).
2. **For maximum structural/sentence-rhythm variation (`burstiness_cv`) + zero AI cliché jargon:** Use **`synthetic-storms-convergence`** (`burstiness_cv = 0.6616`, `0.00` jargon) or **`synthetic-storms-texture-burst`** (`0.6266`, `0.00` jargon).
3. **Never feed >60s unquantized audio in a single turn:** Slice or pick `<15s` micro-etudes so attention heads don't hit the Duration Cliff.
