---
title: Real-time shift SOP - cuts, reconciliation and generator checkout
opportunity: Real-time power schedule, cut and variance corrections
type: SOP
why_this_artifact: The same corrections are done by several traders from memory and procedures keep being re-issued by email, so one written sequence changes the next shift more than a form or a template would.
---

# Real-time shift SOP: cuts, reconciliation, generator checkout

Scope: real-time shift traders and the real-time lead. Roughly 6 occurrences a month (52 dated messages over 9 active months). Steps below use only what the evidence shows. Where the source does not say how something is done, it is marked **[to confirm]**.

## 1. Daily reconciliation (start of shift)
1. Run the CARP report and compare it with the Real Time El Paso model for the EPE reconciliation. (corpus/williams-w3/sent_items/418, line 29)
2. Complete the month's EPE Reconciliation sheet **every day, even with no variances**. Houston assumes the CARP was not run if the sheet is empty. (corpus/williams-w3/sent_items/417, line 18)
3. Compare the SAR and INC sheets. Check whether known imbalance purchases explain the difference. Example: a 42 MW purchase from the imbalance at $44 made the sheets match. (corpus/williams-w3/sent_items/391, line 19)
4. Check Position Manager at each hub. Typical causes are a counterparty-side entry, such as Enron Canada at Mid Columbia, or a missing quantity, such as a 14 MW short at Portland General. (corpus/williams-w3/sent_items/291, line 18; corpus/williams-w3/sent_items/373, line 18)
5. Check for double deal entry in the books, such as ST-WBOM. (corpus/williams-w3/sent_items/453, line 18)

## 2. Recording a cut (Colstrip or counterparty)
Source: the description. Zero the deal and book the offsetting annuity. Enter the cut in every place it is tracked: paper cut sheet and the Lotus Notes database. **[to confirm: exact destination list and owner]**

Rules:
- Log the cut once per destination in the same shift. Do not leave it only on paper, because paper cut sheets get lost (stall point).
- Real-time cuts are not in CAPS, so the SAR and INC will not match until they are added manually. State that in the reconciliation note.
- If deals are added in Enpower only to flatten a report, say so in the note, for example "these deals are only necessary for the sake of the report". (corpus/williams-w3/sent_items/308, line 21)

## 3. Variance found
1. Write to the desk or Houston, naming the book and the cause. Example: "We had a variance in the SAR for the West BOM Book on Friday night." (corpus/williams-w3/sent_items/312, line 41)
2. State the cause and the fix. (corpus/williams-w3/sent_items/372, line 27; corpus/williams-w3/sent_items/308, line 21)
3. Check import IDs and load zones, and create the DA and HA finals in CAPS if the variance came from them. **[to confirm: steps]**

## 4. Weekend and finals checks
- Confirm the HA finals creation and data scrape completed. SQL errors and scrape failures have gone unnoticed over weekends (stall point). **[to confirm: who checks, and when]**

## 5. El Paso Electric schedule
- Before submitting, check that every EPE schedule line has its tag. The sheet has missed tags day after day (stall point). Check out schedules with counterparties by phone as the description states.

## 6. Hourly generator checkout
- Call Grays Harbor and Frontier at the top of **every** hour. (corpus/williams-w3/sent_items/357, line 29)
- Then call BPA and report the **actual** energy generated, not an estimate. (corpus/williams-w3/sent_items/357, line 29)
- Keep an hourly tick list, because calls are sometimes missed (stall point).

## Automation to ask for
Cut-entry form that zeroes the deal, books the annuity and logs the cut once to all destinations. Automated morning SAR, INC and CARP comparison. Automatic tag validation against dispatcher schedules. Alerts on the scrape and finals imports. Metered generator output pulled into the services sheet. Estimated saving about 1.3 h/month (about $110/month): 52 messages / 9 months x 30 min / 60 x 0.45 x $85.
