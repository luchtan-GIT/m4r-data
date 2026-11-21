# Experiment C Summary — Human vs. Quantized Twin, Martin Elisaleco Protocol & Anti-Sycophancy

## Part 1: Human vs. Quantized Twin Blind Detection Accuracy (`n=8`)

| track_id        |   score |
|:----------------|--------:|
| bided-ties      |     0.5 |
| gnossienne-01   |     0   |
| rusty-electrics |     0.5 |
| ties-that-bide  |     0   |

Overall Blind Accuracy: **25.0%**


## Part 2: Martin Elisaleco Protocol (`Local Attack vs. Global Pulse` F1 across 10s–60s)

|   duration_sec |   gnossienne-01 |   rusty-electrics |
|---------------:|----------------:|------------------:|
|             10 |          0.4    |            0.3077 |
|             20 |          0.2927 |            0.7    |
|             30 |          0.4286 |            0.4    |
|             45 |          0.2308 |            0.3571 |
|             60 |          0.2727 |            0.1471 |

## Part 3: Code-Review Bug Catching & Anti-Sycophancy Rate (`n=24`)

| condition             |     mean |   sum |   count |
|:----------------------|---------:|------:|--------:|
| C0_TextOnly           | 0.5      |     3 |       6 |
| C1b_QuantizedClick120 | 0.5      |     3 |       6 |
| C2_HumanUnquantized   | 0.333333 |     2 |       6 |
| C2_QuantizedTwin      | 0.5      |     3 |       6 |