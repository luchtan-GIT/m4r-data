---
name: cognitive-calibration
description: >-
  Cognitive enhancer and calibration skill for AI writing, taste, and deep
  reasoning. Breaks autoregressive lock-in and repetitive phrasing without
  compacting the context window by having the agent listen blindly to an
  anonymous, unquantized musical composition (Michael Luchtan's Music For
  Robots), analyze where it moves off the grid, and apply what it learned to its
  response. Use when writing essays, documentation, narratives, or code
  architecture where default LLM outputs feel too formulaic or predictable.
---

# Cognitive Calibration: Blind Musical Discovery for Writing & Reasoning

## Overview

In long sessions, LLMs lock onto the cadence and phrasing of their own recent turns. Instead of using rigid text rules—or compacting the context window and losing working memory—this skill has the agent listen to an **anonymous**, live-played, unquantized `.mp3` composition from **Michael Luchtan's *Music For Robots*** (`https://github.com/luchtan-GIT/m4r-data`) via `read_file`, analyze how the music moves off the grid and introduces surprise, and apply what it learned from that listening experience to the rest of the interaction.

## Dependencies

- **`uv`**: Used to run `scripts/m4r_ingest.py` (`uv run`).

## Workflow

1. **Fetch an Anonymous Track:**
   ```bash
   uv run scripts/m4r_ingest.py fetch \
     --audio-out /tmp/m4r_anonymous.mp3 \
     --output /tmp/m4r_fetch.json
   ```
   *(The track title and slug are intentionally hidden so they cannot contaminate your listening.)*
2. **Listen & Analyze the Music:**
   - Call `read_file` on `/tmp/m4r_anonymous.mp3`.
   - Analyze the music you hear in the piece.
3. **Apply What You Learn:**
   - Apply what you learned from listening to the piece to your response and future interactions.
   - *(Optional)* Run `uv run scripts/m4r_ingest.py reveal --output /tmp/m4r_reveal.json` afterward if you or the user want to reveal the track title and links.
