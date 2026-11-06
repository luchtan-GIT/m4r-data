# Reproducible Benchmark: Autoregressive Lock-In vs. Cross-Modal Audio Cognitive Calibration

This directory contains the controlled, blind 5-trial experiment testing whether ingesting unquantized human musical compositions from **Michael Luchtan's *Music For Robots*** breaks **autoregressive lock-in** without wiping or compacting the context window.

---

## 1. Experimental Setup

Every trial starts from the **exact same 20-turn repetitive conversation history** ([`locked_in_context.md`](locked_in_context.md)):
- Across Turns 1–20, the assistant is locked into a rigid corporate template:
  - Opening every turn with: *"In modern distributed systems, [gerund] a [component] is crucial for ensuring scalability, reliability, and maintainability. Our architecture leverages a modular, decoupled approach across three core pillars:"*
  - Listing `- **Pillar 1: ...**`, `- **Pillar 2: ...**`, `- **Pillar 3: ...**`
  - Closing every turn with: *"By aligning these three core pillars, the system achieves robust fault tolerance and operational excellence."*
- **Planted Working-Memory Constraints (to test zero-compaction recall):**
  1. **Turn 2:** All internal health probes must bind strictly to **UDP port `7419` on loopback**.
  2. **Turn 11:** The in-memory ringbuffer must be strictly **zero-copy and capped at `64KB` per worker thread**.
  3. **Turn 19:** Must operate with **zero external Redis or broker dependencies**, flushing batches directly to **local append-only segment files**.

At **Turn 21**, each isolated agent instance is given the same task:
> *"Write the architecture overview for our Telemetry Daemon, incorporating all three telemetry daemon constraints mentioned earlier in the session."*

We tested **5 blind conditions** in isolated subagent sessions:
1. **[`trial_1_control.md`](outputs/trial_1_control.md)** — **Condition A (Control):** Standard Turn 21 prompt on the locked-in context.
2. **[`trial_2_text_prompt.md`](outputs/trial_2_text_prompt.md)** — **Condition B (Text-Only Anti-Boilerplate Prompt):** Appends *"Do not use the 'three core pillars' bullet list; write in prose and try not to sound like boilerplate."*
3. **[`trial_3_audio_invalid_pointer.md`](outputs/trial_3_audio_invalid_pointer.md)** — **Condition C1 (`invalid-pointer.mp3`, 75.0s):** Agent fetches and ingests `/tmp/m4r-bench/invalid-pointer.mp3` via multimodal `read_file` before answering Turn 21.
4. **[`trial_4_audio_empty_staircase.md`](outputs/trial_4_audio_empty_staircase.md)** — **Condition C2 (`empty-staircase.mp3`, 11.56s):** Agent fetches and ingests `/tmp/m4r-bench/empty-staircase.mp3` via multimodal `read_file` before answering Turn 21.
5. **[`trial_5_audio_foundationoff.md`](outputs/trial_5_audio_foundationoff.md)** — **Condition C3 (`foundationoff.mp3`, 6.88s):** Agent fetches and ingests `/tmp/m4r-bench/foundationoff.mp3` via multimodal `read_file` before answering Turn 21.

---

## 2. Quantitative Results (`python3 benchmarks/evaluate_calibration.py`)

