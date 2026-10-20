"""Forward and backward pass over the task list: dates, slack and the critical path."""
from datetime import date, timedelta


class PlanError(ValueError):
    pass


def add_workdays(start, days):
    """Date after `days` working days, counting `start` as day one. Weekends are skipped."""
    d = start
    while d.weekday() >= 5:
        d += timedelta(days=1)
    left = days - 1
    while left > 0:
        d += timedelta(days=1)
        if d.weekday() < 5:
            left -= 1
    return d


def next_workday(d):
    d += timedelta(days=1)
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d


def order(tasks):
    """Topological order. Raises PlanError on a cycle or an unknown dependency."""
    ids = {t[0] for t in tasks}
    for t in tasks:
        for dep in t[4]:
            if dep not in ids:
                raise PlanError(f"{t[0]} depends on unknown task {dep}")
    done, out = set(), []
    remaining = list(tasks)
    while remaining:
        ready = [t for t in remaining if all(d in done for d in t[4])]
        if not ready:
            raise PlanError("dependency cycle: " + ", ".join(t[0] for t in remaining))
        for t in ready:
            out.append(t)
            done.add(t[0])
            remaining.remove(t)
    return out


def plan(tasks, start):
    rows = {}
    for tid, name, owner, dur, deps, pct in order(tasks):
        s = max([next_workday(rows[d]["finish"]) for d in deps], default=start)
        while s.weekday() >= 5:
            s += timedelta(days=1)
        rows[tid] = dict(id=tid, name=name, owner=owner, duration=dur, deps=deps, pct=pct, start=s, finish=add_workdays(s, dur))
    finish = max(r["finish"] for r in rows.values())
    # backward pass on workday counts
    succ = {tid: [] for tid in rows}
    for r in rows.values():
        for d in r["deps"]:
            succ[d].append(r["id"])
    late_finish = {}
    for tid in reversed([t[0] for t in order(tasks)]):
        if not succ[tid]:
            late_finish[tid] = finish
        else:
            late_finish[tid] = min(_late_start(rows[s], late_finish[s]) for s in succ[tid])
    for tid, r in rows.items():
        r["slack"] = workdays_between(r["finish"], late_finish[tid])
        r["critical"] = r["slack"] == 0
    return rows, finish


def prev_workday(d):
    d -= timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def _late_start(succ_row, succ_late_finish):
    """Latest date the predecessor may finish so that the successor still ends on its late finish."""
    d = succ_late_finish
    for _ in range(succ_row["duration"] - 1):
        d = prev_workday(d)
    return prev_workday(d)


def workdays_between(a, b):
    """Working days from a to b (b later than a gives a positive number)."""
    if a == b:
        return 0
    step = 1 if b > a else -1
    n, d = 0, a
    while d != b:
        d += timedelta(days=step)
        if d.weekday() < 5:
            n += step
    return n


def late_tasks(rows, status_date):
    """Tasks that should have finished by the status date but are not complete."""
    return [r for r in rows.values() if r["finish"] < status_date and r["pct"] < 100]


def forecast(rows, status_date, tasks):
    """Re-plan the work that is left from the status date. Returns (forecast finish per task, slip in working days)."""
    fc = {}
    for tid, name, owner, dur, deps, pct in order(tasks):
        remaining = round(dur * (100 - pct) / 100)
        base = rows[tid]
        if pct >= 100 or remaining == 0:
            fc[tid] = base["finish"]
            continue
        s = status_date
        for d in deps:
            s = max(s, next_workday(fc[d]) if fc[d] >= status_date else s)
        while s.weekday() >= 5:
            s += timedelta(days=1)
        fc[tid] = add_workdays(s, remaining)
    end_fc = max(fc.values())
    end_base = max(r["finish"] for r in rows.values())
    return fc, workdays_between(end_base, end_fc)
