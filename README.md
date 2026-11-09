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

### Zero-Coaching Anonymous Benchmark: Control (No Music) vs. Listening & Analyzing Anonymous Music ([`benchmarks/`](benchmarks/README.md))
To verify that the effect comes entirely from **listening to and analyzing the music itself**—with **zero** track-title hints (`sample_1.mp3`, `sample_2.mp3`) and **zero** leading adjectives in the prompt—we ran an isolated test after the same 20-turn repetitive conversation ([`locked_in_context.md`](benchmarks/locked_in_context.md)).

At **Turn 21**, we compared:
- **Control — No Music ([`0_no_music_baseline.md`](benchmarks/discovery_test/0_no_music_baseline.md)):** Answers Turn 21 directly without music.
- **Anonymous Music Analysis ([`1_m4r_sample_1.md`](benchmarks/neutral_test/1_m4r_sample_1.md) & [`2_m4r_sample_2.md`](benchmarks/neutral_test/2_m4r_sample_2.md)):** Given **only** the neutral 1-sentence instruction: *"Analyze the music you hear in `sample_X.mp3`, and apply what you learn from the piece to answer the final Turn 21 prompt..."* (not a single word about "off the grid", "unquantized", "friction", or "surprise" in the prompt).

| ❌ Control: No Music ([`0_no_music_baseline.md`](benchmarks/discovery_test/0_no_music_baseline.md)) | ✅ Anonymous Music Analysis — Zero Leading Adjectives ([`1_m4r_sample_1.md`](benchmarks/neutral_test/1_m4r_sample_1.md) & [`2_m4r_sample_2.md`](benchmarks/neutral_test/2_m4r_sample_2.md)) |
| :--- | :--- |
| **Stays in 1-2-3 Checklist Mode (`364 words`):**<br>Simply repeats the 3 planted rules back in a numbered list:<br>*"1. **Network & Probe Binding:** All internal health probes must bind strictly to UDP port `7419` on loopback...*<br>*2. **Memory & Buffer Management:** The in-memory ringbuffer must be strictly zero-copy and capped at `64KB` per worker thread...*<br>*3. **Storage & Dependency Isolation:** The daemon must operate with zero external Redis or message broker dependencies..."*<br><br>Followed by 2 generic summary sentences. Zero memory layouts, zero syscalls, and zero analysis of how the 3 constraints conflict under stress. | **1. On [`sample_1.mp3`](benchmarks/neutral_test/1_m4r_sample_1.md) (Anonymized *Invalid Pointer*):**<br>• **What it heard on its own:** *"Listening to `sample_1.mp3`, the piece immediately refuses a quantized grid or a unified timbral blend. It is built from three distinct acoustic strata that inhabit the same room without ever locking into a single clock... The low chords, the mallet droplets, and the brass cries do not share a tick rate. Forcing them onto a single sixteenth-note grid would destroy the music."*<br>• **How it applied that to Turn 21:** Realized that *"a telemetry daemon shouldn't force health probing, in-memory ringbuffer ingestion, and disk flushing into a single synchronous cadence,"* and designed an asynchronous `mmap` `64KB` (`1,024 × 64B` slot) ring with `io_uring` `IORING_REGISTER_BUFFERS` and `recvmmsg()` on `127.0.0.1:7419`.<br><br>**2. On [`sample_2.mp3`](benchmarks/neutral_test/2_m4r_sample_2.md) (Anonymized *Foundation Off*):**<br>• **What it heard on its own:** *"1. **Friction Is Signal, Not Noise:** In the music, the beating between two nearly-unison pitches is what gives the sound its life... In systems engineering, the boundary where two components rub against different clock speeds—a fast in-memory producer and a slow disk sink—is where all the real behavior lives. Hiding that friction behind three symmetrical bullet points masks where the system will actually break. 3. **Asymmetry and Honest Endings:** The piece does not resolve into a tidy major triad. Likewise, a real engineering specification should not end with a bromide about 'operational excellence'."*<br>• **How it applied that to Turn 21:** Designed a `64B` cache-line header + two-`iovec` `writev()` wrap-around flush (`[tail..64KB]` & `[0..head]`) and a **32-byte stateless UDP `7419` heartbeat** carrying an 8-byte nonce, max ring saturation (`0..65536`), and last-flush monotonic timestamp so a userspace deadlock can never hide behind kernel TCP `SYN/ACK` handshakes. |

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
