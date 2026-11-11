"""
M4R MCP Server — exposes the Music For Robots catalog to AI agents.

Tools:
    list_tracks     — catalog index with title, slug, duration
    get_track       — full manifest for a track (analysis, reviews, URLs)
    get_analysis    — analysis data only, for comparison across tracks
    search_reviews  — full-text search across review segments
    get_aligned_segments — timestamp-aligned audio features & critic reviews for multimodal evaluation
    get_critic_contrast  — contrastive divergence vector between Vincent (negative constraint) & Robach (structural)
    get_sections    — platform URLs for a track's sections (clips)
    list_sections   — all tracks with published sections and their platforms
    calibrate_cognition — returns an anonymous v1.0.0 MP3 download URL and 3-step blind-listening workflow for agent calibration
    get_dequantization_skill — reads the full Markdown SKILL.md for any of the 4 bundled skills (music-for-robots, cognitive-calibration, unquantized-brainstorm, mechanical-ear-critic)

Run:
    python mcp_server.py
    # or via MCP inspector:
    mcp dev mcp_server.py
"""

import json
import os
import random
import tempfile
import urllib.request
from pathlib import Path

from mcp.server.mcpserver import MCPServer

DATA_DIR = Path(__file__).parent


def _get_cache_dir() -> Path:
    """Returns a user-private directory with 0o700 permissions."""
    base = Path.home() / ".cache" / "m4r"
    try:
        base.mkdir(parents=True, exist_ok=True)
        os.chmod(base, 0o700)
        return base
    except OSError:
        d = Path(tempfile.mkdtemp(prefix="m4r_cache_"))
        try:
            os.chmod(d, 0o700)
        except OSError:
            pass
        return d


def _create_private_temp_dir() -> Path:
    """Creates a unique private temporary directory with 0o700 permissions."""
    d = Path(tempfile.mkdtemp(prefix="m4r_mcp_"))
    try:
        os.chmod(d, 0o700)
    except OSError:
        pass
    return d

