---
title: Bankruptcy book-move request and master deal list template
opportunity: Bankruptcy and Netco separation bulk deal moves
type: template
why_this_artifact: Every move request to IT has to be clarified for book ids, commodity and cutoff date, and lists arrive in several versions, so one fixed request form plus one master list layout removes the rework.
---

# Bankruptcy book-move request and master deal list

Use this for every list of deals or counterparties that must be zeroed, killed or moved into bankruptcy books. Credit, legal and contracts staff send lists as updates, stragglers and corrections (corpus/giron-d/inbox/115, line 23; corpus/giron-d/inbox/105, line 22). The gas risk group cross-checks them and sends one request to IT.

## Part 1. Master deal list (one shared spreadsheet)

Keep one document, not one per sender. A combined sheet was already needed once: "Cyndie Balfour-Flanagan will combine all our spreadsheets so that we are working off one document" (corpus/giron-d/inbox/93, line 26).

| Column | Notes |
|---|---|
| List version / source file | Which email and sender it came from, so corrections replace earlier rows |
| Date received | |
| Date reported to risk | Senders already supply this column (corpus/giron-d/inbox/105, line 22) |
| Counterparty | |
| Deal id | Check related legs. Example: EH6453.5 was moved as an unwind of leg 2 while EH6453.2 was missing from the list (corpus/giron-d/inbox/42, line 20) |
| Deal type | Physical or financial. Some requests are financial only (corpus/giron-d/inbox/84, line 19) |
| Action | Zero out, kill or move to bankruptcy book. |
| Zero-out effective date | e.g. "zeroed out 12/01 forward" (corpus/farmer-d/logistics/3, line 23) |
| Source book / target book | Book ids, required |
| Commodity code | Required |
| Canadian or US logic | Required |
| Found in books? (Y/N) | Cross-check by counterparty and deal id |
| Duplicate / superseded? | Flag, do not delete |
| Unify paths affected? | Required before any "kill" (see Part 3) |
| Status | Requested / done / confirmed |

Before sending, the risk group (Love, Giron, Gossett) reconciles the new rows against the books and flags gaps and duplicates.

## Part 2. Move request to IT (email body)

To: {IT contact, e.g. Cecilia Cheung}
Cc: {risk group: Love, Giron, Gossett}
Subject: Book move request {batch no.} - {counterparty or entity} - {commodity}

> Please move the deals in the attached master list, rows {row range / version}.
>
> - Source book: {book id}
> - Target book: {bankruptcy book id}
> - Commodity: {commodity code}
> - Canadian or US logic: {Canadian / US}
> - Deal scope: {all / physical only / financial only}
> - Cutoff / effective date: {date}
> - Action: {move / zero out / kill}
> - Number of deals: {n}. Unify impact check attached: {yes / not required because zero-out}
> - Needed by: {date and time, e.g. before books are calculated today}
>
> Please reply when the move and retranslation are complete.

A deadline phrase like "done by the time we calc our books today - no exceptions" (corpus/giron-d/inbox/84, line 19) belongs in "Needed by".

## Part 3. Before any "kill" request

- If a deal is killed, Unify has a problem when paths are associated with it, so request zero-out instead (corpus/farmer-d/logistics/5, line 29).
- Impact questions were raised only after the announcement (corpus/farmer-d/logistics/4, line 38). Run the Unify paths and volumes check first and attach it to the request.

## Part 4. Closing the loop

- Reply to the requester with the count of deals done, like the list of 66 physical deals zeroed out (corpus/farmer-d/logistics/1, line 27).
- Ask for the final list explicitly: "Is this the last list we are going to get?" (corpus/giron-d/inbox/95, line 40). Record the answer in the master list.
- Route new requests to the named risk contacts (corpus/giron-d/inbox/116, line 25).

## Notes

Required-field choices (book ids, commodity, cutoff date, Canadian or US logic) come from the opportunity's stall points and automation description, not from a quote.
