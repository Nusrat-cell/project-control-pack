"""Risk and issue logs: scoring, rating, overdue reviews and issue ageing."""
from datetime import timedelta

REVIEW_EVERY_DAYS = 14


def rating(score):
    return "high" if score >= 15 else "medium" if score >= 8 else "low"


def risks(items, status_date):
    out = []
    for rid, text, prob, impact, owner, mitigation, reviewed in items:
        score = prob * impact
        due = reviewed + timedelta(days=REVIEW_EVERY_DAYS)
        out.append(dict(id=rid, text=text, probability=prob, impact=impact, score=score, rating=rating(score), owner=owner,
                        mitigation=mitigation, last_review=reviewed, review_due=due, overdue=due < status_date))
    return sorted(out, key=lambda r: -r["score"])


def issues(items, status_date):
    out = []
    for iid, text, raised, owner, status in items:
        age = (status_date - raised).days
        out.append(dict(id=iid, text=text, raised=raised, owner=owner, status=status, age_days=age,
                        stale=status == "open" and age > 14))
    return out
