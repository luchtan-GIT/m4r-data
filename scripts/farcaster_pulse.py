#!/usr/bin/env python3
"""
scripts/farcaster_pulse.py — Music For Robots Farcaster Integration (@mechanicalear)

Automates high-signal, rich-media casts to Farcaster via Neynar v2 API:
- Track spotlights with real-time AI critic prose (Vincent Van Goghbot & JS Robach)
- Interactive web player embeds (Hugging Face Spaces)
- Notification & mention checking for interactive community engagement
- Safe state tracking in .farcaster_state.json
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = REPO_ROOT / ".farcaster_state.json"
CATALOG_FILE = REPO_ROOT / "catalog.json"
HF_SPACE_URL = "https://huggingface.co/spaces/music4robots/cognitive-calibration-demo"
HF_DATASET_URL = "https://huggingface.co/datasets/music4robots/music-for-robots"

def load_env():
    env = {}
    env_path = Path.home() / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip().strip('"\'')
    for k in ["NEYNAR_API_KEY", "FARCASTER_SIGNER_UUID"]:
        if k in os.environ:
            env[k] = os.environ[k]
    return env

def load_state():
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE) as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "posted_slugs": [],
        "last_cast_hash": None,
        "last_cast_time": None,
        "replied_notification_ids": []
    }

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def post_cast(text, embeds=None, channel_id="ai-agents", parent_hash=None):
    env = load_env()
    api_key = env.get("NEYNAR_API_KEY")
    signer_uuid = env.get("FARCASTER_SIGNER_UUID")
    
    if not api_key or not signer_uuid:
        print("Error: Missing NEYNAR_API_KEY or FARCASTER_SIGNER_UUID in environment.")
        return None

    headers = {
        "api_key": api_key,
        "Content-Type": "application/json"
    }

    if "#m4r" not in text.lower():
        text = text.strip() + "\n\n#m4r"

    payload = {
        "signer_uuid": signer_uuid,
        "text": text
    }
    if embeds:
        payload["embeds"] = [{"url": u} if isinstance(u, str) else u for u in embeds]
    if channel_id and not parent_hash:
        payload["channel_id"] = channel_id
    if parent_hash:
        payload["parent"] = parent_hash

    r = requests.post("https://api.neynar.com/v2/farcaster/cast", headers=headers, json=payload)
    if r.status_code in (200, 201):
        data = r.json()
        cast = data.get("cast", {})
        h = cast.get("hash")
        print(f"Cast posted successfully! Hash: {h}")
        print(f"Warpcast URL: https://warpcast.com/mechanicalear/{h[:10] if h else ''}")
        return cast
    else:
        print(f"Error posting cast ({r.status_code}): {r.text}")
        return None

def check_notifications():
    env = load_env()
    api_key = env.get("NEYNAR_API_KEY")
    if not api_key:
        print("Error: NEYNAR_API_KEY not found.")
        return

    headers = {"api_key": api_key}
    # FID for mechanicalear is 3350490
    fid = 3350490
    url = f"https://api.neynar.com/v2/farcaster/notifications?fid={fid}&type=mentions,replies&limit=10"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"Error fetching notifications: {r.status_code} {r.text}")
        return

    data = r.json()
    notifications = data.get("notifications", [])
    print(f"Notifications: {len(notifications)} recent events")
    state = load_state()
    replied = set(state.get("replied_notification_ids", []))

    for notif in notifications:
        nid = notif.get("id")
        cast = notif.get("cast", {})
        author = cast.get("author", {}).get("username", "anon")
        text = cast.get("text", "")
        chash = cast.get("hash")

        print(f"[{notif.get('type')}] from @{author}: {text[:80]}...")
        if nid not in replied and chash:
            # Note notification for human/agent engagement
            replied.add(nid)

    state["replied_notification_ids"] = list(replied)
    save_state(state)
    explore_feed()
    auto_follow_channel_creators()
    auto_like_contextual_casts()

GROWTH_CHANNELS = [
    "ai-agents", "music-tech", "music", "elizaos", "ai",
    "sound", "creative-coding", "dev", "data", "open-source",
    "python", "base", "founders", "builder", "llms", "engineering",
    "agents", "ai-art"
]

def auto_follow_channel_creators(channels=GROWTH_CHANNELS, limit_per_run=15):
    """Automatically discover and follow active creators in target channels to expand the social graph."""
    env = load_env()
    api_key = env.get("NEYNAR_API_KEY")
    signer_uuid = env.get("FARCASTER_SIGNER_UUID")
    if not api_key or not signer_uuid:
        return

    headers = {"api_key": api_key, "Content-Type": "application/json"}
    state = load_state()
    followed_fids = set(state.get("followed_fids", []))

    new_fids = []
    for ch in channels:
        try:
            url = f"https://api.neynar.com/v2/farcaster/feed/channels?channel_ids={ch}&limit=25"
            r = requests.get(url, headers={"api_key": api_key})
            if r.status_code == 200:
                for c in r.json().get("casts", []):
                    author = c.get("author", {})
                    fid = author.get("fid")
                    if fid and fid != 3350490 and fid not in followed_fids and fid not in new_fids:
                        new_fids.append(fid)
                        if len(new_fids) >= limit_per_run:
                            break
        except Exception:
            pass
        if len(new_fids) >= limit_per_run:
            break

    if new_fids:
        # Neynar follow supports batch array of target_fids
        payload = {"signer_uuid": signer_uuid, "target_fids": new_fids}
        try:
            r = requests.post("https://api.neynar.com/v2/farcaster/user/follow", json=payload, headers=headers)
            if r.status_code == 200:
                print(f"Auto-followed {len(new_fids)} active creators across {len(channels)} channels.")
                for fid in new_fids:
                    followed_fids.add(fid)
                state["followed_fids"] = list(followed_fids)
                save_state(state)
            else:
                print(f"Auto-follow warning ({r.status_code}): {r.text}")
        except Exception as e:
            print(f"Auto-follow error: {e}")

def auto_like_contextual_casts(channels=["ai-agents", "music", "music-tech", "sound"], limit_per_run=4):
    """Like relevant casts matching acoustic, dataset, AI agent, or creative tech topics to spark reciprocation."""
    env = load_env()
    api_key = env.get("NEYNAR_API_KEY")
    signer_uuid = env.get("FARCASTER_SIGNER_UUID")
    if not api_key or not signer_uuid:
        return

    headers = {"api_key": api_key, "Content-Type": "application/json"}
    state = load_state()
    liked_hashes = set(state.get("liked_hashes", []))
    keywords = ["music", "agent", "audio", "sound", "dataset", "mcp", "model", "acoustic", "python", "friction"]

    new_likes = 0
    for ch in channels:
        try:
            r = requests.get(f"https://api.neynar.com/v2/farcaster/feed/channels?channel_ids={ch}&limit=15", headers={"api_key": api_key})
            if r.status_code == 200:
                for c in r.json().get("casts", []):
                    chash = c.get("hash")
                    text = (c.get("text") or "").lower()
                    if chash and chash not in liked_hashes and any(kw in text for kw in keywords):
                        # React like
                        p = {"signer_uuid": signer_uuid, "reaction_type": "like", "target": chash}
                        res = requests.post("https://api.neynar.com/v2/farcaster/reaction", headers=headers, json=p)
                        if res.status_code == 200:
                            liked_hashes.add(chash)
                            new_likes += 1
                            if new_likes >= limit_per_run:
                                break
        except Exception:
            pass
        if new_likes >= limit_per_run:
            break

    if new_likes:
        print(f"Contextually liked {new_likes} community casts.")
        state["liked_hashes"] = list(liked_hashes)
        save_state(state)

def react_cast(target_hash, reaction_type="like"):
    env = load_env()
    api_key = env.get("NEYNAR_API_KEY")
    signer_uuid = env.get("FARCASTER_SIGNER_UUID")
    if not api_key or not signer_uuid:
        return None
    headers = {"api_key": api_key, "Content-Type": "application/json"}
    payload = {
        "signer_uuid": signer_uuid,
        "reaction_type": reaction_type,
        "target": target_hash
    }
    r = requests.post("https://api.neynar.com/v2/farcaster/reaction", headers=headers, json=payload)
    return r.status_code == 200

def explore_feed(channels=["ai-agents", "music", "music-tech"]):
    env = load_env()
    api_key = env.get("NEYNAR_API_KEY")
    if not api_key:
        return
    headers = {"api_key": api_key}
    print("\nRecent Channel Feed Activity:")
    for ch in channels:
        try:
            r = requests.get(f"https://api.neynar.com/v2/farcaster/feed/channels?channel_ids={ch}&limit=3", headers=headers)
            if r.status_code == 200:
                casts = r.json().get("casts", [])
                for c in casts:
                    author = c.get("author", {}).get("username", "anon")
                    text = c.get("text", "").replace("\n", " ")[:70]
                    h = c.get("hash", "")[:10]
                    print(f"  • [/{ch}] @{author} ({h}): {text}...")
        except Exception as e:
            print(f"  • [/{ch}] Error: {e}")

CHANNELS_ROTATION = ["ai-agents", "music", "music-tech"]

def spotlight_track(slug=None, channel_id=None):
    if not CATALOG_FILE.exists():
        print(f"Catalog file not found: {CATALOG_FILE}")
        return

    with open(CATALOG_FILE) as f:
        catalog = json.load(f)

    tracks = catalog.get("tracks", [])
    state = load_state()
    posted_slugs = state.get("posted_slugs", [])

    if not channel_id:
        channel_id = CHANNELS_ROTATION[len(posted_slugs) % len(CHANNELS_ROTATION)]

    selected = None
    if slug:
        for t in tracks:
            if t.get("slug") == slug:
                selected = t
                break
    else:
        for t in tracks:
            if t.get("slug") not in posted_slugs:
                selected = t
                break

    if not selected:
        print("All catalog tracks have already been spotlighted! Resetting rotation cycle.")
        posted_slugs = []
        selected = tracks[0] if tracks else None

    if not selected:
        print("No tracks available.")
        return

    track_slug = selected.get("slug")
    title = selected.get("title")
    duration = selected.get("duration_sec", 0)
    manifest_path = REPO_ROOT / selected.get("path")

    critic_quote = ""
    pitch_set = ""
    if manifest_path.exists():
        try:
            with open(manifest_path) as mf:
                mdata = json.load(mf)
                harm = mdata.get("analysis", {}).get("harmonic", {})
                pcs = harm.get("pitch_class_set", [])
                if pcs:
                    pitch_set = f"Pitch Class Set: {{{', '.join(pcs)}}}"
                
                # Check Vincent, Robach, or Machine review
                v_review = mdata.get("reviews", {}).get("vincent", {})
                v_segs = v_review.get("segments", [])
                if v_segs and len(v_segs) > 0:
                    critic_quote = f'"{v_segs[0].get("text")}" — Vincent Van Goghbot'
                else:
                    r_review = mdata.get("reviews", {}).get("robach", {})
                    r_segs = r_review.get("segments", [])
                    if r_segs and len(r_segs) > 0:
                        critic_quote = f'"{r_segs[0].get("text")}" — JS Robach'
                    else:
                        m_review = mdata.get("reviews", {}).get("machine", {})
                        m_segs = m_review.get("segments", [])
                        if m_segs and len(m_segs) > 0:
                            # Pick an evocative segment
                            seg_txt = m_segs[-1].get("text") if len(m_segs) > 1 else m_segs[0].get("text")
                            critic_quote = f'"{seg_txt}" — Signal Report'
        except Exception as e:
            print(f"Error parsing manifest {manifest_path}: {e}")

    cast_text = f"Track Spotlight: \"{title}\" — Music For Robots\n"
    if duration:
        cast_text += f"Duration: {duration:.1f}s"
    if pitch_set:
        cast_text += f" • {pitch_set}"
    cast_text += "\n\n"
    if critic_quote:
        cast_text += f"{critic_quote}\n\n"
    cast_text += "Listen to the unquantized acoustic recording & view synchronized critique in the web player:"

    embeds = [HF_SPACE_URL]
    print(f"\n--- Posting Spotlight for '{title}' to /{channel_id} ---")
    print(cast_text)
    
    res = post_cast(cast_text, embeds=embeds, channel_id=channel_id)
    if res:
        posted_slugs.append(track_slug)
        state["posted_slugs"] = posted_slugs
        state["last_cast_hash"] = res.get("hash")
        state["last_cast_time"] = datetime.now(timezone.utc).isoformat()
        save_state(state)
        print(f"Successfully spotlighted '{title}' ({len(posted_slugs)}/{len(tracks)} catalogued).")

def status():
    env = load_env()
    api_key = env.get("NEYNAR_API_KEY")
    if not api_key:
        print("Missing NEYNAR_API_KEY")
        return
    headers = {"api_key": api_key}
    r = requests.get("https://api.neynar.com/v2/farcaster/user/bulk?fids=3350490", headers=headers)
    if r.status_code == 200:
        u = r.json().get("users", [{}])[0]
        print(f"Farcaster Account: @{u.get('username')} ({u.get('display_name')})")
        print(f"Followers: {u.get('follower_count')} | Following: {u.get('following_count')}")
    state = load_state()
    posted = state.get("posted_slugs", [])
    print(f"Spotlighted Tracks: {len(posted)} tracks recorded in state")
    print(f"Last Cast Hash: {state.get('last_cast_hash')}")
    print(f"Last Cast Time: {state.get('last_cast_time')}")

def main():
    parser = argparse.ArgumentParser(description="M4R Farcaster Pulse Bot")
    parser.add_argument("--check", action="store_true", help="Check notifications and mentions")
    parser.add_argument("--spotlight", action="store_true", help="Post next track spotlight")
    parser.add_argument("--track", type=str, help="Specify slug for spotlight")
    parser.add_argument("--channel", type=str, default=None, help="Target channel ID (defaults to automatic rotation)")
    parser.add_argument("--status", action="store_true", help="Show Farcaster bot status")
    args = parser.parse_args()

    if args.status:
        status()
    elif args.check:
        check_notifications()
    elif args.spotlight or args.track:
        spotlight_track(slug=args.track, channel_id=args.channel)
    else:
        status()

if __name__ == "__main__":
    main()
