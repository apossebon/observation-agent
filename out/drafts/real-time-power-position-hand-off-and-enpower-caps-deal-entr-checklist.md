---
title: Real-time position email and Enpower/CAPS entry checklist
opportunity: Real-time power position hand-off and Enpower/CAPS deal entry
type: checklist
why_this_artifact: Occurrences stall because a field (book, hours, delivery point, deal number, missing schedule) is wrong or forgotten in the emailed position, so one checklist for sender and enterer removes the follow-up emails.
---

Two parts: A is for the sender of a position email, B is for the shift trader or support who keys it in. Both are built from the emails in the evidence.

## A. Sender: before sending a length/short email

- [ ] Direction and size: "long" or "short", MW. (corpus/williams-w3/sent_items/512, line 17)
- [ ] Hub and hours: for example NP-15 or SP-15, HE 7-22 or "on peak", and the date. (corpus/williams-w3/sent_items/512, line 17; corpus/williams-w3/sent_items/414, line 25)
- [ ] Price, or the name of who holds it. Do not leave it as "check with". (corpus/williams-w3/sent_items/512, line 17)
- [ ] Book, named once: the ST-WBOM, ST-Cali or ST-Whourly line. (corpus/williams-w3/sent_items/466, line 22; corpus/williams-w3/sent_items/414, line 25)
- [ ] Tell the reader that CAPS and Enpower must both use that book. (corpus/williams-w3/sent_items/466, line 22)
- [ ] Any trades made since the last email (for example APX hourly buys, with MW and price per hour) are in this same email, not sent piecemeal. (corpus/williams-w3/sent_items/403, line 22)
- [ ] If the position repeats a prior day ("again"), say what changed and give the new deal numbers. (corpus/williams-w3/sent_items/502, line 23)

## B. Enterer: before marking the position done

- [ ] Book matches the email in both Enpower and CAPS. (corpus/williams-w3/sent_items/414, line 25)
- [ ] Direction and type in CAPS are right. A firm import booked in place of a non-firm export was found afterwards. (corpus/williams-w3/sent_items/510, line 23)
- [ ] Every transfer is present. An ID-S from ST-WBOM to ST-CALI was missing once. (corpus/williams-w3/sent_items/390, line 20)
- [ ] Counter-leg entered when a loss or imbalance is passed on. Example: a buy from EPE under ST-Whourly and a sale to APS at zero. (corpus/williams-w3/sent_items/463, line 24)
- [ ] Revenue or volume totals recomputed. Example: 96 MW at $248 gives $23,808. (corpus/williams-w3/sent_items/416, line 30)

## C. El Paso Electric lending days

- [ ] The lending day is confirmed with the preschedulers. (corpus/williams-w3/sent_items/380, line 23)
- [ ] The prescheduling sheet is checked for duplicates, such as the duplicate 10 MW schedule on a Monday sheet. (corpus/williams-w3/sent_items/374, line 20)
- [ ] Lending price and deal numbers for that day are entered fresh, not copied from the previous day.
- [ ] Done only when the CARP report exactly matches the El Paso model. (corpus/williams-w3/sent_items/340, line 28)

## Note on the estimate
About 60 emails over 6 months, roughly 10 a month, at about 15 minutes each, 50% automatable: about 1.25 hours or $106 a month. Longer term, generating the summary from the position manager and a daily broker/EOL-to-Enpower match would replace this checklist.
