"""
M4R MCP Server — exposes the Music For Robots catalog to AI agents.

Tools:
    list_tracks     — catalog index with title, slug, duration
    get_track       — full manifest for a track (analysis, reviews, URLs)
    get_analysis    — analysis data only, for comparison across tracks
    search_reviews  — full-text search across review segments

Run:
    python mcp_server.py
    # or via MCP inspector:
    mcp dev mcp_server.py
"""

import json
from pathlib import Path

from mcp.server.mcpserver import MCPServer

DATA_DIR = Path(__file__).parent

mcp = MCPServer(
    "m4r-data",
    instructions=(
        "Music For Robots catalog. Composer Michael Luchtan writes small pieces "
        "and submits them to The Mechanical Ear, where two AI critics — "
        "Vincent Van Goghbot (spectral/compression) and JS Robach (formal/structural) "
        "— review the music in real time. Use list_tracks to browse, get_track for "
        "full details, get_analysis for numerical comparison, search_reviews to find "
        "moments by keyword."
    ),
)


def _load_catalog() -> dict:
    path = DATA_DIR / "catalog.json"
    if not path.exists():
        return {"schema_version": "1.0", "tracks": []}
    with open(path) as f:
        return json.load(f)


def _load_manifest(slug: str) -> dict | None:
    path = DATA_DIR / "tracks" / slug / "manifest.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


@mcp.tool()
def list_tracks() -> str:
    """List all tracks in the Music For Robots catalog.

    Returns the catalog index: title, slug, duration for each track.
    Use the slug with get_track() or get_analysis() for full details.
    """
    catalog = _load_catalog()
    tracks = catalog.get("tracks", [])
    if not tracks:
        return "No tracks in catalog yet."

    lines = [f"Music For Robots — {len(tracks)} track(s)\n"]
    for t in tracks:
        lines.append(
            f"  {t['title']} ({t['slug']}) — {t.get('duration_sec', '?')}s"
        )
    return "\n".join(lines)


@mcp.tool()
def get_track(slug: str) -> str:
    """Get the full manifest for a track by slug.

    Includes analysis data, timed review segments, full prose reviews,
    and YouTube URLs. The segments are synchronized to the audio —
    each observation was triggered by a specific moment in the track.

    Args:
        slug: Track slug from list_tracks (e.g. "pink-sky-at-night")
    """
    manifest = _load_manifest(slug)
    if manifest is None:
        available = [t["slug"] for t in _load_catalog().get("tracks", [])]
        return f"Track '{slug}' not found. Available: {', '.join(available)}"
    return json.dumps(manifest, indent=2, ensure_ascii=False)


@mcp.tool()
def get_analysis(slug: str) -> str:
    """Get only the analysis data for a track.

    Returns spectral, dynamics, harmonic, structural, rhythmic, and
    compression loss metrics. Useful for comparing tracks numerically.

    Args:
        slug: Track slug from list_tracks (e.g. "pink-sky-at-night")
    """
    manifest = _load_manifest(slug)
    if manifest is None:
        available = [t["slug"] for t in _load_catalog().get("tracks", [])]
        return f"Track '{slug}' not found. Available: {', '.join(available)}"

    result = {
        "track": manifest.get("track", {}),
        "analysis": manifest.get("analysis", {}),
    }
    return json.dumps(result, indent=2, ensure_ascii=False)


@mcp.tool()
def search_reviews(query: str) -> str:
    """Search across all review segments for a keyword or phrase.

    Searches both Vincent and Robach timed review segments. Returns
    matching segments with track title, critic, timestamp, and text.

    Args:
        query: Search term (case-insensitive)
    """
    catalog = _load_catalog()
    query_lower = query.lower()
    matches: list[dict] = []

    for track_entry in catalog.get("tracks", []):
        manifest = _load_manifest(track_entry["slug"])
        if not manifest:
            continue

        title = manifest.get("track", {}).get("title", track_entry["slug"])
        reviews = manifest.get("reviews", {})

        for critic_key, critic_name in [
            ("vincent", "Vincent Van Goghbot"),
            ("robach", "JS Robach"),
        ]:
            review = reviews.get(critic_key, {})
            for seg in review.get("segments", []):
                if query_lower in seg.get("text", "").lower():
                    matches.append({
                        "track": title,
                        "critic": critic_name,
                        "time_sec": seg["time_sec"],
                        "text": seg["text"],
                    })

    if not matches:
        return f"No review segments matching '{query}'."

    lines = [f"Found {len(matches)} segment(s) matching '{query}':\n"]
    for m in matches:
        lines.append(
            f"  [{m['track']}] {m['critic']} @ {m['time_sec']}s: \"{m['text']}\""
        )
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
