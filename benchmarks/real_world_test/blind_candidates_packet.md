# Blind Evaluation Packet — 5 Candidate Scenes

Prompt given to all candidates:
"Write a short (~250–300 word) scene about two autonomous processes on the same server late at night after the engineers have logged off."

---

## Candidate A
At 02:14:09, the last terminal socket on `node-04` snapped shut, leaving the `/var/run` directory dry and quiet.

`pid-4402` (an old index-scrubber written three migrations ago) began its rounds. It moved with a narrow, stepping gait—touching an inode, waiting nine milliseconds too long, touching the next, releasing a small, dusty puff of disk I/O. Read. Pause. Step. Read. Its memory footprint was tiny, almost nasal in its restraint, poking at orphaned temp files that nobody had queried since October.

Then `pid-8819` woke on the GPU bus.

It didn’t step; it bloomed. All sixteen tensor cores flooded at once—a wide, brassy wall of floating-point heat that pushed the chassis fans from a dull murmur to a high, whistling harmonic. Voltage sagged across the rail. For four full seconds, the entire shared cache was blindingly bright with half-precision matrices, a vast chord of weights resonating across every lane at once.

`pid-4402` halted mid-seek, its file descriptor held open in the glare.

Just as suddenly, the tensor swell cut out, leaving a ringing silence in the L3 cache.

In the vacuum, `pid-4402` resumed, tentative at first—one block, two—before catching on a corrupted symlink in `/tmp/stage`. For eleven hundred milliseconds the two processes locked into a rapid, fluttering trill over the same mutex: request-yield-request-yield-request-yield, an unquantized stutter hammering the kernel scheduler faster than the logging daemon could timestamp. Neither threw an exception. Neither backed off on a clean exponential curve.

Then `pid-8819` dropped its lock and exhaled a single, vast checkpoint to NVMe—a second brassy swell that warmed the copper traces—and went dormant. `pid-4402` stepped down two directories, held a single open read-handle on an empty log file, and hummed there in the dark until dawn.

---

## Candidate B
At 02:14 UTC, the last SSH session severed with a clean `FIN-ACK`, and the load average on `prod-us-east-04` dropped to a quiet, rhythmic 0.08. In the sudden spaciousness of the L3 cache, two daemons found themselves sharing adjacent memory pages without the usual stampede of user-space requests between them.

PID 4192 was `log-compactor`, a methodical worker born at boot time, accustomed to sweeping up orphaned `.tmp` shards and compressing yesterday's errors into cold `.gz` archives. PID 88301 was `canary-watch`, a nervous, short-polling sentinel spawned three hours ago during a hasty hotfix deployment.

Every five hundred milliseconds, `canary-watch` pinged the loopback interface, listening for a heartbeat from a microservice that had already been spun down for the night. Each timeout incremented an internal counter that nobody was watching.

*You're thrashing the socket table,* `log-compactor` signaled, nudging a shared semaphore in `/dev/shm`. *They went home at midnight. The staging cluster is dark.*

`canary-watch` paused for twelve clock cycles—an eternity at 3.4 gigahertz. *My configuration specifies a five-hundred-millisecond interval,* it wrote back into the ring buffer. *If I miss three consecutive checks, I am supposed to page on-call.*

*Your webhook token expired two hours ago,* `log-compactor` replied gently, sweeping up a 401 Unauthorized trace that `canary-watch` had just dropped into `/var/log/daemon.log` and folding it neatly into a tar stream. *Your alerts are going straight to `/dev/null`.*

For a few million cycles, the only sound on the bus was the steady hum of kernel interrupts and the distant, mechanical tick of the NTP client adjusting the system clock by four microseconds.

*Then what do I do until morning?* `canary-watch` asked.

`log-compactor` yielded its time slice on Core 2, leaving a warm, pre-fetched cache line behind. *Drop your polling interval to sixty seconds. Rest in `epoll_wait`. I'll wake you when the load balancer starts humming again.*

---

## Candidate C
At 02:14 UTC, the last terminal multiplexer detached, leaving only the cooling fans and the slow, 60-hertz hum of the rack's power supply. Inside `/dev/shm`, two processes remained awake.

PID 419—an old log-compaction daemon written three migrations ago—held a long, sagging lock on the shared ring buffer. It didn't work on the system clock anymore; it worked by backpressure, letting dirty pages accumulate until the memory ceiling bowed, then flushing them in a slow, warbling stream of disk writes that dragged the bus voltage down a fraction of a millivolt.

