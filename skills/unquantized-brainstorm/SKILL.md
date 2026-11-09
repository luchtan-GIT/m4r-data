---
name: unquantized-brainstorm
description: >-
  Cognitive enhancer for brainstorming, ideation, and creative problem-solving.
  Breaks associative ruts and predictable idea generation without compacting
  context by having the agent listen blindly to an anonymous, unquantized
  musical composition (Michael Luchtan's Music For Robots), analyze where it
  moves off the grid, and apply that unpredictability to generating ideas. Use
  when brainstorming product features, architectures, creative concepts, or when
  the user says "surprise me", "think outside the box", or "give me non-obvious
  ideas".
---

# Unquantized Brainstorm: Blind Musical Discovery for Ideation

## Overview

When asked to brainstorm, LLMs often return the same cluster of safe, predictable ideas. **Unquantized Brainstorm** uses **Michael Luchtan's *Music For Robots*** as a cross-modal cognitive enhancer: before generating ideas, the agent downloads an **anonymous**, human-played `.mp3` composition, listens to it via `read_file`, analyzes where the music moves off the grid and introduces surprise or friction, and applies what it learned from the music to generate non-obvious ideas.

## Dependencies

- **`uv`**: Used to run `scripts/m4r_ingest.py` (`uv run`).

## Workflow

1. **Fetch an Anonymous Track:**
   ```bash
   uv run scripts/m4r_ingest.py fetch \
     --audio-out /tmp/m4r_anonymous.mp3 \
     --output /tmp/m4r_fetch.json
   ```
2. **Listen & Analyze:**
   - Call `read_file` on `/tmp/m4r_anonymous.mp3` (without knowing the title or metadata).
   - Analyze the music you hear in the piece.
3. **Apply What You Learn to Brainstorming:**
   - Apply what you learned from listening to the piece to generate ideas for the user's problem.
   - *(Optional)* Run `uv run scripts/m4r_ingest.py reveal --output /tmp/m4r_reveal.json` afterward to reveal the track title and playback links.
