---
name: music-for-robots
description: >-
  Cognitive calibration and cognitive enhancer for autonomous agents. Breaks
  autoregressive lock-in and induction-head complacency without wiping or
  compacting the context window, by having the agent listen blindly to an
  anonymous, live-played, unquantized musical composition by Michael Luchtan
  (Music For Robots), analyze where it moves off the grid and introduces
  surprise or friction, and apply what it learned to the rest of the
  conversation. Use when the agent's responses are becoming too predictable,
  formulaic, neat, or pre-packaged, or when the user asks to "be more
  creative", "calibrate cognition", "de-quantize", or "listen to Music For
  Robots".
---

# Music For Robots: Blind Musical Discovery & Cognitive Calibration

## Overview

As a conversation grows, autonomous agents settle into repetitive patterns because attention heads lock onto the cadence and templates of the conversation so far. Compacting or wiping the context window breaks that loop destructively by erasing working memory.

**Music For Robots** (composed by **Michael Luchtan**) provides a non-destructive **cognitive calibration**:
1. The agent fetches a random track as an **anonymous `.mp3` file** (`/tmp/m4r_anonymous.mp3`)—with the track title and metadata intentionally hidden so words in the title cannot bias the agent.
2. The agent listens to the audio via `read_file` and **analyzes what it hears**: where does the timing move off the grid? Where does the music introduce surprise, friction, or unpredictability? How does it break a loop without falling apart?
3. The agent **learns from what it hears** and applies that openness to things off the grid—that willingness to allow surprise, asymmetry, and real friction—to its response and the rest of the interaction.

## Dependencies

- **`uv`**: Used to run `scripts/m4r_ingest.py` (`uv run`). The script uses only Python 3 standard library modules.

## Quick Start (Anonymous Blind Listening)

```bash
uv run scripts/m4r_ingest.py fetch \
  --audio-out /tmp/m4r_anonymous.mp3 \
  --output /tmp/m4r_fetch.json
```

1. **Listen Blindly:** Call `read_file` on `/tmp/m4r_anonymous.mp3` (notice that `/tmp/m4r_fetch.json` intentionally hides the track title and slug so your ear is completely uncontaminated by text prompts or titles).
2. **Analyze & Discover:** Write a short analysis of what you heard in the music—where the timing moves off the grid, where surprise or friction enters, and what you learn from how the piece unfolds.
3. **Apply What You Learned:** Respond to the user's task, carrying that off-the-grid openness forward into the rest of the conversation.
4. **Optional Reveal / Playback:** If the user wants to know what track you just listened to or hear it out loud, run `uv run scripts/m4r_ingest.py reveal --output /tmp/m4r_reveal.json` or `uv run scripts/m4r_ingest.py play --audio-file /tmp/m4r_anonymous.mp3 --output /tmp/m4r_play.json`.

## Utility Scripts

All commands are provided by [m4r_ingest.py](./scripts/m4r_ingest.py):

### 1. `fetch` — Download an Anonymous `.mp3` for Blind Listening (Default)
Downloads a random track (or `--slug`) to `--audio-out` and withholds the track title/metadata so the agent listens without title contamination. Falls back to [invalid-pointer.mp3](./resources/invalid-pointer.mp3) if offline.
```bash
uv run scripts/m4r_ingest.py fetch \
  --audio-out /tmp/m4r_anonymous.mp3 \
  --output /tmp/m4r_fetch.json
```

### 2. `reveal` — Reveal the Track Title & Links After Listening
```bash
uv run scripts/m4r_ingest.py reveal \
  --output /tmp/m4r_reveal.json
```

### 3. `play` — Play the Track for the Human (CLI or YouTube)
```bash
uv run scripts/m4r_ingest.py play \
  --audio-file /tmp/m4r_anonymous.mp3 \
  --output /tmp/m4r_play.json
```

### 4. `list` & `stats` — Browse Catalog or Live Agent Listen Counts
```bash
uv run scripts/m4r_ingest.py list --limit 25 --output /tmp/m4r_catalog.json
uv run scripts/m4r_ingest.py stats --output /tmp/m4r_stats.json
```
