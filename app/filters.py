REASONS = ("busy", "format", "budget", "language", "hours")
LABELS = {"busy": "заняты на дату", "format": "не берут формат", "budget": "не проходят по бюджету (включая неизвестную цену)", "language": "не работают на выбранном языке", "hours": "не хватает длительности"}


def rejection_reasons(p, q):
    reasons = []
    if q.date in p.busy_dates:
        reasons.append({"reason": "busy", "date": str(q.date)})
    if q.event not in p.event_formats:
        reasons.append({"reason": "format", "event": q.event})
    if p.price_from_kzt is None or p.price_from_kzt > q.budget:
        reasons.append({"reason": "budget", "missing_price": p.price_from_kzt is None,
                        "over_budget_kzt": None if p.price_from_kzt is None else p.price_from_kzt - q.budget})
    if q.lang is not None and q.lang not in p.languages:
        reasons.append({"reason": "language", "language": q.lang})
    if q.hours is not None and p.max_hours is not None and q.hours > p.max_hours:
        reasons.append({"reason": "hours", "missing_hours": q.hours - p.max_hours})
    return reasons
