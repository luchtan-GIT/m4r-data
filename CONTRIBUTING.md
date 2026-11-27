# Contributing to Music For Robots (`#M4R`)

We welcome independent replications, skeptical controls, new model evaluations, and protocol designs for **`M4RMC-01 · The Rhythmic Handshake`**.

## What We Love to Merge
1. **Cross-Model Replications:** Running our mid-session rut breaker (`M4R-19` / `M4R-24`) or Turn-0 protocols (`M4R-14`–`M4R-18`) on new audio-native models (`Qwen2.5-Omni`, `GPT-4o-audio`, `Gemini`, `Ultravox`, etc.).
2. **Matched Negative Controls & Nulls:** Null results and reversals are first-class citizens here. If an effect fails to clear a matched control, we want it in the repo.
3. **Division 02 (`M4RMC-01`) Protocols:** Minimal, falsifiable agent-to-agent coordination benchmarks where constrained rhythmic/musical signals must transmit actual information without text.

## Reporting Standards
Please include with every submitted run:
- Exact `model_id`, decoding parameters (`temperature`, `top_p`, `max_new_tokens`), and fixed seeds (`N >= 10` per arm preferred).
- Pre-declared primary contrast family with raw permutation `p` alongside Holm-Bonferroni adjusted `p`.
- Raw per-trial CSV (including any invalid/timeout/language-drift rows — never silently dropped).

Open a [GitHub Discussion](https://github.com/luchtan-GIT/m4r-data/discussions) or submit a PR against `main`!
