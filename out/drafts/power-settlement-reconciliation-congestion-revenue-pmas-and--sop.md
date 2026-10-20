---
title: Daily congestion revenue check and PMA / dispute reconciliation SOP
opportunity: Power settlement reconciliation: congestion revenue, PMAs and counterparty disputes
type: SOP
why_this_artifact: The work is hand-calculated and chased by email from memory (amounts, PMAs, tapes, distribution lists), so a single written procedure changes the next morning more than a template or one email would.
---

# Daily congestion revenue check and PMA / dispute reconciliation

Roles: **RT desk** (Portland real-time), **Flash and settlement group**, **Volume Management**, **Desk heads / support**, **Settlements**.
Note: the steps below are drawn from the evidence. Automation (CAISO award-file calculation, Enpower matching) is a later step. This SOP is the manual version until then.

## A. Daily: congestion relief revenue vs. the flash (RT desk)

1. Pull the CAISO congestion relief awards for each hour of the operating day, including weekends. Hours go missing from both sides' calculations and from the CAISO site, so list all 24 hours and mark any that are absent. (corpus/williams-w3/sent_items/302, line 21)
2. Calculate revenue as MW awarded x price per hour. Total it. Example of the expected form: "We were awarded 218 mws of congestion relief by the CAISO. This should equal $54059.64 in congestion revenue to ECTRT." (corpus/williams-w3/sent_items/383, line 24)
3. Email the figure with the subject `RT congestion for {MM/DD}` to the flash and settlement group. Use the distribution list, not individual names. A sheet sent to the wrong recipients is a known failure: "the people who need the sheet are still not getting it", and the fix was to send it to EES Power Settlements. (corpus/williams-w3/sent_items/456, line 26)
4. Next morning, compare your figure with the flash. If it matches, reply once to confirm: "we got that exact amount in the flash today." (corpus/williams-w3/sent_items/321, line 26)
5. If it does not match, state the missing hour, MW and price in the first line, for example "missing the congestion revenue from HE {n} on {day} ({x} mws at ${price}) in the flash". Send it to the flash group and Volume Management so they can recalculate by hour. (corpus/williams-w3/sent_items/302, line 21)
6. Exposure is tallied daily from the California flash, so a gap not corrected that day carries into the exposure number. (corpus/williams-w3/sent_items/317, line 22)

## B. Month-end: prior-month adjustments (PMAs) (desk heads and support)

1. Go through every PMA line by line. For each line record: deal, counterparty, revenue amount, cost amount.
2. Flag one-sided PMAs (revenue reversed with no cost reversed, or the reverse). These stay open across several emails if not flagged. Test: does the net loss equal the real net difference? Example query: "We should only lose $40 (the net difference). Any ideas?" (corpus/williams-w3/sent_items/435, line 21)
3. For a counterparty change that shows a loss, ask Settlements to explain it explicitly: "Why does a change in counterparty result in a loss of revenue?" (corpus/williams-w3/sent_items/442, line 21)
4. For large unexplained amounts, name the amount and the entry in the query, for example the WBOM $108,000 item. Do not just say "still a problem". (corpus/williams-w3/sent_items/424, line 20)
5. Check how the deal was restructured; for example, internal transfers such as "ST-Whourly will pay LT-NW our average hourly price per mw for that energy." Use that logic to judge whether the adjustment is correct. (corpus/williams-w3/sent_items/388, line 21)
6. Reconcile ISO revenue against Volume Management totals and the inc sheets. Prior-year inc sheets and service sheets may be needed. (corpus/williams-w3/sent_items/456, line 17)
7. Log each open item with an owner and a date. Anything open after one follow-up goes into the dispute tracker (section C).

## C. Counterparty disputes (El Paso Electric, SRP, MPC)

1. Open one tracker row per disputed deal: deal number, counterparty, hours in question, amount, owner, status, link to tape / evidence, decision.
2. Establish what happened on the specific hours. There is nothing in the notebooks, so request the trade tape, or ask the person who did the deal. Tape access goes through another person, so make the request on day 1 of the dispute. (corpus/williams-w3/sent_items/426, line 17)
3. Record the reason for any deal alteration. About 30 disputes arose from EOL deals altered without notes. Require a reason field for every alteration. (input stall_points)
4. Record the decision and the outcome in the tracker and close the row. Review all open rows at each month-end.

## What to watch for (summary)

| Failure | Control |
|---|---|
| Missing hour in the flash or at CAISO | Hour-by-hour list in A1 and A5 |
| Sheet reaches the wrong people | Use the group list (A3) |
| One-sided PMA | Revenue and cost columns checked in B2 |
| Dispute drags for months | Tape requested on day 1, tracked in C |
| Undocumented deal alteration | Reason required (C3) |

Estimated impact of the manual-to-automated shift: about 2.35 hours/month (about $200/month), from 47 dated messages over 6 months at 45 min each and a 0.4 automatable fraction.
