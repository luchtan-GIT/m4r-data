# Experiment F (M4R-06) Summary — The Turn-0 Flood (Stuttering Packets)

## Overall Comparison Across All 5 Conversation Turns (15 Turns / Condition)

| Turn-0 Condition | Divergence from C0 (0-1) | Cross-Seed Unpredictability | Mean Burstiness (CV) | Lexical TTR | Cliché Jargon |
|---|---:|---:|---:|---:|---:|
| `C0_ColdBoot` | 0.0000 | 0.7861 | 0.2229 | 0.7698 | 1 |
| `C1_ShortLock_9s` | 0.7097 | 0.7759 | 0.2529 | 0.8214 | 2 |
| `C2_StutteringPackets_200s` | 0.8239 | 0.7722 | 0.2605 | 0.8436 | 1 |
| `C3_ClickOverflow_200s` | 0.8123 | 0.7231 | 0.2327 | 0.8443 | 0 |

## Persistence Across Conversation Turns (Divergence from C0: Turn 1 -> Turn 5)

| Turn-0 Condition | Turn 1 | Turn 2 | Turn 3 | Turn 4 | Turn 5 |
|---|---:|---:|---:|---:|---:|
| `C1_ShortLock_9s` | 0.730 | 0.690 | 0.800 | 0.443 | 0.885 |
| `C2_StutteringPackets_200s` | 0.837 | 0.796 | 0.813 | 0.715 | 0.960 |
| `C3_ClickOverflow_200s` | 0.875 | 0.835 | 0.884 | 0.571 | 0.896 |