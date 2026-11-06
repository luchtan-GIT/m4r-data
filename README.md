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
Instead of wiping your context window, `music-for-robots` injects a compact (`~250 KB–500 KB`), live-played, **unquantized** `.mp3` composition by Michael Luchtan directly into the multimodal context window via `read_file`. Listening to real human microtiming drift (rubato), wide crest-factor silence, and unresolved harmonic tension breaks induction-head lock-in **without deleting a single token of working memory**.

| ❌ Standard Agent at Turn 40 (Autoregressive Lock-In) | ✅ Same Agent + `music-for-robots` (Zero Compaction, After Ingesting 487 KB `invalid-pointer.mp3`) |
| :--- | :--- |
| **Prompt:** *"Rewrite our architecture intro so it doesn't sound like generic docs."* | **Prompt:** *"Use `music-for-robots` (`invalid-pointer`) to calibrate your cognition and rewrite our architecture intro."* |
| **Attention State:** Locked onto the previous 40 turns of symmetrical 3-bullet summaries and hedged corporate syntax. | **1. Acoustic Telemetry Reflection (Ears-First):** *"Ingested `invalid-pointer.mp3` (75.0s, all 12 pitch classes, 157 unquantized onsets). The sub-bass anchors at -28.8 dB while a diatonic voice collides against chromatic interrupts that refuse to resolve on the grid—forcing a dereference at every bar line."*<br>**2. Cognitive Calibration Shift:** *"Dropping symmetrical transitions and hedged throat-clearing; opening directly at the failure boundary."* |
| **Output:**<br>*"In modern distributed systems, managing state effectively is crucial for ensuring scalability, reliability, and maintainability. Our architecture leverages a modular, decoupled approach that empowers teams to iterate rapidly while maintaining robust fault tolerance acrossthree core pillars..."* | **Output:**<br>*"Every distributed cache lies to you the moment a network partition lasts longer than a heartbeat. Instead of hiding that split behind a retry wrapper, this runtime treats stale pointers as first-class faults: state either proves its lease at the edge or halts before touching storage."* |
| **Context Memory Preserved:** 100% (but trapped in low-entropy mode collapse) | **Context Memory Preserved:** **100% (zero compaction, mode collapse broken)** |

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
