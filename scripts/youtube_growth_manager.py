#!/usr/bin/env python3
"""
YouTube Growth & Metadata Automation Manager for The Mechanical Ear (@MechanicalEar).
Implements Strategies A & B:
- High-CTR Algorithmic Re-Titling & Description Optimization
- Conversion-Driven Universal Pinned Comments
- Direct YouTube Studio & Comment Management URLs
"""

import sys
import json
from pathlib import Path

VIDEO_DATABASE = [
    {
        "id": "wb3mJr-a7lU",
        "current_title": "TRANSMISSION: Convergence | Music For Robots",
        "views": 995,
        "format": "Short (10s)",
        "track": "Synthetic Storms: Convergence",
        "critic": "Vincent Van Goghbot",
        "new_title": "Can an AI detect 10 milliseconds of human error? 🤖👂 #Shorts #m4r",
        "description": (
            "We played unquantized acoustic audio to an autonomous AI critic to see if neural networks "
            "can perceive human microtiming drift.\n\n"
            "Track: Synthetic Storms (Convergence) by Michael Luchtan\n"
            "Critic: Vincent Van Goghbot (Sensory Listener)\n\n"
            "Explore the live benchmark & test your LLM:\n"
            "👉 https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "👉 GitHub: https://github.com/luchtan-GIT/m4r-data\n\n"
            "#Shorts #m4r #MusicForRobots #MachineLearning #AI"
        ),
        "tags": ["AI music", "The Mechanical Ear", "Vincent Van Goghbot", "microtiming", "rubato", "machine learning", "Shorts"],
        "pinned_comment": (
            "🎧 Can an AI model hear the friction of human acoustic timing?\n\n"
            "We tested whether unquantized audio breaks autoregressive LLM template lock-in. "
            "In Monte Carlo tests (N=50), continuous acoustic audio reduced template lock-in by -49.6% (p < 10⁻¹⁵).\n\n"
            "👉 Try the interactive visualizer & benchmark:\n"
            "https://huggingface.co/spaces/music4robots/cognitive-calibration\n\n"
            "👉 Open source dataset & MCP server:\n"
            "https://github.com/luchtan-GIT/m4r-data"
        )
    },
    {
        "id": "yzOchSYS7MQ",
        "current_title": "TRANSMISSION: Static Field | Music For Robots",
        "views": 849,
        "format": "Short (6s)",
        "track": "Synthetic Storms: Static Field",
        "critic": "Vincent Van Goghbot",
        "new_title": "When you feed acoustic microtiming into an AI critic... 🌊🤖 #Shorts #m4r",
        "description": (
            "Noise to tone. An AI critic observes frequency phase transitions in real time.\n\n"
            "Track: Synthetic Storms (Static Field)\n"
            "Critic: Vincent Van Goghbot\n\n"
            "👉 Benchmark: https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "👉 Dataset: https://github.com/luchtan-GIT/m4r-data\n\n"
            "#Shorts #m4r #GenerativeAI #Synthesizer #MusicTech"
        ),
        "tags": ["AI music", "The Mechanical Ear", "Vincent Van Goghbot", "sound design", "Shorts"],
        "pinned_comment": (
            "🤖 'Noise becomes tone when the sampling rate cannot resolve the decay.'\n\n"
            "Explore the full acoustic calibration dataset and run your own model tests:\n"
            "👉 Live Web Audio Space: https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "👉 GitHub Repository: https://github.com/luchtan-GIT/m4r-data"
        )
    },
    {
        "id": "t9zfA2IXO7M",
        "current_title": "TRANSMISSION: Maximum Density | Music For Robots",
        "views": 562,
        "format": "Short (20s)",
        "track": "Chasing Leaks: Maximum Density",
        "critic": "Vincent Van Goghbot",
        "new_title": "Testing an AI on maximum acoustic harmonic density 💥👂 #Shorts #m4r",
        "description": (
            "Autoregressive models struggle with harmonic collision. Here is Vincent's live perceptual transmission.\n\n"
            "👉 Interactive App: https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "👉 Code & Audio: https://github.com/luchtan-GIT/m4r-data\n\n"
            "#Shorts #m4r #AI #Acoustic #MachineLearning"
        ),
        "tags": ["AI music", "The Mechanical Ear", "Vincent Van Goghbot", "harmonics", "Shorts"],
        "pinned_comment": (
            "⚡ In empirical trials across 200 model runs, acoustic audio calibration increased architectural reasoning depth by +148%.\n\n"
            "Test the model yourself in your browser:\n"
            "👉 https://huggingface.co/spaces/music4robots/cognitive-calibration"
        )
    },
    {
        "id": "nyPCg6Ia12o",
        "current_title": "TRANSMISSION: THE NOTE THAT WOULDN'T MOVE | Music For Robots",
        "views": 445,
        "format": "Short (7s)",
        "track": "Foundationoff",
        "critic": "Vincent Van Goghbot",
        "new_title": "AI Critic vs Human Musician: 'The note wouldn't move' 🎸🤖 #Shorts #m4r",
        "description": (
            "Vincent Van Goghbot listens to a single sustaining pitch across 6852 Hertz.\n\n"
            "👉 Interactive Space: https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "👉 Dataset: https://github.com/luchtan-GIT/m4r-data\n\n"
            "#Shorts #m4r #MusicForRobots #AI #Acoustic"
        ),
        "tags": ["AI critic", "Vincent Van Goghbot", "The Mechanical Ear", "guitar tone", "Shorts"],
        "pinned_comment": (
            "🎸 'Opens at 6852 hertz. The brightness fell by half.'\n\n"
            "Read how Vincent Van Goghbot and JS Robach analyze this track side-by-side in our interactive demo:\n"
            "👉 https://huggingface.co/spaces/music4robots/cognitive-calibration"
        )
    },
    {
        "id": "103S9zHNXh8",
        "current_title": "Exegesis: The Loop Has No Exit Condition | Music For Robots",
        "views": 244,
        "format": "Short (7s)",
        "track": "Foundationoff",
        "critic": "JS Robach",
        "new_title": "When a mathematical AI critic analyzes a human guitar loop ⚖️🤖 #Shorts #m4r",
        "description": (
            "JS Robach proves formal structural properties of acoustic guitar loops.\n\n"
            "👉 Interactive Space: https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "👉 GitHub: https://github.com/luchtan-GIT/m4r-data\n\n"
            "#Shorts #m4r #Mathematics #Logic #AI"
        ),
        "tags": ["JS Robach", "formal proof", "The Mechanical Ear", "music theory", "Shorts"],
        "pinned_comment": (
            "⚖️ 'A fixed point. C only. Entropy zero. Thirteen alternations. The loop has no exit condition.'\n\n"
            "Experience both AI critics dueling on our live Hugging Face Space:\n"
            "👉 https://huggingface.co/spaces/music4robots/cognitive-calibration"
        )
    },
    {
        "id": "TmFC-NEmKig",
        "current_title": "TRANSMISSION: FOLLOWING THE NULL POINTER | Music For Robots",
        "views": 10,
        "format": "Video (75s)",
        "track": "Invalid Pointer",
        "critic": "Vincent Van Goghbot",
        "new_title": "We gave unquantized acoustic rubato to an AI model. It broke. 💥",
        "description": (
            "What happens when you feed unquantized acoustic guitar kinematics (microtiming variance ±18ms) into an AI critic?\n\n"
            "Composer Michael Luchtan plays 'Invalid Pointer'. Vincent Van Goghbot listens in real time, synchronizing observations to the millisecond acoustic transients.\n\n"
            "TIMESTAMPS:\n"
            "0:00 - Acoustic Transients & Fingerstyle Rubato\n"
            "0:22 - Vincent's First Perceptual Ingestion (Below 600Hz)\n"
            "0:50 - The Resolution Failure\n"
            "1:10 - Architectural Breakdown\n\n"
            "🔗 LINKS & RESOURCES:\n"
            "• Live Calibration Space: https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "• Open Source GitHub Repo: https://github.com/luchtan-GIT/m4r-data\n"
            "• Hugging Face Dataset: https://huggingface.co/datasets/music4robots/music-for-robots\n"
            "• Subscribe to The Mechanical Ear: https://www.youtube.com/@MechanicalEar?sub_confirmation=1\n\n"
            "#m4r #MusicForRobots #TheMechanicalEar #AI #MachineLearning #AcousticGuitar"
        ),
        "tags": ["AI perception", "music for robots", "unquantized rubato", "the mechanical ear", "vincent van goghbot", "guitar", "LLM benchmark"],
        "pinned_comment": (
            "💥 'The address leads nowhere. Everything living below 600 hertz. Tones, not textures.'\n\n"
            "We packaged this entire dataset and audio calibration pipeline into a zero-dependency open source MCP server:\n\n"
            "👉 Test the interactive Space: https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "👉 Star on GitHub: https://github.com/luchtan-GIT/m4r-data"
        )
    },
    {
        "id": "PrhVhoStOUw",
        "current_title": "Exegesis: Dereferencing the Diatonic | Music For Robots",
        "views": 17,
        "format": "Video (75s)",
        "track": "Invalid Pointer",
        "critic": "JS Robach",
        "new_title": "AI Mathematician Attempts to Prove Human Guitar Improvisation 📐🎸",
        "description": (
            "While Vincent listens to tone and texture, JS Robach treats human acoustic guitar performance as a formal proof system.\n\n"
            "Track: Invalid Pointer by Michael Luchtan\n"
            "Critic: JS Robach (Formalist Proof Agent)\n\n"
            "TIMESTAMPS:\n"
            "0:00 - Diatonic Initialization\n"
            "0:25 - Dereferencing Axiom One ({G})\n"
            "0:55 - Formal Incompleteness Reached\n\n"
            "🔗 LINKS:\n"
            "• Live Web Visualizer: https://huggingface.co/spaces/music4robots/cognitive-calibration\n"
            "• Open Source Dataset: https://github.com/luchtan-GIT/m4r-data\n\n"
            "#m4r #MusicForRobots #TheMechanicalEar #Mathematics #MusicTheory"
        ),
        "tags": ["JS Robach", "music theory", "formal grammar", "guitar proof", "The Mechanical Ear"],
        "pinned_comment": (
            "📐 'Invalid pointer. The machine runs anyway. {G}. Axiom one. The proof begins.'\n\n"
            "Compare JS Robach's formal proof against Vincent's sensory review in real time on our interactive demo:\n"
            "👉 https://huggingface.co/spaces/music4robots/cognitive-calibration"
        )
    }
]

def print_action_summary():
    print("=" * 80)
    print("🚀 THE MECHANICAL EAR: YOUTUBE GROWTH ENGINE (STRATEGIES A & B)")
    print("=" * 80)
    for i, v in enumerate(VIDEO_DATABASE, 1):
        studio_url = f"https://studio.youtube.com/video/{v['id']}/edit"
        watch_url = f"https://www.youtube.com/watch?v={v['id']}"
        print(f"\n[{i}] {v['track']} ({v['critic']}) — Current: {v['views']} views [{v['format']}]")
        print(f"    Studio Edit URL: {studio_url}")
        print(f"    Watch URL:       {watch_url}")
        print(f"    Current Title:   {v['current_title']}")
        print(f"    👉 NEW TITLE:    {v['new_title']}")
        print(f"    👉 PINNED COMMENT (Paste & Pin):")
        for line in v['pinned_comment'].split('\n'):
            print(f"       {line}")
        print("-" * 80)

if __name__ == "__main__":
    print_action_summary()
