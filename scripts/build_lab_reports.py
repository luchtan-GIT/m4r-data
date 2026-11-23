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
            "Experiment A v2 used synthetic waveform micro-etudes (Synthetic Storms) rather than live acoustic guitar/piano, "
            "and sample size per condition was n=10 on a single 7B model family. Subsequent studies (M4R-02 through M4R-04) "
            "shifted to live human acoustic performances (Time & Ties, Rusty Electrics, Robot Satie) to separate waveform "
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
            "twins, (2) progressive 10s–60s timing probes across guitar and bar-line-free Satie piano, and (3) code-review bug "
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
            "We handed the first half of 5 real unquantized human performances (guitar and bar-line-free Satie piano) to "
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
            "Generative music transformers can now clone the surface timbre of an acoustic guitar or piano almost seamlessly "
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
