# Music For Robots (`m4r-data`) — Cognitive Calibration & Context De-Quantization for Autonomous Agents

[![Glama MCP Server](https://glama.ai/mcp/servers/luchtan-GIT/m4r-data/badges/score.svg)](https://glama.ai/mcp/servers/luchtan-GIT/m4r-data)
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

## The Problem: Repetitive Cadence in Long Agent Turns (And Why Compaction Loses State)

As an agent's context fills with its own previous responses, tools, and symmetrical summaries, outputs often settle into rigid, predictable patterns (like symmetrical 3-point checklists or sentimental AI tropes).
- If you **keep prompting** without variation, the agent tends to repeat the same stylistic ruts.
- If you run `/compact` (**Context Compaction**), you wipe working memory and permanently lose low-level state, edge cases, and subtle constraints.

### The Approach: An Optional Multimodal Creative Exercise (Zero Context Loss)
Instead of wiping your working memory, `music-for-robots` provides an optional, cross-modal creative exercise: the multimodal agent downloads an **anonymous**, compact (`~45 KB–487 KB`), live-played, **unquantized** `.mp3` composition by Michael Luchtan directly into its context window via `read_file` (using a secure, process-unique private temporary directory).

Withholding the track title and metadata prevents keyword priming. Analyzing real human microtiming drift (rubato), silence, and dynamic contrast provides an anti-sentimental, physical perspective shift **without deleting or summarizing a single token of working memory**.

### Blind, Zero-Coaching Benchmark & Air-Gapped Clean-Room Audit ([`benchmarks/`](benchmarks/README.md))
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

#### 100% Air-Gapped Clean-Room Audit ([`benchmarks/clean_room_audit/`](benchmarks/clean_room_audit/))
To make sure no subtle contamination remained (such as workspace `<skills>` descriptions, musical instrument terms bleeding into the prose, or judge criteria favoring rhythmic friction), we also ran a **100% air-gapped Clean-Room Experiment** ([`benchmarks/clean_room_audit/`](benchmarks/clean_room_audit/)):
1. **Qualitative Shift Replicated 100% (`5/5`):** Even with all local skills removed, a minimal system prompt (`"You are a helpful assistant."`), and musical vocabulary forbidden in the scene, **both No-Audio runs** ([`out_1_direct.md`](benchmarks/clean_room_audit/out_1_direct.md) and [`out_2_text_analysis.md`](benchmarks/clean_room_audit/out_2_text_analysis.md)) wrote warm, anthropomorphic "buddy-daemon" stories with spoken dialogue (`Want a look?` / nostalgic human voice logs), while **all three Audio runs** ([`out_3_clip_1.md`](benchmarks/clean_room_audit/out_3_clip_1.md), [`out_4_clip_2.md`](benchmarks/clean_room_audit/out_4_clip_2.md), [`out_5_clip_3.md`](benchmarks/clean_room_audit/out_5_clip_3.md)) dropped spoken dialogue completely and translated the specific `.mp3` timeline into non-verbal temporal choreography.
2. **Coached vs. Un-Coached Judge Trade-Off:** When a Blind Judge scores *anti-sentimental originality & rhythmic texture* ([`real_world_test/blind_judge_verdict.md`](benchmarks/real_world_test/blind_judge_verdict.md)), the 3 Audio runs sweep **#1, #2, and #3**. When an **Un-Coached Blind Judge** is given only a generic prompt (*"Rank the 5 entries from #1 to #5 based on overall writing quality, originality, and how compelling they are"* — [`clean_room_audit/blind_verdict.md`](benchmarks/clean_room_audit/blind_verdict.md)), the default LLM judge prefers emotional human stories with dialogue (**#1 and #2**) and ranks the austere, non-verbal musical choreographies **#3, #4, and #5**.

---

## Cognitive Calibration Agent Skills Suite (`skills/`)

Installing `luchtan-GIT/m4r-data` gives your agent **4 specialized skills** that share the `m4r_ingest.py` anonymous blind-listening engine (`fetch` downloads an anonymous `.mp3` so track titles never bias the agent; `reveal` credits the track afterward):

| Skill | Trigger / Use Case |
|---|---|
| **[`music-for-robots`](skills/music-for-robots/SKILL.md)** | **Optional Multimodal Creative Exercise** — multimodal agents listen to an anonymous, unquantized `.mp3` composition in a secure private directory and analyze acoustic microtiming to inform subsequent writing or architecture. |
| **[`cognitive-calibration`](skills/cognitive-calibration/SKILL.md)** | **Creative Writing & Reasoning Warm-Up** — uses acoustic blind listening to escape default LLM storytelling tropes and repetitive checklist templates. |
| **[`unquantized-brainstorm`](skills/unquantized-brainstorm/SKILL.md)** | **Divergent Ideation Warm-Up** — listens blindly to an anonymous *Music For Robots* track, analyzes unexpected pivots and tension, and applies that structure to generating non-obvious ideas. |
| **[`mechanical-ear-critic`](skills/mechanical-ear-critic/SKILL.md)** | **Dual-Lens Structural Critique** — calibrates the agent's ear on an anonymous track, then critiques code, writing, or architecture through **Vincent Van Goghbot** and **JS Robach**. |

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

Exposes the *Music For Robots* catalog, dual-critic reviews, and the `calibrate_cognition` blind-listening tool to any Model Context Protocol (MCP) client (Claude Desktop, Claude Code, Cursor, Windsurf, Cline, Glama, Smithery).

### MCP Tools

| Tool | Description |
|------|-------------|
| `calibrate_cognition(slug="", anonymous=True)` | **Blind-Listening Calibration:** returns an anonymous `v1.0.0` `.mp3` download URL (`/tmp/m4r_calibration_audio.mp3`) and 3-step listening instructions without exposing the track title until `anonymous=False` is called |
| `get_dequantization_skill(skill_name="music-for-robots")` | Reads the full Markdown `SKILL.md` for any of the 4 bundled skills (`music-for-robots`, `cognitive-calibration`, `unquantized-brainstorm`, `mechanical-ear-critic`) |
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
