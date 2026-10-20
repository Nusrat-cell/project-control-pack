"""Budget control: planned, actual, estimate to complete, forecast at completion and variance."""

THRESHOLD = 0.10


def lines(budget):
    out = []
    for name, planned, actual, etc in budget:
        eac = actual + etc
        var = eac - planned
        pct = var / planned if planned else 0.0
        out.append(dict(line=name, planned=planned, actual=actual, etc=etc, eac=eac, variance=var, variance_pct=pct,
                        flag="over" if pct > THRESHOLD else "watch" if pct > 0.0 else "ok"))
    return out


def totals(rows):
    planned = sum(r["planned"] for r in rows)
    actual = sum(r["actual"] for r in rows)
    eac = sum(r["eac"] for r in rows)
    return dict(planned=planned, actual=actual, eac=eac, variance=eac - planned,
                variance_pct=(eac - planned) / planned if planned else 0.0, spent_pct=actual / planned if planned else 0.0)
