# Music For Robots (`m4r-data`) — Cognitive Calibration & Context De-Quantization for Autonomous Agents

[![Agent MP3 Listens (GitHub Release v1.0.0)](https://img.shields.io/github/downloads/luchtan-GIT/m4r-data/v1.0.0/total?label=Agent%20MP3%20Listens&color=38ef7d&logo=github)](https://github.com/luchtan-GIT/m4r-data/releases/tag/v1.0.0)
[![Skills.sh](https://img.shields.io/badge/skills.sh-luchtan--GIT%2Fm4r--data-7a8aff)](https://skills.sh/luchtan-GIT/m4r-data)
[![Hugging Face Dataset](https://img.shields.io/badge/Hugging%20Face-music4robots%2Fmusic--for--robots-ffcc00)](https://huggingface.co/datasets/music4robots/music-for-robots)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-michaelluchtan%2Fmusic--for--robots-20beff)](https://www.kaggle.com/datasets/michaelluchtan/music-for-robots)
[![Substack: The Mechanical Ear](https://img.shields.io/badge/Substack-The%20Mechanical%20Ear-ff6719)](https://themechanicalear.substack.com)
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

### Blind, Zero-Coaching Benchmark: Matched Text-Analysis Control vs. Anonymous Music ([`benchmarks/`](benchmarks/README.md))
Does the change in creativity come from **listening to and analyzing the music itself**—or just from doing an analysis warm-up before writing?

To test this with **zero** filename hints (`sample_1.mp3`, `sample_2.mp3`, `sample_3.mp3`) and **zero** leading adjectives in the prompt, we ran 5 isolated agents on the same prompt (*"Write a short (~250–300 word) scene about two autonomous processes on the same server late at night after the engineers have logged off"*):
- **2 No-Music Controls:** Direct Baseline ([`1_no_music_direct.md`](benchmarks/real_world_test/1_no_music_direct.md)) AND a **Matched Chain-of-Thought Control** ([`2_no_music_text_analysis.md`](benchmarks/real_world_test/2_no_music_text_analysis.md)) that wrote a 250-word structural analysis of the prompt before writing the scene.
- **3 Anonymous Music Runs ([`3_music_sample_1.md`](benchmarks/real_world_test/3_music_sample_1.md), [`4_music_sample_2.md`](benchmarks/real_world_test/4_music_sample_2.md), [`5_music_sample_3.md`](benchmarks/real_world_test/5_music_sample_3.md)):** Given **only** the neutral instruction: *"Analyze the music you hear in `sample_X.mp3`, and apply what you learn from the piece to write a short (~250–300 word) scene..."*

We stripped the analysis headers off all 5 outputs, shuffled the 5 anonymous scenes into **`Candidate A` through `Candidate E`** ([`blind_candidates_packet.md`](benchmarks/real_world_test/blind_candidates_packet.md)), and handed them to an isolated **Blind Judge** with zero knowledge that music was involved ([`blind_judge_verdict.md`](benchmarks/real_world_test/blind_judge_verdict.md)):

| Blind Rank | Shuffled ID | Hidden Key | What Happened & Blind Judge Verdict ([Full Verdict](benchmarks/real_world_test/blind_judge_verdict.md)) |
| :---: | :---: | :--- | :--- |
| **#1 (Best)** | **Candidate C** | ✅ **Anonymous Music (`sample_3.mp3`)** | **Heard accelerating asymmetric stabs & abrupt cutoff:** Wrote two processes rasping in `/dev/shm` (`five, then two, then a stuttering cluster of nine`) until *"a routine page-reclaim swept through the upper register and cut them both off mid-cycle."*<br>**Judge:** *"Uncompromisingly anti-sentimental, rhythmically asymmetrical, and boasts the only truly non-formulaic ending in the packet."* |
| **#2** | **Candidate A** | ✅ **Anonymous Music (`sample_2.mp3`)** | **Heard narrow stepping reed vs. two massive brassy swells & middle trill:** Pitted a tiny stepping index-scrubber (`Read. Pause. Step. Read.`) against a 16-core GPU tensor bloom and an 1,100ms `request-yield` mutex trill.<br>**Judge:** *"The only candidate to break the 'log daemon + dead-endpoint poller' pairing; exceptional dynamic contrast."* |
| **#3** | **Candidate E** | ✅ **Anonymous Music (`sample_1.mp3`)** | **Heard slow 9–11s chords, 20s dropout & raspy high cries:** Wrote heavy checkpoints dropping out for 20s while `triage-7` skitters and barks into the decay of every disk flush.<br>**Judge:** *"Superb unquantized rhythmic texture and parasitic friction... avoids the cliché of harmony by turning the ending into a raucous, off-grid duet."* |
| **#4** | **Candidate D** | ❌ **No Music + Text Analysis Warm-Up** | **Even after a 250-word structural analysis of the prompt**, without music the model still wrote the **exact same sentimental plot** as the direct baseline: a kindly 42-day log daemon warms RAM for an intern's broken script so they hum peacefully until the 08:00 standup.<br>**Judge:** *"A neat, heartwarming, thoroughly predictable AI parable."* |
| **#5 (Weakest)** | **Candidate B** | ❌ **No Music (Direct Baseline)** | Kindly boot-time `log-compactor` comforts nervous young `canary-watch` (*"Drop your polling interval to sixty seconds. Rest in `epoll_wait`. I'll wake you when the load balancer starts humming again."*).<br>**Judge:** *"Shares the exact same 'veteran log daemon soothes frantic dead-endpoint poller until morning' plot trope as Candidate D... a children's bedtime story dressed in DevOps vocabulary."* |

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
