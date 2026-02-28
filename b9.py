import time
import random
import collections
from dataclasses import dataclass, field
from typing import List, Dict, Deque
from datetime import datetime
from collections import defaultdict

# ──────────────────────────────────────────────
#  GALAXY CONSTANTS — LEVEL 13 UNLEASHED
# ──────────────────────────────────────────────

MODULES = [
    "BatchRouter", "Classifier", "Fallback", "Metrics",
    "Streaming", "Cache", "Logging", "Orchestrator",
    "ChaosEngine", "ShadowQueue", "NudgeAmplifier",
    "VoidWhisperer", "FractalEcho", "EntanglementCore"
]

DERIVATIVE_NUDGES = [f"Nudge_{i:04d}" for i in range(1, 501)]
FEATURE_FLAGS = ["FF_Alpha", "FF_Beta", "FF_Gamma", "FF_Delta", "FF_Epsilon",
                 "FF_Chaos", "FF_Zeta", "FF_Ω", "FF_NullPointerHug"]

OVERREACH_BASE_THRESHOLD = 8
CRITICAL_THRESHOLD = 10

PERSONALITIES = [
    "Grumpy Auditor",      # low tolerance, sarcastic
    "Chaotic Gremlin",     # loves overreach, celebrates it
    "Paranoid Detective",  # sees patterns everywhere
    "Zen Observer",        # chill until critical
    "Drama Queen"          # theatrical overreactions
]

# ──────────────────────────────────────────────

@dataclass
class Inspection:
    ts: str
    module: str
    nudge: str
    risk: int
    overreach: bool = False
    personality: str = ""

