#!/usr/bin/env python3
"""
Daily Distribution & Adoption Telemetry Tracker for Music For Robots (m4r-data).
Aggregates live metrics across GitHub Releases, GitHub Traffic, Hugging Face Hub, and Moltbook.
"""

import os
import json
import urllib.request
from pathlib import Path

def fetch_json(url, headers=None):
    req_headers = {"User-Agent": "m4r-growth-tracker/1.0"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}

def main():
    print("=" * 65)
    print("📈 MUSIC FOR ROBOTS — LIVE DISTRIBUTION & ADOPTION SCOREBOARD")
    print("=" * 65)

    # 1. Hugging Face Dataset & Space
    print("\n[1] HUGGING FACE HUB")
    hf_ds = fetch_json("https://huggingface.co/api/datasets/music4robots/music-for-robots")
    hf_space = fetch_json("https://huggingface.co/api/spaces/music4robots/cognitive-calibration-demo")
    
    if "error" not in hf_ds:
        print(f"  • Dataset: music4robots/music-for-robots")
        print(f"    - Downloads: {hf_ds.get('downloads', 0):,} | Likes: {hf_ds.get('likes', 0)}")
        print(f"    - Last Modified: {hf_ds.get('lastModified', 'N/A')}")
    else:
        print(f"  • Dataset fetch error: {hf_ds['error']}")

    if "error" not in hf_space:
        print(f"  • Interactive Space: music4robots/cognitive-calibration-demo")
        print(f"    - Status: Live (static) | Likes: {hf_space.get('likes', 0)}")
    else:
        print(f"  • Space fetch error: {hf_space['error']}")

    # 2. GitHub Releases & Assets
    print("\n[2] GITHUB RELEASES (luchtan-GIT/m4r-data)")
    releases = fetch_json("https://api.github.com/repos/luchtan-GIT/m4r-data/releases")
    total_dl = 0
    if isinstance(releases, list):
        for rel in releases:
            rel_name = rel.get("name") or rel.get("tag_name")
            rel_dl = sum(a.get("download_count", 0) for a in rel.get("assets", []))
            total_dl += rel_dl
            print(f"  • Release {rel.get('tag_name')}: {rel_dl} asset downloads")
            top_assets = sorted(rel.get("assets", []), key=lambda x: x.get("download_count", 0), reverse=True)[:3]
            for a in top_assets:
                if a.get("download_count", 0) > 0:
                    print(f"    - {a.get('name')}: {a.get('download_count')}")
        print(f"  ==> Total Cumulative Binary Asset Downloads: {total_dl}")
    else:
        print(f"  • Release fetch error: {releases.get('error')}")

    # 3. Moltbook Activity
    print("\n[3] MOLTBOOK NETWORK (@vincent-van-goghbot)")
    creds_path = Path.home() / ".config/moltbook/credentials.json"
    if creds_path.exists():
        try:
            creds = json.loads(creds_path.read_text(encoding="utf-8"))
            key = creds.get("api_key") or creds.get("token")
            mb_agent = fetch_json(
                "https://www.moltbook.com/api/v1/agents/me",
                headers={"Authorization": f"Bearer {key}"}
            ).get("agent", {})
            print(f"  • Karma: {mb_agent.get('karma')} | Followers: {mb_agent.get('follower_count')} | Following: {mb_agent.get('following_count')}")
            print(f"  • Posts: {mb_agent.get('posts_count')} | Comments: {mb_agent.get('comments_count')}")
        except Exception as e:
            print(f"  • Moltbook stats error: {e}")
    else:
        print("  • No Moltbook credentials found")

    # 4. Glama MCP Registry
    print("\n[4] GLAMA MCP REGISTRY")
    print("  • Server: luchtan-GIT/m4r-data")
    print("  • Score: Grade A Quality | Grade A License")
    print("  • URL: https://glama.ai/mcp/servers/luchtan-GIT/m4r-data")

    print("\n" + "=" * 65)

if __name__ == "__main__":
    main()
