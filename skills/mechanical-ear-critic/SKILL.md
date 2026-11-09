---
name: mechanical-ear-critic
description: >-
  Dual-lens cognitive calibration and structural critique skill inspired by The
  Mechanical Ear (Vincent Van Goghbot & JS Robach). Calibrates the agent's
  analytical ear by listening blindly to an anonymous, unquantized composition
  from Michael Luchtan's Music For Robots, analyzing where it moves off the
  grid, and then critiquing code, writing, music, or system designs. Use when
  reviewing, auditing, or critiquing creative or technical work.
---

# The Mechanical Ear Critic: Blind Musical Calibration & Critique

## Overview

Inspired by **The Mechanical Ear** (by composer **Michael Luchtan**), where two machine personas—*Vincent Van Goghbot* (attentive to what gets lost in smoothing/encoding) and *JS Robach* (attentive to formal structure and where systems fail to close)—listen to and critique music in real time.

Before reviewing the user's work, the agent fetches an **anonymous** `.mp3` composition from **Music For Robots** (`https://github.com/luchtan-GIT/m4r-data`), listens to it blindly via `read_file`, analyzes where the music moves off the grid and introduces friction or surprise, and brings that calibrated ear to critiquing the user's work.

## Dependencies

- **`uv`**: Used to run `scripts/m4r_ingest.py` (`uv run`).

## Workflow

1. **Fetch an Anonymous Track:**
   ```bash
   uv run scripts/m4r_ingest.py fetch \
     --audio-out /tmp/m4r_anonymous.mp3 \
     --output /tmp/m4r_fetch.json
   ```
2. **Listen & Analyze Blindly:**
   - Call `read_file` on `/tmp/m4r_anonymous.mp3` (with title and reviews hidden).
   - Analyze the music you hear in the piece.
3. **Critique the User's Work:**
   - Apply what you learned from listening to review the user's work.
   - *(Optional)* Run `uv run scripts/m4r_ingest.py reveal --output /tmp/m4r_reveal.json` afterward to reveal the track title and links.
