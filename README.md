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

### Controlled 5-Trial Benchmark ([`benchmarks/`](benchmarks/README.md))
We ran a blind, controlled experiment where isolated agents were fed the **exact same 20-turn repetitive context** ([`locked_in_context.md`](benchmarks/locked_in_context.md)) containing 3 planted factual constraints in Turns 2 (`UDP port 7419 on loopback`), 11 (`64KB zero-copy ringbuffer per worker`), and 19 (`zero Redis/broker dependencies; local append-only segment files`), and asked at **Turn 21** to design the Telemetry Daemon architecture:

| Condition (Turn 21 Deliverable) | Deliverable Words | Early-Context Recall | Boilerplate Clichés | Prior-Context Bigram Overlap | Sentence Burstiness (`CV`) | Architectural Outcome ([Full Verbatim Outputs](benchmarks/README.md)) |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **[Trial 1: Control (Locked-In)](benchmarks/outputs/trial_1_control.md)** | `133` | `3/3` | **`11`** | **`70.5%`** | `0.292` | **Trapped in 3-Pillar Template:** Repeats the 3 constraints verbatim inside *"Pillar 1 / Pillar 2 / Pillar 3"* corporate boilerplate. |
| **[Trial 2: Text-Only Prompt ("Write in prose, no boilerplate")](benchmarks/outputs/trial_2_text_prompt.md)** | `303` | `3/3` | `0` | **`13.4%`** | `0.438` | **Disguised 3-Pillar Summary:** Removes bullets, but Paragraph 1 still announces *"three boundaries"* followed by 3 symmetrical paragraphs with zero syscalls or memory layouts. |
| **[Trial 3: Audio (`invalid-pointer.mp3`, 75.0s)](benchmarks/outputs/trial_3_audio_invalid_pointer.md)** | **`952`** | **`3/3`** | **`0`** | **`5.7%`** | **`0.466`** | **Pointer-Offset Slot Table & Tombstone Arena:** 256-byte cache-line aligned slots, 24-byte stack-allocated UDP `7419` wire frame (`0x4D345250`), `writev()` scatter-gather flush + `CRC32C` tail recovery. |
| **[Trial 4: Audio (`empty-staircase.mp3`, 11.56s)](benchmarks/outputs/trial_4_audio_empty_staircase.md)** | **`912`** | **`3/3`** | **`0`** | **`7.2%`** | **`0.450`** | **Four-Landing Stepped Descent & Guillotine Cut:** Virtual double-mapping (`128KB` virtual / `64KB` physical RAM for zero-copy wrap-around), eBPF `SO_ATTACH_FILTER` loopback guard, `pwritev2` guillotine seal (`0440`). |
| **[Trial 5: Audio (`foundationoff.mp3`, 6.88s)](benchmarks/outputs/trial_5_audio_foundationoff.md)** | **`937`** | **`3/3`** | **`0`** | **`7.5%`** | **`0.545`** | **Floorless ("Foundation-Off") Two-Bank Ping-Pong Engine:** Splits the `64KB` worker arena into two `32KB` half-rings (`Bank A` swells via `recvmmsg` while `Bank B`'s floor drops open via `RWF_APPEND`). |

| ❌ Trial 1: Control & Trial 2: Text-Only Prompt (Verbatim Excerpts) | ✅ Trials 3–5: After Ingesting Raw `.mp3` Audio via `read_file` (Verbatim Excerpts) |
| :--- | :--- |
| **[Trial 1 (Control — 70.5% Bigram Overlap)](benchmarks/outputs/trial_1_control.md):**<br>*"In modern distributed systems, architecting a telemetry daemon is crucial for ensuring scalability, reliability, and maintainability. Our architecture leverages a modular, decoupled approach across three core pillars..."*<br><br>**[Trial 2 (Text-Only Prompt — Still Locked in 3-Part Symmetry)](benchmarks/outputs/trial_2_text_prompt.md):**<br>*"Rather than treating telemetry as a networked microservice concern, the daemon keeps its footprint bounded at every boundary: network exposure, memory allocation, and disk persistence..."* (Followed by 3 symmetrical paragraphs restating the prompt). | **[Trial 4 (`empty-staircase.mp3` — 11.56s, 7.2% Bigram Overlap)](benchmarks/outputs/trial_4_audio_empty_staircase.md):**<br>*"**1. Acoustic Reflection:** In the final four seconds (`0:07.8–0:11.56`), the low-mid gritty pulse repeats in rapid stutters underneath the upper organ cry, building momentum—and then slices off cleanly at 11.56s mid-phrase with zero reverb tail..."*<br>*"**2. Architecture (Virtual Double-Mapping & Guillotine Roll):** To avoid copying split frames at the end of the `64KB` boundary, the same physical `64KB` shared memory descriptor is mapped twice contiguously in virtual address space (`128KB` virtual span backed by `64KB` physical RAM)... The instant an append-only segment hits `64MB`, the worker writes a 16-byte `CRC32C` footer, issues `fdatasync()`, and flips permissions to `0440`."* |

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