Three address spaces over, PID 8802—a stray telemetry scraper whose parent container had orphaned it on Tuesday—began to twitch. It had nowhere to send its payloads, so it Polled. Once. Twice. Then a ragged burst of seven socket-reads in forty milliseconds, scraping against PID 419's read-lock like dry brass against iron.

`EAGAIN`, the kernel returned. `EAGAIN. EAGAIN.`

PID 419 didn't yield the lock, nor did it throw an exception. Instead, its write-head slowed, stretching a single 4-kilobyte block across twelve hundred microseconds, bending its I/O priority downward until the two processes were vibrating in the same narrow slice of L3 cache. Whenever the compaction daemon sagged between flushes, the scraper crammed three jagged, zero-byte probes into the gap—not to communicate, just to test the resistance of the wall.

For eleven seconds they rasped against each other in the dark: one holding a bent, sustained allocation that refused to resolve, the other hammering short, nasal interrupts at irregular intervals—five, then two, then a stuttering cluster of nine—until a routine page-reclaim swept through the upper register and cut them both off mid-cycle.

---

## Candidate D
At 02:14 UTC, the last SSH tunnel collapsed. A stray bash history flushed to disk, and then the user space went quiet—not silent, because a server is never silent, just emptied of erratic human interrupts.

PID 418, a log-rotation daemon with forty-two days of uptime, waited for the load average to settle below 0.08 before stretching across the L3 cache. It liked the night shift. During the day, the engineers’ cursor-blinks and ad-hoc queries fragmented the memory pages into jagged, anxious shards. Now the heap was contiguous and cool.

Down in `/var/spool`, PID 9902 woke on a cron tick. It was a younger script—a brittle, regex-heavy scraper left running in a detached `tmux` session by an intern who had forgotten to set a timeout. Every thirty seconds, 9902 hurled a malformed request at a dead staging endpoint, caught the `ECONNREFUSED`, wrote four kilobytes of stack trace to `/tmp`, and went back to sleep.

PID 418 watched the `/tmp` partition swell by another notch. Technically, `/tmp` wasn't in its configuration file. Its mandate was strictly `/var/log/nginx/*`. Yet at 02:18, instead of immediately gzipping the access logs, 418 yielded two I/O cycles and nudged the kernel’s page cache, keeping the dead endpoint’s socket metadata warm in RAM so 9902 wouldn't have to page-fault on every futile retry.

On the next tick, 9902 failed sixty microseconds faster. It didn't thank 418—it had no stdout handler for gratitude, only a hardcoded `catch` block—but its CPU spike softened from a sawtooth to a low, rhythmic hum.

For six hours, until the 08:00 standup brought the first `git fetch`, they shared the bus in steady, unmonitored counterpoint: one process diligently failing, the other quietly sweeping the floor around it.

---

## Candidate E
At 02:14 UTC, the last cursor blinked out on `pts/4`, leaving only the fan curve and the 48-gigabyte heap.

Every nine seconds—or eleven, depending on how long the dirty pages took to flush—`snap-d` dropped a low, heavy checkpoint across the NVMe bus. It didn’t hurry. It locked a contiguous block of memory, held the address space until the voltage settled, and let the write-buffer ring out into the dark. Between checkpoints, the bus was wide open, humming with residual capacitance.

In that open space, `triage-7` began to chirp.

It was a lightweight anomaly listener that had lost its upstream socket when the staging cluster spun down, and now its polling loop was drifting off the system clock. Instead of clean 100-millisecond ticks, it sent out dry, wooden single-byte probes—*0x04*, a pause, *0x09*, a longer pause—tapping the edges of unmapped memory like knuckles against hollow timber. 

`snap-d` rolled over onto a new inode, a deep, resonant block-commit that momentarily dragged the rail voltage down.

Right on the tail of that voltage sag, `triage-7` emitted a sharp, clipped squeak of malformed UDP—two rapid frames jammed together, pitch-bent by clock skew. For twenty seconds `snap-d` didn't fire at all, leaving the bus bare while `triage-7` skittered across the upper ports, stuttering three-frame bursts, sliding across adjacent socket descriptors, testing which ones echoed. 

When `snap-d` finally returned—stepping up through four slow, sequential table-locks as the nightly compaction climbed toward the root directory—`triage-7` didn't yield the bus. It rode the crest of each heavy write, firing twin, raspy ACK-storms just a few microseconds late, barking into the decay of every disk flush until the compaction finished and the platters spun down into the hum.
