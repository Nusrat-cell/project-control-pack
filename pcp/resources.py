"""Resource plan: weekly allocation per person and over-allocation."""
from datetime import timedelta


def plan(resources, start):
    out = []
    for person, role, weeks in resources:
        over = [(start + timedelta(weeks=i), pct) for i, pct in enumerate(weeks) if pct > 100]
        out.append(dict(person=person, role=role, weeks=weeks, peak=max(weeks), over=over))
    return out
