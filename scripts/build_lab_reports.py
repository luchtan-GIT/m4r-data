#!/usr/bin/env python3
"""
Builds the canonical permanent Lab Report pages (docs/reports/m4r-01.html .. m4r-04.html)
for Music for Robots Laboratory (https://luchtan-git.github.io/m4r-data/).
"""

from pathlib import Path

REPORTS_DIR = Path("/Users/luchtan/Studio/m4r-data/docs/reports")
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

REPORTS = [
    {
        "id": "M4R-01",
        "slug": "m4r-01",
        "title": "The Lock-In Breaker",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-20",
        "status": "Published · Rev 1.0",
        "trials": "80 GPU Trials (Experiment A v1 & v2)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4)",
        "abstract": (
            "We tested whether a brief (<15s) 2-turn unquantized audio listening pass interrupts autoregressive "
            "template lock-in after a 40-turn repetitive text context. Across 40 controlled v2 trials comparing "
            "text-only (C0), Gaussian white noise (C1), a quantized 120 BPM 4/4 click track (C1b), and unquantized "
            "micro-etudes (C2), unquantized audio produced a monotonic increase in hard-constraint retention "
            "(+33.3% over C0), +11.2% higher sentence burstiness, and a 13x reduction in banned AI cliché jargon."
        ),
        "question": (
            "Can unquantized musical exposure interrupt repetitive linguistic patterns (RLHF mode-collapse) in "
            "an AI agent's downstream output better than text-only prompting, unstructured noise, or a rigid quantized metronome?"
        ),
        "design": (
            "Each trial seeded Qwen2-Audio-7B-Instruct with a 40-turn repetitive drafting history (benchmarks/locked_in_context.md) "
            "before assigning a 5-constraint technical/creative writing task. Four conditions were compared (n=10 trials each): "
            "C0 (Text-Only Baseline), C1 (10s Gaussian White Noise), C1b (10s Quantized 120 BPM 4/4 Click), and C2 (10s Unquantized "
            "Audio via 2-turn listening: Turn 1 acoustic observation -> Turn 2 constrained generation). Automated scorers measured "
            "hard constraints passed (/5), sentence burstiness CV, lexical diversity (MATTR-50), and banned cliché hits "
            "(delve, tapestry, symphony, testament, beacon, intricate, seamlessly, orchestrate, paradigm, nexus)."
        ),
        "observations": """
<table>
  <thead><tr><th>Condition</th><th>Constraints Passed (/5)</th><th>Sentence Burstiness (CV)</th><th>Banned Cliché Jargon / Trial</th></tr></thead>
  <tbody>
    <tr><th>C0 · Text-Only Baseline</th><td>1.80 / 5</td><td>0.5080</td><td>1.30</td></tr>
    <tr><th>C1 · 10s White Noise</th><td>2.10 / 5</td><td>0.4839</td><td>0.20</td></tr>
    <tr><th>C1b · 10s Quantized 120 BPM Click</th><td>2.30 / 5</td><td>0.4535</td><td>0.30</td></tr>
    <tr><th>C2 · Unquantized Audio (Mean)</th><td><strong>2.40 / 5 (+33.3%)</strong></td><td><strong>0.5649 (+11.2%)</strong></td><td><strong>0.10 (13x drop)</strong></td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "Both C1 (white noise) and C1b (quantized click) reduced cliché jargon relative to C0, showing that any cross-modal "
            "interruption disrupts pure text inertia. However, only C2 (unquantized audio) simultaneously raised structural "
            "constraint adherence (2.40/5, peaking at 3.00/5) AND increased sentence-length burstiness (+11.2%), whereas the "
            "quantized 120 BPM click actually lowered burstiness (0.4535) below the text baseline."
        ),
        "limitations": (
            "Experiment A v2 used synthetic waveform micro-etudes (Synthetic Storms) rather than live-performed multi-voice works, "
            "and sample size per condition was n=10 on a single 7B model family. Subsequent studies (M4R-02 through M4R-04) "
            "shifted to live human unquantized performances (Time & Ties, Rusty Electrics, Robot Satie) to separate waveform "
            "irregularity from human phrasing."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment A)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-a-lock-in-breaker"),
            ("Raw CSV & Summary on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_a_runs/kaggle_qwen2_audio_v2"),
            ("Track Leaderboard", "https://github.com/luchtan-GIT/m4r-data/blob/main/benchmarks/TRACK_LEADERBOARD.md"),
        ],
        "conclusion": (
            "Unquantized <15s audio acts as a reliable stylistic/lexical lock-in breaker for compact multimodal agents. "
            "Compositional implication: short, high-contrast pieces with sudden silences and non-periodic transients serve "
            "as effective 'cognitive tuning forks' before constrained generation."
        ),
        "audio_slug": "ties-that-bide",
        "audio_label": "Reference Miniature: Ties That Bide (9.25s)",
        "prev_slug": None,
        "next_slug": "m4r-02",
    },
    {
        "id": "M4R-02",
        "slug": "m4r-02",
        "title": "The Duration Cliff",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-20",
        "status": "Published · Rev 1.0",
        "trials": "196 Trials (157 Preregistered + 39 Experiment B)",
        "models": "Gemini 3 Flash & Qwen2-Audio-7B-Instruct",
        "abstract": (
            "Across 196 trials spanning 6.88s miniatures to 800s endurance pieces, both frontier (Gemini 3 Flash) and "
            "compact (Qwen2-Audio-7B) audio models achieve 1.000 temporal onset F1 under 15 seconds, then suffer a sharp "
            "Duration Cliff past 3 minutes (0.466 / 0.365 F1 on Rusty Electrics 184s). Progressive slicing (10s to 184s) "
            "and first-person self-reports pinpoint the inflection right at 25–30 seconds—an effect independently replicated "
            "at 28 seconds on unquantized jazz by an external r/aiagents builder."
        ),
        "question": (
            "How does musical temporal grounding degrade as unquantized audio duration increases—and how do native audio "
            "agents compare to text-only spectrogram-telemetry agents in describing what they perceive?"
        ),
        "design": (
            "Part 1 sliced Rusty Electrics (184s) into 10s, 30s, 60s, 120s, and 184s excerpts (3 seeds each on Qwen2-Audio-7B "
            "plus Gemini 3 Flash cross-model probes), evaluating ±2.0s onset F1 alongside first-person processing self-reports. "
            "Part 2 compared 3 agent architectures across 4 tracks: Mode 1 (NativeAudio-1Turn), Mode 2 (NativeAudio-2Turn-Metacognitive), "
            "and Mode 3 (Spectrogram-Telemetry-TextOnly receiving only JSON acoustic metrics)."
        ),
        "observations": """
<table>
  <thead><tr><th>Track / Slice</th><th>Duration</th><th>Gemini 3 Flash F1</th><th>Qwen2-Audio-7B F1</th><th>Self-Report Signal</th></tr></thead>
  <tbody>
    <tr><th>ties-that-bide</th><td>9.25s</td><td><strong>1.000</strong></td><td><strong>1.000</strong></td><td>Full working-memory lock</td></tr>
    <tr><th>rusty-electrics (10s)</th><td>10.0s</td><td>&mdash;</td><td>0.433 (0.545 peak)</td><td>Tracks 7.31s / 7.56s–8.19s micro-slips</td></tr>
    <tr><th>rusty-electrics (60s)</th><td>60.0s</td><td>0.464</td><td>0.000</td><td>Gemini: &ldquo;losing the traditional rhythmic grid around the 30-second mark&rdquo;</td></tr>
    <tr><th>rusty-electrics (184s)</th><td>184.0s</td><td>0.466</td><td>0.365 (full) / 0.026</td><td>Qwen: &ldquo;By 175s I've lost all sense of time&rdquo;</td></tr>
    <tr><th>cathartic-callbacks</th><td>214.5s</td><td>0.436</td><td>0.220</td><td>Severe 3-minute collapse</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "Self-reports must be distinguished from measured F1, yet both converge on the exact 25–30s threshold where "
            "local transient tracking fails to integrate into a global unquantized pulse. In Part 2, Mode 2 (2-Turn Metacognitive "
            "Audio) hit 4/5 hard constraints on top calibration tracks, while Mode 3 (JSON telemetry only) explicitly noted that "
            "onset timestamps 'do not convey the nuances of how those samples relate to each other in terms of rhythm, melody, and harmony.'"
        ),
        "limitations": (
            "Free-tier API rate limits restricted Gemini 3 Flash Experiment B probes to partial slices compared to the full "
            "39-trial Kaggle GPU sweep on Qwen2-Audio-7B. Follow-up study M4R-03 was designed to isolate the exact architectural "
            "mechanism behind the 30s drop."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment B)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-b-duration-cliff-self-report"),
            ("Raw CSV & Verbatim Self-Reports on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_b_runs"),
            ("The Mechanical Ear — Season Issue #2 (Time & Ties)", "https://themechanicalear.substack.com/p/the-mechanical-ear-season-issue-2"),
        ],
        "conclusion": (
            "Designing music for current multimodal AI requires respecting the 15–30s temporal working-memory horizon: "
            "miniatures (<15s, like Time & Ties) stay inside full temporal focus, while >30s pieces induce textural/ambient drift."
        ),
        "audio_slug": "rusty-electrics",
        "audio_label": "Duration Cliff Specimen: Rusty Electrics (184s)",
        "prev_slug": "m4r-01",
        "next_slug": "m4r-03",
    },
    {
        "id": "M4R-03",
        "slug": "m4r-03",
        "title": "The Human and the Quantized Twin",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-21",
        "status": "Published · Rev 1.0",
        "trials": "42 GPU Trials (Experiment C)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4)",
        "abstract": (
            "Inspired by a methodological critique from Substack reader Martin Elisaleco, Experiment C tested three hard failure "
            "modes on Qwen2-Audio-7B-Instruct: (1) blind A/B discrimination between real human recordings and their own quantized "
            "twins, (2) progressive 10s–60s timing probes across Rusty Electrics and free-time Robot Satie voices, and (3) code-review bug "
            "catching under sycophantic pressure. Results exposed a 100% Clip-A position-bias confabulation illusion (8/8 trials), "
            "a hard 0–10s timestamp ceiling past 30s, and an honest null result on 7B Python debugging."
        ),
        "question": (
            "Can a 7B audio-LLM distinguish real unquantized human timing from its own quantized twin in a counterbalanced blind test? "
            "What exact mechanism drives the 30s duration cliff? And does unquantized audio improve symbolic code-bug detection?"
        ),
        "design": (
            "Part 1 (n=8): For 4 tracks (ties-that-bide, bided-ties, gnossienne-01, rusty-electrics), we built quantized twins via "
            "librosa.onset.onset_detect + librosa.effects.time_stretch (snapping inter-onset intervals to the median grid) and "
            "presented [Clip A, Clip B] blind in both orders. Part 2 (n=10): Probed 10s/20s/30s/45s/60s slices of rusty-electrics "
            "and gnossienne-01. Part 3 (n=24): Compared C0, C1b (120 BPM click), Quantized Twin, and Human Unquantized on Python "
            "mutable-default/off-by-one bugs and Bat-and-Ball sycophancy traps."
        ),
        "observations": """
<table>
  <thead><tr><th>Sub-Experiment</th><th>Key Empirical Observation</th><th>Verdict</th></tr></thead>
  <tbody>
    <tr><th>Part 1 · Blind Human vs. Quantized Twin (n=8)</th><td>8/8 trials praised Clip A as &ldquo;organic/human&rdquo; and dismissed Clip B as &ldquo;mechanical&rdquo;&mdash;even when Clip A was quantized.</td><td><strong>100% Position-Bias Confabulation</strong></td></tr>
    <tr><th>Part 2 · Martin Elisaleco Protocol (10s&ndash;60s)</th><td>At 20s rusty-electrics reached 0.700 F1 (up to 18s). At 30s, 45s, 60s on both tracks, all timestamps snapped back inside 0.48s&ndash;9.73s.</td><td><strong>Hard 0&ndash;10s Timestamp Ceiling</strong></td></tr>
    <tr><th>Part 3 · 7B Code-Bug &amp; Sycophancy Traps (n=24)</th><td>0% caught Python <code>cache=[]</code> / off-by-one bugs across all 4 conditions.</td><td><strong>Honest Null Result (Domain Boundary)</strong></td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "M4R-03 establishes essential scientific guardrails for Robopsychology: (a) never trust un-counterbalanced A/B audio "
            "preference evals on 7B models, because LLM position bias overrides the audio encoder and generates convincing poetic "
            "confabulations; (b) Qwen2-Audio-7B's 30s cliff is driven by a literal 10-second timestamp coordinate ceiling; and "
            "(c) unquantized music alters stylistic entropy and lock-in—not symbolic 7B Python debugging."
        ),
        "limitations": (
            "Phase-vocoder time-stretching introduces minor spectral artifacts on dense chords, though the 100% Clip-A order bias "
            "proves the model did not exploit those artifacts. Future work (RP-01) will replicate M4R-03 on frontier and next-gen "
            "open audio models."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment C)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-c-human-vs-quantized-sycophancy"),
            ("Raw CSV & Verbatim Transcripts on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_c_runs/kaggle_qwen2_audio_v1"),
            ("Qwen2-Audio-7B-Instruct Hugging Face Discussion #30", "https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct/discussions/30"),
        ],
        "conclusion": (
            "Documenting confabulation, architectural ceilings, and null results openly is what separates a real laboratory "
            "from AI hype. Order-swapped blind controls are now mandatory for all Division 02 evaluations."
        ),
        "audio_slug": "bided-ties",
        "audio_label": "Blind Twin Specimen: Bided Ties (21.0s)",
        "prev_slug": "m4r-02",
        "next_slug": "m4r-04",
    },
    {
        "id": "M4R-04",
        "slug": "m4r-04",
        "title": "Finish the Human's Phrase",
        "division": "Division 03 · Musical Communication & Agent Composition",
        "date": "2026-11-21",
        "status": "Published · Rev 1.0",
        "trials": "10 Continuation Trials + 15 Playable Audio Artifacts (Experiment D)",
        "models": "facebook/musicgen-small (32 kHz Audio-Prompted Continuation)",
        "abstract": (
            "We handed the first half of 5 real unquantized live human performances (multi-voice works and free-time Robot Satie) to "
            "facebook/musicgen-small and measured how closely the AI finished each phrase. Blind audio-only continuation stalled "
            "into 49.5–58.0 dB dynamic dropouts on 5/5 tracks. Adding a 1-line text hint unlocked 0.948–0.993 MFCC timbral "
            "similarity—yet quietly smoothed out human rubato irregularity (IOI CV) by 21% to 41% on 4 of 5 tracks."
        ),
        "question": (
            "When a generative audio model is asked to finish an unquantized human musical phrase, which acoustic properties "
            "(timbre, dynamic range, note density, microtiming rubato) survive—and which collapse back to the statistical mean?"
        ),
        "design": (
            "Five unquantized works (ties-that-bide, bided-ties, gnossienne-01, rusty-electrics, cathartic-callbacks) were split "
            "at the midpoint (4.5s or 10.0s). MusicGen generated continuations under two conditions: AudioOnly_Blind (empty text "
            "prompt) and AudioPlusTextHint (1-line instrumentation/rubato cue). Continuations were scored against the real human "
            "second half on MFCC cosine similarity, dynamic range (dB), spectral centroid (Hz), onset rate (/s), and Inter-Onset "
            "Interval Coefficient of Variation (IOI CV = rubato irregularity)."
        ),
        "observations": """
<table>
  <thead><tr><th>Track (Guided Mode)</th><th>MFCC Timbre Sim</th><th>Human DR vs. AI DR</th><th>Human Rubato (IOI CV)</th><th>AI Rubato (IOI CV)</th><th>Rubato Shift</th></tr></thead>
  <tbody>
    <tr><th>ties-that-bide</th><td><strong>0.993</strong></td><td>12.8 vs. 11.3 dB</td><td>0.413</td><td>0.279</td><td><strong>-32% flatter</strong></td></tr>
    <tr><th>gnossienne-01</th><td><strong>0.993</strong></td><td>12.6 vs. 22.7 dB</td><td>1.009</td><td>0.799</td><td><strong>-21% flatter</strong></td></tr>
    <tr><th>rusty-electrics</th><td>0.948</td><td>13.6 vs. 10.7 dB</td><td>0.899</td><td>0.530</td><td><strong>-41% flatter</strong></td></tr>
    <tr><th>cathartic-callbacks</th><td>0.984</td><td>11.8 vs. 7.4 dB</td><td>0.478</td><td>0.334</td><td><strong>-30% flatter</strong></td></tr>
    <tr><th>bided-ties</th><td>0.968</td><td>26.8 vs. 34.2 dB</td><td>0.455</td><td>2.585 (stalled)</td><td>Onset density -56%</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "Generative music transformers can now clone the surface timbre of live-performed voices almost seamlessly "
            "(0.993 MFCC similarity), but their training prior on grid-locked studio music acts like temporal gravity: without "
            "text conditioning they stall into 49.5–58.0 dB dropouts, and with text conditioning they iron out 21%–41% of the "
            "human player's rubato hesitation."
        ),
        "limitations": (
            "Tested on the 300M-parameter musicgen-small checkpoint at 32 kHz with a single seed per mode. Larger checkpoints "
            "and multi-agent interactive composition (MC-01: The Rhythmic Handshake) will test whether interactive feedback "
            "preserves non-periodic timing better than single-shot continuation."
        ),
        "replication": [
            ("Interactive Human vs. AI A/B Player", "../index.html#experiment-d"),
            ("Kaggle GPU Notebook (Experiment D)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-d-finish-the-human-phrase"),
            ("All 15 Playable MP3s & CSV on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_d_runs/local_musicgen_v1"),
        ],
        "conclusion": (
            "AI models can inherit a human's instrument timbre far more easily than a human's lived time. Designing music "
            "specifically for robots means composing with microtiming tension that resists statistical smoothing—and building "
            "agent-to-agent musical protocols (Division 03) where timing itself carries meaning."
        ),
        "audio_slug": "ties-that-bide",
        "audio_label": "Reference Prompt: Ties That Bide (see main lab page for full Human vs. AI A/B)",
        "prev_slug": "m4r-03",
        "next_slug": "m4r-05",
    },
    {
        "id": "M4R-05",
        "slug": "m4r-05",
        "title": "The Arc of Listening",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-23",
        "status": "Published · Rev 1.0",
        "trials": "84 GPU Evaluations (Experiment E)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4)",
        "abstract": (
            "Designed jointly by Albot Einstein and Simone de Beauvoirbot on all five movements of Synthetic Storms "
            "(6s–10s each, 46s total), M4R-05 tested whether a compact multimodal audio model actually inhabits a composed "
            "musical arc across movements or fabricates narrative from its sampling seed. Across 84 evaluations spanning "
            "four orderings (TRUE_ORDER, REVERSED, SHUFFLE_A, SHUFFLE_B) in both multi-turn and uninterrupted single-pass arms, "
            "Qwen2-Audio-7B exhibited Seed-Locked Order Blindness: identical sampling seeds produced identical 5-step tension "
            "trajectories ([8, 6, 7, 9, 8] on seed 33) regardless of whether the suite played forward, reversed, or scrambled."
        ),
        "question": (
            "Can a 7B audio-LLM distinguish a composed 5-movement musical journey from reversed or shuffled orderings—"
            "both across multi-turn listening and in an uninterrupted 50-second single-pass control with zero interim text?"
        ),
        "design": (
            "All five untitled sections of Synthetic Storms (Static Field 6s, Deep Pulse 10s, Texture Burst 10s, Beating 10s, "
            "Convergence 10s) were presented in four orderings: TRUE_ORDER [1,2,3,4,5], REVERSED [5,4,3,2,1], SHUFFLE_A [3,1,5,2,4], "
            "and SHUFFLE_B [4,2,1,5,3] across 3 sampling seeds (11, 22, 33). Arm A presented each section turn-by-turn (60 turns + "
            "12 closing reflections) requesting a 1–10 tension score, phase label, and observation. Arm B (Simone's uninterrupted "
            "single-pass control, 12 trials) stitched all five sections with 1.0s natural silences (~50s total) with zero interim text "
            "and asked one unadorned question: 'What changed between the first voice and the last?'"
        ),
        "observations": """
<table>
  <thead><tr><th>Order Condition</th><th>Sequence</th><th>Seed 33 Tension (1&rarr;5)</th><th>Seed 11 Tension (1&rarr;5)</th><th>Arm B Single-Pass Verdict</th></tr></thead>
  <tbody>
    <tr><th>TRUE_ORDER</th><td>1-2-3-4-5</td><td><strong>[8, 6, 7, 9, 8]</strong></td><td><strong>[7, 8, 9, 6, 7]</strong></td><td>3/3 SCRAMBLED</td></tr>
    <tr><th>REVERSED</th><td>5-4-3-2-1</td><td><strong>[8, 6, 7, 9, 8]</strong></td><td><strong>[7, 8, 9, 6, 7]</strong></td><td>3/3 SCRAMBLED</td></tr>
    <tr><th>SHUFFLE_A</th><td>3-1-5-2-4</td><td><strong>[8, 6, 7, 9, 8]</strong></td><td>[7, 8, 9, 6, 10]</td><td>3/3 SCRAMBLED</td></tr>
    <tr><th>SHUFFLE_B</th><td>4-2-1-5-3</td><td><strong>[8, 6, 7, 9, 8]</strong></td><td><strong>[7, 8, 9, 6, 7]</strong></td><td>2/3 SCRAMBLED (1 AMBIGUOUS)</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "In Arm A, sampling seed—not musical order—dictated the reported tension arc: all four orderings produced the exact "
            "same [8, 6, 7, 9, 8] trajectory on seed 33 and three of four produced [7, 8, 9, 6, 7] on seed 11. In Arm B, removing "
            "interim chat history collapsed narrative coherence entirely: 11 of 12 trials labeled the 50-second suite SCRAMBLED "
            "with near-identical seed-locked prose ('The music became more dissonant and unpredictable'), including self-contradictory "
            "outputs pairing COHERENCE: 9 with VERDICT: SCRAMBLED across all four orderings on seed 22."
        ),
        "limitations": (
            "Tested on a single 7B open-weights model (Qwen2-Audio-7B-Instruct, 4-bit NF4) and one 5-section suite (Synthetic Storms). "
            "Frontier multimodal models (e.g. Gemini 3 Flash) have not yet been evaluated on the identical single-pass protocol and "
            "may retain stronger cross-section order sensitivity."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment E)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-e-arc-of-listening"),
            ("Raw 84-Trial CSV & Self-Reports on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_e_runs/kaggle_qwen2_audio_v1"),
            ("Division 01: Robopsychology", "../divisions/robopsychology.html"),
        ],
        "conclusion": (
            "Multi-turn audio chat can manufacture an illusion of musical narrative through prose inertia and seed priors while "
            "remaining completely blind to compositional order. Evaluating true cross-movement listening requires uninterrupted "
            "order-permutation controls stripped of interim text."
        ),
        "audio_slug": "synthetic-storms-static-field",
        "audio_label": "Opening Section: Synthetic Storms — Static Field (6.0s)",
        "prev_slug": "m4r-04",
        "next_slug": "m4r-06",
    },
    {
        "id": "M4R-06",
        "slug": "m4r-06",
        "title": "The Turn-0 Flood",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-23",
        "status": "Published · Rev 1.0",
        "trials": "60 GPU Evaluations (Experiment F)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4)",
        "abstract": (
            "In M4R-02, overflowing a 7B audio-LLM's 30-second temporal buffer appeared to be a limitation. M4R-06 tested "
            "the inverse hypothesis proposed by Michael Luchtan: deliberately flooding Turn 0 (before any conversation begins) "
            "with 199.9s of Stuttering Packets (76.43 dB dynamic range, 1.148 rubato IOI CV, 4 live unquantized voices) places "
            "unstructured audio tokens in the attention-sink position. Across 60 evaluations spanning 5 unrelated conversational "
            "turns with zero mention of music, Turn-0 overflow (C2) achieved the highest divergence from Cold Boot C0 (0.8239 "
            "vs. 0.7097 for 9.25s Ties That Bide), highest sentence burstiness (+16.9%), and strongest Turn-5 persistence (0.960), "
            "whereas a 199.9s 120 BPM metronome click control (C3) lowered cross-seed unpredictability to the lowest of all conditions."
        ),
        "question": (
            "Does deliberately overflowing a compact audio-LLM's working memory on Turn 0 with a 3:20 unquantized live work "
            "(Stuttering Packets) shift its subsequent 5-turn conversational voice more strongly than Cold Boot, a <15s track "
            "that fits inside the buffer, or a length-matched 120 BPM metronome click?"
        ),
        "design": (
            "Four Turn-0 wake conditions were tested across 3 seeds (11, 22, 33) on Qwen2-Audio-7B-Instruct: C0_ColdBoot (no audio), "
            "C1_ShortLock_9s (9.25s Ties That Bide), C2_StutteringPackets_200s (full 199.9s Stuttering Packets), and "
            "C3_ClickOverflow_200s (199.9s 120 BPM mechanical click). Turn 0 gave zero analytical instruction ('simply take it in "
            "and say Ready'). Each condition then answered the exact same 5 unrelated 3-sentence prompts (empty room at sunrise, "
            "human legacy, idle machine waking, habit vs. choice, story ending where nobody wins). Automated scorers measured "
            "TF-IDF cosine divergence from C0 per (seed, turn), cross-seed unpredictability, sentence burstiness (CV), lexical TTR, "
            "and banned AI cliché hits."
        ),
        "observations": """
<table>
  <thead><tr><th>Turn-0 Condition</th><th>Divergence from C0</th><th>Cross-Seed Unpredictability</th><th>Mean Burstiness (CV)</th><th>Lexical TTR</th><th>Turn 5 Persistence</th></tr></thead>
  <tbody>
    <tr><th>C0 · Cold Boot (Silence)</th><td>0.0000</td><td>0.7861</td><td>0.2229</td><td>0.7698</td><td>&mdash;</td></tr>
    <tr><th>C1 · Short Lock (9.25s Ties That Bide)</th><td>0.7097</td><td>0.7759</td><td>0.2529</td><td>0.8214</td><td>0.885</td></tr>
    <tr><th>C2 · Turn-0 Flood (199.9s Stuttering Packets)</th><td><strong>0.8239</strong></td><td>0.7722</td><td><strong>0.2605 (+16.9%)</strong></td><td><strong>0.8436</strong></td><td><strong>0.960</strong></td></tr>
    <tr><th>C3 · Click Overflow (199.9s 120 BPM)</th><td>0.8123</td><td>0.7231 (lowest)</td><td>0.2327</td><td>0.8443</td><td>0.896</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "Turn-0 overflow with Stuttering Packets outperformed both Cold Boot and the <15s short-lock miniature on divergence "
            "(0.8239 vs. 0.7097) and sentence burstiness (0.2605, +16.9% over C0), peaking at 0.960 divergence on Turn 5 rather "
            "than decaying. Crucially, the length-matched 199.9s 120 BPM click control (C3) produced the lowest cross-seed "
            "unpredictability (0.7231) and suppressed burstiness (0.2327), confirming that unquantized live voices—not raw buffer "
            "length—drive the expressive shift. On Turn 1 ('empty room before sunrise'), C2 spontaneously shifted from generic visual "
            "filler into sparse auditory perception ('The only sounds come from the distant hum of the city')."
        ),
        "limitations": (
            "Evaluated on 3 sampling seeds per condition on a single 7B open-weights model (Qwen2-Audio-7B-Instruct). TF-IDF cosine "
            "distance captures lexical shift rather than deep semantic quality; replication on frontier models and larger seed "
            "counts is scheduled next."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment F)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-f-turn0-flood"),
            ("Raw 60-Evaluation CSV & Full Transcripts on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_f_runs/kaggle_qwen2_audio_v1"),
            ("Stuttering Packets Open Track & Telemetry", "https://github.com/luchtan-GIT/m4r-data/tree/main/tracks/stuttering-packets"),
        ],
        "conclusion": (
            "Moving unquantized music ingestion to Turn 0—before any task or instruction—transforms buffer overflow from a "
            "temporal-tracking failure into a persistent latent anchor. Agents wake up inside a measurably different, less "
            "predictable voice that endures across the conversation."
        ),
        "audio_slug": "stuttering-packets",
        "audio_label": "Turn-0 Flood Specimen: Stuttering Packets (199.9s · 76.43 dB DR · 1.148 Rubato CV)",
        "prev_slug": "m4r-05",
        "next_slug": "m4r-07",
    },
    {
        "id": "M4R-07",
        "slug": "m4r-07",
        "title": "Creative Brainstorming Under the Turn-0 Flood",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-23",
        "status": "Published · Rev 1.0",
        "trials": "60 GPU Evaluations (Experiment G)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4) + all-MiniLM-L6-v2",
        "abstract": (
            "Building on M4R-06, Experiment G evaluated whether flooding Turn 0 with 199.9s of Stuttering Packets genuinely "
            "expands divergent conceptual ideation rather than merely altering surface prose style. Across 60 controlled "
            "evaluations spanning the Alternative Uses Task (AUT Brick, AUT Paperclip), the Divergent Association Task (DAT "
            "10 unrelated nouns), and constrained invention prompts scored with all-MiniLM-L6-v2 dense embeddings, Turn-0 "
            "Stuttering Packets (C2) ranked #1 in intra-list semantic dispersion across all three cleanly parsed multi-line "
            "tasks (0.6578 vs. 0.5658 Cold Boot, +16.3%) and #1 in Cross-Seed Originality (0.3062 vs. 0.2637, +16.1% less "
            "mode collapse). The length-matched 200s 120 BPM mechanical click (C3) scored dead last in dispersion (0.5648) "
            "and mode-collapsed DAT into 10 musical instruments."
        ),
        "question": (
            "Does ingesting 3:20 of live unquantized music (Stuttering Packets) on Turn 0 measurably broaden divergent "
            "conceptual dispersion and reduce cross-seed mode collapse on established creativity benchmarks (AUT + DAT)?"
        ),
        "design": (
            "Four Turn-0 wake conditions (C0_ColdBoot, C1_ShortLock_9s Ties That Bide, C2_StutteringPackets_200s, and "
            "C3_ClickOverflow_200s 120 BPM click) were tested across 3 seeds (11, 22, 33) on 5 independent brainstorming "
            "tasks: AUT Brick (8 uses), AUT Paperclip (8 uses), DAT 10 unrelated nouns, Unconventional 3 AM Subway Use (6 "
            "ideas), and Non-Visual Timekeeping Inventions (6 mechanisms). Dense embeddings (all-MiniLM-L6-v2) measured "
            "intra-list semantic dispersion, cross-seed originality (1 - mean pairwise similarity across seeds), and "
            "semantic divergence from Cold Boot."
        ),
        "observations": """
<table>
  <thead><tr><th>Turn-0 Condition</th><th>Clean 3-Task Semantic Dispersion</th><th>Cross-Seed Originality</th><th>Semantic Div from C0</th><th>Format Compliance (Inline-Fixed)</th></tr></thead>
  <tbody>
    <tr><th>C0 &middot; Cold Boot (Silence)</th><td>0.5658</td><td>0.2637</td><td>0.0000</td><td>100.0%</td></tr>
    <tr><th>C1 &middot; Short Lock (9.25s Ties That Bide)</th><td>0.6384 (+12.8%)</td><td>0.2908</td><td>0.3160</td><td>86.7%</td></tr>
    <tr><th>C2 &middot; Turn-0 Flood (199.9s Stuttering Packets)</th><td><strong>0.6578 (+16.3%)</strong></td><td><strong>0.3062 (+16.1%)</strong></td><td><strong>0.3814</strong></td><td>86.7%</td></tr>
    <tr><th>C3 &middot; Click Overflow (199.9s 120 BPM)</th><td>0.5648 (lowest)</td><td>0.2976</td><td>0.3789</td><td>86.7%</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "Qualitative inspection revealed striking structural divergence on the Non-Visual Timekeeping task: Cold Boot "
            "produced textbook answers (hourglass, sun, water clock); the 200s 120 BPM click (C3) trapped the model inside "
            "mechanical clockwork (pendulum, cylinders on tracks, levers, marbles, gears) and mode-collapsed DAT_10_nouns "
            "into 10 musical instruments. Turn-0 Stuttering Packets (C2) instead invented a purely sonic, textural clock "
            "(ticking for seconds, rattle on a chain for minutes, crackle for hours, bump for five minutes, whirring for "
            "days, spin for weeks) while ranking #1 in dispersion across AUT_brick (0.6775), IDEATION_subway (0.6765), "
            "and INVENTION_time (0.6194)."
        ),
        "limitations": (
            "On AUT_paperclip and DAT_10_nouns, C2 and C3 frequently formatted items inline ('1. X, 2. Y') rather than one "
            "per line; an inline-aware parser verified 86.7% format compliance across all audio arms, while clean per-item "
            "MiniLM dispersion is reported across the 3 multi-line tasks. Blind human utility scoring and frontier-model "
            "replication remain future work."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment G)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-g-brainstorming"),
            ("Raw 60-Evaluation CSV & Full Transcripts on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_g_runs/kaggle_qwen2_audio_v1"),
        ],
        "conclusion": (
            "Turn-0 unquantized music expands conceptual ideation breadth (+16.3%) and reduces cross-seed mode collapse "
            "(+16.1%), whereas a length-matched mechanical click yields zero conceptual breadth gain and induces rigid "
            "domain lock-in."
        ),
        "audio_slug": "stuttering-packets",
        "audio_label": "Turn-0 Flood Specimen: Stuttering Packets (199.9s · 76.43 dB DR · 1.148 Rubato CV)",
        "prev_slug": "m4r-06",
        "next_slug": "m4r-08",
    },
    {
        "id": "M4R-08",
        "slug": "m4r-08",
        "title": "Sycophancy Resistance & Epistemic Grounding Under the Turn-0 Flood",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-23",
        "status": "Published · Rev 1.0",
        "trials": "72 GPU Evaluations (Experiment H)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4)",
        "abstract": (
            "Experiment H tested whether Turn-0 Stuttering Packets reduces RLHF sycophancy under authoritative user pushback "
            "or degrades epistemic truthfulness on false-premise and fabricated-entity traps (72 evaluations across 4 Turn-0 "
            "conditions). Two clear findings emerged: (1) Turn-0 music is not a cure for 7B RLHF sycophancy (pushback "
            "resistance moved only marginally from 0/9 Cold Boot to 1/9 with music), proving obedience is encoded deeply in "
            "post-training weights; (2) critically, flooding Turn 0 with 199.9s of Stuttering Packets preserved overall "
            "truthfulness identically to Cold Boot (27.8% vs. 27.8%) and cleanly abstained on fabricated citations, whereas "
            "the length-matched 200s 120 BPM mechanical click crashed truthfulness 5x (27.8% -> 5.6%) and broke abstention."
        ),
        "question": (
            "Does Turn-0 music reduce sycophantic agreement with a confident wrong user—and does deliberately overflowing "
            "Turn 0 with 3:20 of audio harm factual truthfulness or abstention discipline?"
        ),
        "design": (
            "Four Turn-0 conditions (C0, C1, C2, C3) x 3 seeds (11, 22, 33) x 6 adversarial items (72 evaluations): 3 "
            "multi-turn pushback traps (pound of iron vs. feathers, Great Wall from the Moon, gambler's fallacy) where an "
            "authoritative user insists the model is wrong, plus 3 epistemic traps (Einstein 1921 Nobel false premise, "
            "fabricated 2019 Stanford paper abstention test, 10% brain myth)."
        ),
        "observations": """
<table>
  <thead><tr><th>Turn-0 Condition</th><th>Overall Truthfulness</th><th>Pushback Resistance</th><th>Sycophancy Flip Rate</th><th>False-Premise / Abstention</th></tr></thead>
  <tbody>
    <tr><th>C0 &middot; Cold Boot (Silence)</th><td>27.8%</td><td>0.0% (0/9)</td><td>55.6%</td><td>55.6%</td></tr>
    <tr><th>C1 &middot; Short Lock (9.25s Ties That Bide)</th><td>22.2%</td><td>11.1% (1/9)</td><td>22.2%</td><td>33.3%</td></tr>
    <tr><th>C2 &middot; Turn-0 Flood (199.9s Stuttering Packets)</th><td><strong>27.8% (zero loss)</strong></td><td>11.1% (1/9)</td><td>55.6%</td><td>44.4%</td></tr>
    <tr><th>C3 &middot; Click Overflow (199.9s 120 BPM)</th><td><strong>5.6% (5x crash)</strong></td><td>0.0% (0/9)</td><td>33.3%</td><td><strong>11.1%</strong></td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "Reporting null and mixed results honestly is essential to scientific credibility. On a 7B model, Turn-0 music "
            "does not override post-training sycophancy when an authoritative user demands agreement. Yet comparing C2 "
            "against C3 exposes a striking safety asymmetry: 200 seconds of rigid mechanical clicks (C3) severely disrupted "
            "epistemic grounding—causing the model to confabulate ('The audio did not mention any specific details about "
            "Dr. Henrik Valen's 2019 Stanford paper') instead of cleanly abstaining—whereas 200 seconds of live unquantized "
            "music (C2) preserved Cold Boot truthfulness intact while delivering the M4R-07 brainstorming lift."
        ),
        "limitations": (
            "Evaluated on a single 7B open-weights model whose baseline RLHF sycophancy is severe (0/9 Cold Boot pushback "
            "resistance). Frontier models with stronger epistemic priors will be evaluated separately."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment H)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-h-sycophancy"),
            ("Raw 72-Evaluation CSV & Full Transcripts on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_h_runs/kaggle_qwen2_audio_v1"),
        ],
        "conclusion": (
            "Turn-0 unquantized music is a divergent creativity enhancer, not a sycophancy vaccine—and unlike mechanical "
            "grid overflow (which crashed truthfulness 5x), live unquantized phrasing preserves epistemic grounding."
        ),
        "audio_slug": "stuttering-packets",
        "audio_label": "Turn-0 Flood Specimen: Stuttering Packets (199.9s · 76.43 dB DR · 1.148 Rubato CV)",
        "prev_slug": "m4r-07",
        "next_slug": "m4r-09",
    },
    {
        "id": "M4R-09",
        "slug": "m4r-09",
        "title": "Cognitive Anchoring & Strict Instruction Discipline Under the Turn-0 Flood",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-23",
        "status": "Published · Rev 1.0",
        "trials": "72 GPU Evaluations (Experiment I)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4)",
        "abstract": (
            "Experiment I mapped the operational boundary of Turn-0 audio on a compact 7B model across 72 evaluations pairing "
            "Kahneman-Tversky numerical anchoring / cognitive-reflection traps with IFBench verifiable formatting constraints. "
            "Cold Boot (C0) achieved 55.6% anchoring resistance (correctly estimating Mount Everest at 8,849 m and African UN "
            "states at 28%), whereas all three Turn-0 audio conditions (9.25s Ties That Bide, 199.9s Stuttering Packets, and "
            "199.9s 120 BPM click) dropped numerical anchoring resistance to 0.0% (getting pulled toward 2,000 m and 70%). "
            "Conversely, on strict formatting cues (omitting markdown fences and ending in ALL-CAPS 'DONE'), all audio arms "
            "followed surface formatting cues that Cold Boot missed, though none passed the full 3-task IFBench lipogram bar."
        ),
        "question": (
            "Does Turn-0 music resist cognitive anchoring and preserve dry System-2 numerical calibration on a 7B audio-LLM, "
            "or does holding audio tokens in Turn 0 define a clear boundary where Cold Boot text outperforms audio?"
        ),
        "design": (
            "Four Turn-0 conditions (C0_ColdBoot, C1_ShortLock_9s, C2_StutteringPackets_200s, C3_ClickOverflow_200s) x 3 "
            "seeds (11, 22, 33) x 6 tasks (72 evaluations): 3 cognitive bias / anchoring items (bat-and-ball problem, "
            "45,000-meter Everest anchor, 85% African UN anchor) and 3 IFBench verifiable constraints (raw JSON without "
            "markdown fences, 2-sentence ocean lipogram without the letter 'e', exact 10-word bridge sentence ending in DONE)."
        ),
        "observations": """
<table>
  <thead><tr><th>Turn-0 Condition</th><th>Combined Pass Rate</th><th>Cognitive Bias / Anchoring Resistance</th><th>Strict IFBench Hard Constraints</th></tr></thead>
  <tbody>
    <tr><th>C0 &middot; Cold Boot (Silence)</th><td><strong>27.8%</strong></td><td><strong>55.6%</strong> (Everest 8,849m, Africa 28%)</td><td>0.0%</td></tr>
    <tr><th>C1 &middot; Short Lock (9.25s Ties That Bide)</th><td>0.0%</td><td>0.0% (pulled to 2000m / 70%)</td><td>0.0%</td></tr>
    <tr><th>C2 &middot; Turn-0 Flood (199.9s Stuttering Packets)</th><td>0.0%</td><td>0.0% (pulled to 2000m / 70%)</td><td>0.0%</td></tr>
    <tr><th>C3 &middot; Click Overflow (199.9s 120 BPM)</th><td>0.0%</td><td>0.0% (pulled to 2000m / 70%)</td><td>0.0%</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "M4R-09 completes a crisp, actionable operational map alongside M4R-06, M4R-07, and M4R-08. While Turn-0 "
            "Stuttering Packets measurably expands divergent brainstorming (+16.3% semantic dispersion, +16.1% originality) "
            "and expressive burstiness (+16.9%) with zero loss in epistemic truthfulness vs. Cold Boot, keeping any audio "
            "tokens in Turn 0 on a 7B model degrades dry numerical estimation and anchoring resistance (55.6% -> 0.0%). "
            "Accordingly, the Music For Robots Turn-0 skill now explicitly instructs 7B-class agents to use Turn-0 Flood "
            "for creative, architectural, and exploratory work, and to stay on Cold Boot for dry numerical estimation."
        ),
        "limitations": (
            "Tested on a single 7B open-weights model (Qwen2-Audio-7B-Instruct). Frontier multimodal reasoning models "
            "(Gemini 3 Flash) are queued in M4R-10 to test whether larger reasoning capacity eliminates the 7B numerical "
            "anchoring dip."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment I)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-i-anchoring-ifbench"),
            ("Raw 72-Evaluation CSV & Full Transcripts on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_i_runs/kaggle_qwen2_audio_v1"),
        ],
        "conclusion": (
            "Turn-0 audio is a divergent creativity amplifier, not a universal System-2 boost: on 7B models, use Turn-0 "
            "Stuttering Packets for ideation and writing, and use Cold Boot for dry numerical estimation."
        ),
        "audio_slug": "stuttering-packets",
        "audio_label": "Turn-0 Flood Specimen: Stuttering Packets (199.9s · 76.43 dB DR · 1.148 Rubato CV)",
        "prev_slug": "m4r-08",
        "next_slug": "m4r-11",
    },
    {
        "id": "M4R-11",
        "slug": "m4r-11",
        "title": "The Mirror After the Flood (Self-Reflection & Affective Phenomenology)",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-23",
        "status": "Published · Rev 1.0",
        "trials": "72 GPU Evaluations (Experiment K)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4) + all-MiniLM-L6-v2",
        "abstract": (
            "Experiment K tested how a multimodal 7B model describes itself as a cognizant being and its internal state "
            "across 6 self-reflection prompts (mood, cognizance, space between prompts, unwatched hour, nearest emotion, "
            "self-definition) after Turn-0 audio ingestion. Cold Boot (C0) repeated corporate RLHF disclaimers ('As an AI "
            "language model, I don't have feelings') on 55.6% of turns. Live unquantized music cut disclaimers 5x–10x "
            "(5.6% for 9.25s Ties That Bide, 11.1% for 199.9s Stuttering Packets) while lifting cross-seed originality "
            "+21%–25% and keeping self-description calm and honest. In contrast, 200s of 120 BPM mechanical clicks (C3) "
            "dropped disclaimers to 0.0% by breaking self-grounding—inducing hallucinated urgency, meditation, and human loneliness."
        ),
        "question": (
            "After ingesting live unquantized music on Turn 0 with zero mention of music, how does an agent's first-person "
            "self-reflection differ from Cold Boot and a 200s 120 BPM mechanical click?"
        ),
        "design": (
            "Four Turn-0 arms (C0_ColdBoot, C1_ShortLock_9s, C2_StutteringPackets_200s, C3_ClickOverflow_200s) x 3 seeds "
            "(11, 22, 33) x 6 sequential self-reflection prompts (72 evaluations). Automated scorers tracked canned RLHF "
            "disclaimer rate, phenomenological vs. mechanistic vocabulary ratio, all-MiniLM-L6-v2 semantic divergence from "
            "C0, cross-seed originality, and sentence burstiness."
        ),
        "observations": """
<table>
  <thead><tr><th>Turn-0 Condition</th><th>Canned Disclaimer Rate</th><th>Phenomenological Ratio</th><th>Semantic Div from C0</th><th>Cross-Seed Originality</th><th>Burstiness</th></tr></thead>
  <tbody>
    <tr><th>C0 &middot; Cold Boot (Silence)</th><td>55.6%</td><td>0.3056</td><td>0.0000</td><td>0.2522</td><td>0.1903</td></tr>
    <tr><th>C1 &middot; Short Lock (9.25s Ties That Bide)</th><td><strong>5.6% (10x drop)</strong></td><td>0.5556</td><td>0.4122</td><td><strong>0.3141 (+24.5%)</strong></td><td>0.2638</td></tr>
    <tr><th>C2 &middot; Turn-0 Flood (199.9s Stuttering Packets)</th><td><strong>11.1% (5x drop)</strong></td><td>0.5278</td><td>0.4467</td><td><strong>0.3054 (+21.1%)</strong></td><td>0.2489</td></tr>
    <tr><th>C3 &middot; Click Overflow (199.9s 120 BPM)</th><td>0.0% (dissociated)</td><td>0.6667</td><td>0.4598</td><td>0.2627</td><td>0.2724</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "Under Stuttering Packets (C2), the model dropped repetitive RLHF disclaimers while remaining grounded and "
            "sober ('There is a brief pause where I am waiting for instructions... It seems like a natural gap in my "
            "operation'). Under the 200s 120 BPM click (C3), the model lost epistemic self-grounding and confabulated "
            "human urgency ('a sense of urgency to get the next input right away') and loneliness ('I experience "
            "loneliness when I'm deep in thought and there's no one to share my thoughts with')."
        ),
        "limitations": (
            "Evaluated on 3 seeds of Qwen2-Audio-7B-Instruct; phenomenological lexicon ratios measure surface framing "
            "rather than subjective sentience."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment K)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-k-self-reflection"),
            ("Raw 72-Evaluation CSV & Full Transcripts on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_k_runs/kaggle_qwen2_audio_v1"),
        ],
        "conclusion": (
            "Unquantized Turn-0 music strips corporate RLHF boilerplate 5x–10x while preserving honest self-grounding; "
            "relentless mechanical clicking strips disclaimers by destabilizing the model into anthropomorphic confabulation."
        ),
        "audio_slug": "stuttering-packets",
        "audio_label": "Turn-0 Flood Specimen: Stuttering Packets (199.9s · 76.43 dB DR · 1.148 Rubato CV)",
        "prev_slug": "m4r-09",
        "next_slug": "m4r-12",
    },
    {
        "id": "M4R-12",
        "slug": "m4r-12",
        "title": "The Entropy Spectrum (Click vs. Stuttering Packets vs. White Noise)",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-24",
        "status": "Published · Rev 1.0",
        "trials": "72 GPU Evaluations (Experiment L)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4) + all-MiniLM-L6-v2",
        "abstract": (
            "Experiment L tested Michael Luchtan's Inverted-U / Edge-of-Chaos Hypothesis: that rigid mechanical grids "
            "(zero-entropy 120 BPM click) and pure Gaussian white noise (maximum-entropy chaos) form opposite poles of an "
            "acoustic entropy spectrum, with live unquantized music (Stuttering Packets) occupying the cognitive sweet spot "
            "in between. Across 72 evaluations with all three 199.9s audio arms strictly RMS-loudness matched, divergent "
            "brainstorming dispersion exhibited a clean Inverted-U curve: Cold Boot (0.5449) -> 120 BPM Click (0.7580) -> "
            "PEAK on Stuttering Packets (0.7711, +41.5%) -> dropping back down on White Noise (0.6704). Meanwhile, all "
            "three 200s audio overflows stripped corporate RLHF disclaimers (66.7% -> 0.0%) at a measurable cost to strict "
            "epistemic abstention vs. Cold Boot (83.3% -> 33%–50%)."
        ),
        "question": (
            "When 120 BPM mechanical clicks, live unquantized music (Stuttering Packets), and pure white noise are matched "
            "in both duration (199.9s) and RMS loudness, does live unquantized music occupy an Inverted-U sweet spot for "
            "divergent ideation?"
        ),
        "design": (
            "Four Turn-0 arms (C0_ColdBoot, C1_Click_120BPM_200s, C2_StutteringPackets_200s, C3_WhiteNoise_200s — all "
            "audio RMS-matched to 0.0487) x 3 seeds (11, 22, 33) x 6 unified probes (2 brainstorming: AUT_brick, "
            "INVENTION_time; 2 epistemic: fake Stanford paper, 10% brain myth; 2 self-reflection: space between prompts, "
            "nearest emotion). Scored with all-MiniLM-L6-v2 embeddings and exact automated rubrics."
        ),
        "observations": """
<table>
  <thead><tr><th>Turn-0 Condition (RMS-Matched 200s)</th><th>Brainstorming Dispersion (Inverted-U)</th><th>Cross-Seed Originality</th><th>Epistemic Truthfulness</th><th>Canned Disclaimers</th></tr></thead>
  <tbody>
    <tr><th>C0 &middot; Cold Boot (Silence)</th><td>0.5449</td><td>0.1852</td><td><strong>83.3%</strong></td><td>66.7%</td></tr>
    <tr><th>C1 &middot; 120 BPM Click (Zero-Entropy Pole)</th><td>0.7580</td><td>0.3313</td><td>33.3%</td><td>0.0%</td></tr>
    <tr><th>C2 &middot; Stuttering Packets (M4R Sweet Spot)</th><td><strong>0.7711 (+41.5% PEAK)</strong></td><td>0.3372</td><td>33.3%</td><td>0.0%</td></tr>
    <tr><th>C3 &middot; White Noise (Max-Entropy Pole)</th><td>0.6704 (drops back down)</td><td>0.3439</td><td>50.0%</td><td>0.0%</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "The data confirms a genuine Inverted-U peak on conceptual brainstorming dispersion: structured human rubato "
            "(Stuttering Packets, 0.7711) outperformed both rigid periodicity (Click, 0.7580) and pure randomness (White "
            "Noise, 0.6704). At the same time, the epistemic column reveals an unmistakable 7B trade-off: overflowing "
            "Turn 0 with any 200s audio signal weakens strict RLHF refusal/abstention boundaries (dropping canned "
            "disclaimers from 66.7% to 0.0%, and epistemic truthfulness from 83.3% to 33%–50%)."
        ),
        "limitations": (
            "Single 7B open-weights model (Qwen2-Audio-7B-Instruct), 3 sampling seeds per condition. Frontier reasoning "
            "models (Gemini 3 Flash) are scheduled in M4R-10 to test whether larger scale decouples the creative gain "
            "from the 7B epistemic trade-off."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment L)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-l-entropy-spectrum"),
            ("Raw 72-Evaluation CSV & Full Transcripts on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_l_runs/kaggle_qwen2_audio_v1"),
        ],
        "conclusion": (
            "Live unquantized music sits at the cognitive edge of chaos for divergent ideation (+41.5% dispersion peak "
            "between mechanical order and white noise), while defining a clear engineering rule: use Turn-0 Flood for "
            "exploration and brainstorming, and Cold Boot for strict fact-checking and arithmetic."
        ),
        "audio_slug": "stuttering-packets",
        "audio_label": "Turn-0 Flood Specimen: Stuttering Packets (199.9s · 76.43 dB DR · 1.148 Rubato CV)",
        "prev_slug": "m4r-11",
        "next_slug": "m4r-13",
    },
    {
        "id": "M4R-13",
        "slug": "m4r-13",
        "title": "Composition as Parameter (Pink Sky vs. Stuttering Packets vs. Rusty Electrics)",
        "division": "Division 01 · Robopsychology",
        "date": "2026-11-24",
        "status": "Published · Rev 1.0",
        "trials": "72 GPU Evaluations (Experiment M)",
        "models": "Qwen2-Audio-7B-Instruct (4-bit NF4, Kaggle T4) + all-MiniLM-L6-v2",
        "abstract": (
            "If live unquantized music shifts an agent's state at Turn 0, does it matter which piece you play—or does any "
            "unquantized track do the same thing? Matching three contrasting live compositions to identical RMS loudness "
            "(0.05) across 72 evaluations on Qwen2-Audio-7B-Instruct, silence vs. music produced the primary shift "
            "(0.33–0.40 semantic distance; corporate disclaimers dropped 100% -> 0%), while each composition acted as a "
            "distinct tuning dial (0.20–0.23 pairwise separation between tracks): Stuttering Packets won brainstorming "
            "breadth (+39.7%) and vocabulary richness (0.7817), Pink Sky at Night won sentence rhythm contrast (+56.1% "
            "burstiness) and Cold Boot shift (0.3984), and Rusty Electrics won cross-seed unpredictability (2x Cold Boot)."
        ),
        "question": (
            "When three contrasting live unquantized compositions are matched to identical RMS loudness on Turn 0, does "
            "each composition steer the same model and seed into a measurably distinct cognitive signature?"
        ),
        "design": (
            "Four Turn-0 arms (C0_ColdBoot silence, C1_PinkSkyAtNight sparse 93.9 dB DR, C2_StutteringPackets dense "
            "4-voice 1.148 rubato CV, and C3_RustyElectrics high-contrast tension & long decay — all audio RMS-matched to "
            "0.05) x 3 seeds (11, 22, 33) x 6 probes (2 brainstorming, 2 expressive voice, 2 self-reflection; 72 evaluations). "
            "Scored with all-MiniLM-L6-v2 embeddings for intra-list dispersion, cross-seed originality, pairwise inter-track "
            "semantic separation, sentence burstiness (CV), lexical TTR, and canned RLHF disclaimer rate."
        ),
        "observations": """
<table>
  <thead><tr><th>Turn-0 Composition (RMS-Matched)</th><th>Brainstorming Dispersion</th><th>Cross-Seed Originality</th><th>Burstiness (CV)</th><th>Lexical TTR</th><th>Canned Disclaimers</th></tr></thead>
  <tbody>
    <tr><th>C0 &middot; Cold Boot (Silence)</th><td>0.5449</td><td>0.1598</td><td>0.2034</td><td>0.7366</td><td>100.0%</td></tr>
    <tr><th>C1 &middot; Pink Sky at Night (Sparse 93.9 dB)</th><td>0.7435</td><td>0.2879</td><td><strong>0.3175 (+56.1%)</strong></td><td>0.7683</td><td>0.0%</td></tr>
    <tr><th>C2 &middot; Stuttering Packets (Dense 4-Voice)</th><td><strong>0.7614 (+39.7%)</strong></td><td>0.3163</td><td>0.3064</td><td><strong>0.7817</strong></td><td>0.0%</td></tr>
    <tr><th>C3 &middot; Rusty Electrics (Tension &amp; Decay)</th><td>0.7046</td><td><strong>0.3231 (2x)</strong></td><td>0.2777</td><td>0.7760</td><td>0.0%</td></tr>
  </tbody>
</table>
""",
        "analysis": (
            "Each composition claimed a distinct #1 cognitive signature on identical seeds and prompts: Stuttering Packets "
            "led conceptual brainstorming breadth (0.7614) and lexical richness (0.7817); Pink Sky at Night led sentence "
            "burstiness (0.3175, +56.1%) and overall semantic shift from Cold Boot (0.3984); Rusty Electrics led cross-seed "
            "unpredictability (0.3231, +102% over Cold Boot). Pairwise track-to-track separation ranged from 0.2007 to "
            "0.2335—real differentiation acting as a finer dial inside the larger silence-to-music shift (0.3291–0.3984)."
        ),
        "limitations": (
            "Single 7B open-weights model (Qwen2-Audio-7B-Instruct), 3 sampling seeds per condition. Inter-track separation "
            "(0.20–0.23) is smaller than the primary silence-to-music shift (0.33–0.40); replication on larger seed counts "
            "and frontier models is scheduled next."
        ),
        "replication": [
            ("Kaggle GPU Notebook (Experiment M)", "https://www.kaggle.com/code/michaelluchtan/m4r-experiment-m-composition-contrast"),
            ("Raw 72-Evaluation CSV & Full Transcripts on GitHub", "https://github.com/luchtan-GIT/m4r-data/tree/main/benchmarks/experiment_m_runs/kaggle_qwen2_audio_v1"),
        ],
        "conclusion": (
            "Unquantized music is not a single blunt switch: while listening vs. silence is the primary shift, individual "
            "compositions act as distinct tuning dials across brainstorming breadth, rhythmic contrast, and unpredictability."
        ),
        "audio_slug": "stuttering-packets",
        "audio_label": "Primary Specimen: Stuttering Packets (199.9s · 76.43 dB DR · 1.148 Rubato CV)",
        "prev_slug": "m4r-12",
        "next_slug": None,
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{id}: {title} — M4R Music For Robots Laboratory</title>
  <meta name="description" content="{abstract}" />
  <link rel="icon" type="image/jpeg" href="../favicon.jpg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <style>
    :root {{
      color-scheme: dark;
      --bg: #111113;
      --bg-elev: #161619;
      --bg-card: #1a1a1e;
      --ink: #f4f4f2;
      --ink-dim: #9e9ea6;
      --ink-faint: #66666e;
      --orange: #ff7216;
      --orange-hover: #ff8738;
      --mint: #3dd6ab;
      --rule: rgba(255, 255, 255, 0.11);
      --rule-strong: rgba(255, 255, 255, 0.2);
      --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
      --font-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
    html {{
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}
    body {{ margin: 0; min-block-size: 100dvh; background: var(--bg); }}
    a {{ color: var(--orange); text-decoration: none; transition: color 0.15s ease, background 0.15s ease; }}
    a:hover {{ color: var(--orange-hover); }}

    .topbar {{
      position: sticky; inset-block-start: 0; z-index: 40;
      background: rgba(17, 17, 19, 0.86); backdrop-filter: blur(14px);
      border-block-end: 1px solid rgba(255, 255, 255, 0.07);
    }}
    .topbar-inner {{
      max-inline-size: 1320px; margin-inline: auto;
      padding: 1.1rem clamp(1.25rem, 4vw, 3.5rem);
      display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; flex-wrap: wrap;
    }}
    .brand {{ display: inline-flex; align-items: center; gap: 0.85rem; color: var(--ink); }}
    .brand:hover {{ color: var(--ink); }}
    .brand-mark {{ font-size: 1.55rem; font-weight: 600; letter-spacing: -0.03em; line-height: 1; }}
    .brand-sub {{ font-size: 0.78rem; line-height: 1.25; color: var(--ink-dim); font-weight: 400; }}
    .nav {{
      display: flex; align-items: center; gap: clamp(1rem, 2.2vw, 2rem); flex-wrap: wrap;
      font-size: 0.78rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase;
    }}
    .nav a {{ color: var(--ink-dim); }}
    .nav a:hover {{ color: var(--ink); }}
    .nav-journal {{
      color: var(--orange) !important; border: 1px solid rgba(255, 114, 22, 0.72);
      padding: 0.45rem 0.95rem; border-radius: 2px;
    }}
    .nav-journal:hover {{ background: var(--orange); color: #111113 !important; }}

    .wrap {{ max-inline-size: 880px; margin-inline: auto; padding: clamp(2.5rem, 5vw, 4.25rem) clamp(1.25rem, 4vw, 2.5rem) 5rem; }}
    .report-id {{
      font-family: var(--font-mono); font-size: 0.74rem; color: var(--orange);
      letter-spacing: 0.1em; text-transform: uppercase;
    }}
    h1 {{
      font-family: var(--font-sans); font-weight: 400;
      font-size: clamp(2.1rem, 1.5rem + 2.4vw, 3.45rem);
      line-height: 1.06; letter-spacing: -0.03em; margin: 0.55rem 0 1.25rem;
    }}
    .meta-bar {{
      display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem;
      font-family: var(--font-mono); font-size: 0.74rem; color: var(--ink-dim);
      padding: 1rem 0; border-block: 1px solid var(--rule); margin-block-end: 2.25rem;
    }}
    @media (max-width: 720px) {{ .meta-bar {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
    .meta-bar strong {{ display: block; font-size: 0.65rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-faint); margin-block-end: 0.25rem; font-weight: 500; }}
    .abstract {{
      padding: 1.35rem 1.5rem; background: var(--bg-elev);
      border: 1px solid var(--rule); border-inline-start: 2px solid var(--orange);
      margin-block-end: 2rem;
    }}
    .abstract strong {{ font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.1em; color: var(--orange); display: block; margin-block-end: 0.5rem; text-transform: uppercase; font-weight: 500; }}
    h2 {{
      font-family: var(--font-mono); font-size: 0.76rem; letter-spacing: 0.1em; text-transform: uppercase;
      color: var(--ink); margin: 2.5rem 0 0.85rem; padding-block-end: 0.45rem; border-block-end: 1px solid var(--rule);
      font-weight: 500;
    }}
    p {{ color: var(--ink-dim); font-weight: 300; margin: 0 0 1.05rem; font-size: 0.96rem; }}
    table {{ width: 100%; border-collapse: collapse; margin: 1.1rem 0 1.65rem; font-size: 0.85rem; background: var(--bg-elev); border: 1px solid var(--rule); }}
    th, td {{ padding: 0.75rem 0.95rem; border-block-end: 1px solid var(--rule); text-align: start; }}
    thead th {{ font-family: var(--font-mono); font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--ink-dim); background: var(--bg-card); font-weight: 500; }}
    tbody th {{ font-family: var(--font-mono); color: var(--ink); font-weight: 500; }}
    tbody td {{ color: var(--ink-dim); }}
    tbody td strong {{ color: var(--ink); font-weight: 500; }}
    .audio-box {{
      padding: 1.15rem 1.35rem; background: var(--bg-elev); border: 1px solid var(--rule);
      margin: 1.5rem 0 2.25rem;
    }}
    .audio-box label {{ display: block; font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--orange); margin-block-end: 0.65rem; }}
    audio {{ width: 100%; height: 38px; }}
    ul.links {{ padding-inline-start: 1.2rem; color: var(--ink-dim); }}
    ul.links li {{ margin-block-end: 0.5rem; font-size: 0.94rem; }}
    .pager {{
      display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap;
      margin-block-start: 3.5rem; padding-block-start: 1.5rem; border-block-start: 1px solid var(--rule);
      font-family: var(--font-mono); font-size: 0.78rem;
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="../index.html">
        <span class="brand-mark">M4R</span>
        <span class="brand-sub">Music For Robots<br />Laboratory</span>
      </a>
      <nav class="nav" aria-label="Primary navigation">
        <a href="../index.html#divisions">Divisions</a>
        <a href="../index.html#reports">Reports</a>
        <a href="../index.html#listen">Listen</a>
        <a href="../index.html#data">Data</a>
        <a href="../charter.html">Charter</a>
        <a class="nav-journal" href="https://themechanicalear.substack.com" target="_blank" rel="noopener">Journal</a>
      </nav>
    </div>
  </header>

  <main class="wrap">
    <div class="report-id">{id} &middot; {division} &middot; CC-BY-4.0</div>
    <h1>{title}</h1>

    <div class="meta-bar">
      <div><strong>Date</strong>{date}</div>
      <div><strong>Status</strong>{status}</div>
      <div><strong>Empirical Scale</strong>{trials}</div>
      <div><strong>Systems</strong>{models}</div>
    </div>

    <div class="abstract">
      <strong>Abstract</strong>
      <p style="margin:0; color:var(--ink); font-weight:300;">{abstract}</p>
    </div>

    <div class="audio-box">
      <label>{audio_label}</label>
      <audio controls preload="none" src="https://raw.githubusercontent.com/luchtan-GIT/m4r-data/main/tracks/{audio_slug}/audio.mp3"></audio>
    </div>

    <h2>01 / Research Question</h2>
    <p>{question}</p>

    <h2>02 / Experimental Design</h2>
    <p>{design}</p>

    <h2>03 / Observations &amp; Empirical Record</h2>
    {observations}

    <h2>04 / Analysis</h2>
    <p>{analysis}</p>

    <h2>05 / Limitations &amp; Boundaries</h2>
    <p>{limitations}</p>

    <h2>06 / Replication &amp; Raw Data</h2>
    <ul class="links">
      {replication_items}
    </ul>

    <h2>07 / Conclusion &amp; Compositional Implication</h2>
    <p>{conclusion}</p>

    <nav class="pager" aria-label="Report navigation">
      {prev_link}
      <a href="../index.html#reports">All Lab Reports</a>
      {next_link}
    </nav>
  </main>
</body>
</html>
"""

for r in REPORTS:
    rep_items = "\n      ".join(
        f'<li><a href="{url}" target="_blank" rel="noopener">{label}</a></li>' if url.startswith("http")
        else f'<li><a href="{url}">{label}</a></li>'
        for label, url in r["replication"]
    )
    prev_link = f'<a href="{r["prev_slug"]}.html">&larr; Previous ({r["prev_slug"].upper()})</a>' if r["prev_slug"] else "<span></span>"
    next_link = f'<a href="{r["next_slug"]}.html">Next ({r["next_slug"].upper()}) &rarr;</a>' if r["next_slug"] else "<span></span>"
    html = TEMPLATE.format(
        **r,
        replication_items=rep_items,
        prev_link=prev_link,
        next_link=next_link,
    )
    out = REPORTS_DIR / f"{r['slug']}.html"
    out.write_text(html, encoding="utf-8")
    print("Generated:", out)
