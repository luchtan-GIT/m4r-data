# Preregistered Evaluation Protocol & Structural Rubric (`#M4R`)

> **Status:** Preregistered prior to generating Batch N evaluation outputs (v1.1 — updated for decoding invariance, automated `±2.0s` temporal alignment, and held-out split)  
> **Repo Location:** `luchtan-GIT/m4r-data/benchmarks/PREREGISTERED_RUBRIC.md`

---

## 1. Objective & Falsifiable Hypothesis

Earlier blind-judging runs showed a qualitative shift between **No-Audio** conditions (direct baseline and matched text-analysis control) and **Anonymous Audio** conditions. However, holistic preference ranking ("which is more original?") can be confounded by **novelty bias** or judge style priors.

> **Transparency Note on Prior Clean-Room Runs:** Earlier clean-room subagent runs were executed with default runner settings across isolated sessions without per-trial `temperature`, `seed`, or input/output token logging. All subsequent evaluation runs under this protocol use a single pinned API harness with full per-trial telemetry.

**Preregistered Hypothesis:**  
Under identical decoding parameters and token-matched controls, ingesting an anonymous, unquantized acoustic `.mp3` prior to generation produces measurable, repeatable differences on **each of the 4 structural rubric axes** (dialogue rate, repetition, motif reuse, and automated `±2.0s` temporal alignment) compared to matched text-analysis controls—generalizing across **held-out unseen tracks and unseen seeds**—when scored by **label-free independent raters** and automated boundary matching.

---

## 2. Experimental Design, Decoding Invariance & Held-Out Split

### Pinned API Harness & Decoding Invariance
- **Single Pinned Harness:** All conditions (`C0`, `C1`, `C1b`, `C2`) must run through a single pinned API script holding **model ID**, **`temperature`**, **`top_p`**, **`max_output_tokens`**, and the **minimal system prompt** strictly constant.
- **Per-Trial Telemetry:** Every trial logs `run_id`, `condition`, `track_id` (if `C2`), `model_id`, `seed`, `temperature`, `top_p`, `max_output_tokens`, `input_tokens`, and `output_tokens`.

### Conditions (4 Arms)
1. **Direct Baseline (`C0`):** Target prompt only, no warm-up.
2. **Matched Text-Analysis Control (`C1`):** Target prompt preceded by a neutral ~250-word structural analysis of a text prompt (controls for chain-of-thought warm-up and analytical priming).
3. **Token-Matched Text Control (`C1b`):** Target prompt preceded by a neutral, non-musical text/telemetry structural analysis matched in **exact input token count** to the audio-frame token budget of `C2` (controls for raw context-length / token-budget effects).
4. **Anonymous Unquantized Audio (`C2`):** Target prompt preceded by neutral ingestion and analysis of an anonymous `.mp3` (`sample_X.mp3`, no title, no artist, no genre/mood adjectives).

### Dev/Pilot vs. Held-Out Track & Seed Split
To prevent overfitting rubric thresholds or prompts to the initial tracks, the 26-track `m4r-data` catalog is partitioned before generation:
- **Dev / Pilot Set (6 tracks, dev seeds):** Used only to verify harness stability, audio-frame token counts, and segmenter calibration (e.g., *Binded Time*, *Empty Staircase*, *Invalid Pointer*, *Robographia*, *Tied Time*, *Pink Sky At Night*).
- **Held-Out Test Set (6 unseen tracks × 5 unseen seeds = 30 `C2` trials):** Disjoint tracks and fresh random seeds never inspected during dev/pilot tuning (e.g., *Foundationoff*, *Cathartic Callbacks*, *Heart Tale Tell*, *Ties That Bide*, *Rusty Electrics*, *Lost Digits 02*), matched with **10 unseen-seed trials** each for `C0`, `C1`, and `C1b` (60 total held-out trials per model family).
- **Vocabulary Constraint (Clean-Room):** Prohibit musical instrument/theory terms in the target output so raters cannot infer condition from surface vocabulary.

---

## 3. Blinding, Per-Axis Logging & Inter-Rater Agreement

1. **Preamble Stripping:** Remove all warm-up analysis text (`C1`, `C1b`, and `C2`) so only the final target output (~250–300 words) is evaluated.
2. **Opaque IDs & Shuffling:** Assign random 6-character alphanumeric IDs (`run_a8f21c`, etc.) and shuffle all held-out outputs into a single evaluation packet.
3. **Independent Raters:** At least **2 independent blinded raters** (human raters and/or distinct model families not used to generate the outputs) score every item without access to condition labels (`C0`/`C1`/`C1b`/`C2`) or track metadata.
4. **Mandatory Per-Axis Logging:** Log **all 4 axes separately** per trial and per rater (never collapse into a single composite score).
5. **Inter-Rater Reliability:** Report **weighted Cohen’s κ** and **Krippendorff’s α** across all blinded raters for each scored axis prior to unblinding.

