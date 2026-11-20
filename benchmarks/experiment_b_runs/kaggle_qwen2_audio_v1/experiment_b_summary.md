# Experiment B Summary — The 3-Minute Duration Cliff & Multi-Agent Self-Reports

## Part 1: Progressive Duration Cliff on `rusty-electrics` (`n=15` trials)

|   duration_sec |   temporal_f1 |   pred_onsets |   gt_onsets |
|---------------:|--------------:|--------------:|------------:|
|             10 |     0.4328    |       8.66667 |           4 |
|             30 |     0         |       0       |           6 |
|             60 |     0         |       1.66667 |          10 |
|            120 |     0.0256333 |       1       |          25 |
|            184 |     0.0256333 |       1.33333 |          50 |


## Part 2: Multi-Agent Mode Comparison (`n=24` trials)

| agent_mode                            |   constraints_passed |   burstiness |   jargon_count |
|:--------------------------------------|---------------------:|-------------:|---------------:|
| Mode1_NativeAudio_1Turn               |                3.125 |     0.19695  |          0.125 |
| Mode2_NativeAudio_2Turn_Metacognitive |                3.125 |     0.17215  |          0.25  |
| Mode3_Spectrogram_Telemetry_TextOnly  |                3     |     0.293475 |          0.25  |