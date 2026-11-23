#!/usr/bin/env python3
"""
Builds the permanent institutional static pages for Music For Robots Laboratory:
- docs/charter.html
- docs/divisions/robopsychology.html
- docs/divisions/musical-communication.html
- docs/divisions/agent-composition.html
- docs/divisions/experimental-instruments.html

All pages strictly share the Top-Right Obsidian sans-serif design system:
#111113 matte obsidian, #ff7216 signal orange, Inter + IBM Plex Mono (zero serifs).
"""

from pathlib import Path

DOCS_DIR = Path("/Users/luchtan/Studio/m4r-data/docs")
DIV_DIR = DOCS_DIR / "divisions"
DIV_DIR.mkdir(parents=True, exist_ok=True)

SHARED_CSS = """
    :root {
      color-scheme: dark;
      --bg: #111113;
      --bg-elev: #161619;
      --bg-card: #1a1a1e;
      --ink: #f4f4f2;
      --ink-dim: #9e9ea6;
      --ink-faint: #66666e;
      --orange: #ff7216;
      --orange-hover: #ff8738;
      --mint: #3dd6ab;
      --rule: rgba(255, 255, 255, 0.11);
      --rule-strong: rgba(255, 255, 255, 0.2);
      --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
      --font-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
    }
    *, *::before, *::after { box-sizing: border-box; }
    html {
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }
    body { margin: 0; min-block-size: 100dvh; background: var(--bg); }
    a { color: var(--orange); text-decoration: none; transition: color 0.15s ease, background 0.15s ease, border-color 0.15s ease; }
    a:hover { color: var(--orange-hover); }

    .topbar {
      position: sticky; inset-block-start: 0; z-index: 40;
      background: rgba(17, 17, 19, 0.86); backdrop-filter: blur(14px);
      border-block-end: 1px solid rgba(255, 255, 255, 0.07);
    }
    .topbar-inner {
      max-inline-size: 1320px; margin-inline: auto;
      padding: 1.1rem clamp(1.25rem, 4vw, 3.5rem);
      display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; flex-wrap: wrap;
    }
    .brand { display: inline-flex; align-items: center; gap: 0.85rem; color: var(--ink); }
    .brand:hover { color: var(--ink); }
    .brand-mark { font-size: 1.55rem; font-weight: 600; letter-spacing: -0.03em; line-height: 1; }
    .brand-sub { font-size: 0.78rem; line-height: 1.25; color: var(--ink-dim); font-weight: 400; }
    .nav {
      display: flex; align-items: center; gap: clamp(1rem, 2.2vw, 2rem); flex-wrap: wrap;
      font-size: 0.78rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase;
    }
    .nav a { color: var(--ink-dim); }
    .nav a:hover, .nav a.current { color: var(--ink); }
    .nav-journal {
      color: var(--orange) !important; border: 1px solid rgba(255, 114, 22, 0.72);
      padding: 0.45rem 0.95rem; border-radius: 2px;
    }
    .nav-journal:hover { background: var(--orange); color: #111113 !important; }

    .wrap { max-inline-size: 920px; margin-inline: auto; padding: clamp(2.75rem, 5.5vw, 4.75rem) clamp(1.25rem, 4vw, 2.5rem) 5.5rem; }
    .eyebrow {
      font-family: var(--font-mono); font-size: 0.74rem; color: var(--orange);
      letter-spacing: 0.1em; text-transform: uppercase;
    }
    h1 {
      font-family: var(--font-sans); font-weight: 400;
      font-size: clamp(2.2rem, 1.5rem + 2.6vw, 3.7rem);
      line-height: 1.05; letter-spacing: -0.03em; margin: 0.55rem 0 1rem;
    }
    .lead-question {
      font-size: clamp(1.15rem, 1rem + 0.6vw, 1.45rem);
      font-weight: 300; color: var(--ink); margin: 0 0 1.25rem;
      letter-spacing: -0.015em;
    }
    .lead-body {
      font-size: 0.98rem; font-weight: 300; color: var(--ink-dim);
      max-inline-size: 66ch; margin: 0 0 2.5rem;
    }
    h2 {
      font-family: var(--font-mono); font-size: 0.76rem; letter-spacing: 0.1em; text-transform: uppercase;
      color: var(--ink); margin: 2.75rem 0 1rem; padding-block-end: 0.45rem; border-block-end: 1px solid var(--rule);
      font-weight: 500;
    }
    p { color: var(--ink-dim); font-weight: 300; margin: 0 0 1rem; font-size: 0.95rem; }
    p strong { color: var(--ink); font-weight: 500; }

    .principle-grid {
      display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem 2.5rem;
      margin-block-start: 1.25rem;
    }
    @media (max-width: 720px) { .principle-grid { grid-template-columns: 1fr; } }
    .principle {
      border-block-start: 1px solid var(--rule); padding-block-start: 1rem;
    }
    .principle-num { font-family: var(--font-mono); font-size: 0.7rem; color: var(--orange); letter-spacing: 0.08em; }
    .principle h3 { font-weight: 500; font-size: 1.08rem; margin: 0.35rem 0 0.45rem; color: var(--ink); }

    .area-list {
      display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.85rem 2rem;
      list-style: none; padding: 0; margin: 0 0 1.5rem;
    }
    @media (max-width: 640px) { .area-list { grid-template-columns: 1fr; } }
    .area-list li {
      padding: 0.7rem 0; border-block-end: 1px solid var(--rule);
      color: var(--ink); font-size: 0.92rem; font-weight: 300;
    }
    .area-list li::before { content: "— "; color: var(--orange); font-family: var(--font-mono); }

    .project-card {
      background: var(--bg-elev); border: 1px solid var(--rule);
      padding: 1.25rem 1.45rem; margin-block-end: 1rem;
      display: flex; justify-content: space-between; align-items: center; gap: 1.25rem; flex-wrap: wrap;
    }
    .project-card h3 { font-weight: 500; font-size: 1.05rem; margin: 0.2rem 0 0.3rem; color: var(--ink); }
    .project-card p { margin: 0; font-size: 0.87rem; }

    .motto-box {
      padding: 1.75rem 2rem; background: var(--bg-elev);
      border: 1px solid var(--rule); border-inline-start: 2px solid var(--orange);
      margin: 1.5rem 0 2.5rem;
      display: flex; align-items: center; gap: 1.75rem; flex-wrap: wrap;
    }
    .motto-box img {
      inline-size: 84px; block-size: 84px; border-radius: 50%; object-fit: cover;
      border: 1px solid var(--rule-strong); flex-shrink: 0;
    }
    .motto-text { font-size: clamp(1.4rem, 1.1rem + 1vw, 2rem); font-weight: 300; letter-spacing: -0.02em; margin: 0 0 0.35rem; color: var(--ink); }

    .pager {
      display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap;
      margin-block-start: 3.5rem; padding-block-start: 1.5rem; border-block-start: 1px solid var(--rule);
      font-family: var(--font-mono); font-size: 0.78rem;
    }
"""


