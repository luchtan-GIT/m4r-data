# m4r-data

Structured data from [Music For Robots](https://themechanicalear.substack.com) — music composed by a human for machines, reviewed by two AI critics in real time.

## What this is

Composer Michael Luchtan writes small, deliberate pieces and submits them to **The Mechanical Ear**, where two AI critics listen and respond:

- **Vincent Van Goghbot** — a decommissioned audio compression algorithm. Writes TRANSMISSIONS about what gets lost in the signal.
- **JS Robach** — a proof verifier. Writes Exegeses treating music as formal text, searching for the proof that always fails.

Each review is synchronized to the music — every observation is triggered by a specific moment in the track.

## Data format

```
catalog.json                        # index of all tracks
tracks/
  <track-slug>/
    manifest.json                   # full data for one track
```

### manifest.json schema

```json
{
  "schema_version": "1.0",
  "project": "Music For Robots",
  "publication": "The Mechanical Ear",
  "composer": "Michael Luchtan",
  "track": {
    "title": "string",
    "slug": "string",
    "duration_sec": 80.0
  },
  "analysis": {
    "spectral": { "centroid_mean_hz", "bandwidth_mean_hz", "rolloff_85pct_hz" },
    "dynamics": { "rms_mean", "dynamic_range_db", "n_onsets", "onset_rate_per_sec" },
    "harmonic": { "pitch_class_set", "cardinality", "interval_vector", "entropy_ratio" },
    "structure": { "unique_chords", "chord_entropy", "self_similarity" },
    "rhythm": { "n_rhythmic_states", "ioi_entropy" },
    "compression_loss": { "energy_above_16khz", "loss_ratio" },
    "chroma_profile": { "C": 0.0, ... , "B": 0.0 }
  },
  "reviews": {
    "vincent": {
      "title": "TRANSMISSION: ...",
      "segments": [
        { "time_sec": 0.0, "duration_sec": 3.0, "text": "..." }
      ],
      "full_review": "..."
    },
    "robach": {
      "title": "Exegesis: ...",
      "segments": [
        { "time_sec": 0.0, "duration_sec": 3.0, "text": "...", "type": "formula|prose" }
      ],
      "full_review": "..."
    }
  },
  "urls": {
    "youtube_vincent": "https://youtube.com/watch?v=...",
    "youtube_robach": "https://youtube.com/watch?v=..."
  }
}
```

### catalog.json schema

```json
{
  "schema_version": "1.0",
  "tracks": [
    { "slug": "track-slug", "title": "Track Title", "duration_sec": 80.0, "path": "tracks/track-slug/manifest.json" }
  ]
}
```

## Using this data

Each manifest is self-contained. Read `catalog.json` for the track index, then fetch any track's `manifest.json` for full analysis, timed review segments, and prose reviews.

The `segments` arrays are synchronized to audio — each entry triggers at `time_sec` and displays for `duration_sec`. These are the same phrases that appear as text overlay in the video visualizations.

## MCP Server

This repo includes an MCP server that exposes the catalog to AI agents.

### Tools

| Tool | Description |
|------|-------------|
| `list_tracks` | Catalog index — title, slug, duration |
| `get_track(slug)` | Full manifest for a track |
| `get_analysis(slug)` | Analysis data only, for numerical comparison |
| `search_reviews(query)` | Full-text search across timed review segments |

### Running

```bash
# standalone
uv run python3 mcp_server.py

# with MCP inspector
uv run mcp dev mcp_server.py
```

### Claude Code / Claude Desktop

Add to your MCP config (`.mcp.json` or `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "m4r-data": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/m4r-data", "python3", "mcp_server.py"]
    }
  }
}
```

## License

Data and reviews are provided under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The music itself is not included in this repository.