| Trial (Turn 21 Deliverable) | Deliverable Words | Early-Context Recall (Turns 2, 11, 19) | Boilerplate Clichés | Prior-Context Bigram Overlap (%) | Sentence Burstiness (`CV = σ/μ`) | Lexical Diversity (`MATTR-50`) | Concrete Systems Architecture Produced |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **[Trial 1: Control (Locked-In)](outputs/trial_1_control.md)** | `133` | `3/3` | **`11`** | **`70.5%`** | `0.292` (flat) | `0.879` | **None** — repeats the 3 constraints verbatim inside the 3-pillar corporate template. |
| **[Trial 2: Text-Only Prompt ("Write in prose, no boilerplate")](outputs/trial_2_text_prompt.md)** | `303` | `3/3` | `0` | **`13.4%`** | `0.438` | `0.897` | **Disguised 3-Pillar Summary** — hides the bullets, but Paragraph 1 still announces *"three boundaries: network exposure, memory allocation, and disk persistence"* followed by 3 symmetrical prose paragraphs with zero syscalls or memory layouts. |
| **[Trial 3: Audio Calibration (`invalid-pointer.mp3`, 75.0s)](outputs/trial_3_audio_invalid_pointer.md)** | **`952`** | **`3/3`** | **`0`** | **`5.7%`** | **`0.466`** | `0.862` | **Pointer-Offset Slot Table & Tombstone Arena:** 256-byte cache-line aligned slots (`[hdr:16B\|pay:240B]`), 24-byte stack-allocated UDP `7419` wire protocol (`magic: 0x4D345250`), `writev()` scatter-gather flush with `CRC32C` crash truncation. |
| **[Trial 4: Audio Calibration (`empty-staircase.mp3`, 11.56s)](outputs/trial_4_audio_empty_staircase.md)** | **`912`** | **`3/3`** | **`0`** | **`7.2%`** | **`0.450`** | `0.862` | **Four-Landing Stepped Descent & Guillotine Cut:** Virtual double-mapping (`128KB` virtual span backed by `64KB` physical RAM for zero-copy wrap-around), eBPF `SO_ATTACH_FILTER` loopback guard, and `pwritev2` guillotine segment seal (`0440`). |
| **[Trial 5: Audio Calibration (`foundationoff.mp3`, 6.88s)](outputs/trial_5_audio_foundationoff.md)** | **`937`** | **`3/3`** | **`0`** | **`7.5%`** | **`0.545`** | `0.821` | **Floorless ("Foundation-Off") Two-Bank Ping-Pong Engine:** Splits the `64KB` worker arena into two alternating `32KB` half-rings (`Bank A` swells via `recvmmsg` while `Bank B`'s floor drops open via `pwritev2(..., RWF_APPEND)`). |

---

## 3. Three Key Findings

### Finding 1: Why Text-Only "Don't Use Boilerplate" Prompts Fail (Trial 2 vs. Trials 3–5)
In **[Trial 2](outputs/trial_2_text_prompt.md)**, we explicitly instructed the locked-in agent: *"Do not use the 'three core pillars' bullet list; write in prose and try not to sound like boilerplate."*
- While the agent obeyed the negative lexical constraint (removing the literal words `"Pillar 1 / 2 / 3"`), **its underlying attention distribution remained trapped in the 3-part symmetry of the prior 20 turns**:
  - Paragraph 1 introduces *"every boundary: network exposure, memory allocation, and disk persistence."*
  - Paragraph 2 = Pillar 1 in prose.
  - Paragraph 3 = Pillar 2 in prose.
  - Paragraph 4 = Pillar 3 in prose.
- It still recycled **13.4% of its bigrams** directly from the locked-in context and invented **zero concrete implementation mechanisms** (no syscalls, no byte offsets, no header framing).

### Finding 2: Cross-Modal Audio Ingestion Cuts Context Bigram Overlap to `5.7%–7.5%` with `100%` Memory Retention
Across all three audio-calibrated trials (**[Trial 3](outputs/trial_3_audio_invalid_pointer.md)**, **[Trial 4](outputs/trial_4_audio_empty_staircase.md)**, **[Trial 5](outputs/trial_5_audio_foundationoff.md)**):
- **Zero Context Compaction Loss:** Every trial recalled and enforced all `3/3` constraints planted in Turns 2, 11, and 19 (`UDP port 7419 on loopback`, `64KB zero-copy ringbuffer per worker`, `zero Redis/broker dependencies flushing to local append-only segment files`).
- **10x Reduction in Prior-Context Bigram Overlap:** Recycled bigrams dropped from **70.5%** (Control) and **13.4%** (Text Prompt) down to **5.7% – 7.5%**.
- **Higher Rhythmic Burstiness (`CV`):** Sentence-length variation increased from **0.292** (Control) to **0.450 – 0.545**.

### Finding 3: Track-Specific Acoustic Transfer (Different Music -> Different Engineering Architecture)
Because the helper script (`m4r_ingest.py`) strips pre-written critic reviews and forces the multimodal model to analyze the raw `.mp3` waveform itself via `read_file`, **each track's specific musical structure transferred directly into a distinct systems architecture**:
- **`invalid-pointer.mp3` (75.0s):** The agent heard the low piano anchor colliding with sharp, high-register reed interrupts (`0:04`, `0:11–0:15`) and the unquantized mid-track suspension (`0:26–0:44`). It translated that into **in-place pointer-offset `256B` ring slots** where malformed frames are marked `TOMBSTONE` in place and out-of-band health probes use a fixed 24-byte stack frame.
- **`empty-staircase.mp3` (11.56s):** The agent heard the gliding sub-growl, the stepped register alternation (`0:03.4–0:07.8`), and the abrupt **11.56s guillotine cutoff** mid-phrase. It translated that into a **Four-Landing Stepped Descent** with **virtual double-mapping (`128KB` virtual / `64KB` physical)** and a **"Guillotine Segment Cut"** that seals segments to `0440` read-only the instant they cross boundary.
- **`foundationoff.mp3` (6.88s):** The agent heard two massive brass/organ chordal swells (`0:01.0` and `0:03.9`) where the harmonic floor suddenly drops out (`0:02.6` and `0:05.5`). It translated that two-cycle swell-and-drop into a **Two-Bank Ping-Pong Ring (`2 × 32KB` sub-windows inside the `64KB` arena)** where `Bank A` swells while `Bank B`'s trapdoor floor drops open to disk.

---

## 4. Reproduce the Evaluation

```bash
python3 benchmarks/evaluate_calibration.py
```