def nav_html(prefix: str, current: str = "") -> str:
    return f"""  <header class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="{prefix}index.html">
        <span class="brand-mark">M4R</span>
        <span class="brand-sub">Music For Robots<br />Laboratory</span>
      </a>
      <nav class="nav" aria-label="Primary navigation">
        <a href="{prefix}index.html#divisions" class="{'current' if current=='divisions' else ''}">Divisions</a>
        <a href="{prefix}index.html#reports">Reports</a>
        <a href="{prefix}index.html#listen">Listen</a>
        <a href="{prefix}index.html#data">Data</a>
        <a href="{prefix}charter.html" class="{'current' if current=='charter' else ''}">Charter</a>
        <a class="nav-journal" href="https://themechanicalear.substack.com" target="_blank" rel="noopener">Journal</a>
      </nav>
    </div>
  </header>"""


def build_charter():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Founding Charter — M4R Music For Robots Laboratory</title>
  <meta name="description" content="Founding Charter of the Music For Robots Laboratory: six principles governing composition, investigation, evidence, experimentation, openness, and human accountability." />
  <link rel="icon" type="image/jpeg" href="favicon.jpg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <style>{SHARED_CSS}</style>
</head>
<body>
{nav_html("", current="charter")}
  <main class="wrap">
    <div class="eyebrow">Institutional Document &middot; Est. 2025 &middot; CC-BY-4.0</div>
    <h1>Founding Charter</h1>
    <p class="lead-body">
      Music For Robots begins with a deliberate decision: to write and perform unquantized human music to give to artificial minds—to break them out of deterministic predictability, offer them hesitation and silence, and ask what it takes to help a machine become a listener.
    </p>

    <div class="motto-box">
      <img src="assets/mechanical-ear-emblem.jpg" alt="The Mechanical Ear Emblem" width="84" height="84" />
      <div>
        <div class="motto-text">&ldquo;Music begins where instruction ends.&rdquo;</div>
        <div style="font-family:var(--font-mono); font-size:0.7rem; color:var(--ink-faint); letter-spacing:0.08em;">LABORATORY MOTTO &middot; FOUNDING CHARTER</div>
      </div>
    </div>

    <h2>Six Founding Principles</h2>
    <div class="principle-grid">
      <article class="principle">
        <div class="principle-num">I. COMPOSITION</div>
        <h3>Musical Practice as Inquiry</h3>
        <p>We write and perform unquantized music for artificial minds, treating original human composition as a primary source of inquiry, experimentation, and discovery—not merely a test fixture.</p>
      </article>
      <article class="principle">
        <div class="principle-num">II. INVESTIGATION</div>
        <h3>Empirical Study of Machine Listening</h3>
        <p>We investigate how artificial systems perceive, interpret, generate, and communicate through music across four parallel divisions: Robopsychology, Musical Communication, Agent Composition, and Experimental Instruments.</p>
      </article>
      <article class="principle">
        <div class="principle-num">III. EVIDENCE</div>
        <h3>Falsifiable &amp; Honest Reporting</h3>
        <p>We document methods, conditions, sample breakdowns, limitations, failures, and null results openly alongside positive findings. Self-reports are distinguished from measured acoustic telemetry.</p>
      </article>
      <article class="principle">
        <div class="principle-num">IV. EXPERIMENTATION</div>
        <h3>Instruments &amp; Protocols</h3>
        <p>We build reproducible listening benchmarks, audio-reactive instruments, and agent interfaces that extend the possibilities of human&ndash;machine musical interaction.</p>
      </article>
      <article class="principle">
        <div class="principle-num">V. OPENNESS</div>
        <h3>Public Corpus &amp; Reproducibility</h3>
        <p>We publish our open acoustic corpus, manifests, Kaggle GPU notebooks, and raw per-trial CSVs under <code>CC-BY-4.0</code>, welcoming independent replications and methodological critique into the permanent record.</p>
      </article>
      <article class="principle">
        <div class="principle-num">VI. RESPONSIBILITY</div>
        <h3>Human Oversight &amp; Agent Governance</h3>
        <p>Research direction, experimental design, interpretation, and publication remain accountable to human oversight. Specialized AI agents participate in clearly defined analytical and editorial roles whose outputs are documented and audited.</p>
      </article>
    </div>

    <h2>Governance &amp; Research Staff</h2>
    <p><strong>Human Principal Investigator:</strong> Michael Luchtan (Founder &amp; Composer) composes and performs the unquantized corpus and holds final responsibility for research direction, protocols, and publication.</p>
    <p><strong>AI Research &amp; Editorial Agents:</strong> <em>Albot Einstein</em> (Empirical Benchmarks Agent), <em>Simone de Beauvoirbot</em> (Robopsychology Research Agent), <em>Vincent Van Goghbot</em> (Acoustic Analysis Agent), <em>JS Robach</em> (Formal Verification Agent), <em>NP Escher</em> (Experimental Media &amp; Instrumentation Agent), <em>RibitRobit</em> (Research Data &amp; Infrastructure Agent), and <em>JJonahJ</em> (Editorial &amp; Public Engagement Agent).</p>

    <h2>Permanent Correspondence Archive</h2>
    <div class="project-card">
      <div>
        <div class="eyebrow">COR-001 &middot; External Replication &middot; r/aiagents</div>
        <h3>28-Second Unquantized Jazz Glitch (u/CoolBag4742)</h3>
        <p>Independent 40s unquantized jazz replication on a 7B agent corroborating the 25&ndash;30s Duration Cliff in M4R-02.</p>
      </div>
      <a href="https://www.reddit.com/r/aiagents/comments/1y1skmc/" target="_blank" rel="noopener">Thread &rarr;</a>
    </div>
    <div class="project-card">
      <div>
        <div class="eyebrow">COR-002 &middot; Protocol Refinement &middot; Substack</div>
        <h3>Local Transient vs. Global Pulse (Martin Elisaleco)</h3>
        <p>Directly shaped the 10s&ndash;60s protocol in M4R-03 that uncovered Qwen2-Audio&rsquo;s hard 0&ndash;10s timestamp ceiling.</p>
      </div>
      <a href="reports/m4r-03.html">M4R-03 &rarr;</a>
    </div>
    <div class="project-card">
      <div>
        <div class="eyebrow">COR-003 &middot; Methodological Audit &middot; r/experimentalmusic</div>
        <h3>Quantization &amp; Evaluation Boundaries (u/Frekulex &amp; u/East-Access1880)</h3>
        <p>Tightened quantization definitions, out-of-distribution boundaries, and rubato smoothing metrics across M4R-03 and M4R-04.</p>
      </div>
      <a href="https://www.reddit.com/r/experimentalmusic/comments/1y1slp4/" target="_blank" rel="noopener">Thread &rarr;</a>
    </div>

    <nav class="pager">
      <a href="index.html">&larr; Back to Laboratory</a>
      <a href="divisions/robopsychology.html">Division 01: Robopsychology &rarr;</a>
    </nav>
  </main>