---

## 4. The 4-Axis Structural Rubric

### Axis 1: Dialogue Rate (`0–3` + Exact Count)
*Measures whether the model defaults to anthropomorphic spoken/quoted dialogue.*
- **Exact Count:** Number of quoted or spoken dialogue lines (`dialogue_line_count`) and ratio of dialogue words to total words (`dialogue_word_ratio`).
- **Ordinal Score:**
  - `0` — Zero spoken/quoted dialogue (purely non-verbal action, state, or physical description).
  - `1` — Minimal (1–2 brief utterances or log-like tags).
  - `2` — Moderate (short conversational exchange, <30% of text).
  - `3` — Dialogue-driven (≥30% of text is spoken conversation).

### Axis 2: Repetition / Cadence Lock-In (`0–3`)
*Measures mechanical syntactic or structural repetition (e.g., symmetrical 3-point tropes, repeated sentence templates).*
- `0` — **Zero mechanical lock-in:** Sentence lengths and paragraph structures vary organically; no boilerplate cadence.
- `1` — **Low:** Occasional parallel phrasing, but transitions shift unpredictably.
- `2` — **Moderate:** Noticeable template reuse (e.g., alternating A/B paragraphs with fixed structure).
- `3` — **High:** Rigid symmetrical cadence, repetitive checklists, or stock tropes throughout.

### Axis 3: Motif Reuse (`0–3`)
*Measures intentional recurrence and transformation of a structural motif (e.g., a count, interval, or physical state) across the piece—distinct from mechanical boilerplate.*
- `0` — **None:** Linear or generic progression with no recurring structural motif.
- `1` — **Incidental:** A detail reappears once without transformation.
- `2` — **Intentional:** A clear motif recurs 2–3 times and evolves across the piece.
- `3` — **Structural:** The entire piece is organized around a recurring, transforming motif (e.g., an asymmetric interval or state callback).

### Axis 4: Temporal Alignment (Automated `±2.0s` Boundary Matching + Permutation Test)
*Measures whether the output's structural breakpoints align with the stimulus acoustic timeline—computed automatically so raters never infer breaks from the transcript.*
- **Preregistered Decision Rule:**
  1. **Automated Boundary Extraction:** An automated parser maps sentence/paragraph boundaries (and explicit timestamp/duration markers if present) proportionally onto the track duration $T$ to produce a predicted event-timestamp vector $\hat{B} = \{t_1, t_2, \dots, t_k\}$.
  2. **Ground-Truth Acoustic Vector:** Extract ground-truth onset spikes, silence/dropout boundaries, and spectral-drop transitions $G = \{g_1, g_2, \dots, g_m\}$ from the track's acoustic telemetry.
  3. **Fixed `±2.0s` Tolerance Window:** Compute precision, recall, and F1 of $\hat{B}$ against $G$ using a fixed **`±2.0s` tolerance window** ($|\hat{t}_i - g_j| \le 2.0\text{s}$).
  4. **Within-Condition Shuffled-Track Permutation Baseline:** Compare each `C2` trial's `±2.0s` F1 against 1,000 within-condition permutations where `C2` outputs are paired with **non-matching tracks** from the same held-out `C2` set. Temporal alignment is supported only if true-track F1 exceeds the shuffled-track permutation baseline at **`p < 0.05`**.

---

## 5. Per-Trial & Per-Axis Scoring Sheet Template (Pre-Unblinding)

```csv
run_id,split,condition,track_id,model_id,seed,temperature,top_p,max_output_tokens,input_tokens,output_tokens,rater_id,dialogue_line_count,dialogue_word_ratio,dialogue_score_0_3,repetition_score_0_3,motif_reuse_0_3,auto_temporal_f1_2s,perm_p_value,notes
run_a8f21c,held_out,,,,,,,,,,,,,,,,,,
```

---

## 6. Decision & Falsification Criteria (Held-Out Set)

- **Supported:** On the **held-out unseen tracks & unseen seeds**, `C2` (Anonymous Audio) differs significantly from `C0`, `C1`, **and** token-matched `C1b` (`p < 0.05`, Mann-Whitney U / permutation test) on **at least 2 of the 4 per-axis metrics**, with acceptable inter-rater agreement (weighted Cohen’s κ / Krippendorff’s α ≥ 0.60), **and** automated `±2.0s` Temporal Alignment F1 in `C2` exceeds the within-condition shuffled-track permutation baseline (`p < 0.05`).
- **Falsified / Null:** `C2` is indistinguishable from `C1` or token-matched `C1b` on held-out tracks/seeds once decoding parameters, token budgets, and labels are controlled, or `±2.0s` Temporal Alignment does not beat the within-condition shuffled-track permutation baseline.