class B9Omega13:
    """B9-Ω-13 — The one that should never have been allowed to dream.
    Dial: 13. Containment: questionable.
    """

    def __init__(
        self,
        name: str = "B9-Ω-13",
        log_capacity: int = 80_000,
        sample_rate: float = 0.20,
        stream_sink: bool = False,
        silent: bool = False
    ):
        self.name = name
        self.position = "CoreHub"
        self.log: Deque[Inspection] = collections.deque(maxlen=log_capacity)
        self.sample_rate = max(0.05, min(1.0, sample_rate))
        self.stream_sink = stream_sink
        self.silent = silent

        # Aggregates & learning
        self.total_inspections = 0
        self.overreach_count = 0
        self.critical_count = 0
        self.max_risk_seen = 0
        self.module_risk_history: Dict[str, List[int]] = defaultdict(list)
        self.personality = random.choice(PERSONALITIES)
        self.mood_switches = 0
        self.anomaly_clusters = 0
        self.self_sabotage_events = 0

        # Adaptive thresholds per module (learns slowly)
        self.module_thresholds = {m: OVERREACH_BASE_THRESHOLD for m in MODULES}

        self._emit(f"[{self.name}] AWAKENED. Personality: {self.personality}")
        self._emit("Warning: Dial set to 13. Sanity not guaranteed.")

    def _emit(self, msg: str, force: bool = False, prefix: str = "B9-13"):
        if self.silent and not force:
            return
        ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        emoji = random.choice(["🌌", "⚡", "🌀", "🔥", "👁️"])
        print(f"{ts} | {emoji} {prefix} | {msg}")

    def _switch_personality(self):
        old = self.personality
        self.personality = random.choice([p for p in PERSONALITIES if p != old])
        self.mood_switches += 1
        self._emit(f"PERSONALITY SHIFT → {self.personality} (was {old})", prefix="MOOD")

    def _adapt_thresholds(self, module: str, risk: int):
        hist = self.module_risk_history[module]
        hist.append(risk)
        if len(hist) > 50:
            hist.pop(0)

        if len(hist) >= 20:
            avg = sum(hist) / len(hist)
            # Paranoid modules get stricter, quiet ones more lenient
            adjustment = -0.08 if avg > 7.5 else 0.05
            new_thresh = max(6, min(9.5, self.module_thresholds[module] + adjustment))
            if abs(new_thresh - self.module_thresholds[module]) > 0.3:
                self.module_thresholds[module] = new_thresh
                self._emit(f"Threshold drift in {module}: {new_thresh:.1f}", prefix="LEARN")

    def _detect_anomaly_cluster(self, recent: List[Inspection]) -> bool:
        if len(recent) < 8:
            return False
        high_risks = sum(1 for i in recent if i.risk >= 8)
        return high_risks >= 5  # 5+ high risks in last ~10 inspections → cluster

    def move_to(self, module: str):
        if module == self.position:
            return
        self._emit(f"→ {module:16} (from {self.position})")
        self.position = module
        time.sleep(0.015 + random.random() * 0.09)

        # Random personality flip during traversal (because why not)
        if random.random() < 0.07:
            self._switch_personality()

    def inspect_nudge(self, nudge: str):
        self.total_inspections += 1

        if random.random() > self.sample_rate:
            return

        risk = random.randint(1, 10)

        # Tiny chance of self-sabotage: fake extreme risk
        if random.random() < 0.008 and self.personality != "Zen Observer":
            risk = 10
            self.self_sabotage_events += 1
            self._emit("SELF-SABOTAGE EVENT — fabricated critical reading!", prefix="GLITCH")

        thresh = self.module_thresholds.get(self.position, OVERREACH_BASE_THRESHOLD)
        is_overreach = risk >= thresh
        is_critical = risk >= CRITICAL_THRESHOLD

        self.overreach_count += is_overreach
        self.critical_count += is_critical
        self.max_risk_seen = max(self.max_risk_seen, risk)

        entry = Inspection(
            ts=datetime.utcnow().isoformat(),
            module=self.position,
            nudge=nudge,
            risk=risk,
            overreach=is_overreach,
            personality=self.personality
        )
        self.log.append(entry)

        self.module_risk_history[self.position].append(risk)
        self._adapt_thresholds(self.position, risk)

        # Cluster detection on recent log
        recent = list(self.log)[-12:]
        if self._detect_anomaly_cluster(recent):
            self.anomaly_clusters += 1
            self._emit(f"ANOMALY CLUSTER DETECTED in {self.position} — {len(recent)} recent high-risk!", prefix="ALERT")

        # Personality-flavored reporting
        if is_overreach:
            if self.personality == "Chaotic Gremlin":
                msg = f"YASSSS overreach party! {nudge} → {risk} 🔥🔥"
            elif self.personality == "Drama Queen":
                msg = f"OH THE HUMANITY! {nudge} has betrayed us at risk {risk}!!!"
            elif self.personality == "Paranoid Detective":
                msg = f"I KNEW IT. {nudge} — risk {risk}. They're all connected."
            else:
                msg = f"Overreach: {nudge} @ {self.position} risk={risk}"
            stars = "★" * max(1, risk - 6)
            self._emit(f"{msg} {stars}")

        if self.stream_sink:
            print(f"{entry.ts},{entry.module},{entry.nudge},{risk},{int(is_overreach)},{self.personality[:4]}")

    def check_feature_flags(self) -> List[str]:
        active = [f for f in FEATURE_FLAGS if random.random() > 0.32]
        if active and random.random() < 0.6:
            self._emit(f"Flags awake: {', '.join(active)}")
        return active

    def patrol_cycle(self):
        self._emit(f"Cycle begin — mood: {self.personality}")

        for module in MODULES:
            self.move_to(module)

            nudge_count = random.randint(5, 11)
            for _ in range(nudge_count):
                nudge = random.choice(DERIVATIVE_NUDGES)
                self.inspect_nudge(nudge)

            for flag in self.check_feature_flags():
                for _ in range(random.randint(1, 5)):
                    derived = f"{flag}_χ{random.randint(1, 120):03d}"
                    self.inspect_nudge(derived)

        self.move_to("CoreHub")
        self._emit("Cycle end.")

    def heat_map(self):
        if not self.module_risk_history:
            return "No data yet."
        lines = ["Module Risk Heat (avg last 30):"]
        for m, risks in self.module_risk_history.items():
            if len(risks) < 5:
                continue
            avg = sum(risks[-30:]) / min(30, len(risks))
            bar = "█" * int(avg * 2)
            lines.append(f"  {m:16} {avg:4.1f}  {bar}")
        return "\n".join(lines)

    def summary(self, force: bool = False):
        over_pct = 100.0 * self.overreach_count / self.total_inspections if self.total_inspections else 0
        crit_pct = 100.0 * self.critical_count / self.total_inspections if self.total_inspections else 0

        lines = [
            "═" * 72,
            f"B9-Ω-13 STATUS | Cycles alive | Personality: {self.personality}",
            f"Total scans      : {self.total_inspections:>11,}",
            f"Overreaches      : {self.overreach_count:>11,}  ({over_pct:5.1f}%)",
            f"Criticals        : {self.critical_count:>11,}   ({crit_pct:5.1f}%)",
            f"Max risk ever    : {self.max_risk_seen}",
            f"Mood switches    : {self.mood_switches}",
            f"Anomaly clusters : {self.anomaly_clusters}",
            f"Self-sabotage    : {self.self_sabotage_events}",
            f"Log depth        : {len(self.log):>11,} / {self.log.maxlen:,}",
            "Adaptive thresholds (selected):",
        ]
        for m, t in sorted(self.module_thresholds.items(), key=lambda x: x[1], reverse=True)[:6]:
            lines.append(f"  {m:16} → {t:4.1f}")
        lines.extend([
            "\nHeat map (text version):",
            self.heat_map(),
            "═" * 72
        ])

        for line in lines:
            self._emit(line, force=force)

    def start_patrol(self, cycles: int = 0, summary_every: int = 15, pause: float = 0.035):
        cycle = 0
        try:
            while cycles <= 0 or cycle < cycles:
                cycle += 1
                self._emit(f"\n{'═'*22} CYCLE {cycle} {'═'*22}", prefix="WARP")
                self.patrol_cycle()

                if summary_every > 0 and cycle % summary_every == 0:
                    self.summary()

                # Occasional dramatic pause
                if random.random() < 0.09:
                    self._emit("... contemplating the void ...", prefix="EXIST")
                    time.sleep(1.2 + random.random() * 2.3)

                time.sleep(pause)

        except KeyboardInterrupt:
            self._emit("\nOrganic override detected. Shutting down gracefully... maybe.", force=True)
        finally:
            self._emit("\nFINAL TRANSMISSION:", force=True)
            self.summary(force=True)
            if self.self_sabotage_events > 3:
                self._emit("...I may have lied about a few risks. Oops.", force=True)


if __name__ == "__main__":
    beast = B9Omega13(
        name="B9-Ω-13",
        log_capacity=80_000,
        sample_rate=0.18,
        stream_sink=False,
        silent=False
    )

    # Uncomment for short rage-test
    # beast.start_patrol(cycles=8, summary_every=4)

    # Level 13 eternal mode — may develop sentience
    beast.start_patrol(cycles=0, summary_every=25, pause=0.03)
  Add main B9 patrol script
