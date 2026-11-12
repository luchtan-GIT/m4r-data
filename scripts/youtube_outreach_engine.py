#!/usr/bin/env python3
"""
YouTube Outreach & Thought-Leadership Engine for @MechanicalEar.

Discovers high-affinity videos (AI audio, microtiming, human groove, musicology)
and posts authoritative, high-signal technical critiques and observations
to build organic reach and drive channel discoverability.
"""

import os
import sys
import json
import time
import argparse
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

TOKEN_PATHS = [
    "/Users/luchtan/Documents/stock-signal-engine/m4r/token.json",
    "/Users/luchtan/Studio/m4r-data/token.json"
]
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "youtube_outreach_log.json")

# High-affinity video targets with bespoke technical analyses
CURATED_TARGETS = [
    {
        "video_id": "QVXfcIb3OKo",
        "creator": "Benn Jordan",
        "title": "Using AI To Detect AI Music (and other music industry data-porn)",
        "comment": (
            "One of the most reliable physical watermarks separating raw human acoustic performance "
            "from generative diffusion/transformer models isn't frequency response, but temporal phase drift. "
            "Generative models trained on quantized stems learn stationary periodicity; when they attempt to synthesize "
            "rubato or expressive acoustic instruments, they produce micro-smearing because the network doesn't model "
            "viscoelastic momentum. A human player's acoustic transients exhibit slight mechanical friction and string rebound "
            "that cannot be faked by adding Gaussian jitter to a quantized grid."
        )
    },
    {
        "video_id": "NkNdnPYtXRw",
        "creator": "Venus Theory",
        "title": "So AI Makes Better Music Than You...Now What?",
        "comment": (
            "The bottleneck for AI music isn't melody or harmonic texture—it's kinetic intentionality. "
            "A generative model predicts what sounds statistically plausible next based on dataset averages, "
            "which inherently biases it toward harmonic equilibrium. But human musical expression lives in the friction "
            "of unquantized rubato: leaning 15-20 milliseconds behind the beat specifically to create harmonic dissonance, "
            "then catching up on the downbeat. You can't prompt an LLM or diffusion model for that kind of physical risk "
            "because risk is precisely what the training loss function penalizes."
        )
    },
    {
        "video_id": "9MzKx0fKg5o",
        "creator": "Adam Neely",
        "title": 'How to Play Music With a "Drunk" Feel',
        "comment": (
            "What makes the 'drunk' or lopsided subdivision work mechanically is that human performers aren't randomizing "
            "error—they are conserving phase momentum across larger structural windows. When you feed unquantized acoustic "
            "recordings into an algorithmic analyzer, the deviation from the nearest 16th grid looks like chaotic noise in small "
            "windows, but over 4 to 8 measures the integral of the timing error approaches zero. The moment you quantize or "
            "even apply a uniform swing percentage, you destroy that long-range viscoelastic pull that the ear reads as intentional gravity."
        )
    },
    {
        "video_id": "BRWquZdEigw",
        "creator": "Two Minute Papers",
        "title": "New AI Listened To 20,000 Hours Of Music. What Did It Learn?",
        "comment": (
            "The fascinating engineering bottleneck with models like MusicGen and EnCodec is that residual vector quantization "
            "compresses audio into discrete tokens (often around a 50Hz frame rate). At a 20ms frame resolution, fine human "
            "microtiming variations (like 8-15ms snare drag or finger rubato) get quantalized or smoothed into the latent representation "
            "before the transformer even begins autoregression. To capture real expressive human timing, future acoustic architectures "
            "will need continuous time representations rather than discrete quantized frames."
        )
    },
    {
        "video_id": "7NWpOl1cUEw",
        "creator": "Verysickbeats",
        "title": "J Dilla Inspired Techniques",
        "comment": (
            "The magic of flipping a 6/8 acoustic phrase into a 4/4 grid without quantization is the polyrhythmic cross-talk. "
            "When the triplet swing of the acoustic source fights against the duple pulse of the MPC pads, the brain stops hearing "
            "'tempo' and starts feeling kinetic push and pull. That tension is impossible to replicate with a standard DAW swing template "
            "because every chop carries its own decaying acoustic room tail."
        )
    }
]

def get_youtube_client():
    token_path = None
    for p in TOKEN_PATHS:
        if os.path.exists(p):
            token_path = p
            break
    if not token_path:
        raise FileNotFoundError(f"No valid token.json found in {TOKEN_PATHS}")
    creds = Credentials.from_authorized_user_file(token_path)
    return build('youtube', 'v3', credentials=creds)

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return {"posted_comments": {}, "scanned_videos": []}

def save_log(log_data):
    with open(LOG_FILE, 'w') as f:
        json.dump(log_data, f, indent=2)

def post_comment(youtube, video_id, comment_text):
    """Post a top-level comment to a YouTube video."""
    body = {
        "snippet": {
            "videoId": video_id,
            "topLevelComment": {
                "snippet": {
                    "textOriginal": comment_text
                }
            }
        }
    }
    response = youtube.commentThreads().insert(
        part="snippet",
        body=body
    ).execute()
    return response["id"]

def run_outreach(dry_run=False):
    youtube = get_youtube_client()
    log_data = load_log()
    posted = log_data.get("posted_comments", {})

    print(f"[{datetime.now().isoformat()}] Starting YouTube Outreach Engine for @MechanicalEar...")
    print(f"Total curated targets: {len(CURATED_TARGETS)}")
    print(f"Previously posted count: {len(posted)}\n")

    new_posts = 0
    for target in CURATED_TARGETS:
        vid = target["video_id"]
        creator = target["creator"]
        title = target["title"]
        comment = target["comment"]

        if vid in posted:
            print(f"⏩ Already commented on [{vid}] ({creator} - '{title}') on {posted[vid].get('timestamp')}")
            continue

        print(f"🎯 Target Found: [{vid}] {creator} - '{title}'")
        print(f"   Draft Comment:\n   \"{comment}\"")

        if dry_run:
            print("   [DRY-RUN] Skipping actual post.\n")
            continue

        try:
            print("   Posting comment via YouTube Data API...")
            comment_id = post_comment(youtube, vid, comment)
            posted[vid] = {
                "creator": creator,
                "title": title,
                "comment_id": comment_id,
                "timestamp": datetime.now().isoformat(),
                "comment_text": comment
            }
            log_data["posted_comments"] = posted
            save_log(log_data)
            print(f"   ✅ SUCCESS! Comment ID: {comment_id}\n")
            new_posts += 1
            # Respect rate limit between comment submissions
            time.sleep(3)
        except Exception as e:
            print(f"   ❌ ERROR posting to [{vid}]: {e}\n")

    print(f"Outreach run completed. New comments posted: {new_posts}")

def check_channel_stats():
    youtube = get_youtube_client()
    res = youtube.channels().list(part="snippet,statistics", mine=True).execute()
    for ch in res.get("items", []):
        title = ch["snippet"]["title"]
        stats = ch["statistics"]
        print(f"Channel: {title}")
        print(f"Subscribers: {stats.get('subscriberCount')}")
        print(f"Total Views: {stats.get('viewCount')}")
        print(f"Total Videos: {stats.get('videoCount')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Outreach Engine for @MechanicalEar")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without posting")
    parser.add_argument("--stats", action="store_true", help="Print channel statistics")
    args = parser.parse_args()

    if args.stats:
        check_channel_stats()
    else:
        run_outreach(dry_run=args.dry_run)
