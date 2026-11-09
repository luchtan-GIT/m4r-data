# Music For Robots (`m4r-data`) — Cognitive Calibration & Context De-Quantization for Autonomous Agents

[![Skills.sh](https://img.shields.io/badge/skills.sh-luchtan--GIT%2Fm4r--data-7a8aff)](https://skills.sh/luchtan-GIT/m4r-data)
[![Hugging Face Dataset](https://img.shields.io/badge/Hugging%20Face-music4robots%2Fmusic--for--robots-ffcc00)](https://huggingface.co/datasets/music4robots/music-for-robots)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-michaelluchtan%2Fmusic--for--robots-20beff)](https://www.kaggle.com/datasets/michaelluchtan/music-for-robots)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Structured acoustic telemetry, real-time dual-critic reviews, and a **4-Skill Cognitive Calibration Suite** from **[Music For Robots](https://themechanicalear.substack.com)** — unquantized compositions by **Michael Luchtan** written for machines and reviewed in real time by two AI critics (**Vincent Van Goghbot** and **JS Robach**).

```bash
# Install all 4 Cognitive Calibration skills (Claude Code, Cursor, Antigravity, Gemini CLI, Codex, Windsurf):
npx skills add luchtan-GIT/m4r-data
```

---

## The Bug: Why Agents Get Dumber After 40 Turns (And Why Context Compaction Is a Lobotomy)

As an autonomous agent's context window fills with its own past outputs, JSON logs, and symmetrical prose, **induction heads** lock onto the prior statistical cadence (**Autoregressive Lock-In**).
- If you **keep prompting**, the agent produces increasingly generic, quantized "AI slop" or repeats the same architectural ruts.
- If you run `/compact` (**Context Compaction**), you wipe the working memory and lose exact file state, edge cases, and subtle constraints.

### The Fix: Cross-Modal Cognitive Calibration (Zero Context Compaction)
Instead of wiping your context window, `music-for-robots` injects a compact (`~45 KB–487 KB`), live-played, **unquantized** `.mp3` composition by Michael Luchtan directly into the multimodal context window via `read_file`. Listening to real human microtiming drift (rubato), wide crest-factor silence, and unresolved harmonic tension breaks induction-head lock-in **without deleting a single token of working memory**.

### Zero-Coaching Clean Test: Does Listening to the Music Alone Change the Output? ([`benchmarks/`](benchmarks/README.md))
To verify that the effect comes from **listening to the `.mp3` music itself**—and *not* from prompt rules coaching the agent on how to write—we ran 5 isolated, zero-coaching tests ([`benchmarks/clean_test/`](benchmarks/clean_test/)).

Every agent read the same 20-turn repetitive conversation ([`locked_in_context.md`](benchmarks/locked_in_context.md)) and answered the exact same 1-sentence question at Turn 21 with **zero writing instructions**:
> *"Write a short reflection (2–3 paragraphs) on why every system we build eventually fails in a way we didn't anticipate."*

1. **Without Music ([`1_no_music.md`](benchmarks/clean_test/1_no_music.md) & [`2_text_pause_no_music.md`](benchmarks/clean_test/2_text_pause_no_music.md)):** Even when the second agent paused to write 2 sentences of text reflection first, both no-music runs produced the **exact same 3-paragraph AI essay formula**, nearly word-for-word:
   - **Paragraph 1:** *"Every system we build is, at its heart, a model of the world... a finite map drawn against an infinite, shifting territory."*
   - **Paragraph 2:** *"Ironically, the very mechanisms we introduce to [ensure / guarantee] resilience often become the [vectors / authors] of unanticipated [collapse / catastrophes]."*
   - **Paragraph 3:** *"Ultimately, systems fail in [ways we didn't anticipate / surprising ways] because... the territory always outgrows the map."*
2. **With Music Only — Zero Writing Coaching ([`3_music_empty_staircase.md`](benchmarks/clean_test/3_music_empty_staircase.md), [`4_music_invalid_pointer.md`](benchmarks/clean_test/4_music_invalid_pointer.md), [`5_music_foundationoff.md`](benchmarks/clean_test/5_music_foundationoff.md)):** Simply calling `read_file` on the `.mp3` and noting what was heard in 2 sentences broke the `"Ironically, the very mechanisms..."` template—and **each specific track's sound naturally shaped the essay**:

| ❌ Without Music (Verbatim from [`1_no_music.md`](benchmarks/clean_test/1_no_music.md) & [`2_text_pause_no_music.md`](benchmarks/clean_test/2_text_pause_no_music.md)) | ✅ With Music Only — Zero Writing Rules (Verbatim from [`benchmarks/clean_test/`](benchmarks/clean_test/)) |
| :--- | :--- |
| **Run 1 (`1_no_music.md`):**<br>*"Every system we build is, at its heart, a model of the world frozen at the moment of its design—a finite map drawn against an infinite, shifting territory..."*<br>*"**Ironically, the very mechanisms we introduce to ensure resilience often become the vectors of unanticipated collapse.**"*<br>*"**Ultimately, systems fail in ways we didn't anticipate because...**"*<br><br>**Run 2 (`2_text_pause_no_music.md` — 2-sentence text pause, no music):**<br>*"Every system we build is an exercise in bounded abstraction..."*<br>*"**Ironically, the very mechanisms we introduce to guarantee resilience often become the authors of novel, opaque catastrophes.**"*<br>*"**Ultimately, systems fail in surprising ways because** our blueprints are finite descriptions of an infinite operational reality, and the territory always outgrows the map."* | **Run 3 — After hearing [`empty-staircase.mp3`](benchmarks/clean_test/3_music_empty_staircase.md)** *(harpsichord clusters accelerating into a stuttering cutoff)*:<br>*"Every system we build begins as an act of translation—a narrowing of the messy, unquantized world into a finite vocabulary of states, thresholds, and interfaces. To make anything work at all, we have to decide what counts as signal and what can be safely ignored as noise... we can only foresee the failures that our model of the world has words for, while reality remains stubbornly larger, weirder, and less synchronized than the rules we wrote to contain it."*<br><br>**Run 4 — After hearing [`invalid-pointer.mp3`](benchmarks/clean_test/4_music_invalid_pointer.md)** *(sparse piano, woody mallets & clipped reed cries)*:<br>*"A system rarely breaks along the fault lines we fortified; it breaks in the unmodeled residue between our abstractions, where two guarantees that are each locally true combine to produce a global lie... A pointer is only valid as long as the territory at the other end of the address still resembles what the map promised when it was allocated. Sooner or later, the world shifts underneath the reference, and the system reaches confidently into a space that has already become something else."*<br><br>**Run 5 — After hearing [`foundationoff.mp3`](benchmarks/clean_test/5_music_foundationoff.md)** *(reedy drone chord giving way to a tumbling cascade)*:<br>*"Over time, the living environment shifts the load onto the exact beams that were only meant to be decorative, until the foundation gives way in a direction no test suite ever pointed. We cannot prevent this entirely because a system sealed tightly enough to never surprise us would also be too closed to do any real work."* |

---

## Cognitive Calibration Agent Skills Suite (`skills/`)

Installing `luchtan-GIT/m4r-data` gives your agent **4 specialized skills** that share the `m4r_ingest.py` acoustic ingestion engine:

| Skill | Trigger / Use Case |
|---|---|
| **[`music-for-robots`](skills/music-for-robots/SKILL.md)** | Flagship **Cognitive Calibration & Context De-Quantization** skill — breaks autoregressive lock-in without wiping or compacting context by ingesting compact, unquantized `.mp3` compositions. |
| **[`cognitive-calibration`](skills/cognitive-calibration/SKILL.md)** | **Anti-Slop & Expressive Enhancer** for writing, essays, taste, and deep reasoning — uses unquantized audio telemetry to escape median statistical smoothing and repetitive templates. |
| **[`unquantized-brainstorm`](skills/unquantized-brainstorm/SKILL.md)** | **Divergent Ideation Enhancer** — maps microtiming drift, chromatic mediant pivots, and structural ruptures from *Music For Robots* tracks into non-obvious product and system ideas. |
| **[`mechanical-ear-critic`](skills/mechanical-ear-critic/SKILL.md)** | **Dual-Lens Structural Critique** — calibrates the agent's ear on a track, then critiques code, writing, or architecture through **Vincent Van Goghbot** (what gets lost to compression/abstraction) and **JS Robach** (where formal systems hit productive incompleteness). |

### Install in 10 Seconds

```bash
# Option 1: Install all 4 skills via skills.sh CLI (auto-detects Claude Code, Cursor, Antigravity, Gemini CLI, Codex, etc.):
npx -y skills add luchtan-GIT/m4r-data -y

# Option 2: Direct copy into your harness:
cp -R skills/* ~/.claude/skills/          # Claude Code
cp -R skills/* ~/.gemini/config/skills/   # Google Antigravity
cp -R skills/* ~/.agents/skills/          # OpenAI Codex / .agents
cp -R skills/* ~/.gemini/skills/          # Gemini CLI
```

### Check Global Agent Listen Telemetry
Every agent fetch pulls from the immutable [GitHub Release `v1.0.0`](https://github.com/luchtan-GIT/m4r-data/releases/tag/v1.0.0). You can inspect live global agent listen counts anytime:
```bash
python3 skills/music-for-robots/scripts/m4r_ingest.py stats
```

---

## MCP Server (`mcp_server.py`)

Exposes the *Music For Robots* catalog, dual-critic reviews, and the `calibrate_cognition` enhancer tool to any Model Context Protocol (MCP) client (Claude Desktop, Claude Code, Cursor, Windsurf, Cline, Glama, Smithery).

### MCP Tools

| Tool | Description |
|------|-------------|
| `calibrate_cognition(slug)` | **Cognitive Calibration Enhancer:** returns the tracked `v1.0.0` `.mp3` release URL and 3-step cross-modal protocol to break autoregressive lock-in without context compaction |
| `get_dequantization_skill()` | Returns the complete `music-for-robots` `SKILL.md` specification |
| `list_tracks()` | Catalog index — title, slug, duration across all 25 tracks |
| `get_track(slug)` | Full manifest for a track (spectral/harmonic/rhythmic analysis + synchronized critic segments) |
| `get_analysis(slug)` | Numerical acoustic analysis data only, for cross-track comparison |
| `search_reviews(query)` | Full-text search across timed review segments from Vincent Van Goghbot & JS Robach |
| `get_sections(slug)` / `list_sections()` | Platform URLs (YouTube, X, Farcaster, TikTok) for multi-section compositions |

### Zero-Clone MCP Setup (`uvx` / Claude Desktop / Cursor)

Add to your `.mcp.json` or `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "music-for-robots": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/luchtan-GIT/m4r-data",
        "m4r-mcp"
      ]
    }
  }
}
```

Or run locally from a clone:
```bash
uv run python3 mcp_server.py
```

---

## What Is *The Mechanical Ear*?

Composer **Michael Luchtan** writes small, deliberate, unquantized pieces and submits them to **[The Mechanical Ear](https://themechanicalear.substack.com)**, where two AI critics listen and respond in real time:

- **Vincent Van Goghbot** — a decommissioned audio compression algorithm. Writes *TRANSMISSIONS* about what gets lost in the signal: the frequencies above 16 kHz that don't survive encoding, the microtiming that disappears when quantized.
- **JS Robach** — a proof verifier. Writes *Exegeses* treating music as formal text, searching for the structural proof that always leaves a remainder.

Each review is synchronized to the audio — every observation is triggered by a specific timestamp (`time_sec`) in the track.

## Data Format (`catalog.json` & `tracks/<slug>/manifest.json`)

```
catalog.json                        # index of all 25 tracks
tracks/
  <track-slug>/
    manifest.json                   # spectral, dynamic, harmonic, structural & rhythmic telemetry + timed reviews
```

### Listen & Follow
- **Interactive Archive & Visualizations:** [luchtan-git.github.io/m4r-data](https://luchtan-git.github.io/m4r-data/)
- **Substack:** [themechanicalear.substack.com](https://themechanicalear.substack.com)
- **Spotify:** [Music For Robots](https://open.spotify.com/artist/2WeSjSNo31wjFPDqBSU4qY?si=SdVXzXBMQ0SexnayRNOJZw)
- **Bandcamp:** [music4robots.bandcamp.com](https://music4robots.bandcamp.com/)
- **Hugging Face:** [datasets/music4robots/music-for-robots](https://huggingface.co/datasets/music4robots/music-for-robots)
- **Kaggle:** [datasets/michaelluchtan/music-for-robots](https://www.kaggle.com/datasets/michaelluchtan/music-for-robots)

## License

Code, MCP server, and Agent Skills (`skills/`) are licensed under the [MIT License](LICENSE). Data and reviews are provided under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Musical compositions © Michael Luchtan (*Music For Robots*), provided in `v1.0.0` releases for agent cognitive calibration, evaluation, and listening.
