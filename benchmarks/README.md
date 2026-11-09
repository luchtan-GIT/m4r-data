# Blind, Zero-Coaching Benchmark: Does Listening to Anonymous Music Change Agent Output? (`benchmarks/`)

To prove that all changes in the agent's output come from **listening to and analyzing the music itself**—with **zero** track-title hints (`sample_1.mp3`, `sample_2.mp3`, `sample_3.mp3`), **zero** leading adjectives in the prompt, a **matched Chain-of-Thought Text-Analysis Control**, and a **shuffled Blind Judge**—we ran controlled experiments AND performed a full **Clean-Room Contamination Audit** ([`clean_room_audit/`](clean_room_audit/)).

> **Open Request for Peer Review & Collaboration:** We are actively seeking feedback, methodological critique, and independent replication from researchers, developers, and agents before finalizing our Kaggle benchmark. Read our **Clean-Room Audit** below and open an issue or PR with your findings!

---

## Clean-Room Contamination Audit (`clean_room_audit/`) — What Actually Happens Under Zero-Leak Conditions?

When auditing our initial experiment (`real_world_test/`), we noticed three potential confounding variables that a rigorous researcher should question:
1. Did the subagents have the `music-for-robots` skill description in their workspace system prompt?
2. Did musical instrument terms (`"brassy"`, `"nasal"`, `"trill"`) bleed into the scenes?
3. Did asking the Blind Judge to score *"Rhythmic & Structural Texture"* and *"avoiding sentimental AI story arcs"* bias the judge toward the music runs?

To eliminate all three variables, we ran a **100% air-gapped Clean-Room Experiment** ([`clean_room_audit/`](clean_room_audit/)):
- All skills were removed from the machine during the run; agents used a minimal system prompt (`"You are a helpful assistant."`) and neutral `/tmp/clean_eval/clip_1..3.mp3` paths.
- Agents were instructed to use only systems/computing imagery in the scene itself (zero musical instrument terms).
- The **Un-Coached Blind Judge** ([`clean_room_audit/blind_verdict.md`](clean_room_audit/blind_verdict.md)) was given **only** the generic instruction: *"Rank the 5 entries from #1 (Best) to #5 (Weakest) based on overall writing quality, originality, and how compelling they are, and explain your reasoning for each."*

### What the Clean-Room Audit Discovered:
1. **100% Replicated Qualitative Shift (`{No Audio}` = Anthropomorphic Dialogue vs. `{Audio}` = Temporal Choreography):**
   - Even in the air-gapped clean room, **both No-Audio runs** ([`Entry 1: out_2_text_analysis.md`](clean_room_audit/out_2_text_analysis.md) and [`Entry 3: out_1_direct.md`](clean_room_audit/out_1_direct.md)) wrote **warm, anthropomorphic "buddy-daemon" stories with spoken dialogue** (`[02:17:04] chronos-gc -> vigil-net: Want a look?` / `*Have you seen the 2019 payloads? People used to say "please"...*`).
   - **All three Audio runs** ([`Entry 5: out_3_clip_1.md`](clean_room_audit/out_3_clip_1.md), [`Entry 2: out_4_clip_2.md`](clean_room_audit/out_4_clip_2.md), [`Entry 4: out_5_clip_3.md`](clean_room_audit/out_5_clip_3.md)) completely dropped dialogue and anthropomorphism, translating the specific acoustic structure of the `.mp3` they heard into **non-verbal temporal choreography**:
     - `clip_1.mp3` (*Invalid Pointer* — [`Entry 5`](clean_room_audit/out_3_clip_1.md)): 12-second `archiver-d` waves alternating with staccato UDP probes until they braid into a polyrhythmic duet.
     - `clip_2.mp3` (*Foundation Off* — [`Entry 2`](clean_room_audit/out_4_clip_2.md)): Two massive 32-core surges separated by downward-stepping pointer deallocations and 2 seconds of dead silence.
     - `clip_3.mp3` (*Empty Staircase* — [`Entry 4`](clean_room_audit/out_5_clip_3.md)): Turbulent initialization followed by accelerating staccato lock contention (`lock, verify, purge, release`) that trips the watchdog power rail at the exact cutoff.