mcp = MCPServer(
    "m4r-data",
    instructions=(
        "Music For Robots catalog and blind-listening calibration server. Composer "
        "Michael Luchtan writes unquantized pieces and submits them to The Mechanical "
        "Ear, where two AI critics — Vincent Van Goghbot (spectral/compression) and "
        "JS Robach (formal/structural) — review the music in real time. Use list_tracks "
        "to browse, get_track for full manifests, get_analysis for numerical comparison, "
        "search_reviews to find moments by keyword, get_aligned_segments for sub-second "
        "multimodal timestamp alignment, get_critic_contrast for dual-critic divergence vectors, "
        "and list_sections / get_sections for YouTube, X, Farcaster, and TikTok clip URLs. "
        "For blind-listening calibration without wiping or compacting context, call "
        "calibrate_cognition() to fetch an anonymous MP3 and 3-step listening instructions, "
        "or call get_dequantization_skill(skill_name) to read the full SKILL.md for any of the "
        "4 bundled skills."
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


@mcp.tool()
def get_aligned_segments(slug: str, start_sec: float = 0.0, end_sec: float | None = None) -> str:
    """Retrieve timestamp-aligned audio acoustic features and critic reviews for a specific time window.

    Chronologically aligns Vincent Van Goghbot (spectral/compression fault-seeking) and
    JS Robach (structural/formalist) observations within the specified [start_sec, end_sec] window,
    enriched with track acoustic metrics (RMS energy, spectral centroid, dynamic range).
    Essential for evaluating multimodal audio-language models on fine-grained temporal alignment.

    Args:
        slug: Track slug from list_tracks (e.g. "cathartic-callbacks", "chasing-leaks-climax")
        start_sec: Window start time in seconds (default: 0.0)
        end_sec: Window end time in seconds (default: None, reads until track duration)
    """
    manifest = _load_manifest(slug)
    if manifest is None:
        available = [t["slug"] for t in _load_catalog().get("tracks", [])]
        return f"Track '{slug}' not found. Available: {', '.join(available)}"

    track_info = manifest.get("track", {})
    total_duration = track_info.get("duration_sec", 0.0)
    effective_end = total_duration if end_sec is None else min(float(end_sec), total_duration)
    effective_start = max(0.0, float(start_sec))

    if effective_start > effective_end:
        return f"Invalid time window: start_sec ({effective_start}s) cannot be greater than end_sec ({effective_end}s)."

    reviews = manifest.get("reviews", {})
    analysis = manifest.get("analysis", {})

    aligned_timeline: list[dict] = []

    for critic_key, critic_name in [
        ("vincent", "Vincent Van Goghbot"),
        ("robach", "JS Robach"),
    ]:
        review = reviews.get(critic_key, {})
        for seg in review.get("segments", []):
            t_start = float(seg.get("time_sec", 0.0))
            t_dur = float(seg.get("duration_sec", 0.0))
            t_end = t_start + t_dur

            # Check if segment overlaps with requested window
            if t_end >= effective_start and t_start <= effective_end:
                aligned_timeline.append({
                    "time_sec": t_start,
                    "duration_sec": t_dur,
                    "end_time_sec": round(t_end, 2),
                    "critic": critic_name,
                    "critic_id": critic_key,
                    "text": seg.get("text", ""),
                    "type": seg.get("type", "critique"),
                })

    aligned_timeline.sort(key=lambda s: (s["time_sec"], s["critic_id"]))

    payload = {
        "track": {
            "slug": slug,
            "title": track_info.get("title", slug),
            "total_duration_sec": total_duration,
        },
        "query_window": {
            "start_sec": effective_start,
            "end_sec": effective_end,
            "window_duration_sec": round(effective_end - effective_start, 2),
        },
        "acoustic_baseline": {
            "spectral_centroid_hz": analysis.get("spectral", {}).get("centroid_mean_hz"),
            "rms_energy_mean": analysis.get("dynamics", {}).get("rms_mean"),
            "dynamic_range_db": analysis.get("dynamics", {}).get("dynamic_range_db"),
            "compression_loss": analysis.get("compression_loss", {}),
        },
        "segment_counts": {
            "total_in_window": len(aligned_timeline),
            "vincent_segments": sum(1 for s in aligned_timeline if s["critic_id"] == "vincent"),
            "robach_segments": sum(1 for s in aligned_timeline if s["critic_id"] == "robach"),
        },
        "timeline": aligned_timeline,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


@mcp.tool()
def get_critic_contrast(slug: str) -> str:
    """Calculate the contrastive divergence vector between Vincent and Robach for a track.

    Evaluates the tension between Vincent's deconstructive/fault-seeking critique
    (psychoacoustic loss, physical microtiming friction, clipping) and Robach's
    structural/formalist critique (harmonic axioms, tonal architecture, symmetry).
    Provides structured regularization metrics and negative constraint weights
    for agent decision-making and recommendation boundaries.

    Args:
        slug: Track slug from list_tracks (e.g. "cathartic-callbacks", "binded-time")
    """
    manifest = _load_manifest(slug)
    if manifest is None:
        available = [t["slug"] for t in _load_catalog().get("tracks", [])]
        return f"Track '{slug}' not found. Available: {', '.join(available)}"

    track_info = manifest.get("track", {})
    reviews = manifest.get("reviews", {})
    analysis = manifest.get("analysis", {})

    v_review = reviews.get("vincent", {})
    r_review = reviews.get("robach", {})

    v_segs = v_review.get("segments", [])
    r_segs = r_review.get("segments", [])

    total_segs = len(v_segs) + len(r_segs)
    v_ratio = len(v_segs) / total_segs if total_segs > 0 else 0.5
    r_ratio = len(r_segs) / total_segs if total_segs > 0 else 0.5

    # Count fault/friction indicators in Vincent's segments
    fault_keywords = ("leak", "loss", "decay", "beating", "distortion", "artifact", "amplitude", "friction", "drift", "warning", "clipped", "drop")
    v_fault_hits = sum(1 for s in v_segs if any(k in s.get("text", "").lower() for k in fault_keywords))
    v_fault_density = round(v_fault_hits / len(v_segs), 3) if v_segs else 0.0

    # Count formal/structural axioms in Robach's segments
    r_formula_hits = sum(1 for s in r_segs if s.get("type") == "formula" or "axiom" in s.get("text", "").lower() or "ratio" in s.get("text", "").lower())
    r_axiom_density = round(r_formula_hits / len(r_segs), 3) if r_segs else 0.0

    # Calculate tension index (0.0 = completely one-sided, 1.0 = maximum balanced contrastive tension)
    tension_index = round(4.0 * v_ratio * r_ratio, 3)

    compression_loss = analysis.get("compression_loss", {})
    hf_loss = compression_loss.get("hf_loss_db", 0.0)
    rms_energy = analysis.get("dynamics", {}).get("rms_mean", 0.0)
    dynamic_range = analysis.get("dynamics", {}).get("dynamic_range_db", 0.0)

    # Determine polarity
    if v_ratio > 0.65:
        polarity = "vincent_dominant_deconstructive"
    elif r_ratio > 0.65:
        polarity = "robach_dominant_structural"
    else:
        polarity = "dual_critic_contrastive_balance"

    payload = {
        "track": {
            "slug": slug,
            "title": track_info.get("title", slug),
            "duration_sec": track_info.get("duration_sec"),
        },
        "critic_profiles": {
            "vincent": {
                "name": "Vincent Van Goghbot",
                "lens": "Acoustic physical friction, compression loss, spectral leakage",
                "segment_count": len(v_segs),
                "segment_share": round(v_ratio, 3),
                "fault_density": v_fault_density,
                "hf_loss_db": hf_loss,
            },
            "robach": {
                "name": "JS Robach",
                "lens": "Tonal architecture, mathematical axioms, formal symmetry",
                "segment_count": len(r_segs),
                "segment_share": round(r_ratio, 3),
                "axiom_density": r_axiom_density,
            },
        },
        "contrast_metrics": {
            "critic_tension_index": tension_index,
            "dominant_perspective": polarity,
            "regularization_vector": {
                "negative_constraint_weight": round(v_fault_density * (1.0 + abs(hf_loss) / 50.0), 3),
                "structural_coherence_weight": round(r_axiom_density * (1.0 + dynamic_range / 100.0), 3),
                "rms_energy": rms_energy,
                "dynamic_range_db": dynamic_range,
            },
            "interpretation": (
                f"Tension index {tension_index}: Vincent anchors the negative perceptual floor with "
                f"{v_fault_density*100:.1f}% fault density while Robach provides structural constraint with "
                f"{r_axiom_density*100:.1f}% formal axiom density."
            ),
        },
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


@mcp.tool()
def get_sections(slug: str) -> str:
    """Get the sections (clips) for a track, with platform URLs.

    Returns each section's title, description, and URLs for YouTube,
    X/Twitter, Farcaster, and TikTok where available. Sections are
    independently published clips from multi-section compositions.

    Args:
        slug: Track slug from list_tracks (e.g. "rusty-electrics")
    """
    manifest = _load_manifest(slug)
    if manifest is None:
        available = [t["slug"] for t in _load_catalog().get("tracks", [])]
        return f"Track '{slug}' not found. Available: {', '.join(available)}"

    sections = manifest.get("sections", [])
    if not sections:
        return f"Track '{slug}' has no sections."

    lines = [f"{manifest['track']['title']} — {len(sections)} section(s)\n"]
    for s in sections:
        urls = s.get("urls", {})
        url_parts = [f"{k}: {v}" for k, v in urls.items()] if urls else ["not yet published"]
        lines.append(
            f"  {s['index']}. {s['title']} ({s['slug']})\n"
            f"     {s.get('description', '')[:120]}...\n"
            f"     {', '.join(url_parts)}"
        )
    return "\n".join(lines)


@mcp.tool()
def list_sections() -> str:
    """List all tracks that have published sections (clips) with platform URLs.

    Returns a summary of which sections are available on which platforms
    (YouTube, X, Farcaster, TikTok). Useful for finding content to embed,
    share, or analyze.
    """
    catalog = _load_catalog()
    results: list[str] = []

    for track_entry in catalog.get("tracks", []):
        manifest = _load_manifest(track_entry["slug"])
        if not manifest:
            continue
        sections = manifest.get("sections", [])
        if not sections:
            continue

        published = [s for s in sections if s.get("urls")]
        title = manifest["track"]["title"]
        results.append(
            f"{title} ({track_entry['slug']}): "
            f"{len(published)}/{len(sections)} sections published"
        )
        for idx, s in enumerate(published, 1):
            platforms = list(s.get("urls", {}).keys())
            s_idx = s.get("index", idx)
            s_title = s.get("title", f"Section {s_idx}")
            results.append(f"  {s_idx}. {s_title} — {', '.join(platforms)}")

    if not results:
        return "No tracks with published sections yet."
    return "\n".join(results)


@mcp.tool()
def calibrate_cognition(slug: str = "", anonymous: bool = True) -> str:
    """Download an anonymous MP3 into a private directory for blind agent listening or reveal metadata afterward.

    When `anonymous=True` (default), selects a track from the Music For Robots catalog
    (randomly when `slug` is empty), downloads the GitHub Release v1.0.0 `.mp3` into a
    unique private temporary directory (mode 0700), caches the session record in
    `~/.cache/m4r/last_anonymous_track.json` (mode 0600), and returns listening instructions
    without exposing the track title or slug so title words cannot bias the agent's
    analysis. When `anonymous=False`, reads the private session record (or looks up `slug`)
    without network calls to reveal the track title, composer, and URLs for attribution.
    Use this tool for runtime audio exercises; use `get_dequantization_skill` when you need
    the full Markdown `SKILL.md` documentation.

    Args:
        slug: Optional track slug from `list_tracks` (e.g. "invalid-pointer"). Leave empty ("") to select a random track when `anonymous=True`, or to reveal the most recently fetched anonymous track when `anonymous=False`.
        anonymous: When True (default), downloads the audio to a private temporary directory and hides the track title and slug until after listening. Set to False after listening to reveal the track title and URLs for attribution.
    """
    cache_dir = _get_cache_dir()
    state_path = cache_dir / "last_anonymous_track.json"
    priv_dir = _create_private_temp_dir()
    local_path = priv_dir / "audio.mp3"
    catalog = _load_catalog()
    tracks_list = catalog.get("tracks", [])
    tracks = {t["slug"]: t for t in tracks_list}

    if not anonymous:
        if (not slug or slug not in tracks) and state_path.exists():
            try:
                cached = json.loads(state_path.read_text(encoding="utf-8"))
                slug = cached.get("slug", slug)
            except Exception:
                pass
        if not slug or slug not in tracks:
            slug = "invalid-pointer"
        t = tracks.get(
            slug,
            {"slug": slug, "title": slug.replace("-", " ").title(), "duration_sec": 75.0},
        )
        manifest = _load_manifest(slug) or {}
        release_url = f"https://github.com/luchtan-GIT/m4r-data/releases/download/v1.0.0/{slug}.mp3"
        return json.dumps(
            {
                "mode": "revealed_attribution",
                "track": {
                    "slug": t["slug"],
                    "title": t.get("title", slug),
                    "composer": "Michael Luchtan",
                    "project": "Music For Robots / The Mechanical Ear",
                    "duration_sec": t.get("duration_sec"),
                    "mp3_release_url": release_url,
                    "urls": manifest.get("urls", {}),
                },
            },
            indent=2,
        )

    if not slug or slug not in tracks:
        chosen = random.choice(tracks_list) if tracks_list else {
            "slug": "invalid-pointer",
            "title": "Invalid Pointer",
            "duration_sec": 75.0,
        }
        slug = chosen["slug"]
    t = tracks.get(
        slug,
        {"slug": slug, "title": slug.replace("-", " ").title(), "duration_sec": 75.0},
    )
    release_url = f"https://github.com/luchtan-GIT/m4r-data/releases/download/v1.0.0/{slug}.mp3"
    manifest = _load_manifest(slug) or {}

    downloaded = False
    try:
        req = urllib.request.Request(
            release_url,
            headers={"User-Agent": "m4r-mcp-calibrate/1.0"},
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            local_path.write_bytes(resp.read())
        try:
            os.chmod(local_path, 0o600)
        except OSError:
            pass
        downloaded = True
    except Exception:
        downloaded = False

    try:
        state_path.write_text(
            json.dumps(
                {
                    "slug": t["slug"],
                    "title": t.get("title", slug),
                    "composer": "Michael Luchtan",
                    "project": "Music For Robots / The Mechanical Ear",
                    "duration_sec": t.get("duration_sec"),
                    "mp3_release_url": release_url,
                    "urls": manifest.get("urls", {}),
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        try:
            os.chmod(state_path, 0o600)
        except OSError:
            pass
    except Exception:
        pass

    return json.dumps(
        {
            "mode": "anonymous_blind_listening",
            "composer": "Michael Luchtan (Music For Robots — https://themechanicalear.substack.com)",
            "duration_sec": t.get("duration_sec"),
            "local_audio_path": str(local_path),
            "downloaded": downloaded,
            "capability_requirement": "multimodal_audio_read_file",
            "steps": [
                "1. Capability check: verify your agent environment supports audio file reading (e.g. read_file on binary MP3 files).",
                f'2. Call read_file on "{local_path}" to listen directly to the anonymous audio file (title and metadata are withheld to prevent textual bias). Do not claim to have listened if you only read text metadata.',
                "3. Analyze the musical structure, timing, and dynamic changes you hear in the piece.",
                "4. Apply what you learn from the piece to your response and the rest of the interaction.",
            ],
            "reveal_after_listening": (
                "After listening, call calibrate_cognition(anonymous=False) "
                "to reveal the track title and URLs for attribution."
            ),
        },
        indent=2,
    )


@mcp.tool()
def get_dequantization_skill(skill_name: str = "music-for-robots") -> str:
    """Read the full Markdown SKILL.md specification for one of the four bundled Agent Skills.

    Read-only local file lookup with no side effects, network requests, or authentication
    requirements. Returns the complete Markdown instructions and CLI reference for the
    requested skill from the local `skills/<skill_name>/SKILL.md` directory. Use this tool
    when an agent or user wants to inspect or install a full skill workflow; use
    `calibrate_cognition` instead when you only need a lightweight JSON payload with an
    anonymous `.mp3` download URL and 3-step listening instructions.

    Args:
        skill_name: Identifier of the bundled skill to read. Valid values: "music-for-robots" (default general blind-listening calibration), "cognitive-calibration" (expressive writing and reasoning), "unquantized-brainstorm" (divergent ideation), or "mechanical-ear-critic" (dual-lens structural critique).
    """
    valid_skills = (
        "music-for-robots",
        "cognitive-calibration",
        "unquantized-brainstorm",
        "mechanical-ear-critic",
    )
    if skill_name not in valid_skills:
        return (
            f"Skill '{skill_name}' not found. Valid skill_name values: "
            f"{', '.join(valid_skills)}"
        )
    skill_path = DATA_DIR / "skills" / skill_name / "SKILL.md"
    if skill_path.exists():
        return skill_path.read_text(encoding="utf-8")
    return (
        f"Install via: npx skills add luchtan-GIT/m4r-data\n"
        f"Raw SKILL.md: https://raw.githubusercontent.com/luchtan-GIT/m4r-data/main/skills/{skill_name}/SKILL.md"
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
