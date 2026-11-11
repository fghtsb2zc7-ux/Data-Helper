#!/usr/bin/env python3
"""Progress helper for the study-9014 coach.

Keeps the learner's state in study/state/ using the ADHD Study Coach plugin's file formats
(profile.json, review-schedule.json, sessions.log.jsonl). Standard library only.

  python3 study/tools/coach.py status              # due topics, weakest topics, coverage
  python3 study/tools/coach.py next [N] [--sprint] # which topics to ask next, and unasked question ids
  python3 study/tools/coach.py grade <topic> <solid|shaky|blank> [--qid ID] [--key "one-line rule"]
  python3 study/tools/coach.py log '<json>'        # append one session line
  python3 study/tools/coach.py questions <topic>   # question ids in the bank for a topic
"""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

STUDY = Path(__file__).resolve().parent.parent
BANK = STUDY / "bank"
STATE = STUDY / "state"
SCHEDULE = STATE / "review-schedule.json"
LOG = STATE / "sessions.log.jsonl"
PROFILE = STATE / "profile.json"

SUBJECT = "ENVRSUST 9014"
INTERVALS = [1, 3, 7, 16, 35, 90]
HEADER = re.compile(r"^### (\S+) · (\S+) · (\S+) · (.+)$")


def today():
    return date.today()


def load_schedule():
    if SCHEDULE.exists():
        return json.loads(SCHEDULE.read_text())
    return []


def save_schedule(items):
    STATE.mkdir(parents=True, exist_ok=True)
    tmp = SCHEDULE.with_suffix(".tmp")
    tmp.write_text(json.dumps(items, indent=2, ensure_ascii=False))
    tmp.replace(SCHEDULE)


def bank_questions(include_drills=False):
    """Return {topic: [question ids]} from every bank file (drills only when asked)."""
    out = {}
    for f in sorted(BANK.glob("*.md")):
        if f.name == "README.md":
            continue
        for line in f.read_text().splitlines():
            m = HEADER.match(line)
            if m and (include_drills or m.group(3) != "drill"):
                out.setdefault(m.group(2), []).append(m.group(1))
    return out


def bank_topics():
    """Topic keys and tools from the table in bank/README.md."""
    topics = {}
    for line in (BANK / "README.md").read_text().splitlines():
        m = re.match(r"^\| `([a-z0-9-]+)` \| (\w+) \|", line)
        if m:
            topics[m.group(1)] = m.group(2)
    return topics


def find(items, topic):
    for it in items:
        if it["topic"] == topic:
            return it
    return None


def cmd_status():
    items = load_schedule()
    topics = bank_topics()
    t = today().isoformat()
    print(f"profile: {'yes' if PROFILE.exists() else 'MISSING (run onboarding)'}")
    due = [i for i in items if i["dueDate"] <= t]
    print(f"due today ({len(due)}): " + (", ".join(i["topic"] for i in due) or "none"))
    weak = sorted([i for i in items if i.get("lastResult") in ("blank", "shaky")],
                  key=lambda i: (i.get("lastResult") != "blank", -i.get("lapses", 0)))
    print("weakest: " + (", ".join(f"{i['topic']} ({i['lastResult']})" for i in weak[:6]) or "none yet"))
    seen = {i["topic"]: i.get("lastResult", "?") for i in items}
    for tool in ("Excel", "QGIS", "R", "All"):
        keys = [k for k, v in topics.items() if v == tool]
        solid = sum(seen.get(k) == "solid" for k in keys)
        shaky = sum(seen.get(k) == "shaky" for k in keys)
        blank = sum(seen.get(k) == "blank" for k in keys)
        unseen = sum(k not in seen for k in keys)
        print(f"{tool}: {solid} solid, {shaky} shaky, {blank} blank, {unseen} not seen (of {len(keys)})")
    if LOG.exists():
        lines = [l for l in LOG.read_text().splitlines() if l.strip()]
        print(f"sessions logged: {len(lines)}")
        if lines:
            print("last session: " + lines[-1])


