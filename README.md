# B9-Omega-Galactic-Patrol

**Class B9 utility bot for chaotic patrol simulation, anomaly theater, and optional ops-sidecar ideas.**

B9 started as a silly patrol script and evolved into a personality-driven simulator with adaptive thresholds, anomaly clusters, and occasional self-sabotage for drama.

It is intentionally weird — but it’s also useful as:
- terminal entertainment
- a toy model for emergent behavior
- a prototype sidecar concept for systems like Sentinel (as observability flavor, not core routing)

---

## What it does

- Patrols pseudo-modules (`BatchRouter`, `Cache`, `Orchestrator`, `ChaosEngine`, etc.)
- Scores nudges with simulated risk (1–10)
- Flags overreach/critical events with personality-dependent output
- Learns per-module thresholds over time
- Detects anomaly clusters from recent patrol history
- Emits periodic summaries + text heat map
- Runs forever (`cycles=0`) until interrupted

---

## Current status

- **State:** experimental / playful
- **Language:** Python 3 (stdlib only)
- **Dependencies:** none outside Python standard library
- **Primary entrypoint:** `b9.py`

---

## Quickstart (60 seconds)

```bash
git clone https://github.com/SimonMallas/B9-Omega-Galactic-Patrol.git
cd B9-Omega-Galactic-Patrol
python3 b9.py
```

Stop with `Ctrl+C`.

---

## Running modes

Right now, runtime options are set directly in `b9.py` under `if __name__ == "__main__":`.

Default is eternal patrol:
```python
beast.start_patrol(cycles=0, summary_every=25, pause=0.03)
```

For short test runs, replace with e.g.:
```python
beast.start_patrol(cycles=8, summary_every=4, pause=0.03)
```

---

## Tunable knobs (in code)

In `B9Omega13(...)`:
- `log_capacity` — ring buffer size (default `80_000`)
- `sample_rate` — fraction of scans processed (clamped `0.05..1.0`)
- `stream_sink` — CSV-style event output
- `silent` — suppress non-forced output

In `start_patrol(...)`:
- `cycles` — `0` for eternal mode
- `summary_every` — print summary cadence
- `pause` — cycle pacing

---

## Output signals

B9 emits:
- patrol transitions
- overreach/critical alerts
- personality shifts
- anomaly cluster alerts
- periodic status summary
- text heat map by module risk

This makes it useful for screenshot-based demos and behavior debugging.

---

## Where B9 fits (and doesn’t)

### Where B9 adds real value

**1) Operator signal layer (best fit)**
- Turns dry metrics into a human-readable watchlist
- Flags odd patterns (latency drift, cache-hit collapse, guardrail/block spikes)
- Pushes output to logs/Slack/console dashboards
- Adds context and urgency without taking control of routing

**2) Drill / chaos assistant (controlled mode)**
- Injects synthetic failure patterns in staging drills
- Helps validate runbooks and on-call reaction speed
- Great for “game day” rehearsal and resilience storytelling
- Explicitly disabled by default in production

**3) Demo + observability storytelling**
- Makes system behavior easier to present to non-engineers
- Turns technical signals into memorable operational narratives
- Useful in release demos, postmortems, and incident walkthroughs

### What B9 can do today
- Run autonomous patrol simulations with adaptive threshold behavior
- Emit anomaly cluster alerts and text heat maps
- Provide personality-rich status output for terminal demos
- Serve as a sidecar concept for Sentinel observability features

### What B9 should not do (yet)
- Own production routing decisions
- Replace deterministic policy enforcement
- Sit in safety-critical request paths

---

## Known limitations

- No CLI flags yet (runtime edits are in code)
- No structured config file yet
- No formal test suite yet
- No package/release automation yet

---

## Roadmap (practical)

1. Add CLI (`--cycles`, `--summary-every`, `--pause`, `--sample-rate`)
2. Add config file mode
3. Add deterministic seed option for repeatable demos
4. Add optional Sentinel sidecar mode (`/b9/status` style output)
5. Add tests for threshold adaptation and anomaly clustering

---

## License

TBD (recommend MIT for fast adoption unless you want stricter terms).

---

## Screenshot

![Class B9 in the Chaos Galaxy](./Screenshot%20from%202026-02-28%2014-00-18.png)

---

> “Here I am, brain the size of a planet, and they ask me to inspect derivative nudges in an imaginary galaxy.”