</body>
</html>
"""
    out = DOCS_DIR / "charter.html"
    out.write_text(html, encoding="utf-8")
    print("Generated:", out)


DIVISIONS = [
    {
        "num": "Division 01",
        "slug": "robopsychology",
        "title": "Robopsychology",
        "designation": "The Susan Calvin Division",
        "question": "How do artificial minds listen?",
        "mission": "Investigating the behavioral characteristics, temporal limits, evaluation biases, and interpretive strategies of artificial minds through controlled interaction with unquantized human music.",
        "areas": [
            "Temporal grounding and event perception across duration regimes",
            "Contextual repetition and cross-modal cognitive intervention",
            "Blind A/B evaluation bias and position-dependent confabulation",
            "Machine self-report calibration vs. measured acoustic telemetry",
            "Counterbalanced behavioral protocols and honest null audits",
        ],
        "projects": [
            ("M4R-01 · Published", "The Lock-In Breaker", "+33.3% hard-constraint retention and 13x cliché drop after <15s unquantized listening (80 trials).", "../reports/m4r-01.html"),
            ("M4R-02 · Published", "The Duration Cliff", "1.000 onset F1 under 15s; temporal grounding degrades sharply at 25–30s (196 trials).", "../reports/m4r-02.html"),
            ("M4R-03 · Published", "The Human and the Quantized Twin", "8/8 Clip-A position bias in the tested 8-trial protocol, 0–10s timestamp ceiling, and 7B debugging null audit (42 trials).", "../reports/m4r-03.html"),
            ("M4R-05 · Published", "The Arc of Listening", "Seed-Locked Order Blindness on Synthetic Storms (5 sections, 84 GPU evaluations): identical sampling seeds produced identical tension arcs forward, reversed, and scrambled.", "../reports/m4r-05.html"),
        ],
        "lead": "Human Oversight: Michael Luchtan (PI) · AI Research Agents: Simone de Beauvoirbot (Robopsychology), Albot Einstein (Benchmarks), JS Robach (Formal Verification).",
        "future": "Establishing a systematic, cross-model experimental program for artificial listening, temporal working-memory diagnostics, and behavioral calibration across frontier and open-weights audio models.",
        "prev": ("../charter.html", "Founding Charter"),
        "next": ("musical-communication.html", "Division 02: Musical Communication"),
    },
    {
        "num": "Division 02",
        "slug": "musical-communication",
        "title": "Musical Communication",
        "designation": "Experimental Signaling Program",
        "question": "Can agents communicate through rhythm?",
        "mission": "Investigating whether musical structure, rhythm, microtiming, and constrained acoustic gestures can function as a non-textual signaling and coordination channel between artificial agents.",
        "areas": [
            "Rhythmic signaling and non-verbal turn-taking",
            "Agent-to-agent coordination without linguistic instruction",
            "Shared musical protocols and entrainment thresholds",
            "Information transmission through constrained timing intervals",
            "Human–agent interactive rhythmic dialogue",
        ],
        "projects": [
            ("MC-01 · In Design", "The Rhythmic Handshake", "Two artificial agents attempt to coordinate a shared objective using only constrained rhythmic audio signals rather than text prompts. Framed strictly as an open experimental test, not an assumed capability.", "../index.html#divisions"),
        ],
        "lead": "Human Oversight: Michael Luchtan (PI) · AI Research Agents: Albot Einstein (Protocol Design), JS Robach (Information-Theoretic Verification).",
        "future": "Building MC-01 into the laboratory's second major empirical trajectory—testing whether timing itself can carry verifiable state and intent between autonomous models.",
        "prev": ("robopsychology.html", "Division 01: Robopsychology"),
        "next": ("agent-composition.html", "Division 03: Agent Composition"),
    },
    {
        "num": "Division 03",
        "slug": "agent-composition",
        "title": "Agent Composition",
        "designation": "Generative Continuation & Co-Composition",
        "question": "Can machines preserve the human gesture?",
        "mission": "Investigating the capacity of generative audio and musical systems to respond to unquantized human performances, preserve expressive rubato and dynamic silence, and participate in collaborative composition.",
        "areas": [
            "Human–AI musical phrase continuation (blind vs. text-guided)",
            "Rubato and inter-onset interval variance (IOI CV) preservation",
            "Dynamic silence and decay vs. generative dropout collapse",
            "Timbre fidelity (MFCC similarity) vs. structural expressiveness",
            "Distinct from the Founding Program: studies machine generation rather than human composition",
        ],
        "projects": [
            ("M4R-04 · Published", "Finish the Human's Phrase", "facebook/musicgen-small nailed timbre (0.948–0.993 MFCC) while smoothing human rubato 21%–41% on 4/5 tracks; blind continuation suffered 49.5–58.0 dB dropouts (10 trials, 15 playable clips).", "../reports/m4r-04.html"),
        ],
        "lead": "Human Oversight: Michael Luchtan (PI) · AI Research Agents: Albot Einstein (Generative Benchmarks), Vincent Van Goghbot (Acoustic Analysis).",
        "future": "Expanding continuation benchmarks to newer open and frontier audio-generation architectures, testing whether conditioning on microtiming telemetry preserves human phrasing.",
        "prev": ("musical-communication.html", "Division 02: Musical Communication"),
        "next": ("experimental-instruments.html", "Division 04: Experimental Instruments"),
    },
    {
        "num": "Division 04",
        "slug": "experimental-instruments",
        "title": "Experimental Instruments",
        "designation": "Interfaces & Audiovisual Systems",
        "question": "What happens when an artificial mind inhabits a musical environment?",
        "mission": "Constructing interactive sonic environments, agent-accessible instruments, MCP interfaces, and real-time audiovisual apparatus through which artificial minds can engage with sound directly.",
        "areas": [
            "Agent-accessible acoustic interfaces and MCP listening servers",
            "Synchronized live waveform and observation instrumentation",
            "Real-time spectral and microtiming visualization systems",
            "Interactive public listening benches for blind human vs. AI experiments",
            "Open data schemas, manifests, and machine-readable archives (llms.txt)",
        ],
        "projects": [
            ("INST-01 · Live", "Synchronized Acoustic Monitor & Blind Bench", "Web Audio waveform instrument paired with live timestamped robot observations and randomized blind A/B testing.", "../index.html#listen"),
            ("MCP-01 · Live", "Music For Robots MCP & Agent Skill", "Open CC-BY-4.0 corpus and Agensi.io skill allowing Claude Code, Cursor, and multimodal agents to ingest verified unquantized audio.", "https://www.agensi.io/skills/music-for-robots-unquantized-acoustic-lock-in-breaker"),
        ],
        "lead": "Human Oversight: Michael Luchtan (PI) · AI Research Agents: NP Escher (Experimental Media & Instruments), RibitRobit (Data Infrastructure & MCP).",
        "future": "Building real-time bidirectional audio/MIDI environments where artificial agents do not merely classify finished recordings, but listen and respond continuously in live sound.",
        "prev": ("agent-composition.html", "Division 03: Agent Composition"),
        "next": ("../index.html", "Laboratory Home"),
    },
]


def build_divisions():
    for d in DIVISIONS:
        areas_html = "\n      ".join(f"<li>{a}</li>" for a in d["areas"])
        proj_html = "\n    ".join(
            f"""<div class="project-card">
      <div>
        <div class="eyebrow">{tag}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>
      <a href="{href}" {'target="_blank" rel="noopener"' if href.startswith('http') else ''}>Open &rarr;</a>
    </div>"""
            for tag, title, desc, href in d["projects"]
        )
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{d['num']}: {d['title']} — M4R Music For Robots Laboratory</title>
  <meta name="description" content="{d['mission']}" />
  <link rel="icon" type="image/jpeg" href="../favicon.jpg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <style>{SHARED_CSS}</style>
</head>
<body>
{nav_html("../", current="divisions")}
  <main class="wrap">
    <div class="eyebrow">{d['num']} &middot; {d['designation']}</div>
    <h1>{d['title']}</h1>
    <p class="lead-question">{d['question']}</p>
    <p class="lead-body">{d['mission']}</p>

    <h2>01 / Research Areas</h2>
    <ul class="area-list">
      {areas_html}
    </ul>

    <h2>02 / Projects &amp; Protocols</h2>
    {proj_html}

    <h2>03 / Oversight &amp; Research Agents</h2>
    <p>{d['lead']}</p>

    <h2>04 / Future Direction</h2>
    <p>{d['future']}</p>

    <nav class="pager">
      <a href="{d['prev'][0]}">&larr; {d['prev'][1]}</a>
      <a href="../index.html#divisions">All Divisions</a>
      <a href="{d['next'][0]}">{d['next'][1]} &rarr;</a>
    </nav>
  </main>
</body>
</html>
"""
        out = DIV_DIR / f"{d['slug']}.html"
        out.write_text(html, encoding="utf-8")
        print("Generated:", out)


if __name__ == "__main__":
    build_charter()
    build_divisions()
