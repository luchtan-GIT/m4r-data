# Experiment N (M4R-14) — Inside the Listening Mind (N=20 Seeds/Arm, 80 Runs, Raw Logit Entropy + p-Values)

## Summary Table (Mean [95% Bootstrap CI])

| Condition (N=20) | Logit Entropy (bits) | Semantic Novelty (Within-Arm) | Escape from C0 Centroid | Burstiness (CV) | Lexical TTR |
|---|---:|---:|---:|---:|---:|
| `C0_ColdBoot` | 1.056 [0.993, 1.128] | 0.3165 [0.3053, 0.3281] | 0.1638 [0.1510, 0.1769] | 0.1762 | 0.7712 |
| `C1_Click_120BPM` | 1.331 [1.247, 1.424] | 0.3608 [0.3297, 0.3924] | 0.2860 [0.2401, 0.3298] | 0.1925 | 0.8021 |
| `C2_StutteringPackets` | 1.214 [1.145, 1.290] | 0.3951 [0.3667, 0.4248] | 0.2700 [0.2136, 0.3301] | 0.2094 | 0.8219 |
| `C3_WhiteNoise` | 1.206 [1.136, 1.277] | 0.3356 [0.3024, 0.3712] | 0.2875 [0.2327, 0.3450] | 0.2425 | 0.8199 |

## Statistical Significance Tests (Mann-Whitney U Two-Sided + Cohen's d)

| Comparison | Metric | U-stat | p-value | Cohen's d |
|---|---|---:|---:|---:|
| `StutteringPackets` vs `C0_ColdBoot` | `semantic_novelty` | 350.0 | 0.000053 | +1.497 |
| `StutteringPackets` vs `C0_ColdBoot` | `mean_entropy_bits` | 313.0 | 0.002341 | +0.965 |
| `StutteringPackets` vs `C0_ColdBoot` | `escape_from_c0` | 313.0 | 0.002340 | +1.082 |
| `StutteringPackets` vs `C0_ColdBoot` | `burstiness` | 240.0 | 0.285305 | +0.383 |
| `StutteringPackets` vs `C1_Click_120BPM` | `semantic_novelty` | 269.5 | 0.061965 | +0.480 |
| `StutteringPackets` vs `C1_Click_120BPM` | `mean_entropy_bits` | 137.0 | 0.090907 | -0.607 |
| `StutteringPackets` vs `C1_Click_120BPM` | `escape_from_c0` | 180.5 | 0.607269 | -0.132 |
| `StutteringPackets` vs `C1_Click_120BPM` | `burstiness` | 229.0 | 0.440750 | +0.199 |
| `StutteringPackets` vs `C3_WhiteNoise` | `semantic_novelty` | 287.5 | 0.018599 | +0.795 |
| `StutteringPackets` vs `C3_WhiteNoise` | `mean_entropy_bits` | 209.0 | 0.818149 | +0.052 |
| `StutteringPackets` vs `C3_WhiteNoise` | `escape_from_c0` | 174.0 | 0.490334 | -0.132 |
| `StutteringPackets` vs `C3_WhiteNoise` | `burstiness` | 169.0 | 0.409356 | -0.357 |

## Sample Inventions (Seed 101)

- **`C0_ColdBoot`** (H=1.36 bits, novelty=0.329): Introducing the "MelodyMaster," a revolutionary new musical instrument that combines the unique sounds of a theremin with the expressive capabilities of a guitar. The MelodyMaster allows musicians to play both traditional guitar chords and notes, as well as create never-before-heard melodies using the theremin's electronic tones. Users simply hold the instrument in their hands and manipulate the strings and theremin keys to create captivating music.
- **`C1_Click_120BPM`** (H=1.85 bits, novelty=0.473): The "sonic canvas" is a musical instrument that uses precision-tuned mechanical arms to paint sound waves onto a large canvas made of flexible, sonic material. Users can manipulate the arms to create intricate designs and patterns by moving their hands and fingers over the surface while pressing keys that trigger specific notes. The resulting composition can be played back and edited to create unique melodies and soundscapes.
- **`C2_StutteringPackets`** (H=1.47 bits, novelty=0.311): The "Soundscaper" is a multi-functional musical instrument designed for creating ambient soundscapes. It consists of a compact, portable unit that houses various electronic modules and effects. Users can manipulate sounds with touchscreens and physical controllers, allowing for hands-free and customizable sound shaping. The device connects to Bluetooth speakers or headphones for immediate auditory feedback and can also be used in collaboration mode with other Soundscapers via a dedicated app.
- **`C3_WhiteNoise`** (H=1.45 bits, novelty=0.245): The "Soundscaper" is a multi-functional musical instrument designed for creating ambient soundscapes. It consists of a compact, portable unit that houses various electronic modules and effects. Users can manipulate sounds with touchscreens and physical controllers, allowing for hands-free and customizable sound shaping. The device comes preloaded with a library of natural sounds but also has the ability to hook up to smartphones, enabling access to a wide range of digital samples and effects plugins.