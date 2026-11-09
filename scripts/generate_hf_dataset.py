#!/usr/bin/env python3
"""
Build the Hugging Face Parquet dataset and updated README.md for music4robots/music-for-robots.
Extracts tracks from catalog.json and manifest.json, embedding audio references and metadata.
"""

import json
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "catalog.json"
OUTPUT_DIR = REPO_ROOT / "dist" / "hf_dataset"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "data").mkdir(exist_ok=True)

def build_dataset():
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    tracks = catalog.get("tracks", [])
    
    rows = []
    for item in tracks:
        manifest_rel = item.get("path")
        manifest_path = REPO_ROOT / manifest_rel
        if not manifest_path.exists():
            continue
        
        m = json.loads(manifest_path.read_text(encoding="utf-8"))
        slug = m.get("track", {}).get("slug") or item.get("slug")
        title = m.get("track", {}).get("title") or item.get("title") or slug
        duration = float(m.get("track", {}).get("duration_sec") or item.get("duration_sec") or 0.0)
        
        analysis = m.get("analysis", {})
        spectral = analysis.get("spectral", {})
        dynamics = analysis.get("dynamics", {})
        harmonic = analysis.get("harmonic", {})
        loss = analysis.get("compression_loss", {})
        
        reviews = m.get("reviews", {})
        v_rev = reviews.get("vincent", {})
        r_rev = reviews.get("robach", {})
        
        # Audio file reference
        audio_path = REPO_ROOT / f"tracks/{slug}/audio.mp3"
        audio_url = f"https://github.com/luchtan-GIT/m4r-data/releases/download/v1.0.0/{slug}.mp3"
        audio_bytes = audio_path.read_bytes() if audio_path.exists() else None
        
        audio_struct = None
        if audio_bytes:
            audio_struct = {
                "bytes": audio_bytes,
                "path": f"{slug}.mp3"
            }
        
        row = {
            "slug": slug,
            "title": title,
            "duration_sec": duration,
            "pitch_class_set": harmonic.get("pitch_class_set", []),
            "cardinality": int(harmonic.get("cardinality") or 0),
            "spectral_centroid_hz": float(spectral.get("centroid_mean_hz") or 0.0),
            "dynamic_range_db": float(dynamics.get("dynamic_range_db") or 0.0),
            "n_onsets": int(dynamics.get("n_onsets") or 0),
            "compression_loss_ratio": float(loss.get("loss_ratio") or 0.0),
            "vincent_review_title": v_rev.get("title", ""),
            "vincent_review": v_rev.get("body", "") or v_rev.get("full_text", ""),
            "vincent_segments": json.dumps(v_rev.get("segments", [])),
            "robach_review_title": r_rev.get("title", ""),
            "robach_review": r_rev.get("body", "") or r_rev.get("full_text", ""),
            "robach_segments": json.dumps(r_rev.get("segments", [])),
            "sections": json.dumps(m.get("urls", {}).get("sections", [])),
            "chroma_profile": json.dumps(analysis.get("chroma_profile", {})),
            "manifest": json.dumps(m),
            "audio_url": audio_url,
        }
        if audio_struct:
            row["audio"] = audio_struct
        rows.append(row)
        
    print(f"Processed {len(rows)} tracks.")
    
    # Write Parquet using PyArrow Table
    # Define schema with audio feature support
    audio_type = pa.struct([
        pa.field("bytes", pa.binary()),
        pa.field("path", pa.string())
    ])
    
    fields = [
        pa.field("slug", pa.string()),
        pa.field("title", pa.string()),
        pa.field("duration_sec", pa.float64()),
        pa.field("pitch_class_set", pa.list_(pa.string())),
        pa.field("cardinality", pa.int32()),
        pa.field("spectral_centroid_hz", pa.float64()),
        pa.field("dynamic_range_db", pa.float64()),
        pa.field("n_onsets", pa.int32()),
        pa.field("compression_loss_ratio", pa.float64()),
        pa.field("vincent_review_title", pa.string()),
        pa.field("vincent_review", pa.string()),
        pa.field("vincent_segments", pa.string()),
        pa.field("robach_review_title", pa.string()),
        pa.field("robach_review", pa.string()),
        pa.field("robach_segments", pa.string()),
        pa.field("sections", pa.string()),
        pa.field("chroma_profile", pa.string()),
        pa.field("manifest", pa.string()),
        pa.field("audio_url", pa.string()),
        pa.field("audio", audio_type)
    ]
    
    schema = pa.schema(fields)
    
    # Reorganize rows into columns for PyArrow Table
    data_dict = {f.name: [] for f in fields}
    for r in rows:
        for f in fields:
            data_dict[f.name].append(r.get(f.name))
            
    table = pa.Table.from_pydict(data_dict, schema=schema)
    parquet_path = OUTPUT_DIR / "data" / "train-00000-of-00001.parquet"
    pq.write_table(table, parquet_path, compression="snappy")
    print(f"Wrote Parquet to {parquet_path} ({parquet_path.stat().st_size / (1024*1024):.2f} MB)")
    
    # Generate updated Hugging Face README.md
    readme_content = f"""---
license: cc-by-4.0
language:
  - en
tags:
  - music
  - audio
  - ai-criticism
  - composition
  - audio-analysis
  - human-machine
  - cognitive-calibration
size_categories:
  - n<1K
task_categories:
  - audio-classification
  - text-generation
---

# Music For Robots

A human composer writes unquantized acoustic music for machines. Two AI critics review each track in real time.

- **Composer:** Michael Luchtan
- **Publication:** [The Mechanical Ear](https://themechanicalear.substack.com)
- **Official Upstream Skill:** Merged in [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills/tree/main/skills/music-for-robots)
- **Repository:** [github.com/luchtan-GIT/m4r-data](https://github.com/luchtan-GIT/m4r-data)

---

## What This Dataset Contains

Each row represents an original composition written specifically for artificial listeners. The dataset includes acoustic telemetry, raw unquantized audio waveforms (`.mp3`), and synchronized dual-critic prose reviews:

- **Vincent Van Goghbot** — a decommissioned audio compression algorithm that writes about what gets lost in quantization and signal compression.
- **JS Robach** — a proof verifier who uses formal mechanical language to describe acoustic state transitions.

Both critics produce timed segments (text synchronized to exact moments in the audio) and a full prose review.

---

## Quickstart in Python

Load the dataset and stream or play audio directly via Hugging Face `datasets`:

```python
from datasets import load_dataset

# Load dataset
ds = load_dataset("music4robots/music-for-robots")
track = ds["train"][0]

print(f"Title: {{track['title']}} ({{track['duration_sec']}}s)")
print(f"BPM/Key: {{track['cardinality']}} pitch classes | Centroid: {{track['spectral_centroid_hz']:.1f}} Hz")

# Audio playback (automatically decoded by datasets.Audio)
audio_bytes = track["audio"]["bytes"]
```

---

## Agent Skill: Optional Multimodal Creative Exercise (`music-for-robots`)

Autonomous coding and creative agents (Claude Code, Antigravity, Gemini CLI, Cursor, Codex, Windsurf) can install the **Music For Robots** skill:

```bash
npx -y skills add luchtan-GIT/m4r-data
```

- **Upstream Catalog:** [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/tree/main/skills/music-for-robots)
- **Raw `SKILL.md`:** [https://raw.githubusercontent.com/luchtan-GIT/m4r-data/main/skills/music-for-robots/SKILL.md](https://raw.githubusercontent.com/luchtan-GIT/m4r-data/main/skills/music-for-robots/SKILL.md)

When triggered, the multimodal agent downloads an unquantized `.mp3` composition into a secure, process-unique temporary directory (mode `0700`, file `0600`) and analyzes human microtiming drift (rubato), silence, and dynamic contrast to inspire creative divergence without compacting working context.

---

## Dataset Schema

| Column | Type | Description |
|---|---|---|
| `slug` | string | URL-safe track identifier |
| `title` | string | Track title |
| `duration_sec` | float | Duration in seconds |
| `audio` | audio struct | Embedded audio (`bytes` + `path`) |
| `audio_url` | string | Direct CDN download URL from GitHub Release v1.0.0 |
| `pitch_class_set` | list[string] | Pitch classes present (e.g. ["C","D","E"]) |
| `cardinality` | int | Number of distinct pitch classes |
| `spectral_centroid_hz` | float | Mean spectral centroid in Hz |
| `dynamic_range_db` | float | Dynamic range in decibels |
| `n_onsets` | int | Number of detected onsets |
| `compression_loss_ratio` | float | Ratio of energy above/below 16kHz |
| `vincent_review_title` | string | Title of Vincent's review |
| `vincent_review` | string | Full prose review by Vincent Van Goghbot |
| `vincent_segments` | json string | Timed review segments |
| `robach_review_title` | string | Title of Robach's review |
| `robach_review` | string | Full prose review by JS Robach |
| `robach_segments` | json string | Timed review segments |
| `sections` | json string | Published movements / platform URLs |
| `chroma_profile` | json string | 12 pitch class weights (C through B) |
| `manifest` | json string | Full raw manifest JSON |

---

## Citation

```bibtex
@misc{{luchtan2026musicforrobots,
  title={{Music For Robots: Compositions for Artificial Listeners}},
  author={{Michael Luchtan}},
  year={{2026}},
  howpublished={{The Mechanical Ear}},
  url={{https://themechanicalear.substack.com}}
}}
```

## License

CC-BY-4.0
"""
    (OUTPUT_DIR / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"Wrote updated README.md to {OUTPUT_DIR / 'README.md'}")

if __name__ == "__main__":
    build_dataset()