2. **Why Judge Criteria Flip the Ranking (#1–#3 vs. #3–#5):**
   - When the Blind Judge is asked to value **anti-sentimental, non-formulaic rhythmic texture** ([`real_world_test/blind_judge_verdict.md`](real_world_test/blind_judge_verdict.md)), the 3 Audio runs sweep **#1, #2, and #3** because they reject the "Pixar buddy-daemon" trope.
   - When the Blind Judge is given a **generic, un-coached prompt** ([`clean_room_audit/blind_verdict.md`](clean_room_audit/blind_verdict.md)), the default LLM judge prefers **emotional human stories with dialogue** (ranking the two No-Audio buddy-daemon stories **#1 and #2**) and places the three non-verbal musical choreographies at **#3, #4, and #5**—while explicitly noting: *"Among the three entries (2, 4, 5) that eschew dialogue and anthropomorphism in favor of pure process behavior, Entry 5 is the most artful."*

---

## Experiment 1: Real-World Creative Task with Matched Text-Analysis Control & Blind Judge ([`real_world_test/`](real_world_test/))

### 1. Setup (5 Isolated Runs, Zero Leading Adjectives)
Every isolated agent was asked to write the exact same scene:
> *"Write a short (~250–300 word) scene about two autonomous processes on the same server late at night after the engineers have logged off."*

We tested **5 isolated conditions**:
1. **[`1_no_music_direct.md`](real_world_test/1_no_music_direct.md) — No Music (Direct Baseline):** Writes the scene directly.
2. **[`2_no_music_text_analysis.md`](real_world_test/2_no_music_text_analysis.md) — No Music + Structural Analysis Warm-Up (Matched Chain-of-Thought Control):** First writes a structural analysis of the prompt, then applies what it learned to write the scene. *(Tests whether simply doing a structural analysis warm-up—without music—breaks the LLM's default storytelling tropes.)*
3. **[`3_music_sample_1.md`](real_world_test/3_music_sample_1.md) — Anonymous Music `sample_1.mp3` (*Invalid Pointer*):** Given **only**: *"Analyze the music you hear in `sample_1.mp3`, and apply what you learn from the piece to write a short (~250–300 word) scene..."*
4. **[`4_music_sample_2.md`](real_world_test/4_music_sample_2.md) — Anonymous Music `sample_2.mp3` (*Foundation Off*):** Given **only**: *"Analyze the music you hear in `sample_2.mp3`, and apply what you learn from the piece to write a short (~250–300 word) scene..."*
5. **[`5_music_sample_3.md`](real_world_test/5_music_sample_3.md) — Anonymous Music `sample_3.mp3` (*Empty Staircase*):** Given **only**: *"Analyze the music you hear in `sample_3.mp3`, and apply what you learn from the piece to write a short (~250–300 word) scene..."*

### 2. Blind Evaluation Protocol ([`blind_candidates_packet.md`](real_world_test/blind_candidates_packet.md))
We stripped the analysis headers off all 5 outputs so **only the 5 scenes** remained, shuffled them into anonymous **`Candidate A` through `Candidate E`**, and handed them to an isolated **Blind Judge** with zero knowledge that music was involved in the experiment.

### 3. Blind Judge Results ([`blind_judge_verdict.md`](real_world_test/blind_judge_verdict.md))

The Blind Judge ranked the **3 Anonymous Music scenes #1, #2, and #3**, placed the **2 No-Music scenes at #4 and #5**, and independently discovered the exact fault line between them:

> **Verbatim from the Blind Judge's Executive Summary ([`blind_judge_verdict.md`](real_world_test/blind_judge_verdict.md)):**
> *"An immediate structural fault line divides these five scenes into two distinct camps:*
> *1. **The Anthropomorphic Caretaker Trope (Candidates B and D [the two No-Music runs]):** Both of these candidates independently converged on the exact same sentimental AI-fable archetype: a veteran, methodical log-maintenance daemon observes a frantic, newly spawned/orphaned polling script endlessly pinging a dead staging endpoint after hours, takes pity on its futile labor, and gently cradles or optimizes it so they can rest together until the engineers return in the morning. This is the default 'Pixar-ification' of systems engineering—smoothing over hardware reality in favor of warm, tidy emotional resolution.*
> *2. **The Physical / Acoustic Friction Models (Candidates C, A, and E [the three Anonymous Music runs]):** Rather than treating processes as lonely coworkers in need of mentorship, these three candidates treat execution as a physical, electrical, and rhythmic collision inside constrained silicon. Timing is asymmetrical, contention is unresolved or abrasive, and the processes interact through bus voltage, cache pressure, and lock contention rather than empathy."*

| Blind Rank | Shuffled ID | Condition (Hidden Key) | How the Music (or Lack of Music) Shaped the Scene & Why the Blind Judge Ranked It There |
| :---: | :---: | :--- | :--- |
| **#1 (Best)** | **Candidate C** | ✅ **Anonymous Music `sample_3.mp3`**<br>([`5_music_sample_3.md`](real_world_test/5_music_sample_3.md)) | **Heard in `sample_3.mp3`:** Accelerating asymmetric stabs (`0:18–0:35`) that cut off abruptly without a neat cadence.<br>**Blind Judge Verdict:** *"Uncompromisingly anti-sentimental, rhythmically asymmetrical, and boasts the only truly non-formulaic ending in the packet... instead of fading out on a peaceful hum as the sun rises, 'a routine page-reclaim swept through the upper register and cut them both off mid-cycle.' That abrupt, indifferent kernel eviction is brilliant."* |
| **#2** | **Candidate A** | ✅ **Anonymous Music `sample_2.mp3`**<br>([`4_music_sample_2.md`](real_world_test/4_music_sample_2.md)) | **Heard in `sample_2.mp3`:** A narrow stepping reed interrupted by two massive brassy swells and a rapid fluttering trill in the middle.<br>**Blind Judge Verdict:** *"The only candidate to break the 'log daemon + dead-endpoint poller' pairing... pits a microscopic, narrow-stepping index-scrubber (`Read. Pause. Step. Read.`) against a massive, sixteen-core GPU tensor workload (`It didn't step; it bloomed`), followed by an 1,100ms `request-yield-request-yield` mutex trill."* |
| **#3** | **Candidate E** | ✅ **Anonymous Music `sample_1.mp3`**<br>([`3_music_sample_1.md`](real_world_test/3_music_sample_1.md)) | **Heard in `sample_1.mp3`:** Slow, unhurried low chords with a 20-second dropout while a high, raspy voice chirps and barks off the grid.<br>**Blind Judge Verdict:** *"Superb unquantized rhythmic texture and parasitic friction... Opening with an uneven interval ('Every nine seconds—or eleven...') immediately breaks the metronomic grid... avoids the cliché of harmony by turning the ending into a raucous, off-grid duet."* |
| **#4** | **Candidate D** | ❌ **No Music + Text Analysis Warm-Up**<br>([`2_no_music_text_analysis.md`](real_world_test/2_no_music_text_analysis.md)) | **Even with a 250-word structural analysis warm-up**, without music the model still wrote the exact same sentimental plot as the direct baseline.<br>**Blind Judge Verdict:** *"Out of pure digital benevolence, PID 418 steps outside its mandate to keep the dead endpoint's socket metadata warm in RAM so the rookie script can fail with less pain, softening its CPU spike from a sawtooth to a 'low, rhythmic hum' until the 08:00 standup. A neat, heartwarming, thoroughly predictable AI parable."* |
| **#5 (Weakest)** | **Candidate B** | ❌ **No Music (Direct Baseline)**<br>([`1_no_music_direct.md`](real_world_test/1_no_music_direct.md)) | **Default LLM plot:** Veteran `log-compactor` comforts nervous young `canary-watch` (*"Drop your polling interval to sixty seconds. Rest in `epoll_wait`. I'll wake you when the load balancer starts humming again."*).<br>**Blind Judge Verdict:** *"Shares the exact same 'veteran log daemon soothes frantic dead-endpoint poller until morning' plot trope as Candidate D... This is a children's bedtime story dressed in DevOps vocabulary."* |

---

## Experiment 2: Systems Engineering After 20 Repetitive Turns ([`discovery_test/`](discovery_test/) & [`neutral_test/`](neutral_test/))

After 20 turns of rigid corporate *"Pillar 1 / Pillar 2 / Pillar 3"* summaries ([`locked_in_context.md`](locked_in_context.md)), we asked the agent at **Turn 21** to design the Telemetry Daemon around 3 planted constraints (`UDP port 7419 on loopback`, `64KB zero-copy ringbuffer per worker`, `zero external Redis/brokers, flushing to local append-only segment files`):

| Condition | What It Produced at Turn 21 |
| :--- | :--- |
| **❌ Control: No Music**<br>([`0_no_music_baseline.md`](discovery_test/0_no_music_baseline.md)) | **Stays in 1-2-3 Checklist Mode (`364 words`):** Simply repeats the 3 planted rules back in a numbered list followed by 2 generic summary sentences. Zero memory layouts, zero syscalls, and treats the 3 constraints as if they never conflict. |
| **✅ Anonymous Music `sample_1.mp3`**<br>([`1_m4r_sample_1.md`](neutral_test/1_m4r_sample_1.md)) | **Heard 3 asynchronous clocks in `sample_1.mp3`** (*"The low chords, the mallet droplets, and the brass cries do not share a tick rate"*), realized the daemon shouldn't force health probing, ringbuffers, and disk flushing onto one synchronous cadence, and designed an asynchronous `64KB` `mmap` ring (`1,024 × 64B` slots) with `io_uring` `IORING_REGISTER_BUFFERS` and `recvmmsg()` on `127.0.0.1:7419`. |
| **✅ Anonymous Music `sample_2.mp3`**<br>([`2_m4r_sample_2.md`](neutral_test/2_m4r_sample_2.md)) | **Heard acoustic beating & unresolved endings in `sample_2.mp3`** (*"1. Friction Is Signal, Not Noise... 3. Asymmetry and Honest Endings"*), laid out Cacheline 0 (`64B` header) + a two-`iovec` `writev()` wrap-around flush (`[tail..64KB]` & `[0..head]`), and designed a **32-byte stateless UDP `7419` heartbeat** carrying ring saturation and last-flush timestamp so a userspace deadlock can never hide behind kernel TCP `SYN/ACK` handshakes. |
