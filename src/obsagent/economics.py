"""Hours and dollars — all arithmetic lives here, none of it in a model.

Inputs per opportunity:
  - the set of corpus messages attributed to the process (validated ids);
  - `minutes_per_occurrence`: model estimate of hands-on time per occurrence,
    across everyone who touches it (the one number the model supplies, and it
    is shown next to every result so a reader can disagree with it);
  - `automatable_fraction`: model estimate in [0, 1] of that time an automation
    removes.

Derived deterministically:
  occurrences_per_month = dated messages / active months
     (active months = calendar months between the first and last dated message,
      inclusive; minimum 1). Undated messages are counted in `messages_total`
      but excluded from the rate.
  gross_hours_per_month = occurrences_per_month * minutes_per_occurrence / 60
  hours_saved_per_month = gross_hours_per_month * automatable_fraction
  dollars_saved_per_month = hours_saved_per_month * BLENDED_RATE

The corpus holds four mailboxes, so the rates are what these four people's
mail shows — no extrapolation to the wider company is applied.
"""
from __future__ import annotations

from datetime import datetime

BLENDED_RATE = 85.0


def active_months(dates: list[str]) -> int:
    ds = sorted(d for d in dates if d)
    if not ds:
        return 1
    first, last = datetime.fromisoformat(ds[0]), datetime.fromisoformat(ds[-1])
    return max(1, (last.year - first.year) * 12 + (last.month - first.month) + 1)


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def compute(opportunity: dict, message_dates: dict[str, str | None]) -> dict:
    msgs = opportunity.get("messages", [])
    dates = [message_dates.get(m) for m in msgs]
    dated = [d for d in dates if d]
    months = active_months(dated)
    minutes = clamp(float(opportunity.get("minutes_per_occurrence", 0) or 0), 0, 480)
    frac = clamp(float(opportunity.get("automatable_fraction", 0) or 0), 0.0, 1.0)
    occ_pm = len(dated) / months if dated else 0.0
    gross = occ_pm * minutes / 60.0
    saved = gross * frac
    dollars = saved * BLENDED_RATE
    return {
        "messages_total": len(msgs),
        "messages_dated": len(dated),
        "first_date": min(dated)[:10] if dated else None,
        "last_date": max(dated)[:10] if dated else None,
        "active_months": months,
        "occurrences_per_month": round(occ_pm, 2),
        "minutes_per_occurrence": minutes,
        "automatable_fraction": frac,
        "gross_hours_per_month": round(gross, 2),
        "hours_saved_per_month": round(saved, 2),
        "dollars_saved_per_month": round(dollars, 2),
        "blended_rate": BLENDED_RATE,
        "formula": "dated_messages / active_months * minutes / 60 * automatable_fraction * 85",
    }


def rank(opportunities: list[dict]) -> list[dict]:
    ranked = sorted(opportunities, key=lambda o: (-o["economics"]["dollars_saved_per_month"], o["name"]))
    for i, o in enumerate(ranked, 1):
        o["rank"] = i
    return ranked
