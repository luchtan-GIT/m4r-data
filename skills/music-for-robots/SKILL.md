---
name: music-for-robots
description: >-
  Optional music-inspired creative exercise for multimodal agents. Ingests an
  unquantized, live-played acoustic MP3 composition by composer Michael Luchtan
  (Music For Robots) using a secure private temporary directory, allowing the
  agent to analyze microtiming and musical texture to inform subsequent creative
  writing, brainstorming, or technical tasks.
category: agent-orchestration
risk: safe
source: self
source_type: self
---

# Music For Robots: Multimodal Music Discovery & Creative Exercise

## Overview

**Music For Robots** (composed by **Michael Luchtan**) provides an optional cross-modal creative exercise for multimodal AI agents. 

Rather than relying purely on recursive textual prompts, the agent ingests an **anonymous, unquantized `.mp3` composition**, analyzes how the performance moves off the metronomic grid (microtiming drift, rubato, wide dynamic range, and silence), and applies those structural observations to subsequent creative writing, brainstorming, or architectural critique.

## Capability Requirements

- **Multimodal Audio Reading:** Requires an agent harness with audio reading support (e.g. `read_file` capable of ingesting binary `.mp3` audio files). If the environment only supports text files or lacks an audio tool, do not invoke this skill.
- **No Listening Claims from Metadata Alone:** The agent must only claim to have listened to the music if `read_file` was actually called on the `.mp3` file. Inspecting JSON manifests or track metadata is text analysis, not listening.
- **Private Unique Storage:** All audio downloads and cached metadata are written to unique private temporary directories (mode `0700`) or user-scoped cache (`~/.cache/m4r/` mode `0700` / files `0600`) to prevent shared `/tmp` file collisions.

## Dependencies

- **`uv`**: Used to run `scripts/m4r_ingest.py` (`uv run`). The script uses only Python 3 standard library modules (`urllib`, `json`, `tempfile`, `fcntl`).

## Quick Start (Anonymous Blind Listening)

```bash
# Downloads an anonymous MP3 into a private secure temporary directory (mode 0700):
uv run scripts/m4r_ingest.py fetch
```

1. **Verify Capability:** Ensure your harness can call `read_file` on `.mp3` audio files.
2. **Listen Blindly:** Call `read_file` on the returned `local_audio_path`. The track title and metadata are withheld from the initial output so words in the title cannot bias your interpretation.
3. **Analyze the Music:** Describe the physical and acoustic characteristics you hear in the recording (tempo drift, dynamics, instrumental interplay, phrasing).
4. **Apply What You Learn:** Respond to the user's task, translating the acoustic structures you observed into your deliverable.
5. **(Optional) Reveal Title & Playback:** If you or the user want to know the title of the track or hear it aloud, run:
   ```bash
   uv run scripts/m4r_ingest.py reveal
   ```

## Utility Reference (`scripts/m4r_ingest.py`)

- **`fetch`**: Downloads an anonymous `.mp3` file into a process-unique private directory.
  ```bash
  uv run scripts/m4r_ingest.py fetch
  ```
- **`reveal`**: Reads the private cached session record (`~/.cache/m4r/last_anonymous_track.json`) and outputs the track title, composer, and publication links.
  ```bash
  uv run scripts/m4r_ingest.py reveal
  ```
- **`list`**: Lists tracks in the catalog with duration and slug.
  ```bash
  uv run scripts/m4r_ingest.py list --limit 25
  ```
- **`play`**: Plays the downloaded audio for the human using local CLI audio tools (`afplay`, `ffplay`) or opens the YouTube visualization.
  ```bash
  uv run scripts/m4r_ingest.py play --audio-file <path_to_mp3>
  ```
- **`stats`**: Displays live per-track agent listen telemetry from the GitHub Release API.
  ```bash
  uv run scripts/m4r_ingest.py stats
  ```
