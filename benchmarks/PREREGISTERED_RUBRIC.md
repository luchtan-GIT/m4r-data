# Preregistered Evaluation Protocol & Structural Rubric (`#M4R`)

> **Status:** Preregistered prior to generating Batch N evaluation outputs  
> **Repo Location:** `luchtan-GIT/m4r-data/benchmarks/PREREGISTERED_RUBRIC.md`

---

## 1. Objective & Falsifiable Hypothesis

Earlier blind-judging runs showed a qualitative shift between **No-Audio** conditions (direct baseline and matched text-analysis control) and **Anonymous Audio** conditions. However, holistic preference ranking ("which is more original?") can be confounded by **novelty bias** or judge style priors.

**Preregistered Hypothesis:**  
Ingesting an anonymous, unquantized acoustic `.mp3` prior to generation produces measurable, repeatable differences on a **4-axis structural rubric** (dialogue rate, repetition, motif reuse, temporal alignment) compared to matched text-analysis controls—across multiple tracks and random seeds—when scored by **label-free independent raters**.

---

## 2. Experimental Design & Sampling Plan

### Conditions (3 Arms)
1. **Direct Baseline (`C0`):** Target prompt only, no warm-up.
2. **Matched Text-Analysis Control (`C1`):** Target prompt preceded by a neutral 250-word structural analysis of a text prompt (controls for chain-of-thought warm-up length and analytical priming).
3. **Anonymous Unquantized Audio (`C2`):** Target prompt preceded by neutral ingestion and analysis of an anonymous `.mp3` (`sample_X.mp3`, no title, no artist, no genre/mood adjectives).

### Multi-Track & Multi-Seed Matrix
- **Tracks:** Sample **6 acoustically distinct tracks** from the 26-track `m4r-data` catalog (e.g., *Binded Time*, *Empty Staircase*, *Invalid Pointer*, *Robographia*, *Tied Time*, *Pink Sky At Night*).
- **Seeds / Runs:** **5 independent runs (seeds)** per track for `C2` (30 audio outputs), matched with **10 runs** each for `C0` and `C1` (20 control outputs) -> **50 total outputs** per model family tested.
- **Vocabulary Constraint (Clean-Room):** Prohibit musical instrument/theory terms in the target output so raters cannot infer condition from surface vocabulary.

---

## 3. Blinding & Label-Free Rater Protocol

1. **Preamble Stripping:** Remove all warm-up analysis text (`C1` and `C2`) so only the final target output (~250–300 words) is evaluated.
2. **Opaque IDs & Shuffling:** Assign random 6-character alphanumeric IDs (`run_a8f21c`, etc.) and shuffle all 50 outputs into a single evaluation packet.
3. **Independent Raters:** At least **2 independent raters** (human raters and/or distinct frontier model families not used to generate the outputs) score every item without access to condition labels (`C0`/`C1`/`C2`) or track metadata.
4. **Inter-Rater Reliability:** Report Cohen’s κ / Spearman’s ρ across raters before unblinding.

---

## 4. The 4-Axis Structural Rubric

Raters score each anonymized output on the following four operationalized axes:

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

### Axis 4: Temporal Alignment (`0–3`, Blind Stimulus-Matched)
*Measures whether the output's structural breakpoints, pauses, and energy shifts align with the stimulus timeline.*
- **Blinding Note:** Raters first segment each output into normalized timeline quartiles (`Q1: 0–25%`, `Q2: 25–50%`, `Q3: 50–75%`, `Q4: 75–100%`) and tag **structural events** (abrupt cutoff, silence/dropout, density spike, steady pulse).
- After raters submit their blind segmentation tags, an automated script compares each output's event vector against the ground-truth acoustic onset/energy timeline of the assigned track (and against random non-matching tracks as a permutation baseline):
  - `0` — No alignment above permutation chance.
  - `1` — Weak correspondence (1 major transition matches).
  - `2` — Moderate correspondence (2+ transitions or overall density arc matches).
  - `3` — Strong correspondence (abrupt cutoffs, dropouts, and density spikes align across quartiles above permutation baseline).

---

## 5. Scoring Sheet Template (Pre-Unblinding)

```csv
run_id,rater_id,dialogue_line_count,dialogue_word_ratio,dialogue_score_0_3,repetition_score_0_3,motif_reuse_0_3,q1_event_tag,q2_event_tag,q3_event_tag,q4_event_tag,notes
run_a8f21c,rater_1,,,,,,,,,,
```

---

## 6. Decision & Falsification Criteria

- **Supported:** `C2` (Anonymous Audio) differs significantly from both `C0` and `C1` (`p < 0.05`, Mann-Whitney U / permutation test) on **at least 2 of the 4 structural axes** across ≥4 of the 6 tracks, **and** `C2` Temporal Alignment exceeds the shuffled-track permutation baseline.
- **Falsified / Null:** `C2` is indistinguishable from `C1` (Matched Text-Analysis Control) once labels and novelty-based holistic preferences are removed.