def cmd_next(n=5, sprint=False):
    """Due first; in sprint mode then blank > shaky > not seen > solid, else not seen next.
    Ties are interleaved across tools so one round mixes Excel, QGIS and R."""
    items = load_schedule()
    qs = bank_questions()
    tools = bank_topics()
    t = today().isoformat()
    state = {i["topic"]: i for i in items}

    def band(topic):
        it = state.get(topic)
        if it is None:
            return 1.0 if sprint else 2.0
        if it["dueDate"] <= t:
            return 0.0
        if sprint:
            return {"blank": 0.2, "shaky": 0.4, "solid": 3.0}.get(it.get("lastResult"), 1.0)
        return 9.0

    picked = []
    for b in sorted({band(k) for k in qs}):
        if b >= 9:
            break
        group = sorted([k for k in qs if band(k) == b], key=lambda k: -state.get(k, {}).get("lapses", 0))
        by_tool = {}
        for k in group:
            by_tool.setdefault(tools.get(k, "All"), []).append(k)
        while any(by_tool.values()):
            for tool in ("R", "QGIS", "Excel", "All"):
                if by_tool.get(tool):
                    picked.append(by_tool[tool].pop(0))
    for k in picked[:n]:
        asked = set(state.get(k, {}).get("asked", []))
        fresh = [q for q in qs[k] if q not in asked] or qs[k]
        status = state[k].get("lastResult", "?") if k in state else "not seen"
        print(f"{k} [{status}]: {', '.join(fresh)}")


def cmd_grade(topic, result, qid=None, key=None):
    if result not in ("solid", "shaky", "blank"):
        sys.exit("result must be solid, shaky or blank")
    items = load_schedule()
    it = find(items, topic)
    if it is None:
        it = {"subject": SUBJECT, "topic": topic, "notePath": f"notes/{SUBJECT}/{topic}.md",
              "lastReviewed": None, "intervalDays": 1, "dueDate": today().isoformat(),
              "streak": 0, "lapses": 0, "keyPoints": [], "asked": []}
        items.append(it)
        new = True
    else:
        new = False
    if result == "solid":
        if not new:
            idx = INTERVALS.index(it["intervalDays"]) if it["intervalDays"] in INTERVALS else 0
            it["intervalDays"] = INTERVALS[min(idx + 1, len(INTERVALS) - 1)]
        it["streak"] += 1
    elif result == "blank":
        it["intervalDays"] = 1
        it["streak"] = 0
        it["lapses"] += 1
    # shaky keeps the same interval
    it["lastReviewed"] = today().isoformat()
    it["dueDate"] = (today() + timedelta(days=it["intervalDays"])).isoformat()
    it["lastResult"] = result
    if qid and qid not in it.setdefault("asked", []):
        it["asked"].append(qid)
    if key:
        kp = it.setdefault("keyPoints", [])
        if key not in kp:
            kp.append(key)
    save_schedule(items)
    print(f"{topic}: {result}, next due {it['dueDate']} (interval {it['intervalDays']}d, streak {it['streak']}, lapses {it['lapses']})")


def cmd_log(raw):
    entry = json.loads(raw)
    entry.setdefault("date", today().isoformat())
    entry.setdefault("subject", SUBJECT)
    STATE.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print("logged")


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd, rest = argv[0], argv[1:]
    if cmd == "status":
        cmd_status()
    elif cmd == "next":
        sprint = "--sprint" in rest
        nums = [a for a in rest if a.isdigit()]
        cmd_next(int(nums[0]) if nums else 5, sprint)
    elif cmd == "grade":
        if len(rest) < 2:
            sys.exit("usage: grade <topic> <solid|shaky|blank> [--qid ID] [--key TEXT]")
        opts = {}
        i = 2
        while i < len(rest):
            if rest[i] in ("--qid", "--key") and i + 1 < len(rest):
                opts[rest[i][2:]] = rest[i + 1]
                i += 2
            else:
                i += 1
        cmd_grade(rest[0], rest[1], opts.get("qid"), opts.get("key"))
    elif cmd == "log":
        cmd_log(rest[0])
    elif cmd == "questions":
        print(", ".join(bank_questions(include_drills=True).get(rest[0], [])) or "no questions for that topic")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
