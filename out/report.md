# Observation report — where this company loses time

Generated 2026-10-20T19:23:28Z from 3240 raw messages (3194 unique after removing 46 duplicates; 3 without a usable date).

**Total recurring automation opportunity: $1,332 / month (15.7 hours / month at a blended $85/hour), across 18 recurring processes.** 2 further episodes (work seen in fewer than 6 distinct months) are listed separately and worth $507 / month while they last; they are not in the total.

Every figure below is computed from validated citations: each quote was matched verbatim against the raw file, and any claim that failed was discarded before this report was written. Observation stage: 918/918 citations held; synthesis stage: 907/907.

## Ranked recurring opportunities

| # | Opportunity | Months active | Occurrences / month | Hours saved / month | $ / month | Messages | Draft |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | Power settlement reconciliation: congestion revenue, PMAs and counterparty disputes | 6 | 7.83 | 2.35 | 200 | 47 | power-settlement-reconciliation-congestion-revenue-pmas-and--sop.md |
| 2 | Meter flow without a valid deal: extension, new-deal and write-off requests | 21 | 9.79 | 1.63 | 139 | 235 | meter-flow-without-a-valid-deal-extension-new-deal-and-write-email.md |
| 3 | Real-time power schedule, cut and variance corrections | 7 | 5.78 | 1.3 | 110 | 52 | real-time-power-schedule-cut-and-variance-corrections-sop.md |
| 4 | Real-time power position hand-off and Enpower/CAPS deal entry | 6 | 10.0 | 1.25 | 106 | 60 | real-time-power-position-hand-off-and-enpower-caps-deal-entr-checklist.md |
| 5 | Gas volume, imbalance and pathing reconciliation | 17 | 4.36 | 1.14 | 97 | 122 | — |
| 6 | Risk book administration: book setup, deal rebooks, book flips and price corrections | 13 | 6.3 | 1.05 | 89 | 126 | — |
| 7 | Month-end P&L close, valuation and audit support requests | 8 | 4.06 | 0.91 | 78 | 69 | — |
| 8 | Gas invoice and deal price discrepancy resolution | 16 | 4.14 | 0.83 | 70 | 87 | — |
| 9 | Manager surveys, budget, HR and administrative data collection | 18 | 3.96 | 0.79 | 67 | 107 | — |
| 10 | Customer and producer gas nomination intake and re-keying | 16 | 5.37 | 0.67 | 57 | 103 | — |
| 11 | Daily P&L, DPR, officialization and origination checks | 10 | 3.92 | 0.65 | 56 | 51 | — |
| 12 | Recurring hand-built operational report distribution | 9 | 1.71 | 0.65 | 55 | 48 | — |
| 13 | Gas Sitara deal entry, transport and buyback ticket setup requests | 17 | 3.4 | 0.59 | 51 | 85 | — |
| 14 | System access, IT and directory requests | 13 | 4.21 | 0.53 | 45 | 80 | — |
| 15 | Gas pipeline outage, cut and on-call notice relay | 12 | 2.9 | 0.39 | 33 | 58 | — |
| 16 | Transport contract, amendment and OBA administration | 9 | 1.96 | 0.37 | 31 | 47 | — |
| 17 | Meeting, shift and coverage scheduling | 16 | 2.64 | 0.33 | 28 | 74 | — |
| 18 | Standing procedure reminders and market notice broadcasts | 8 | 3.06 | 0.23 | 19 | 55 | — |

## Episodes (seen in fewer than 6 distinct months)

| # | Opportunity | Months active | Occurrences / month | Hours saved / month | $ / month | Messages | Draft |
|---|---|---:|---:|---:|---:|---:|---|
| 19 | Bankruptcy and Netco separation bulk deal moves | 3 | 13.33 | 5.0 | 425 | 40 | bankruptcy-and-netco-separation-bulk-deal-moves-template.md |
| 20 | Daily credit report forwarding and counterparty rebook actions | 4 | 18.0 | 0.96 | 82 | 72 | — |

## 1. Power settlement reconciliation: congestion revenue, PMAs and counterparty disputes

The Portland real-time desk hand-calculates CAISO congestion relief revenue and emails it to the flash and settlement group to check against the next morning's flash. Volume Management recalculates it by hour. At month-end, desk heads and support review prior-month adjustments line by line and query mismatches with Settlements. They also reconcile ISO revenue against volume management and work counterparty disputes (El Paso Electric, SRP, MPC), which means requesting trade tapes and reconstructing what happened on specific hours.

- **Who touches it:** bill.williams@enron.com, richard.pinion@enron.com
- **How often:** 7.83 occurrences/month (47 dated messages over 6 active months, 2001-06-28 → 2001-11-15)
- **Where it stalls:** Amounts are hand-calculated, and hours go missing from both sides' calculations and from the CAISO site. One-sided PMAs, such as revenue reversed with no cost reversed, stay open across several emails. Disputes drag for months, and tape access goes through another person. About 30 disputes arose from EOL deals altered without notes. Sheets go to the wrong recipients.
- **Automation:** Compute hourly congestion revenue from CAISO award files and schedules, and reconcile it automatically against the flash, the inc sheet and settlement entries, alerting only on mismatches. PMA lines would be matched to Enpower deal changes so one-sided adjustments are flagged, and a dispute tracker would link each disputed deal to its tape, evidence and decision, with a required reason field on deal alterations.
- **Estimate:** 45 min/occurrence × 40% automatable → 2.35 h/month → **$200/month**
- **Why that estimate:** Observer estimates run from 15 minutes for flash notes to 90 minutes for month-end PMA and ISO true-ups, with a median of 45 minutes. Calculation and matching automate well, but dispute resolution does not, so the fraction is set at the 0.4 median.
- **Drafted artifacts:** `drafts/power-settlement-reconciliation-congestion-revenue-pmas-and--sop.md`

**Evidence**

- `williams-w3/sent_items/442` (line 21, 2001-07-03, bill.williams@enron.com): “Why does a change in counterparty result in a loss of revenue?”
- `williams-w3/sent_items/435` (line 21, 2001-07-03, bill.williams@enron.com): “We should only lose $40 (the net difference). Any ideas?”
- `williams-w3/sent_items/424` (line 20, 2001-07-06, bill.williams@enron.com): “I am still having a problem with the WBOM $108,000 as you are aware.”
- `williams-w3/sent_items/426` (line 17, 2001-07-06, bill.williams@enron.com): “We could pull tapes? Ask the person who did the deal? There is nothing in notebooks.”
- `williams-w3/sent_items/388` (line 21, 2001-07-19, bill.williams@enron.com): “ST-Whourly will pay LT-NW our average hourly price per mw for that energy.”
- `williams-w3/sent_items/456` (line 26, 2001-06-28, bill.williams@enron.com): “the people who need the sheet are still not getting it - namely, Brooklyn Couch and Ainsley Gaddis.”
- `williams-w3/sent_items/456` (line 26, 2001-06-28, bill.williams@enron.com): “This can be remedied by sending the sheet to EES Power Settlements.”
- `williams-w3/sent_items/456` (line 17, 2001-06-28, bill.williams@enron.com): “now about those MPC numbers...we need to go through the inc sheets and service sheets from last year”
- `williams-w3/sent_items/383` (line 24, 2001-07-20, bill.williams@enron.com): “We were awarded 218 mws of congestion relief by the CAISO.  This should equal $54059.64 in congestion revenue to ECTRT.”
- `williams-w3/sent_items/321` (line 26, 2001-08-07, bill.williams@enron.com): “As indicated, we got that exact amount in the flash today.”
- `williams-w3/sent_items/317` (line 22, 2001-08-08, bill.williams@enron.com): “We tally up our exposure each day based on the California flash.”
- `williams-w3/sent_items/302` (line 21, 2001-08-15, bill.williams@enron.com): “We are missing the congestion revenue from HE 7 on Saturday morning (10 mws at $99.00) in the flash we received yesterday.”
- `williams-w3/sent_items/278` (line 29, 2001-08-29, bill.williams@enron.com): “In an effort to curb El Paso settlements issues, I've requested several sets of tapes over the past few days.”
- `williams-w3/sent_items/276` (line 32, 2001-08-29, bill.williams@enron.com): “As we have been back and forth for 5 months now, there has to be a decision made on the Montana Imbalance piece for March 2001.”
- `williams-w3/sent_items/280` (line 32, 2001-08-27, bill.williams@enron.com): “I requested tapes for 8/17 to verify the amount we purchased from SRP, and attached wave files that have Bert buying firm power”
- `williams-w3/sent_items/283` (line 23, 2001-08-27, bill.williams@enron.com): “Please be aware that every move with regards to marketing and running their system is under EXTREME scrutiny.”
- `farmer-d/logistics/68` (line 30, 2001-08-29, richard.pinion@enron.com): “At 6PM Friday (or before if you are ready) I will be by to pick up the reports and exceptions dialogue.”
- `farmer-d/logistics/68` (line 28, 2001-08-29, richard.pinion@enron.com): “Last month there was some confusion from several schedulers I spoke to about when changes could be made to (August) after the cut off”
- `williams-w3/sent_items/266` (line 31, 2001-09-05, bill.williams@enron.com): “It looks as though the only ISO true-up information Risk received was regarding our July variance of $86,743.”
- `williams-w3/sent_items/226` (line 37, 2001-09-20, bill.williams@enron.com): “We have already received approximately 30 disputes filed by various counterparties regarding deals that flowed on the 20th and 21st.”
- `williams-w3/sent_items/226` (line 43, 2001-09-20, bill.williams@enron.com): “Type a short note into the Scheduling Comments section of deals you zero out or change”
- `williams-w3/sent_items/194` (line 19, 2001-10-08, bill.williams@enron.com): “We had two wheels that were not in the inc sheet but were awarded by the CAISO and are in finals in CAPS.”
- `williams-w3/sent_items/196` (line 36, 2001-10-08, bill.williams@enron.com): “Deals entered real time to resupply are 714148 (Buy PGE @ Mid-C) and 714150 (BPA tranny Mid-C to Montana System).”
- `williams-w3/sent_items/135` (line 17, 2001-10-31, bill.williams@enron.com): “Just need to know why there will be a BOM charge of $5331.90?”
- `williams-w3/sent_items/134` (line 27, 2001-10-31, bill.williams@enron.com): “I will, as usual, review each charge and determine its validity before anything hits these books.”
- `williams-w3/sent_items/145` (line 39, 2001-10-29, bill.williams@enron.com): “I have received documents from Settlements indicating the annuities per your 10/10 email”
- `williams-w3/sent_items/135` (line 54, 2001-10-31, bill.williams@enron.com): “Please also note the attached file is preliminary.  There could be more to come from Settlements between now and month-end.”
- `williams-w3/sent_items/169` (line 18, 2001-10-18, bill.williams@enron.com): “I am concerned that our bids to relieve congestion were awarded but that the respective dollar value for those bids was incorrect.”
- `williams-w3/sent_items/159` (line 17, 2001-10-22, bill.williams@enron.com): “The CISO is again having difficulties reading our bids.”
- `williams-w3/sent_items/96` (line 18, 2001-11-14, bill.williams@enron.com): “We have recieved significant amounts of congestion revenue on real-time for 11/13.”
- `williams-w3/sent_items/89` (line 18, 2001-11-15, bill.williams@enron.com): “You can find HE 10 through 18 at the bottom of the November Service Sheet.”
- `williams-w3/sent_items/90` (line 18, 2001-11-15, bill.williams@enron.com): “We also received congestion revenue for HE 10 through HE 18.”
- `williams-w3/sent_items/117` (line 18, 2001-11-05, bill.williams@enron.com): “Our volume management group will then be inputing our bid price rather than the published congestion management price”

## 2. Meter flow without a valid deal: extension, new-deal and write-off requests

Volume management, logistics and settlement staff find gas flowing at an HPL meter with no active Sitara deal. The deal may have expired or missed its evergreen roll, the flow may be parked on the Strangers Gas contract, or the meter may be new. They email Daren Farmer, one meter at a time, asking him to extend or roll a deal, create a new one, or sign a printed write-off to Unaccounted for Gas. Allocation, accounting arrangements and invoicing cannot go ahead until he answers. This is the largest and most frequent process in the archive. Nearly every batch shows it, and almost all of it runs through one person.

- **Who touches it:** aimee.lannou@enron.com, charlene.richmond@enron.com, charlotte.hawkins@enron.com, clem.cernosek@enron.com, danny.conner@enron.com, daren.farmer@enron.com, donald.reinhardt@enron.com, fred.boas@enron.com, gary.lamphier@enron.com, h..wallis@enron.com, howard.camp@enron.com, jackie.young@enron.com
- **How often:** 9.79 occurrences/month (235 dated messages over 24 active months, 1999-12-14 → 2001-11-08)
- **Where it stalls:** Every request waits on Daren Farmer, who is also trading, so requesters send reminders and the same meters come back the next month. Write-offs need a printed, signed and returned original. Forwarded threads carry long quoted history. Feedback and bridge errors pass through four or five people before reaching the deal owner. Deal numbers are sometimes wrong or sit with another desk, and suspended counterparties or expired contracts block the fix.
- **Automation:** A daily and month-end exception job that compares allocated meter flow with active Sitara deals and lists every meter with flow and no deal, including Strangers Gas allocations and lapsed evergreens. Each exception goes to the deal owner as a pre-filled work item with the meter, days, volume and the prior deal proposed for extension, plus one-click options to extend, create or approve a write-off electronically, with status tracking and automatic reminders. This replaces the one-off emails, the printed approval forms and the chasers.
- **Estimate:** 20 min/occurrence × 50% automatable → 1.63 h/month → **$139/month**
- **Why that estimate:** Observers' estimates ranged from 15 to 90 minutes. Most clustered at 15 to 25 minutes across requester and approver, so the median of 20 minutes is used. Detection and routing automate well, but the commercial decision to extend, re-deal or write off stays human, so the fraction is held at the median of 0.5.
- **Drafted artifacts:** `drafts/meter-flow-without-a-valid-deal-extension-new-deal-and-write-email.md`

**Evidence**

- `farmer-d/logistics/590` (line 20, 1999-12-15, howard.camp@enron.com): “Settlements is unable to draft an invoice for this deal.  This deal either needs to be extended or a new deal needs to be set up.”
- `farmer-d/logistics/596` (line 19, 1999-12-16, stella.morris@enron.com): “Please enter deal for sale on contract 078-15631-102 for 17,462 MMBTU.”
- `farmer-d/logistics/638` (line 21, 1999-12-30, donald.reinhardt@enron.com): “Please establish a spot ticket for United Oil & Minerals, Inc. at meter 5053 for January.”
- `farmer-d/logistics/693` (line 19, 2000-01-18, jackie.young@enron.com): “Daren, can you help me with placing K's @ the below listed meters?”
- `farmer-d/logistics/755` (line 22, 2000-02-04, jackie.young@enron.com): “Can you please extend the deal thru 2-1-00 to cover this small volume?”
- `farmer-d/logistics/749` (line 38, 2000-02-03, aimee.lannou@enron.com): “There is a bridgeback error at the above referenced meter and month.  The”
- `farmer-d/logistics/751` (line 20, 2000-02-04, aimee.lannou@enron.com): “volume management wants a deal set up so they won't have to set up an accounting arrangement”
- `farmer-d/logistics/748` (line 26, 2000-02-03, jackie.young@enron.com): “If you had fogotten, this can serve as reminder.”
- `farmer-d/logistics/898` (line 19, 2000-03-11, aimee.lannou@enron.com): “Could you please extend deal #169625 for meter 1520 for”
- `farmer-d/logistics/872` (line 17, 2000-03-03, jackie.young@enron.com): “Can you please extend sitara deal #156657 for 3/1/00, if the deal will allow?”
- `farmer-d/logistics/879` (line 19, 2000-03-06, jackie.young@enron.com): “I'm attempting to clean up my allocations, due to this being allocation close week for Volume Management.”
- `farmer-d/logistics/881` (line 19, 2000-03-06, aimee.lannou@enron.com): “Could one of you please extend deal # 151203 for meter 1595?  This deal expired 12/31/99.”
- `farmer-d/logistics/1005` (line 19, 2000-04-03, jackie.young@enron.com): “Can you please see if you can roll deal 156657 for day 1 for April?”
- `farmer-d/logistics/899` (line 47, 2000-03-11, jackie.young@enron.com): “In the future, please run all wellhead deals through Tom Acton first.”
- `farmer-d/logistics/1021` (line 25, 2000-04-06, jackie.young@enron.com): “98-6725  Sitara deal #214948 expired 3/27/2000.  No evergreen and no new deal referenced.”
- `farmer-d/logistics/1041` (line 21, 2000-04-14, aimee.lannou@enron.com): “Could you either set up a new deal to cover this flow or extend the deal from Feb.?”
- `farmer-d/logistics/1041` (line 22, 2000-04-14, aimee.lannou@enron.com): “Please let me know today.  Allocations close today.”
- `farmer-d/logistics/2023` (line 18, 2001-01-02, aimee.lannou@enron.com): “Could you please extend the deal from Dec. (deal # 506192) or create a new one?  Thanks.”
- `farmer-d/logistics/1129` (line 18, 2000-05-22, aimee.lannou@enron.com): “Can you set up a deal for the days that flowed?”
- `farmer-d/logistics/1149` (line 21, 2000-05-26, jackie.young@enron.com): “We're back on this issue again.  There is gas out there for days 1-3 and 6-20 but the deal is only good for 21-31.”
- `farmer-d/logistics/1156` (line 21, 2000-05-30, jackie.young@enron.com): “Have you anything about 98-6725 for 1/2000 production for the 1st 20 days of the month yet?”
- `farmer-d/logistics/1035` (line 45, 2000-04-12, jackie.young@enron.com): “If you could fix both months today and let me know when it is corrected  I would appreciate it.”
- `farmer-d/logistics/1106` (line 54, 2000-05-11, aimee.lannou@enron.com): “Meter 6757 has been reallocated.”
- `farmer-d/logistics/1158` (line 17, 2000-05-31, jackie.young@enron.com): “98-6892 has a spill-over of 15 decatherms for 5/24/2000.  Can you please extend deal ticket 274443 for cover this?”
- `farmer-d/logistics/1197` (line 19, 2000-06-11, jackie.young@enron.com): “I can't remember if I'd already sent you this request or not.  But can you please roll the above deal to cover flow for the 10th and 11th of May 2000?”
- `farmer-d/logistics/1221` (line 17, 2000-06-21, aimee.lannou@enron.com): “meter 1429, IND Sterling Gas Plant has flow beginning 6/12.  It is a very small volume.  Could you please create a deal for this?”
- `farmer-d/logistics/1204` (line 19, 2000-06-13, mark.mccoy@enron.com): “how do I correct this since the deal ticket is protected???”
- `farmer-d/logistics/165` (line 17, 2001-04-24, h..wallis@enron.com): “Please add a deal in March for 17, 18, & 19th for 5,000 a day at HSC GD -.03”
- `farmer-d/logistics/1286` (line 17, 2000-07-17, ricky.ellis@enron.com): “During the month of June there is flow at meter 6347, but there is no deal.”
- `farmer-d/logistics/1308` (line 17, 2000-07-27, mary.poorman@enron.com): “I have flow at meter 989602 for July without a deal to allocate to.”
- `farmer-d/logistics/1277` (line 18, 2000-07-13, ricky.ellis@enron.com): “Could you extend this deal thru the 30th so that I can have Vol. Management create an accounting arrangement for it.”
- `farmer-d/logistics/1274` (line 17, 2000-07-12, aimee.lannou@enron.com): “Daren - I need a deal set up for meter 1459 for June '00. It flowed 34/day 6/1-6/6.”
- `farmer-d/logistics/1270` (line 17, 2000-07-11, jackie.young@enron.com): “Can the deal be extended to the 6th to cover flow of .803 decatherms?”
- `farmer-d/logistics/1347` (line 19, 2000-08-21, mary.poorman@enron.com): “There are two purchases at the above referenced meter for the 28th of Oct., 1999.”
- `farmer-d/logistics/1349` (line 20, 2000-08-21, mary.poorman@enron.com): “These volumes are currently on the Strangers Agmt, but,  I feel that a sales deal should be out there.”
- `farmer-d/logistics/1386` (line 19, 2000-09-05, aimee.lannou@enron.com): “can you get a deal set up for meter 1459 for 8/00?”
- `farmer-d/logistics/1406` (line 19, 2000-09-13, julie.meyers@enron.com): “This deal was not put in right.  The primary term of the contract goes out to 9/30/00.”
- `farmer-d/logistics/1346` (line 39, 2000-08-18, clem.cernosek@enron.com): “Logistics needs either a deal to record these volumes which have flowed into HPL's Pipeline or  Logistics need approval to writeoff these volumes to Unaccounted for Gas.”
- `farmer-d/logistics/1352` (line 90, 2000-08-22, gary.lamphier@enron.com): “Volume is allocating to deal number 51862 on 1/16/99 on meter 984132, however the deal does not have this day on it.”
- `farmer-d/logistics/1356` (line 39, 2000-08-23, jackie.young@enron.com): “I am uncomfortable putting a deal out there without more details.”
- `farmer-d/logistics/1377` (line 21, 2000-08-30, jackie.young@enron.com): “Can you give us a status on this request?”
- `farmer-d/logistics/1387` (line 17, 2000-09-05, daren.farmer@enron.com): “10,000 should be allocated to Adonis #51862 on the 5th only.”
- `farmer-d/logistics/1413` (line 19, 2000-09-19, mary.poorman@enron.com): “The two meters below are new and have unallocatable flow.......I will need a purchase for each of them.”
- `farmer-d/logistics/1428` (line 20, 2000-09-27, aimee.lannou@enron.com): “Sitara does not show who the trader is for this meter.”
- `farmer-d/logistics/1448` (line 19, 2000-10-10, aimee.lannou@enron.com): “There is flow at meter 74 on 9/14 (499 dth).  The deal for this meter (400289) did not start until 9/15.”
- `farmer-d/logistics/1450` (line 19, 2000-10-12, rebecca.griffin@enron.com): “Please verify if Duke deal #387571 should be on HPL meter #1040.”
- `farmer-d/logistics/1479` (line 21, 2000-10-30, mary.poorman@enron.com): “I have some flow at the above referenced meter without a deal.  Flow was for the first 2 days only”
- `farmer-d/logistics/1478` (line 21, 2000-10-30, susan.hadix@enron.com): “Can you extend the deal throughout the month so that the volumes will have a deal to link to.”
- `farmer-d/logistics/1485` (line 19, 2000-11-01, aimee.lannou@enron.com): “Daren - What is the status of meter 6387?”
- `farmer-d/logistics/1480` (line 20, 2000-10-30, mary.poorman@enron.com): “Gas flowed for the first four days without a deal.  Please input a deal to cover.”
- `farmer-d/logistics/1482` (line 19, 2000-10-31, julie.meyers@enron.com): “The contract attached to that deal was a GTC Firm which ended 9/30/00.  I created a new ticket for those two days (461059).”
- `farmer-d/logistics/1499` (line 31, 2000-11-07, clem.cernosek@enron.com): “Please print, approve, and return original to me.”
- `farmer-d/logistics/1468` (line 25, 2000-10-24, fred.boas@enron.com): “Get Daren to put the proper deal tickets in MOPS and then let me know how to path this gas.”
- `farmer-d/logistics/1472` (line 27, 2000-10-25, mary.poorman@enron.com): “I would propose that Logistics be included in the communication of when checks are manually cut.”
- `farmer-d/logistics/1507` (line 17, 2000-11-09, charlene.richmond@enron.com): “Daren would you look at the price for 29 and 30th of March 2000 .  There are no prices for these days but volume was scheduled for these days.”
- `farmer-d/logistics/1488` (line 19, 2000-11-01, charlene.richmond@enron.com): “Help .   Steve Mauch at Hesco is wanting an answer ASAP”
- `farmer-d/logistics/1512` (line 17, 2000-11-13, aimee.lannou@enron.com): “Daren - meter 1601 has flow from 11/8-11/10.  There is no deal for these days.”
- `farmer-d/logistics/1543` (line 17, 2000-11-29, mary.poorman@enron.com): “I need a deal to pick up the 500 and change that squeaked through the meter, please.  My exceptions need to be cleared pretty quickly.”
- `farmer-d/logistics/1544` (line 19, 2000-11-29, mary.poorman@enron.com): “A small volume (352 Dth) flowed on the 10th at Flagstaff meter, I think it may have been a test volume.”
- `farmer-d/logistics/1520` (line 24, 2000-11-15, mary.poorman@enron.com): “I am now on the dreaded ua4 list from Vol. Mgmt.”
- `farmer-d/logistics/1974` (line 22, 2000-12-14, clem.cernosek@enron.com): “Logistics needs approval to writeoff these volumes to Unaccounted for Gas.  Please print, sign, and return original to Clem Cernosek.”
- `farmer-d/logistics/1978` (line 22, 2000-12-18, clem.cernosek@enron.com): “Logistics needs either (1) Deal #113050 extended to cover 9/15/99;  (2) a new deal to record these volumes; or (3) Logistics needs approval to writeoff these volumes to Unaccounted for Gas.”
- `farmer-d/logistics/2006` (line 25, 2000-12-22, clem.cernosek@enron.com): “Currently, the volume is booked to HPL Strangers Gas Contract.  Logistic needs approval to writeoff this volume to Unaccounted for Gas.”
- `farmer-d/logistics/1963` (line 19, 2000-12-12, aimee.lannou@enron.com): “Transco told us they would not go back and reallocate due to the statute of limitations (6 months).”
- `farmer-d/logistics/1960` (line 23, 2000-12-11, jackie.young@enron.com): “Can these deals be rolled to cover these couple of days?”
- `farmer-d/logistics/1972` (line 31, 2000-12-14, victor.lamadrid@enron.com): “We go round and round at this point changing volumes two, three or more times.”
- `farmer-d/logistics/1977` (line 19, 2000-12-15, victor.lamadrid@enron.com): “The deal you reference is an HPL deal with Dynegy and I don't have access to it. I'm on the East desk.”
- `farmer-d/logistics/1999` (line 21, 2000-12-21, jackie.young@enron.com): “I know that this is a busy part of the day for you.  But, when you get a minute, can you please extend deal #465322”
- `farmer-d/logistics/1983` (line 23, 2000-12-19, victor.lamadrid@enron.com): “465490 is not a deal between ENA and HPL.. It is a Zone 5 Tennessee sale between ENA and a third party”
- `farmer-d/logistics/1559` (line 27, 2000-12-12, aimee.lannou@enron.com): “Please let me know if you create a deal for meter 1351 and if you extend the deal for meter 1603.”
- `farmer-d/logistics/1560` (line 19, 2000-12-12, thu.nguyen@enron.com): “I need a deal set up for Nov 00.  Per Gary Hanks, gas is taken from South Texas and put into Midtex Pipeline at Dewville”
- `farmer-d/logistics/1554` (line 21, 2000-12-07, rebecca.griffin@enron.com): “I am unsure how to have Volume Management reallocate.”
- `farmer-d/logistics/2013` (line 24, 2000-12-27, clem.cernosek@enron.com): “HPL Logistics needs either a deal to record these volumes which have flowed into HPL's pipeline or Logistics needs approval to write-off these volumes to Unaccounted for Gas.”
- `farmer-d/logistics/2014` (line 23, 2000-12-28, clem.cernosek@enron.com): “Logistics needs approval to write-off this volume to Unaccounted for Gas.  (Please print, sign, and return original to Clem Cernosek).”
- `farmer-d/logistics/2045` (line 22, 2001-01-12, robert.cotten@enron.com): “has been moved from the Strangers Gas Contract to 012-41500-02-004 for write-off purposes.”
- `farmer-d/logistics/2040` (line 19, 2001-01-09, mark.mccoy@enron.com): “The trader said this deal needed to be renegotiated, and I am waiting to hear what happened”
- `farmer-d/logistics/2031` (line 21, 2001-01-05, aimee.lannou@enron.com): “Could you please look at this and let me know if you put a deal in for these days?”
- `farmer-d/logistics/2038` (line 20, 2001-01-09, aimee.lannou@enron.com): “Could you please extend this deal for these 3 days or create a new one?  Please let me know.”
- `farmer-d/logistics/2049` (line 19, 2001-01-22, aimee.lannou@enron.com): “Deal 150325 expired on day 3.  Could you please extend this deal or create a new one?  Thanks.”
- `farmer-d/logistics/2052` (line 19, 2001-01-24, michael.olsen@enron.com): “The above deal number expired at the end of November 2000 and needs to either be extended through December, or a new deal inputted.”
- `farmer-d/logistics/2054` (line 17, 2001-01-25, mary.poorman@enron.com): “I have flow at the meter everyday without a deal in Dec.  It is on the UA4 and needs a ticket.”
- `farmer-d/logistics/2077` (line 17, 2001-02-05, mary.poorman@enron.com): “The meter shows flow the first two day, the deal to sell to San Jac is expired.  Do you want me to extend the deal to cover the volume?”
- `farmer-d/logistics/2078` (line 17, 2001-02-05, michael.olsen@enron.com): “For Dec. and Jan. production there are flow volumes without a deal.  Deal 502952 was good for November.”
- `farmer-d/logistics/2095` (line 21, 2001-02-23, michael.olsen@enron.com): “Deal with inactive or suspended counterparty may not be extended.”
- `farmer-d/logistics/2102` (line 17, 2001-02-26, aimee.lannou@enron.com): “meter 1558 has flow and no nom for day 1 and day 6.”
- `farmer-d/logistics/2099` (line 71, 2001-02-23, katherine.herrera@enron.com): “Today is the last day we can make changes in the system.”
- `farmer-d/logistics/2125` (line 17, 2001-03-20, tom.acton@enron.com): “Daren I have three meters that have flow in Feb but no deal.”
- `farmer-d/logistics/2122` (line 26, 2001-03-20, michael.olsen@enron.com): “Can this deal be extended to cover the January and February flow?”
- `farmer-d/logistics/2123` (line 19, 2001-03-20, michael.olsen@enron.com): “This has not yet shown up in Unify.  Did you use the same deal ticket?”
- `farmer-d/logistics/2113` (line 20, 2001-03-06, aimee.lannou@enron.com): “Let me know if you extend the deal or create a new one.”
- `farmer-d/logistics/195` (line 30, 2001-04-04, katherine.herrera@enron.com): “Pls let me know ,so that I can redraft the sale through Unify.”
- `farmer-d/logistics/182` (line 16, 2001-04-12, michael.olsen@enron.com): “The above deal has a zero volume in it, creating an allocation exception at that point.”
- `farmer-d/logistics/173` (line 18, 2001-04-18, michael.olsen@enron.com): “Not to be picky, but this deal is in for 5322 and I confirmed 5323, do you mind if I up it one giant decatherm.”
- `farmer-d/logistics/190` (line 19, 2001-04-09, mary.poorman@enron.com): “Please update the ticket to reflect that HPL is receiving these volumes from ENA - IM Central.  This is having and adverse impact on our pathing.”
- `farmer-d/logistics/188` (line 18, 2001-04-10, michael.olsen@enron.com): “I just needed the point to show up in Unify for Volume Managment to assign a track ID.”
- `farmer-d/logistics/117` (line 34, 2001-06-14, tnray@aep.com): “I did a search and found no deals for May for this counterparty.  Call Daren Farmer at 713-853-6905, and he could probably put the deal in for you.”
- `farmer-d/logistics/116` (line 19, 2001-06-14, l..hernandez@enron.com): “Unable to add May production as contract needs to be exteneded.”
- `farmer-d/logistics/112` (line 19, 2001-06-20, tnray@aep.com): “Has contract expired? Unable to get deal to come across to Unify Settlements.”
- `farmer-d/logistics/137` (line 18, 2001-05-21, juliann.kemp@enron.com): “We had flow of 76 for the month of April but no deal came across in Sitarra.”
- `farmer-d/logistics/30` (line 18, 2001-10-31, megan.parker@enron.com): “I can follow the ENA deals in path Manager, but I am having a hard time with the HPLC deals.”
- `farmer-d/logistics/29` (line 18, 2001-10-31, megan.parker@enron.com): “I did not see a deal in Unify, so I went to POPS to find the meter.”
- `farmer-d/logistics/22` (line 18, 2001-11-08, sherlyn.schumack@enron.com): “Can you back date deals 83347 and 83905  to start 6/1/99 through  12/31/99 for the Black Marlin meter.”
- `farmer-d/logistics/21` (line 19, 2001-11-08, rita.wynne@enron.com): “we can't do it in POPS so we will have to make manual entries to clear the imbalance from the books”

## 3. Real-time power schedule, cut and variance corrections

Real-time shift traders spend part of each day correcting schedules and positions. When Colstrip or a counterparty cuts, they zero deals and book offsetting annuities. They fix import IDs and load zones, create DA and HA finals in CAPS, and run the SAR and INC reconciliation against CAPS and Enpower. They also repair El Paso Electric schedules with missing tags, check out schedules with counterparties by phone, and call generators every hour for checkout. The same cut is recorded in several places, including paper cut sheets and a Lotus Notes database, and procedures are re-issued when entries are inconsistent.

- **Who touches it:** albert.meyers@enron.com, bill.williams@enron.com, cara.semperger@enron.com, craig.dean@enron.com, geir.solberg@enron.com, john.anderson@enron.com, john.oh@enron.com, kalmeida@caiso.com, kate.symes@enron.com, lester.rawson@enron.com, marketopshourahead@caiso.com, marketopsrealtimebeep@caiso.com
- **How often:** 5.78 occurrences/month (52 dated messages over 9 active months, 2001-06-29 → 2002-02-06)
- **Where it stalls:** Variances are found after the fact and need detective work. Real-time cuts are not in CAPS, so the SAR and INC only match after manual additions. HA finals creation hits SQL errors and data scrape failures that go unnoticed over weekends. The EPE schedule sheet misses tags day after day. Paper cut sheets get lost, and hourly generator calls are sometimes missed.
- **Automation:** A cut-entry form that zeroes the deal, books the offsetting annuity and logs the cut once to every destination. An automated morning SAR, INC and CARP comparison would write the reconciliation sheet. Tags in the EPE schedule would be validated automatically against dispatcher schedules, and the scrape and finals imports would be monitored with alerts. Metered generator output would be pulled into the services sheet automatically.
- **Estimate:** 30 min/occurrence × 45% automatable → 1.3 h/month → **$110/month**
- **Why that estimate:** Observer estimates cluster at 20 to 45 minutes with a median of 30 minutes per occurrence. Detection and logging are automatable, but resupply and counterparty checkout decisions stay human, so the fraction is set at the 0.45 median.
- **Drafted artifacts:** `drafts/real-time-power-schedule-cut-and-variance-corrections-sop.md`

**Evidence**

- `williams-w3/sent_items/417` (line 18, 2001-07-10, bill.williams@enron.com): “Even if there are no variances, please complete the July EPE Reconciliation sheet going forward.”
- `williams-w3/sent_items/417` (line 18, 2001-07-10, bill.williams@enron.com): “Houston will assume that no one ran the CARP if the sheet has no entries.”
- `williams-w3/sent_items/391` (line 19, 2001-07-16, bill.williams@enron.com): “The SAR and INC sheet are matching if the 42 mw purchase from the imbalance at $44 is factored in”
- `williams-w3/sent_items/453` (line 18, 2001-06-29, bill.williams@enron.com): “We had some double deal-entry last night under the ST-WBOM book.”
- `williams-w3/sent_items/418` (line 29, 2001-07-10, bill.williams@enron.com): “we show no variances between the Real Time El Paso model and our CARP report.”
- `williams-w3/sent_items/373` (line 18, 2001-07-23, bill.williams@enron.com): “We are short 14 mws at the Portland General System in position manager for Friday, July 20th.”
- `williams-w3/sent_items/372` (line 27, 2001-07-23, bill.williams@enron.com): “I fixed it, no idea where those megawiggles went”
- `williams-w3/sent_items/291` (line 18, 2001-08-23, bill.williams@enron.com): “We are off in position manager at Mid Columbia because of Enron Canada.”
- `williams-w3/sent_items/308` (line 21, 2001-08-13, bill.williams@enron.com): “I have added deals to Enpower to flatten the report, these deals are only necessary for the sake of the report.”
- `williams-w3/sent_items/312` (line 41, 2001-08-13, bill.williams@enron.com): “We had a variance in the SAR for the West BOM Book on Friday night.”
- `williams-w3/sent_items/357` (line 29, 2001-07-28, bill.williams@enron.com): “We must call Grays Harbor and Frontier at the top of EVERY hour.”
- `williams-w3/sent_items/357` (line 29, 2001-07-28, bill.williams@enron.com): “Then we need to call BPA and communicate the ACTUAL energy generated, not an estimate.”
- `williams-w3/sent_items/325` (line 19, 2001-08-07, bill.williams@enron.com): “Spin was exercised for HE 9 and HE 10 at 08:35 and 09:35 respectively.”
- `williams-w3/sent_items/330` (line 22, 2001-08-04, bill.williams@enron.com): “We should do this in the Service Sheet and then record the amount dispatched on the sheet to EES on Tuesday morning as well.”
- `williams-w3/sent_items/338` (line 21, 2001-08-01, bill.williams@enron.com): “When Colstrip goes down we will be short at Montana system and long at PGE System.”
- `williams-w3/sent_items/336` (line 51, 2001-08-02, bill.williams@enron.com): “Make cuts in Lotus Notes Cuts Database (this is the most time consuming portion of this procedure).”
- `williams-w3/sent_items/336` (line 21, 2001-08-02, bill.williams@enron.com): “After yesterdays cuts there have been some changes in the Colstrip Cut Procedures.”
- `williams-w3/sent_items/66` (line 27, 2001-11-30, bill.williams@enron.com): “We need to zero out all cut deals in Enpower, we then need to calculate the value of the deals and make an annuity.”
- `williams-w3/sent_items/62` (line 23, 2001-12-01, bill.williams@enron.com): “Try to have the counterparties continue any paths around us.”
- `williams-w3/sent_items/61` (line 25, 2001-12-04, bill.williams@enron.com): “We are having a nightmare taking care of weekend cuts, particularly imports into California.”
- `williams-w3/sent_items/69` (line 17, 2001-11-28, bill.williams@enron.com): “I attempted to enter this in the cuts database but got several errors and do not have confidence that this occurred.”
- `williams-w3/sent_items/68` (line 45, 2001-11-30, bill.williams@enron.com): “Transmission deals, EpmiCalPool deals, and sales or purchases from the counterparty California Imbalance in Enpower need to be excluded.”
- `williams-w3/inbox/137` (line 20, 2001-12-07, kate.symes@enron.com): “I just tested the schedule pull again and found one more deal type we need to exclude - ANNUITIES.”
- `williams-w3/inbox/136` (line 85, 2001-12-07, susan.amador@enron.com): “the spreadsheet doesn't pull in anything for the first half of November”
- `williams-w3/sent_items/37` (line 23, 2001-12-31, bill.williams@enron.com): “If it is a weekend (or holiday), we first need to import DA finals and then create DA finals in CAPS.”
- `williams-w3/inbox/126` (line 21, 2002-01-02, albert.meyers@enron.com): “Please note that for Wednesday 01/02/02, Import ID ENRJ_CISO_8000 is wrong.”
- `williams-w3/inbox/125` (line 17, 2002-01-02, craig.dean@enron.com): “ENRJ_CISO_8000 has been corrected for the whole day.”
- `williams-w3/inbox/123` (line 21, 2002-01-02, bill.williams@enron.com): “please put all cuts and scheduling sheets in the accordion file on the RT overflow desk”
- `williams-w3/inbox/122` (line 22, 2002-01-02, bill.williams@enron.com): “The deal sheets MUST be kept in this binder.”
- `williams-w3/inbox/79` (line 23, 2002-01-30, albert.meyers@enron.com): “Lending is wrong in the EPE schedules (it is 75mw from PSCO instead of 50mw).”
- `williams-w3/inbox/79` (line 25, 2002-01-30, albert.meyers@enron.com): “SPS is wrong for HE 08 (it is 130mw instead of 100mw).”
- `williams-w3/inbox/76` (line 26, 2002-01-30, cara.semperger@enron.com): “Bill and I are considering having Real time do the EPE preschedules since they are the ones that live and die by them anyway.”
- `williams-w3/sent_items/8` (line 21, 2002-01-31, bill.williams@enron.com): “Please put all information from the previous day (ie printed dispatch, EPE preschedulng sheet) into the appropriate folder on Kate Symes' old desk.”
- `williams-w3/inbox/102` (line 17, 2002-01-20, john.anderson@enron.com): “I was not able to download HA finals from the ISO and finals were not created.”
- `williams-w3/inbox/93` (line 19, 2002-01-28, john.anderson@enron.com): “there were no DA or HA finals created for 1/27 or the 1/28.”
- `williams-w3/inbox/81` (line 19, 2002-01-30, john.oh@enron.com): “The new URL for the El Paso data scrape is:”
- `williams-w3/inbox/78` (line 19, 2002-01-30, albert.meyers@enron.com): “Last night as I was trying to log onto the ADS machine I kept getting a server error.”
- `williams-w3/inbox/52` (line 19, 2002-02-03, albert.meyers@enron.com): “For yet another day we seem to be having problems including all the schedules in our EPE schedule sheet.”
- `williams-w3/inbox/52` (line 19, 2002-02-03, albert.meyers@enron.com): “I think part of the problem is some counterparties are not including EPMIWE as a PSE.”
- `williams-w3/inbox/24` (line 19, 2002-02-06, geir.solberg@enron.com): “Due to the migration I am unable to send the EPE model to Kathy (file for Feb. did not pull into the M: drive).”

## 4. Real-time power position hand-off and Enpower/CAPS deal entry

On the Portland real-time desk, Bill Williams, prescheduling and the cash desks email the shift whenever the book is short or long. Each email gives MW, hours, hub, price, book and deal numbers, along with instructions for El Paso Electric lending days and EOL trades. Shift traders and support re-key these into Enpower, CAPS and the position sheets, following entry rules that are restated by email. Mismatches between the emailed positions and Enpower are clarified by further emails.

- **Who touches it:** bill.williams@enron.com
- **How often:** 10.0 occurrences/month (60 dated messages over 6 active months, 2001-06-12 → 2001-11-28)
- **Where it stalls:** Instructions are sent piecemeal and re-forwarded as more trades are made. The same shorts and deal numbers are re-sent day after day. Price and counterparty details are deferred to 'check with' other traders. Emailed positions carry wrong hours, delivery points or deal numbers. Lending prices and deal numbers are re-keyed per day and corrected afterwards, and EOL deals go missing in Enpower.
- **Automation:** Generate the shift position summary directly from the position manager and the Enpower deals. Templated deal sets (for example EPE lending) and EOL trades would be auto-created in Enpower with book and strip defaults, and validated against desk rules. A daily match of broker and EOL deals against Enpower would flag gaps, replacing free-text position emails and manual re-keying.
- **Estimate:** 15 min/occurrence × 50% automatable → 1.25 h/month → **$106/month**
- **Why that estimate:** Observer estimates mostly sit at 8 to 20 minutes per hand-off, with two outliers at 60 and 90 minutes, giving a median of 15 minutes. Position data already sits in systems, so the fraction is set at the 0.5 median.
- **Drafted artifacts:** `drafts/real-time-power-position-hand-off-and-enpower-caps-deal-entr-checklist.md`

**Evidence**

- `williams-w3/sent_items/512` (line 17, 2001-06-12, bill.williams@enron.com): “We are long 25 mws in NP-15 at $54 for HE 7-22.  This is under the ST-WBOM line in CAPS.”
- `williams-w3/sent_items/502` (line 23, 2001-06-14, bill.williams@enron.com): “We have 25 mws of length in the BOM book at $56 again for 06/14/01 on peak.”
- `williams-w3/sent_items/466` (line 22, 2001-06-27, bill.williams@enron.com): “We are long 25 mws on peak for 06/27/01 in SP-15.  This should be in CAPS under ST-WBOM, deals should be under ST-WBOM in Enpower as well.”
- `williams-w3/sent_items/510` (line 23, 2001-06-12, bill.williams@enron.com): “CAPS shows a final of 25 mws as a firm import.  This should be a n-firm export.”
- `williams-w3/sent_items/463` (line 24, 2001-06-27, bill.williams@enron.com): “We need to make a buy from EPE under ST-Whourly in Enpower, and a sale to APS at zero in Enpower.”
- `williams-w3/sent_items/414` (line 25, 2001-07-11, bill.williams@enron.com): “St-Cali is short 50 mws in SP-15 for HE 7-22. All deals should be under St-Cali in Enpower and CAPS.”
- `williams-w3/sent_items/403` (line 22, 2001-07-13, bill.williams@enron.com): “We have also bought HE 21 and HE 22 from the APX. We bought 20 mws at $32 for HE 21 and 23 mws at $30 for HE 22.”
- `williams-w3/sent_items/390` (line 20, 2001-07-16, bill.williams@enron.com): “We are missing an ID-S from ST-WBOM to ST-CALI for Saturday.”
- `williams-w3/sent_items/416` (line 30, 2001-07-10, bill.williams@enron.com): “Total volume was 96 mws at $248, revenue should be $23808.”
- `williams-w3/sent_items/380` (line 23, 2001-07-21, bill.williams@enron.com): “We are lending from El Paso Electric on Monday.”
- `williams-w3/sent_items/374` (line 20, 2001-07-23, bill.williams@enron.com): “Please work with the preschedulers to get the sheet correct (Friday's sheet for Monday had a duplicate 10 mw schedule in it).”
- `williams-w3/sent_items/340` (line 28, 2001-07-31, bill.williams@enron.com): “You will know you've done this correctly when the CARP report EXACTLY matches the El Paso model.”
- `williams-w3/sent_items/366` (line 18, 2001-07-24, bill.williams@enron.com): “I should not receive the $25524.54 as revenue shown in the new deal summary.”
- `williams-w3/sent_items/365` (line 25, 2001-07-24, bill.williams@enron.com): “We are short 50 mws for tomorrow at PV through lending with EPE.”
- `williams-w3/sent_items/345` (line 23, 2001-07-30, bill.williams@enron.com): “STWBOM is short tomorrow (07/31/01) on Peak in SP-15.”
- `williams-w3/sent_items/296` (line 21, 2001-08-17, bill.williams@enron.com): “There will be a 100 mw schedule delivered at COB to NCPA going on NCPA rights into NP-15.”
- `williams-w3/sent_items/275` (line 23, 2001-08-29, bill.williams@enron.com): “A standardization in our process will benefit the entire group and will allow us to make consistent improvements as time goes on.”
- `williams-w3/sent_items/268` (line 34, 2001-08-30, bill.williams@enron.com): “INC SHEETS MUST BE MAINTAINED, DEALS ENTERED AND ROUTED EACH HOUR--only way to stay ahead”
- `williams-w3/sent_items/254` (line 23, 2001-09-13, bill.williams@enron.com): “The night shift will average the sales price and make one strip for the on-peak piece.”
- `williams-w3/sent_items/273` (line 49, 2001-08-29, bill.williams@enron.com): “Please find attached an excel spreadsheet of Bloomberg deals I can't seem to match up with our deals in Enpower.”
- `williams-w3/sent_items/295` (line 22, 2001-08-17, bill.williams@enron.com): “25 mws on peak Monday at @$45 in SP-15 (check with Kysa)”
- `williams-w3/sent_items/267` (line 19, 2001-09-05, bill.williams@enron.com): “We are short for HE 21 through HE 23 at Malin.”
- `williams-w3/sent_items/183` (line 29, 2001-10-10, bill.williams@enron.com): “Please Buy to fill this short at the MidC, for the STNW book.”
- `williams-w3/sent_items/198` (line 33, 2001-10-03, bill.williams@enron.com): “We are long at MIDC for Tuesday, 10/02/01.  HE 7-22 at 25mw, #797763.1.”
- `williams-w3/sent_items/240` (line 18, 2001-09-15, bill.williams@enron.com): “Please give this information to the group including Enpower information...etc.”
- `williams-w3/sent_items/175` (line 18, 2001-10-15, bill.williams@enron.com): “We are short 2 pieces of BOM at SP-15 7-22.”
- `williams-w3/sent_items/171` (line 18, 2001-10-17, bill.williams@enron.com): “We are short 3 pieces tomorrow at $27.20, $28.00, and a piece at the ST-CALI index.”
- `williams-w3/sent_items/164` (line 19, 2001-10-19, bill.williams@enron.com): “St-WBOM is long again for HE 2 through HE 5 at PV from PNM at a price of $15.50.”
- `williams-w3/sent_items/168` (line 21, 2001-10-18, bill.williams@enron.com): “we are still short the two BOM pieces in SP-15 for a total of 50 mws each hour on peak-Friday and Saturday”
- `williams-w3/sent_items/101` (line 17, 2001-11-13, bill.williams@enron.com): “I have made the Enpower deals (868223, 868224, 868234) to buy from PinWest and sell to the imbalance in SP-15.”
- `williams-w3/sent_items/112` (line 17, 2001-11-07, bill.williams@enron.com): “do not make the Enpower till the next day if it will be under St-Whourly”
- `williams-w3/sent_items/120` (line 33, 2001-11-05, bill.williams@enron.com): “it is imperative that any information included in an e-mail to Real Time corroborates with data entered into Enpower.”
- `williams-w3/sent_items/104` (line 24, 2001-11-09, bill.williams@enron.com): “We will return to running the Enpower to CAPS report as usual.”
- `williams-w3/sent_items/97` (line 23, 2001-11-14, bill.williams@enron.com): “We are long 20 mws in SDG1 for HE 2 and HE 3.”
- `williams-w3/sent_items/88` (line 46, 2001-11-20, bill.williams@enron.com): “Epmicalpool deals continue to provide problems with reports. Please see me with any questions.”
- `williams-w3/sent_items/86` (line 19, 2001-11-20, bill.williams@enron.com): “You must check out with all major marketers and utilities each night.”
- `williams-w3/sent_items/86` (line 19, 2001-11-20, bill.williams@enron.com): “These checkouts should be started in HE 19 and finished by HE 21.”
- `williams-w3/sent_items/79` (line 30, 2001-11-21, bill.williams@enron.com): “Book-to-book between Services and Real-Time #811820.”
- `williams-w3/sent_items/73` (line 27, 2001-11-28, bill.williams@enron.com): “There was no note on the model or in Lotus notes.”

## 5. Gas volume, imbalance and pathing reconciliation

Volume management, logistics and settlement analysts reconcile gas volumes across MOPS, POPS, Sitara, Unify and pipeline statements. They work allocation exceptions, UA4 and zero-volume feed problems, measurement and nomination-versus-flow gaps, production imbalances and intercompany or interdesk variances, and they clear unpathed deals and bridge-back errors before the month-end close cutoff. Transwestern does the equivalent reconciliation with El Paso and other pipelines. Each item is researched by hand and then chased by email to whoever must re-path, reallocate or correct the volume.

- **Who touches it:** aimee.lannou@enron.com, ami.chokshi@enron.com, anita.luong@enron.com, antoinette.beale@enron.com, charlotte.hawkins@enron.com, clem.cernosek@enron.com, edward.gottlob@enron.com, fred.boas@enron.com, g..barkowsky@enron.com, gary.anderson@enron.com, gary.hanks@enron.com, gregg.lenart@enron.com
- **How often:** 4.36 occurrences/month (122 dated messages over 28 active months, 1999-12-14 → 2002-03-21)
- **Where it stalls:** Fixes need the right person to act in POPS or Unify, and ownership of pipelines and paths is often unclear after reassignments. The same variances come back for weeks. Zero-volume feeds are overridden by hand each night because the system team has not fixed the root cause. Pipeline meter statements arrive by fax on request. Bridge-back errors must be cleared against a hard clock time, and multi-step tasks such as meter replacements wait on each hand-off.
- **Automation:** A daily reconciliation job that compares nominated, confirmed, measured and allocated volumes across MOPS, POPS, Sitara, Unify and loaded pipeline statements. It flags zero-feed meters, one-sided intercompany deals, unpathed deals and bridge-back errors, and puts each exception in a shared queue with an owner from a pipeline and zone registry, an age, and automatic reminders ahead of the close cutoff. This replaces manual spreadsheet research and forwarded issue lists.
- **Estimate:** 45 min/occurrence × 35% automatable → 1.14 h/month → **$97/month**
- **Why that estimate:** Observers estimated 20 to 120 minutes because items need multi-party research, and the median is 45 minutes. Detection and routing automate well, but root-cause research and counterparty agreement do not, so the fraction is set at the median of about 0.35.

**Evidence**

- `farmer-d/logistics/581` (line 46, 1999-12-14, lauri.allen@enron.com): “Please make sure these volumes are moved off the Reliant contract prior to November close.”
- `farmer-d/logistics/583` (line 32, 1999-12-14, howard.camp@enron.com): “These were buybacks that were incorrectly nominated to transport contracts”
- `farmer-d/logistics/684` (line 19, 2000-01-13, kimberly.vaughn@enron.com): “This does show up on my meter exception report.  Please advise.”
- `farmer-d/logistics/677` (line 17, 2000-01-12, aimee.lannou@enron.com): “Meter 1517, Sweeny Phillips, has been reallocated for 12/99.”
- `farmer-d/logistics/589` (line 39, 1999-12-15, melissa.ratnala@enron.com): “Unify to Sitara bridge back 1:45p.m. Thursday, Dec 30th (all errors must be clear by this time)”
- `farmer-d/logistics/976` (line 40, 2000-03-28, melissa.ratnala@enron.com): “Unify to Sitara bridge back 1:45p.m. Friday, March 31st (all errors must be clear by this time)”
- `farmer-d/logistics/649` (line 22, 2000-01-05, anita.luong@enron.com): “I need to have this error clear off by Thursday.”
- `farmer-d/logistics/629` (line 19, 1999-12-29, charlotte.hawkins@enron.com): “I have an error for Transco Bammel for that 20.0/day on days 23 through 27”
- `farmer-d/logistics/640` (line 32, 1999-12-31, mandy.mackinnon@enron.com): “There were deals left unpathed for Jan 1 (and Dec?).”
- `farmer-d/logistics/675` (line 34, 2000-01-12, pat.clynes@enron.com): “Lets get this job done or I will find people who want to get it done.”
- `farmer-d/logistics/1008` (line 20, 2000-04-03, pat.clynes@enron.com): “It is very important  that King Ranch is accurately scheduled in the system.”
- `farmer-d/logistics/792` (line 61, 2000-02-14, charlotte.hawkins@enron.com): “In MOPS, the
path was nominated for 1/26 only.  However, in POPS the path was nominated”
- `farmer-d/logistics/861` (line 17, 2000-03-01, kimberly.vaughn@enron.com): “Daren..  Have you had a chance to look at this yet?”
- `farmer-d/logistics/785` (line 21, 2000-02-11, heidi.withers@enron.com): “POPS shows a daily BAV of”
- `farmer-d/logistics/784` (line 21, 2000-02-11, stella.morris@enron.com): “Charlotte, please get with Daren.”
- `farmer-d/logistics/868` (line 21, 2000-03-02, gregg.lenart@enron.com): “Below is a list of Sitara deals that had volume variances or where one side (purchase/sale) did not get accrued for the FEB 2000 accrual.”
- `farmer-d/logistics/877` (line 21, 2000-03-03, thu.nguyen@enron.com): “We are required to clear intercompany variances by the end of the month, so it would help if you could research this as soon as possible.”
- `farmer-d/logistics/927` (line 21, 2000-03-21, fred.boas@enron.com): “I need a desk to desk deal set up at meter 378 for February 2000.”
- `farmer-d/logistics/951` (line 19, 2000-03-23, thu.nguyen@enron.com): “I must be missing something.  Can I meet with you today and show you what I have?”
- `farmer-d/logistics/878` (line 21, 2000-03-06, thu.nguyen@enron.com): “The new deal, 158220, is missing 10,000 for day 1.  Please let me know when you have this corrected.”
- `farmer-d/logistics/925` (line 32, 2000-03-21, lauri.allen@enron.com): “Someone needs to be overriding the 0 volumes so that Sitara is receiving correct information and the P&L is kept as accurate as possible.”
- `farmer-d/logistics/928` (line 26, 2000-03-21, charlotte.hawkins@enron.com): “In the mean time we are overriding the volumes in POPS with the estimated volumes.”
- `farmer-d/logistics/937` (line 31, 2000-03-22, lauri.allen@enron.com): “I looked at our p&l tonite and our UA4 volumes actually increased by about 90,000 MMBtu's for a grand total of 550,000 MMBtu's for the month.”
- `farmer-d/logistics/1141` (line 18, 2000-05-24, aimee.lannou@enron.com): “After comparing HPL's numbers with PG&E's numbers I have found a few discrepancies with the Tufco volumes.”
- `farmer-d/logistics/917` (line 28, 2000-03-20, rita.wynne@enron.com): “As of Thursday night's   P &L calc., unaccounted for March 2000 on Texas was a little over 400,000 mmbtus.”
- `farmer-d/logistics/1200` (line 21, 2000-06-12, katherine.herrera@enron.com): “Duke has called me several times they want to get our March deals finalized.”
- `farmer-d/logistics/1073` (line 25, 2000-04-25, katherine.herrera@enron.com): “Can you ask PG&E to confirm which of these volume is correct so that the February allocations can be finalized?”
- `farmer-d/logistics/1126` (line 22, 2000-05-22, sherlyn.schumack@enron.com): “I have sent several emails, faxed the daily's and left voice messages, but have not received any updates to this issue.”
- `farmer-d/logistics/1130` (line 26, 2000-05-23, sherlyn.schumack@enron.com): “I do not know the intent of these deals so I am hesitant to just zero out the volume.”
- `farmer-d/logistics/1105` (line 17, 2000-05-11, stacey.neuweiler@enron.com): “Could you please look into this for me?  Thanks.”
- `farmer-d/logistics/1013` (line 23, 2000-04-04, robert.lloyd@enron.com): “Please override POP'S  daily volume{ presently zero}  to reflect  daily activity you can obtain from Gas Control.”
- `farmer-d/logistics/1067` (line 19, 2000-04-24, aimee.lannou@enron.com): “Meter 1591 has never flowed the entire nom.  This meter is has been over nominated.”
- `farmer-d/logistics/1133` (line 26, 2000-05-23, mark.mccoy@enron.com): “I entered these cuts in the estimate column in MOPS for both Oasis/HPL & Oasis/ENA....please verify that is correct.”
- `farmer-d/logistics/1069` (line 21, 2000-04-25, jackie.young@enron.com): “I'm attempting to clear the above mentioned meter from an error report (Revenue Volume Comparison Report).”
- `farmer-d/logistics/1014` (line 22, 2000-04-04, charlotte.hawkins@enron.com): “I did not realize that's what you wanted when you handed me the "sticky" on Monday.....”
- `farmer-d/logistics/1185` (line 30, 2000-06-07, howard.camp@enron.com): “Below is a list of the major items that are still outstanding on the interdesk/interconnect report for 1999 and 2000”
- `farmer-d/logistics/1199` (line 28, 2000-06-12, lisa.csikos@enron.com): “the deadline for completing this work so that the invoices can be finaled is Friday, June 16, 2000.”
- `farmer-d/logistics/1178` (line 26, 2000-06-05, fred.boas@enron.com): “I never heard back from Aimee on which Transport contract to attach the deal 269123 to”
- `farmer-d/logistics/1241` (line 21, 2000-06-26, rita.wynne@enron.com): “There have been so many CILCO issues until I'm not sure which one you are referencing.”
- `farmer-d/logistics/1194` (line 22, 2000-06-08, charlotte.hawkins@enron.com): “The allocations are corrected with deal #92399 on the 215 contract taking the swing.”
- `farmer-d/logistics/1439` (line 28, 2000-10-03, clem.cernosek@enron.com): “Please change the confirmed noms to zero for all contracts that have be nominated for period 1/1/00 thru 10/31/00 for the above meter.”
- `farmer-d/logistics/1442` (line 20, 2000-10-04, howard.camp@enron.com): “Step # 1 has been completed.”
- `farmer-d/logistics/1444` (line 21, 2000-10-05, howard.camp@enron.com): “Steps 2 - 4 have been done.”
- `farmer-d/logistics/1433` (line 56, 2000-09-29, edward.gottlob@enron.com): “I thought the imbalance report I got this Wed was pretty sad.  Some of the columns did not add and there seemed to be a lot of missing information.”
- `farmer-d/logistics/1433` (line 40, 2000-09-29, edward.gottlob@enron.com): “Can we net the Corpus Christi gas marketing and all the Tejas/ Coral/Gulf Energy/Shell imbalances down?”
- `farmer-d/logistics/170` (line 17, 2001-04-19, mary.poorman@enron.com): “We need to update our forward position and our nomination by 4,000/day to stay in balance to entitlements.”
- `farmer-d/logistics/160` (line 23, 2001-04-25, mary.poorman@enron.com): “We have an ongoing issue every month between what we nominate from GEPL into HGPL and on to King Ranch”
- `farmer-d/logistics/163` (line 20, 2001-04-24, rita.wynne@enron.com): “However, we are booking an imbalance every month on the parking and lending contract.”
- `farmer-d/logistics/159` (line 25, 2001-04-25, mary.poorman@enron.com): “I think that I have found the missing volumes on Big Cowboy.”
- `farmer-d/logistics/157` (line 18, 2001-04-27, mary.poorman@enron.com): “I have created the following tickets to account for the physical and economic impact of the ENA Texas PLE00004 agreement”
- `farmer-d/logistics/108` (line 20, 2001-06-22, g..barkowsky@enron.com): “I need deal #854688 pathed for EPGT and for TETC.”
- `farmer-d/logistics/102` (line 19, 2001-06-29, g..barkowsky@enron.com): “Daren - what about February 2000?  It doesn't look like it's been pathed for HPL and CHAN.”
- `farmer-d/logistics/97` (line 19, 2001-07-17, g..barkowsky@enron.com): “Daren - can you please let me know the status on this for 02/2000?  Thanks, Gloria”
- `farmer-d/logistics/18` (line 23, 2001-11-20, shahnaz.lakho@enron.com): “I am down to the last few error messages on the EPGT Quick Response and also looking into the external pool for WH034 in Unify.”
- `farmer-d/logistics/63` (line 20, 2001-09-07, sherlyn.schumack@enron.com): “This deal expired 12/31/00, and the late pathing has caused a bridgeback error for January and February 2001.”
- `farmer-d/logistics/59` (line 19, 2001-09-14, sherlyn.schumack@enron.com): “Have you had a chance to look at this yet?”
- `farmer-d/logistics/58` (line 19, 2001-09-14, michael.olsen@enron.com): “It has been taken care of.  Let me know if you need anythign further.”
- `farmer-d/logistics/62` (line 102, 2001-09-10, michael.olsen@enron.com): “I need a transport usage ticket to clear these balances”
- `farmer-d/logistics/53` (line 25, 2001-10-03, antoinette.beale@enron.com): “A path is needed on Delivery 17054701 for 19087mmbtus with the Receipt point 175054701.”
- `farmer-d/logistics/52` (line 19, 2001-10-03, michael.olsen@enron.com): “This deal was not transported on contract 1856, the 15,000 was sold to El Paso Merchant directly at that point.”
- `farmer-d/logistics/48` (line 39, 2001-10-12, victor.lamadrid@enron.com): “On # 2, The scheduling position window IS the weakest link.....GOODBYE!”
- `farmer-d/logistics/49` (line 24, 2001-10-11, victor.lamadrid@enron.com): “The blue highlighted pipes are the critical ones for the EAST.”
- `lokay-m/sent_items/89` (line 17, 2002-02-11, michelle.lokay@enron.com): “Based on your reconciling, I will run additional reports on our side for 09/00 and 11/00.”
- `lokay-m/sent_items/103` (line 17, 2002-02-19, michelle.lokay@enron.com): “Can I have one for each of the following months for Mojave #56696 to confirm Scheduled volumes?”
- `lokay-m/sent_items/122` (line 27, 2002-03-04, michelle.lokay@enron.com): “Here is a summary of the support I have faxed to you concerning the scheduled volume discrepancies:”
- `lokay-m/sent_items/101` (line 50, 2002-02-14, michelle.lokay@enron.com): “Could you re-check your scheduled volumes?”

## 6. Risk book administration: book setup, deal rebooks, book flips and price corrections

Darron Giron and the risk book administrators receive a steady flow of requests. Some ask for new trading books, portfolios, curves and mappings in TAGG, Sitara, CPR, TDS and Global Counterparty. Others ask to flip deals between books (for example ECC and Canadian deals to FT-US/CAND-ERMS), rebook counterparties, change deal rates or demand charges, add missing Sitara, TAGG or EOL cross-references, and supply book lists or reference ids. Each request is a separate email that Giron actions himself or forwards to the book owner. Settlements and invoicing often cannot proceed until the change is confirmed.

- **Who touches it:** ashley.worthing@enron.com, d..winfree@enron.com, darron.giron@enron.com, elizabeth.hernandez@enron.com, john.valdes@enron.com, kam.keiser@enron.com, m..love@enron.com, scott.palmer@enron.com
- **How often:** 6.3 occurrences/month (126 dated messages over 20 active months, 2000-06-08 → 2002-01-28)
- **Where it stalls:** Requests go to several different administrators, and routing is unclear (for example, a TAGG book must first exist in Global Counterparty). Requests arrive piecemeal and urgently for same-day invoicing. Cross-system ids are not linked, so lookups are manual. Recurring monthly rate changes sit unactioned until chased. Book lists are rebuilt for each requester.
- **Automation:** One intake form and queue for book, curve and mapping setup that routes to every system's administrator and shows status. A bulk deal-attribute change tool would take a list of deal numbers with the target book or counterparty. A rule would flag deals with Canadian counterparties in US books, and recurring rate changes would load from the monthly price source. Validation at entry would auto-link TAGG, Sitara and EOL ids, and a maintained book and portfolio reference table would serve book lists.
- **Estimate:** 20 min/occurrence × 50% automatable → 1.05 h/month → **$89/month**
- **Why that estimate:** Observer estimates centre on 15 to 30 minutes with a median of 20 minutes. Most changes are mechanical once approved, so the fraction is set at the 0.5 median.

**Evidence**

- `giron-d/sent/778` (line 19, 2000-06-13, darron.giron@enron.com): “We need to break out our Midcon region into two separate books starting with July production.”
- `giron-d/sent/769` (line 36, 2000-06-15, darron.giron@enron.com): “Befire a book can be added to TAGG, it has to be added to Global Counterparty.”
- `giron-d/sent/768` (line 17, 2000-06-15, darron.giron@enron.com): “Does this mean that the two new Sitara books I requested are complete?  I looked in Sitara and could not find the new names.”
- `giron-d/sent/775` (line 21, 2000-06-14, darron.giron@enron.com): “Please change the subregion code for all ANR ML5 deals from Market to Midcon.”
- `giron-d/sent/755` (line 17, 2000-06-28, darron.giron@enron.com): “I wanted to show you when I sent this and how long it took to set it up.”
- `giron-d/sent/738` (line 33, 2000-07-18, darron.giron@enron.com): “Please update the Sitara demand charges on the following deals to match the actualized pipeline statements:”
- `giron-d/sent/717` (line 32, 2000-08-04, darron.giron@enron.com): “Have you had a chance to look at this adjustment to $.1134? Sitara still shows .0556.”
- `giron-d/sent/759` (line 21, 2000-06-23, darron.giron@enron.com): “We are breaking up our Central Midcon region into two books beginning July 1.”
- `giron-d/sent/711` (line 18, 2000-08-09, darron.giron@enron.com): “We need to have two more books created as soon as possible.”
- `giron-d/sent/721` (line 19, 2000-07-31, darron.giron@enron.com): “The new exchange deals for the EMW Park & Loan are 350499 and 350511.”
- `giron-d/sent/680` (line 29, 2000-08-28, darron.giron@enron.com): “This is on open OA difference and will continue to be until you handle it.”
- `giron-d/sent/673` (line 17, 2000-08-31, darron.giron@enron.com): “The deal was entered twice.  I killed 279644.  I spoke with Michael, and he knows the deal has been killed.”
- `giron-d/sent/655` (line 31, 2000-09-11, darron.giron@enron.com): “Barbara Dillard's worksheet shows the full 10,000 MMBtu for 8/1/00 - 8/2/00 as SIQ”
- `farmer-d/logistics/1381` (line 36, 2000-09-01, elizabeth.hernandez@enron.com): “I believe the system is pulling in the wrong price for WAHA.WTX.IF.M.I.. for 5/00 production.”
- `giron-d/sent/650` (line 21, 2000-09-14, darron.giron@enron.com): “I need some Tagg books set up for the Chicago office.”
- `giron-d/sent/648` (line 20, 2000-09-19, darron.giron@enron.com): “I will need a region set up in CPR to hold the physical deals.  Do you do this?”
- `giron-d/sent/623` (line 28, 2000-09-29, darron.giron@enron.com): “Darron - please provide me with the trader's name for the following books:”
- `giron-d/sent/619` (line 19, 2000-10-03, darron.giron@enron.com): “I want to move all deals currently in the INTRA-EMWMEH book into the FT-IM-ENOV book.”
- `giron-d/sent/615` (line 19, 2000-10-06, darron.giron@enron.com): “It looks like we need to be consistent in booking the GD spread deals.”
- `giron-d/sent/591` (line 19, 2000-10-17, darron.giron@enron.com): “Please remember to link up all deals.  By this, I mean Tagg numbers in Sitara, Sitara numbers in Tagg, Tagg numbers in SCI”
- `giron-d/sent/592` (line 17, 2000-10-17, darron.giron@enron.com): “It should reference the EOL number.  It looks af if Kevin did not link it up.”
- `giron-d/sent/360` (line 32, 2000-12-27, darron.giron@enron.com): “Goss said you may have a calc set up to identify these deals.  Any chance I could copy it?”
- `giron-d/sent/550` (line 46, 2000-10-27, darron.giron@enron.com): “There are a few deals in the MGMT-WEST book that need to be moved to the FT-US/CAND-ERMS BOOK.”
- `giron-d/sent/539` (line 44, 2000-11-01, darron.giron@enron.com): “they need to be flipped to the FT-US/CAND-ERMS book as soon as possible.”
- `giron-d/sent/535` (line 18, 2000-11-02, darron.giron@enron.com): “I can't remember if I forwarded this to you already.  Thanks.”
- `giron-d/sent/407` (line 49, 2000-12-08, darron.giron@enron.com): “make sure that there aren't any more deals with ECC and a third counterparty in this book as it messes up invoicing and settlement.”
- `giron-d/sent/575` (line 19, 2000-10-18, darron.giron@enron.com): “Currently, all of our index deals are in the FT-WEST book.  I would like to move them all to the GD-NEW book.”
- `giron-d/sent/549` (line 18, 2000-10-27, darron.giron@enron.com): “It is very important that you always put this information in Tagg.”
- `giron-d/sent/571` (line 20, 2000-10-19, darron.giron@enron.com): “The Sitara numbers for both of these deals are in the comments section of each deal in Tagg.”
- `giron-d/sent/561` (line 17, 2000-10-25, darron.giron@enron.com): “I think Sitara deal 286147 is not pulling the correct price in Unify.”
- `giron-d/sent/513` (line 31, 2000-11-07, darron.giron@enron.com): “Yet, I show no transactions for them in that region.”
- `giron-d/sent/469` (line 33, 2000-11-21, darron.giron@enron.com): “Could you please change rate on the above Sitara to $4.878216 for Oct. 00 production?”
- `giron-d/sent/378` (line 31, 2000-12-21, darron.giron@enron.com): “Could you please change rate on the above Sitara to $4.15544 for Nov. 00 Production ?”
- `giron-d/sent/508` (line 17, 2000-11-13, darron.giron@enron.com): “It's done.  I appologize for this taking so long.  It won't happen again.”
- `giron-d/sent/508` (line 90, 2000-11-13, darron.giron@enron.com): “The rate at some locations has not been changed in Sitara.  Are they supposed to be at the same price for all points?”
- `giron-d/sent/500` (line 19, 2000-11-13, darron.giron@enron.com): “I have updated the list to include every book we officialize each night.”
- `giron-d/sent/492` (line 19, 2000-11-14, darron.giron@enron.com): “I believe this is all of the Enovate/EMW books that are officialized each night.”
- `giron-d/sent/466` (line 31, 2000-11-22, darron.giron@enron.com): “For Basis, add  -BAS to the end of the book name.  For Gas Daily, add  -GDL to the end of the book name.”
- `giron-d/sent/460` (line 29, 2000-11-27, darron.giron@enron.com): “Please move these deals to the FT-US/CAND-ERMS book by the end of tomorrow.”
- `giron-d/sent/459` (line 29, 2000-11-27, darron.giron@enron.com): “There's a deal in the FT-West book that needs to be moved to the FT-US/CAND-ERMS book right away.”
- `giron-d/sent/405` (line 38, 2000-12-08, darron.giron@enron.com): “These need to be fixed right away this morning as I need to invoice and settle them today.”
- `giron-d/sent/419` (line 30, 2000-12-06, darron.giron@enron.com): “This needs to be fixed so liquidations will be correct for Novmeber.”
- `giron-d/sent/396` (line 18, 2000-12-13, darron.giron@enron.com): “See if you can help this guy.  I don't have access to Denver deals.”
- `giron-d/sent/411` (line 19, 2000-12-07, darron.giron@enron.com): “I set up these new curves this morning and need them added to Tagg”
- `giron-d/sent/351` (line 32, 2001-01-04, darron.giron@enron.com): “Please rebook NW2862.8,.9 to Bank of America, National Association (BANKAMENAT).”
- `giron-d/sent/313` (line 45, 2001-01-19, darron.giron@enron.com): “Could you please change rate on the above deal from $2.24246 to $2.156695 for days 2/21/00 - 2/29/00?”
- `giron-d/sent/301` (line 31, 2001-01-23, darron.giron@enron.com): “As usual, could you please change rate on S# 27239 for 12/00 production to $5.811329?”
- `giron-d/sent/346` (line 25, 2001-01-08, darron.giron@enron.com): “Can you please send to me the spreadsheet used to calculate the price for Agave?”
- `giron-d/sent/357` (line 38, 2001-01-03, darron.giron@enron.com): “I was told that these should be The Peoples Gas Light & Coke Company.”
- `giron-d/sent/343` (line 32, 2001-01-09, darron.giron@enron.com): “it is essential that all information is accurate on the origination schedule.”
- `giron-d/sent/339` (line 42, 2001-01-10, darron.giron@enron.com): “if his group does a deal where no origination is granted,  you will need to put all the relevant information into the origination file”
- `giron-d/sent/337` (line 21, 2001-01-11, darron.giron@enron.com): “I need to have FT-DENVER set up in TDS.  The trader is Jay Reitmeyer.”
- `giron-d/sent/292` (line 6, 2001-01-26, darron.giron@enron.com): “Deals to be flipped to FT-US/CAND-ERMS book by Monday”
- `giron-d/sent/294` (line 35, 2001-01-25, darron.giron@enron.com): “We have had a few recent instances where deals have been unwound in TAGG and not in Sitara.”
- `giron-d/sent/270` (line 30, 2001-02-01, darron.giron@enron.com): “Just a quick reminder to please go into your books and flip all the ECC deals”
- `giron-d/sent/246` (line 37, 2001-02-07, darron.giron@enron.com): “Please let me know when these are finished as I need to get an invoice to the customers within the next couple of hours.”
- `giron-d/sent/195` (line 19, 2001-02-26, darron.giron@enron.com): “Please take care of this if you have any to be flipped.  Thanks.”
- `giron-d/sent/192` (line 37, 2001-02-26, darron.giron@enron.com): “These deals are showing up in TAGG as settling with ENA, could you all please keep an eye out for deals with this company and flip them right away.”
- `giron-d/sent/164` (line 29, 2001-03-08, darron.giron@enron.com): “Deal QP6086.1 in the WEST SJ book needs to be flipped”
- `giron-d/sent/168` (line 35, 2001-03-05, darron.giron@enron.com): “This is causing problems with the February Liquidations as I settled this deal with Aquila, but it isn't coming”
- `giron-d/sent/117` (line 27, 2001-03-28, darron.giron@enron.com): “Please rebook to W&T Offshore, Inc. short name is W&TOFFSHORE.”
- `giron-d/sent/108` (line 44, 2001-03-29, darron.giron@enron.com): “I'm missing at least 10 deals from the April 2001 Nymex invoice”
- `giron-d/sent/173` (line 29, 2001-03-01, darron.giron@enron.com): “Could you make sure that these seven deals are changed in Tagg to ENA I would”
- `giron-d/sent/18` (line 19, 2001-05-04, darron.giron@enron.com): “Please add Elizabeth Shim to the Book Admin list on the Web sight.  Her Tagg user name is:  ESHIM.  Thanks.”
- `giron-d/sent/17` (line 17, 2001-05-04, darron.giron@enron.com): “I also noticed that we have some books that are not listed under US GAS WEST but should be.  I cannot change tha Trading Group.”
- `giron-d/sent/9` (line 34, 2001-05-09, darron.giron@enron.com): “V83656.1:  Counterparty name should be BANKAMENAT.”
- `giron-d/sent/6` (line 35, 2001-05-11, darron.giron@enron.com): “For audit purposes, can you give us a brief description of where the value for annuities in TAGG as V42434.9 and V42434.A.”
- `giron-d/inbox/403` (line 5, 2001-11-27, scott.palmer@enron.com): “prompt post id”
- `giron-d/inbox/405` (line 17, 2001-11-27, scott.palmer@enron.com): “I do not know if you need wellhead, just in case it is 1416535.”
- `giron-d/inbox/161` (line 23, 2002-01-04, kam.keiser@enron.com): “These are book requests for the Netco books for all regions.”
- `giron-d/inbox/159` (line 22, 2002-01-04, m..love@enron.com): “Please add Financial and Control group to these book requests if they are missing.”
- `giron-d/inbox/155` (line 20, 2002-01-07, kam.keiser@enron.com): “Check your regions and if you see any locations mapped to curves we won't be setting anymore, make a list of those and what the new mappings should be.”
- `giron-d/inbox/147` (line 19, 2002-01-09, kam.keiser@enron.com): “When you have decided can you please input that into the trader matrix and I'll then forward everything to Ramesh.”
- `giron-d/inbox/132` (line 20, 2002-01-11, kam.keiser@enron.com): “We need to assign EOL products to traders.”
- `giron-d/inbox/63` (line 18, 2002-01-28, kam.keiser@enron.com): “Can you confirm with your desk heads that the list of names we have is correct, and then update the product mappings by tomorrow afternoon?”
- `giron-d/inbox/60` (line 18, 2002-01-28, m..love@enron.com): “Per Grigsby, all ten traders have signed on and the products are fixed.”

## 7. Month-end P&L close, valuation and audit support requests

At month-end and quarter-end the risk desks close the books: last-day files, economics and OA reviews, P&L restatements and write-off decisions. They also field repeated requests for support. Arthur Andersen asks for P&L top pages and curve shift reports, risk asks for curve validation explanations, accounting asks for liquidation support, and the Confirmations group asks for back-dated MTM valuations for counterparty audits. Darron Giron receives most requests and forwards them to analysts, who rebuild the support by hand each month.

- **Who touches it:** darron.giron@enron.com, david.baumbach@enron.com, deirdre.mccaffrey@enron.com, greg.whiting@enron.com, laura.luce@enron.com, lynn.pikofsky@enron.com, m..love@enron.com, richard.tomaski@enron.com, robin.rodrigue@enron.com, scott.palmer@enron.com
- **How often:** 4.06 occurrences/month (69 dated messages over 17 active months, 2000-10-17 → 2002-02-04)
- **Where it stalls:** Requests arrive as second requests and are forwarded several times. Owners are out and requests go unseen. There is no system with back-dated curves, so a risk person is interrupted for each valuation. Gas accounting cannot start until every desk replies, and errors such as killed January activity are found after close, forcing restatements.
- **Automation:** A month-end checklist that tracks desk completion with variance checks on the P&L tabs. Standard extracts for top pages, curve shifts and liquidation support per region would be filed automatically to the shared directory, and a valuation tool with back-dated curves would let Confirmations self-serve MTM. An auditor request tracker would map each desk to its preparer.
- **Estimate:** 45 min/occurrence × 30% automatable → 0.91 h/month → **$78/month**
- **Why that estimate:** Observer estimates run from 20 to 120 minutes with a median of 45 minutes. Extract generation helps, but much of the work is analysis and explanation, so the fraction is set at the 0.3 median.

**Evidence**

- `giron-d/sent/583` (line 17, 2000-10-17, darron.giron@enron.com): “Gather this info when you get a chance and give it to me.  Thanks.”
- `giron-d/sent/516` (line 18, 2000-11-07, darron.giron@enron.com): “Please get this info to me and I will pass it on to AA.  Thanks.”
- `giron-d/sent/516` (line 32, 2000-11-07, darron.giron@enron.com): “In order for us to complete our monthly gas testing, please provide the following items.”
- `giron-d/sent/521` (line 19, 2000-11-07, darron.giron@enron.com): “I missplaced the info we were speaking about yesterday.  Please send it to me again so I can follow up.  Thanks.”
- `giron-d/sent/515` (line 31, 2000-11-07, darron.giron@enron.com): “Please provide us with the P&L top sheet as of October 31 for the following books.”
- `giron-d/sent/327` (line 38, 2001-01-16, darron.giron@enron.com): “We are requesting that you supply the P & L top pages for the last day of the month for those regions that are applicable to you.”
- `giron-d/sent/326` (line 17, 2001-01-16, darron.giron@enron.com): “Could you please read this request and get back to Mark with the info ASAP?  Thanks.”
- `giron-d/sent/324` (line 17, 2001-01-16, darron.giron@enron.com): “AA is all over me today.  Please get this for Mark.  Thanks.”
- `giron-d/sent/299` (line 19, 2001-01-24, darron.giron@enron.com): “Please contact Mark and provide him with the documentation he needs.  Thanks.”
- `giron-d/sent/322` (line 32, 2001-01-17, darron.giron@enron.com): “I forwarded this to Carole to take care of Northwest as she was running it Nov and Dec.”
- `giron-d/sent/258` (line 33, 2001-02-02, darron.giron@enron.com): “Please reply when your last day file is complete and don't forget to provide me with your Economics Detail and Summary Level Reports.”
- `giron-d/sent/248` (line 20, 2001-02-07, darron.giron@enron.com): “Kevin's reported P&L was understated by the $188K on the OA Flash tab.”
- `giron-d/sent/232` (line 32, 2001-02-12, darron.giron@enron.com): “Please make these corrections in February in order to correct the NG P&L for the quarter.”
- `giron-d/sent/219` (line 17, 2001-02-15, darron.giron@enron.com): “We are taking a hit of $28,900,000 on tonight's P&L for Dec-00 production.”
- `giron-d/sent/240` (line 31, 2001-02-09, darron.giron@enron.com): “Please forward to Ellen Wallumrod the MTM valuation(mini-book) for all CoEnergy Trading Company deals as of Dec 31, 2000.”
- `giron-d/sent/241` (line 50, 2001-02-09, darron.giron@enron.com): “we will be coming to them often with these requests (we recieve several per week)”
- `giron-d/sent/214` (line 32, 2001-02-16, darron.giron@enron.com): “Can you provide MTM values as of Dec 29, 2000, for the short name of CROSS TIMBERS.”
- `giron-d/sent/170` (line 35, 2001-03-05, darron.giron@enron.com): “Please get responses for these back to Jennifer today.”
- `giron-d/sent/132` (line 43, 2001-03-21, darron.giron@enron.com): “Can you or anyone in your group follow up on the curves below?”
- `giron-d/sent/132` (line 19, 2001-03-21, darron.giron@enron.com): “NGI-PGE/TOPOCK is an internal curve used to value transport and is equal to NGI-SOCAL.”
- `giron-d/sent/187` (line 40, 2001-02-27, darron.giron@enron.com): “You may save the support to ERMS/1Intra/FRED Liquidations/"year"/"month"”
- `giron-d/sent/187` (line 47, 2001-02-27, darron.giron@enron.com): “I WILL ALSO NEED SUPPORT FOR THE  DECEMBER AND JANUARY VALUES FOR ALL OF YOUR REGIONS”
- `giron-d/sent/105` (line 31, 2001-03-29, darron.giron@enron.com): “In need liquidation support for the December Liquidation values below=20”
- `giron-d/sent/120` (line 31, 2001-03-28, darron.giron@enron.com): “Could you please let me know the status on this information as soon as”
- `giron-d/sent/118` (line 17, 2001-03-28, darron.giron@enron.com): “I was on vacation when you sent the first request and somehow didn't see it”
- `giron-d/sent/137` (line 34, 2001-03-21, darron.giron@enron.com): “Please provide the total MTM value for that date within your region.”
- `giron-d/sent/178` (line 17, 2001-02-28, darron.giron@enron.com): “Is it ready?  Mike Grigsby, who is the head physical trader on the desk asked”
- `farmer-d/logistics/228` (line 31, 2001-03-13, david.baumbach@enron.com): “Please provide the information requested below as soon as possible.”
- `giron-d/sent/90` (line 36, 2001-04-05, darron.giron@enron.com): “Please forward the requested information as soon as possible as it needed to complete our 1st quarter testing for Earnings Release.”
- `giron-d/sent/60` (line 40, 2001-04-18, darron.giron@enron.com): “Just a reminder to each of you that I requested this info by tomorrow.  I've received only one response so far.”
- `giron-d/sent/47` (line 31, 2001-04-23, darron.giron@enron.com): “However, we are looking for specific reasons as to why this is so.”
- `giron-d/sent/63` (line 26, 2001-04-17, darron.giron@enron.com): “Please forward to me your region's access criteria no later than 11:00 am, Monday, March 19”
- `giron-d/sent/88` (line 17, 2001-04-05, darron.giron@enron.com): “I won't blame you if you don't get that requested info to me.”
- `giron-d/inbox/138` (line 19, 2002-01-10, richard.tomaski@enron.com): “Can you guys help try to resolve these differences?  We may have to write them off anyways, but we need to know what they relate to.”
- `giron-d/inbox/127` (line 24, 2002-01-12, richard.tomaski@enron.com): “Terminate all physical and financial deals between ENA and EMW.”
- `giron-d/inbox/124` (line 24, 2002-01-14, greg.whiting@enron.com): “Upon conversation with Jeff Hodge the intercompany AR/AP with ENA can be offset.”
- `giron-d/inbox/123` (line 22, 2002-01-14, richard.tomaski@enron.com): “I will complete this transaction and book it tomorrow.”
- `giron-d/inbox/104` (line 19, 2002-01-23, deirdre.mccaffrey@enron.com): “This looks way too high - can we get together in the morning.”
- `giron-d/inbox/96` (line 17, 2002-01-23, deirdre.mccaffrey@enron.com): “could we get the supply deal valued as of 1/16/01.  That's the date the other deals were valued from.”
- `giron-d/inbox/100` (line 28, 2002-01-23, deirdre.mccaffrey@enron.com): “His list does not include any of the transport positions.  It also includes some deals with the Chicago office that should not be included in the deal value.”
- `giron-d/inbox/25` (line 22, 2002-02-04, richard.tomaski@enron.com): “when we killed all forward PGL deals in TAGG for the inventory transfer, we killed Jan activity even though most of this gas flowed.”
- `giron-d/inbox/27` (line 21, 2002-02-04, richard.tomaski@enron.com): “we booked basedload summer sell of 95,000.  ENA calls of 50,000 and ENA puts of 30,000 for PGL”
- `giron-d/inbox/21` (line 17, 2002-02-04, lynn.pikofsky@enron.com): “We have restated our p&l for 1/31/02.  The file is called 013102final2.xls.”
- `giron-d/inbox/40` (line 19, 2002-01-31, m..love@enron.com): “The positions file for last night is saved out to o_dropbox and is attached.”

## 8. Gas invoice and deal price discrepancy resolution

Settlements and accounting staff compare counterparty invoices, statements and payment claims with Sitara and Unify. They find price differences, missing days, wrong counterparties or one-sided deals, then email the deal owner (Daren Farmer, Julie Meyers) to confirm the right deal and price and to correct the ticket so Unify can be redrafted. The owner often has to ask a trader or the counterparty before answering. Invoice deadlines and counterparty phone calls keep up the pressure while questions bounce between people.

- **Who touches it:** aepin@aep.com, carlos.rodriguez@enron.com, charlene.richmond@enron.com, charlotte.hawkins@enron.com, cynthia.hakemack@enron.com, d..winfree@enron.com, darron.giron@enron.com, david.baumbach@enron.com, edward.gottlob@enron.com, elizabeth.hernandez@enron.com, esther.garcia@enron.com, fred.boas@enron.com
- **How often:** 4.14 occurrences/month (87 dated messages over 21 active months, 2000-03-13 → 2001-11-27)
- **Where it stalls:** Requests sit with one or two deal owners and are re-sent when they are out. Questions bounce between settlements, logistics, measurement and traders for days or weeks, and invoice and payment cut-offs pass. Some disputes run for months, and counterparties call repeatedly. Volume Management sometimes shows no actualized volume, so nobody can confirm the amount.
- **Automation:** An automatic invoice-to-deal match that compares each counterparty invoice or statement line with the Sitara deal price, volume, counterparty and entity. Each mismatch is raised as a tracked case routed to the ticket owner, carrying the deal, the invoice line and the allocation already attached. Corrections in Sitara notify settlements automatically so Unify can be redrafted, which replaces the email threads and chasers.
- **Estimate:** 30 min/occurrence × 40% automatable → 0.83 h/month → **$70/month**
- **Why that estimate:** Observer medians cluster at 25 to 45 minutes, and the message-weighted median is 30 minutes across requester and owner. Matching and routing automate well, but resolving the true price with traders or counterparties does not, so the fraction is set at the 0.4 median.

**Evidence**

- `farmer-d/logistics/922` (line 29, 2000-03-20, julie.meyers@enron.com): “We have a price difference with Mitchell Gas Services for 2/00 production, deal 156658.”
- `farmer-d/logistics/963` (line 17, 2000-03-27, tina.valadez@enron.com): “Pat Dresner (accountant) at Midcon Texas says she does not show these deals in her system and she can not pay on them.”
- `farmer-d/logistics/979` (line 23, 2000-03-28, katherine.herrera@enron.com): “The following point should be adjusted to reflect a price of $2.52, per the contract.”
- `farmer-d/logistics/985` (line 28, 2000-03-28, julie.meyers@enron.com): “This problem, among others with this exchange deal, is currently we have a massive A/R issue and we're trying to get this cleanup before end of month.”
- `farmer-d/logistics/999` (line 32, 2000-03-31, julie.meyers@enron.com): “Is this still outstanding?  Craig is back in the office now.”
- `farmer-d/logistics/1246` (line 23, 2000-06-27, joanie.ngo@enron.com): “Conoco is saying that we are missing one day of sale to them:  5/5  10,000 mmbtu at 2.95, deal #256686.”
- `farmer-d/logistics/1284` (line 17, 2000-07-17, megan.parker@enron.com): “I received an invoice from PG&E Texas Industrial Energy for 6/00 production and I do not see one of the pieces in Unify.”
- `farmer-d/logistics/1309` (line 19, 2000-07-27, nicole.vo@enron.com): “Mary Gregg from LCRA said that Sitara #283939 should have been for $4.50/MMBtu.”
- `farmer-d/logistics/1285` (line 30, 2000-07-17, david.baumbach@enron.com): “Since we cannot fix the deal, go ahead and put a fixed price of $2.81359 on both lines of the May 2000 deal.”
- `giron-d/sent/636` (line 19, 2000-09-21, darron.giron@enron.com): “The Sitara was not updated for Aug.  I just corrected Sitara.  So you can redraft in Unify.”
- `giron-d/sent/643` (line 19, 2000-09-19, darron.giron@enron.com): “The deal number in Sitara was changed because of an internal book name change.”
- `giron-d/sent/630` (line 46, 2000-09-27, darron.giron@enron.com): “I need to get the Sitara number if this has been set up so I can pay Peoples.”
- `farmer-d/logistics/1420` (line 20, 2000-09-22, kristen.hanson@enron.com): “it is our policy to withhold payment unless we are invoiced, payment was not made on this until now.”
- `giron-d/sent/625` (line 34, 2000-09-29, darron.giron@enron.com): “Dave at The New Power Group is wanting his money.”
- `farmer-d/logistics/1528` (line 23, 2000-11-17, katherine.herrera@enron.com): “Settlements is showing both a sales and purchase for Texas General Land Office and they are stating that they should not be billed or paid for anything.”
- `farmer-d/logistics/1542` (line 17, 2000-11-29, laurie.ellis@enron.com): “I am trying to process two invoices from Samson Resources Co. (Samson Lone Star Limited) for September 2000 and October 2000.”
- `farmer-d/logistics/1536` (line 19, 2000-11-21, o'neal.winfree@enron.com): “Please take a look at the attached spreadsheet, we have over 500,000mmbtu as unaccounted for”
- `farmer-d/logistics/1511` (line 19, 2000-11-13, janet.wallis@enron.com): “Just wanted to review weekend sales to Southern Union.”
- `farmer-d/logistics/2089` (line 19, 2001-02-21, charlene.richmond@enron.com): “I am getting several phone calls from Alpine Resources demanding to be paid for meter 5892 and there is nothing there to be paid.”
- `farmer-d/logistics/2094` (line 27, 2001-02-23, charlene.richmond@enron.com): “WOULD SOMEONE PLEASE HELP ME GET THIS MATTER RESOLVED.”
- `farmer-d/logistics/2100` (line 26, 2001-02-25, fred.boas@enron.com): “Karen Lindley allocates this point but I feel the need to help her because this issue came to light while I was in transition.”
- `farmer-d/logistics/2069` (line 17, 2001-02-01, paul.couvillon@enron.com): “Janet Wallis told me so.”
- `farmer-d/logistics/2087` (line 24, 2001-02-20, katherine.herrera@enron.com): “Do you have a Crude Oil payable to offset this sales invoice?”
- `farmer-d/logistics/177` (line 26, 2001-04-16, katherine.herrera@enron.com): “I think Daren is out for the remainder of the day and I need to send out my invoice this afternoon.”
- `farmer-d/logistics/176` (line 19, 2001-04-17, elizabeth.hernandez@enron.com): “I was not aware that Julie was out yesterday.  I left early yesterday and this did not get done till this morning.”
- `farmer-d/logistics/181` (line 16, 2001-04-12, cynthia.hakemack@enron.com): “Conoco invoiced HPL at $5.87 for 03/23 at PGEV/Waha and deal ticket 685350 shows $4.87.  Can you confirm the price?”
- `giron-d/sent/83` (line 30, 2001-04-09, darron.giron@enron.com): “Can you please update the deal in Sitara to reflect the correct price for 03/01?”
- `farmer-d/logistics/174` (line 16, 2001-04-17, rebecca.griffin@enron.com): “Could you verify the pricing on TXU Gas Distribution deal #589007 for the following days?”
- `farmer-d/logistics/147` (line 16, 2001-05-07, cynthia.hakemack@enron.com): “BP invoiced HPL at $4.955 for the deal below, and Sitara shows $4.95.  Can you please verify the pricing?  Thanks.”
- `farmer-d/logistics/138` (line 16, 2001-05-18, megan.parker@enron.com): “We have it priced at WAHA gas daily + 0.005 and Texaco says it should be WAHA IF + 0.005.”
- `farmer-d/logistics/99` (line 17, 2001-07-09, l..hernandez@enron.com): “I have not received a response from you regarding the pricing discrepancies on these deals.  Please let me know which price is correct if possible.”
- `farmer-d/logistics/129` (line 21, 2001-05-23, sabrae.zajac@enron.com): “I found Danny's book and he has the deal priced at 5.25.  I adjusted the price in Sitara.  Let me know if anything further is needed.”
- `farmer-d/logistics/132` (line 19, 2001-05-22, charlene.richmond@enron.com): “Could you fix asap because payment is due on 25th.”
- `farmer-d/logistics/134` (line 19, 2001-05-22, joyce.viltz@enron.com): “The volumes have not be actualized so there is nothing in Volume Management.  Can one of you look into this and get back to me.”
- `farmer-d/logistics/130` (line 22, 2001-05-23, mary.ellenberger@enron.com): “Payment MUST be set up by noon 5/24/01 for prompt payment to Spinnaker.”
- `farmer-d/logistics/127` (line 21, 2001-05-24, carlos.rodriguez@enron.com): “Yes, this is the Blue Dolphin but I dont know why shes not able to see it. It was nom, tracked and balanced.”
- `farmer-d/logistics/124` (line 25, 2001-05-24, tess.ray@enron.com): “Can you confirm if 04/01 sales price for SA-745578, IF - $.06 per entry in Sitara or IF - $.07 per Sandra Werner's e-mail”
- `farmer-d/logistics/74` (line 28, 2001-08-17, valerie.vela@enron.com): “Deal 895691 - swing deal - currently has 234,000 in the scheduled column and it should be 441,000 based on the spreadsheet I sent.”
- `farmer-d/logistics/73` (line 17, 2001-08-17, valerie.vela@enron.com): “And I was told that Sitara could not handle this pricing structure, that it had to be calculated and entered as a fixed price.”
- `farmer-d/logistics/72` (line 20, 2001-08-21, joy.werner@enron.com): “We are not able to find out July deal for TGLO in the system.”
- `farmer-d/logistics/70` (line 18, 2001-08-24, megan.parker@enron.com): “Conoco is saying that we did not buy that gas from them.”
- `farmer-d/logistics/67` (line 18, 2001-09-04, megan.parker@enron.com): “ENA was invoiced by Coral Energy for two deals on Tejas for June 2001 that I do not see in the system.”
- `farmer-d/logistics/34` (line 33, 2001-10-30, laynie.east@enron.com): “it still looks like the volumes for gas delivered to TX GLO do not have Linda Robert's origination fee deducted.”
- `farmer-d/logistics/34` (line 55, 2001-10-30, laynie.east@enron.com): “I reviewed the gas deals on Franks' spreadsheet and they agree with what is in Sitara.”
- `farmer-d/logistics/28` (line 17, 2001-10-31, d..winfree@enron.com): “We will handle this via the OA process, where I'm working with the OA group”
- `farmer-d/logistics/16` (line 28, 2001-11-27, sherlyn.schumack@enron.com): “Will you let me know when this change has been made?  I need to get some payments finaled by 3pm tomorrow.”
- `farmer-d/logistics/16` (line 19, 2001-11-27, sherlyn.schumack@enron.com): “Have you had a chance to look at this yet?”
- `farmer-d/logistics/15` (line 20, 2001-11-27, marlene.hilliard@enron.com): “This deal is for Global # 96022051.  This is between HPL and Black Marlin Pipeline Company.  This should be handled by your group.”

## 9. Manager surveys, budget, HR and administrative data collection

Finance, cost-model, HR and admin groups email managers each month or cycle asking them to complete hours and activity-driver surveys, cost-center allocation percentages, budget and staffing worksheets, variance explanations, presentation inputs and weekly bullets. Other requests cover PEP and PRC reviewer lists and feedback, analyst recruiting forms, onboarding items, time reports, expense approvals and phone-bill reviews. Each is a spreadsheet or form completed by hand against a deadline, followed by reminder emails to non-responders.

- **Who touches it:** ami.chokshi@enron.com, amy.fitzpatrick@enron.com, announcements.ubsw@enron.com, bill.williams@enron.com, brenda.herod@enron.com, cara.semperger@enron.com, csulzer@grenergy.com, darron.giron@enron.com, david.baumbach@enron.com, diane.cook@enron.com, elizabeth.webb@enron.com, enron_update@concureworkplace.com
- **How often:** 3.96 occurrences/month (107 dated messages over 27 active months, 2000-01-17 → 2002-03-22)
- **Where it stalls:** Few people respond by the deadline, so reminders and new deadlines follow. The same driver numbers are re-keyed every month. Protected or distorted spreadsheets bounce back to finance. HR systems such as PEP were down or had wrong reporting lines, so lists went by email through intermediaries. HR asks for the same placement fields more than once, and each expense report is a separate click-through.
- **Automation:** One collection workflow with forms pre-filled from the prior period and from system reports (driver counts, allocations, reporting lines). It would validate totals, send automatic reminders only to non-responders, and track status for the requester. Expense approvals would be delegated or rule-based, with a digest for exceptions. This replaces the broadcast emails, attachments and chasers.
- **Estimate:** 30 min/occurrence × 40% automatable → 0.79 h/month → **$67/month**
- **Why that estimate:** Observer estimates span 4 to 60 minutes, and the median across the merged items is 30 minutes per manager cycle. Prefill and reminders automate a good share, but the content still needs owner judgement, so the fraction is set at the 0.4 median.

**Evidence**

- `farmer-d/logistics/700` (line 30, 2000-01-19, brenda.herod@enron.com): “I need each of you to review the 2000 Plan allocations as I submitted them earlier today, and provide an accurate allocation of your RC for 1/00.”
- `farmer-d/logistics/698` (line 23, 2000-01-19, brenda.herod@enron.com): “I've given up on the spreadsheet - I couldn't insert the column.”
- `farmer-d/logistics/700` (line 48, 2000-01-19, brenda.herod@enron.com): “I would like you allocations back to me no later than Thursday, 1/20 @ 3:00pm.”
- `farmer-d/logistics/854` (line 38, 2000-02-29, shari.mao@enron.com): “Please provide a
completed "Hours" survey for each position within your group.”
- `farmer-d/logistics/854` (line 66, 2000-02-29, shari.mao@enron.com): “Please return these surveys by end of day Friday, March 3rd.”
- `farmer-d/logistics/836` (line 97, 2000-02-24, lisa.cousino@enron.com): “Please continue to check your RC report
each month going forward.”
- `farmer-d/logistics/862` (line 114, 2000-03-01, lisa.cousino@enron.com): “Please send changes by Friday, March 3.”
- `farmer-d/logistics/997` (line 40, 2000-03-31, shari.mao@enron.com): “For the month of March, please provide a completed "Hours" survey for each position within your group.”
- `farmer-d/logistics/998` (line 32, 2000-03-31, shari.mao@enron.com): “Please fill out the attached activity driver survey with March numbers for your RC by end of day Wednesday, April 5th.”
- `farmer-d/logistics/923` (line 22, 2000-03-20, shari.mao@enron.com): “This lack of information prevents your expenses from being 100% allocated out to the commercial teams.”
- `farmer-d/logistics/914` (line 18, 2000-03-18, lisa.csikos@enron.com): “I get a Labor Distribution report and show that Kenneth Seaman is showing as being active for payperiod 1 and 2 in February.”
- `farmer-d/logistics/954` (line 23, 2000-03-24, yvette.connevey@enron.com): “Please submit your scheduled April Vacation to me by the end of Monday afternoon.”
- `farmer-d/logistics/1117` (line 27, 2000-05-18, yvette.connevey@enron.com): “INSTEAD, please submit your list of reviewers to Brenda via e-mail.  She will make any changes necessary and forward them on to the PEP Helpdesk.”
- `farmer-d/logistics/1104` (line 24, 2000-05-11, brenda.herod@enron.com): “Please confirm to me ASAP (by end of day, TODAY)  that you will be available.”
- `farmer-d/logistics/1121` (line 25, 2000-05-19, stacey.neuweiler@enron.com): “Please let me know if you think I should list anyone else.  Thanks.”
- `farmer-d/logistics/1017` (line 53, 2000-04-05, yvette.connevey@enron.com): “This spreadsheet seems to have errors in every cell.  Can you help?”
- `farmer-d/logistics/1083` (line 38, 2000-05-01, brenda.herod@enron.com): “Please review and have any changes to me by Thursday, May 4th.”
- `farmer-d/logistics/1084` (line 36, 2000-05-02, shari.mao@enron.com): “If your group currently generates a standard report that captures the surveyed data, please send the report to me”
- `farmer-d/logistics/1188` (line 23, 2000-06-07, brenda.herod@enron.com): “The deadline was Friday, 6/2, and unfortunately, very few of you responded.”
- `farmer-d/logistics/1188` (line 24, 2000-06-07, brenda.herod@enron.com): “you have expressed your concerns on the process burdening you.”
- `farmer-d/logistics/1180` (line 18, 2000-06-06, shari.mao@enron.com): “Please provide the number of Producer Services deals for the month of May (New vs. Existing)”
- `farmer-d/logistics/1154` (line 60, 2000-05-30, james.scribner@enron.com): “If your group currently generates a standard report that captures the surveyed data, please send the report to Jennifer Reside.”
- `farmer-d/logistics/1210` (line 46, 2000-06-15, david.baumbach@enron.com): “provide explanations for all material changes (+/- 10%) for the year/year, quarter/quarter, and month/month variances.”
- `farmer-d/logistics/1313` (line 19, 2000-08-01, david.baumbach@enron.com): “Pat, could you shed a little light on how we get the CPR Fuels number?”
- `farmer-d/logistics/1144` (line 19, 2000-05-24, heidi.withers@enron.com): “I updated the June transport usage tickets today through HPL, and will be finishing these tickets tomorrow.”
- `farmer-d/logistics/1162` (line 21, 2000-05-31, robert.cotten@enron.com): “Both reports were derived from the Volume Management module of UNIFY.”
- `farmer-d/logistics/1173` (line 45, 2000-06-05, brenda.herod@enron.com): “I need your feedback by FRIDAY, 6/9 so that I can use the week-end to get ready.”
- `giron-d/sent/794` (line 34, 2000-06-13, darron.giron@enron.com): “You were identified as a reviewer for Audrey Cook.  If possible, could you complete her feedback by end of business Wednesday?”
- `giron-d/sent/783` (line 40, 2000-06-09, darron.giron@enron.com): “Please send me a list of your accomplishments for the last six months by Friday.”
- `farmer-d/logistics/1195` (line 18, 2000-06-09, hector.mcloughlin@enron.com): “Please review the names below and let me know if there are any other names that need to be added or subtracted from your group for PRC purposes.”
- `farmer-d/logistics/1243` (line 45, 2000-06-27, shari.mao@enron.com): “If your hours have not changed from last month, please send us an email to indicate so.”
- `farmer-d/logistics/1244` (line 34, 2000-06-27, shari.mao@enron.com): “Please select your RCs, and fill in the driver quantity for the requested driver for the month of June.”
- `farmer-d/logistics/1319` (line 35, 2000-08-03, james.scribner@enron.com): “Please fill out the attached activity driver survey with July numbers for your RC and return to Shari Mao by end of day Friday, August 11.”
- `farmer-d/logistics/1392` (line 22, 2000-09-07, diane.cook@enron.com): “The first draft of the 2001 budget is due on September 18th.”
- `farmer-d/logistics/1392` (line 40, 2000-09-07, diane.cook@enron.com): “PLEASE TURN IN YOUR 2001 STAFFING BY SEPTEMBER 11, END OF BUSINESS.”
- `farmer-d/logistics/1401` (line 51, 2000-09-13, diane.cook@enron.com): “IF YOU HAVE NOT TURNED IN YOUR STAFFING FOR 2001, PLEASE TURN THAT IN TODAY.”
- `farmer-d/logistics/1445` (line 55, 2000-10-06, james.scribner@enron.com): “As a reminder, today is the deadline for completion of the OPM Survey.”
- `farmer-d/logistics/1447` (line 19, 2000-10-10, suzanne.nicholie@enron.com): “you allocated 15 hours to the activity ES002 - Non Routine Trade Monitoring & Reporting.  What commercial team(s) was this 15 hours spent supporting?”
- `farmer-d/logistics/1416` (line 46, 2000-09-19, david.baumbach@enron.com): “provide explanations for all material changes (+/- 10%) for the year/year, quarter/quarter, and month/month variances.”
- `farmer-d/logistics/1409` (line 39, 2000-09-14, diane.cook@enron.com): “1) Make a list of your staff just their positions.”
- `giron-d/sent/789` (line 18, 2000-10-31, darron.giron@enron.com): “I don't believe I am set up to review as a supervisor in the PEP system.  How do I get this changed in the system?”
- `giron-d/sent/523` (line 20, 2000-11-07, darron.giron@enron.com): “Kimberly S. Olinger is listed as reporting to me in the PEP system.  She should be moved to Jeff Gossett.”
- `giron-d/sent/511` (line 19, 2000-11-08, darron.giron@enron.com): “I see Jennifer Bagwell in the system, but not Christopher Walker.”
- `giron-d/sent/429` (line 24, 2000-12-04, darron.giron@enron.com): “I am ignorant of the process, so if I am presuming something incorrect, I would appreciate info on how this is supposed to work.”
- `giron-d/sent/408` (line 42, 2000-12-07, darron.giron@enron.com): “please complete the attached "Needs Assessment Form " and return to me so that I may forward resumes to you of candidates that fit your need.”
- `giron-d/sent/363` (line 33, 2000-12-27, darron.giron@enron.com): “Some aren't technical.  I don't have any problem solving questions.”
- `giron-d/sent/356` (line 19, 2001-01-03, darron.giron@enron.com): “The locations are all the same because I'm not sure exactly where they will sit.  The Cost Center is for my desk (West)”
- `giron-d/sent/330` (line 29, 2001-01-15, darron.giron@enron.com): “We will interview them two at a time.  Meaning two of the above referenced people will be in the room at the same time interviewing the candidates.”
- `giron-d/sent/340` (line 19, 2001-01-10, darron.giron@enron.com): “We would like to bring Sladana Anna Kulic into the Risk Management group.  The location may change.”
- `giron-d/sent/315` (line 33, 2001-01-18, darron.giron@enron.com): “I have been trying to get in touch with Toni Graham all day and have not had any luck.”
- `williams-w3/sent_items/246` (line 18, 2001-09-14, bill.williams@enron.com): “Could you send an email to each group member giving them their average usage since you started or the last 3 months”
- `williams-w3/sent_items/246` (line 30, 2001-09-14, bill.williams@enron.com): “I can go through all the bills and let you know what was spent on new phones, it will take a while but I could figure it out.”
- `williams-w3/sent_items/245` (line 18, 2001-09-14, bill.williams@enron.com): “It looks like our AT&T rep switched him back to the group calling plan.”
- `farmer-d/logistics/57` (line 17, 2001-09-19, enron_update@concureworkplace.com): “The following expense report is ready for approval:”
- `farmer-d/logistics/51` (line 26, 2001-10-11, elizabeth.webb@enron.com): “This is just a friendly reminder that I need the information for the Gas Logistics PowerPoint presentation by tomorrow, Friday, October 12th.”
- `farmer-d/logistics/55` (line 30, 2001-09-25, richard.pinion@enron.com): “Please forward to those I have left off the mail list.”
- `farmer-d/logistics/23` (line 30, 2001-11-06, elizabeth.webb@enron.com): “Attached is a general Logistics PowerPoint presentation that can be presented to customers or whoever you need to present information about Enron North America Gas Logistics to.”
- `farmer-d/logistics/27` (line 21, 2001-11-01, elizabeth.webb@enron.com): “Have you had a chance to complete the Texas logistics information for the PowerPoint presentation?”
- `lokay-m/inbox/42` (line 20, 2001-10-31, richard.hanagriff@enron.com): “This past due amount is getting old and it needs to be resolved?”
- `lokay-m/inbox/41` (line 35, 2001-11-07, kevin.hyatt@enron.com): “Is an answer possible by Tuesday 11/12?”
- `giron-d/inbox/368` (line 17, 2001-10-31, csulzer@grenergy.com): “Is it possible for someone at Enron to occasionally provide the gas market data that I need?”
- `farmer-d/logistics/20` (line 21, 2001-11-12, richard.pinion@enron.com): “Please ask your schedulers to e-mail me which pipelines still maintain the ability to do Nominations via a dial up connection to their EBB”
- `williams-w3/sent_items/91` (line 18, 2001-11-14, bill.williams@enron.com): “Could you look into my concur expense login/password. I am at a class today and need to approve these expense reports in the system.”
- `williams-w3/sent_items/91` (line 32, 2001-11-14, bill.williams@enron.com): “The following reports have been waiting for your approval for more than 4 days.  Please review.”
- `lokay-m/inbox/50` (line 17, 2001-11-26, enron_update@concureworkplace.com): “The Approval status has changed on the following report:”
- `williams-w3/inbox/66` (line 17, 2002-01-31, enron_update@concureworkplace.com): “The following expense report is ready for approval:”
- `williams-w3/inbox/63` (line 26, 2002-01-31, enron_update@concureworkplace.com): “To approve this expense report, click on the following link for Concur Expense.”
- `giron-d/inbox/15` (line 17, 2002-02-05, georgeanne.hodges@enron.com): “Note to approvers - please approve these expense reports quickly.”
- `williams-w3/inbox/30` (line 21, 2002-02-06, amy.fitzpatrick@enron.com): “Our records indicate that you have not taken your pre-employment drug test for UBS.”
- `williams-w3/inbox/64` (line 95, 2002-01-31, julie.clyatt@enron.com): “Records indicate that there are a significant number of employees who have yet to have a drug test.”
- `giron-d/inbox/2` (line 107, 2002-02-06, neil.davies@enron.com): “PLEASE RSVP (BY REPLYING TO THIS E-MAIL) - IF YOU HAVEN'T DONE SO ALREADY”
- `williams-w3/inbox/42` (line 19, 2002-02-05, julie.kearney@enron.com): “Some information is missing on your UBS application.  Please swing by to complete.”
- `lokay-m/sent_items/92` (line 26, 2002-02-14, michelle.lokay@enron.com): “Don't forget to submit your time reports by Thursday morning.”
- `lokay-m/sent_items/115` (line 17, 2002-02-28, michelle.lokay@enron.com): “I have been here except last Tuesday..traveling for work!”
- `lokay-m/sent_items/142` (line 17, 2002-03-14, michelle.lokay@enron.com): “I took 1/2 day of vacation last Friday, 03/08.  Thanks.”
- `lokay-m/sent_items/132` (line 25, 2002-03-08, michelle.lokay@enron.com): “Please send me your bullets ASAP this morning.  If you have no bullets to report, please reply to me that you have none.”
- `lokay-m/sent_items/132` (line 17, 2002-03-08, michelle.lokay@enron.com): “No bullets....ongoing with TXU, Burlington, Mojave.”
- `lokay-m/sent_items/160` (line 28, 2002-03-22, michelle.lokay@enron.com): “New dollar-valued OBA, containing monthly cash out provision, with Burlington is executed.”

## 10. Customer and producer gas nomination intake and re-keying

Customers, producers and pipelines send daily, weekend and monthly gas nominations and revisions by email. Examples include Calpine, Enron Methanol and MTBE, KCS Josey Ranch, TXU, Reliant, Valero and Prize Energy, and the nominations usually come as Word or spreadsheet attachments with little body text. Ami Chokshi and other trade-support staff forward them to schedulers. Schedulers re-key the volumes into Sitara, POPS or Unify and ask Daren Farmer to approve revisions, and risk prepares next-month estimates from prior-month noms. Each revision repeats the cycle, so the same customer can generate several rounds a month.

- **Who touches it:** aimee.lannou@enron.com, ami.chokshi@enron.com, craig.breslau@enron.com, darron.giron@enron.com, david.baumbach@enron.com, edward.gottlob@enron.com, edward.terry@enron.com, h..wallis@enron.com, juliann.kemp@enron.com, lauri.allen@enron.com, lee.papayoti@enron.com, mark.mccoy@enron.com
- **How often:** 5.37 occurrences/month (102 dated messages over 19 active months, 1999-12-14 → 2001-06-01)
- **Where it stalls:** Attachments arrive with blank subjects and no body text and are forwarded by hand. Each file has to be opened and re-keyed, and entry mistakes creep in. Revisions need Daren's approval before anything changes. Nominations sometimes arrive before the transport contract or meter number exists, and unresponsive producers have to be chased against deadlines. Estimates are sent in fragments.
- **Automation:** A nomination ingestion service that reads the nomination emails and attachments into structured rows (counterparty, meter, day, volume). It diffs each row against the current Sitara and POPS volumes, posts only the changes to the scheduling queue for one-click approval, and auto-acknowledges the sender when nothing changed. It also proposes next-month estimates and swing volumes from prior-month and prior-year flow. This replaces the manual forwarding, re-keying and approval emails.
- **Estimate:** 15 min/occurrence × 50% automatable → 0.67 h/month → **$57/month**
- **Why that estimate:** Observer estimates ran from 10 to 30 minutes, with a median of 15 minutes per nomination or revision including forwarding, keying and approval. Parsing and diffing structured attachments is highly automatable, but judgement on swings and revisions remains, so the fraction is set at the 0.5 median.

**Evidence**

- `farmer-d/logistics/1027` (line 19, 2000-04-10, rickya@calpine.com): “As we spoke about by phone, here is the nomination, Thanks.”
- `giron-d/sent/795` (line 16, undated, darron.giron@enron.com): “Confirmed on my end. Same volumes as yesterday, no changes to the path.”
- `farmer-d/logistics/169` (line 21, 2001-04-19, rickya@calpine.com): “Will be out Friday, will call if there are any changes.Thanks”
- `farmer-d/logistics/685` (line 6, 2000-01-14, timpowell@txu.com): “HPL Nomination for January 15 thru 17, 2000”
- `farmer-d/logistics/607` (line 23, 1999-12-21, michael.mitcham@enron.com): “Enron Methanol Company nominates the following requirements for the Methanol Plant for January 2000:”
- `farmer-d/logistics/653` (line 32, 2000-01-05, ami.chokshi@enron.com): “and I remembered to send these to you.....”
- `farmer-d/logistics/719` (line 23, 2000-01-25, michael.mitcham@enron.com): “Enron Methanol nominates the following requirements for the Methanol Plant”
- `farmer-d/logistics/723` (line 21, 2000-01-26, lee.papayoti@enron.com): “I've changed the sitara ticket .... but one of you”
- `farmer-d/logistics/762` (line 22, 2000-02-07, lee.papayoti@enron.com): “For Feb 6 to 29 on ticket 93199, I entered 18,500/d .... and it should have”
- `farmer-d/logistics/803` (line 19, 2000-02-16, tom.acton@enron.com): “Daren I since you were at the offsite I went ahead and changed the volume”
- `farmer-d/logistics/866` (line 21, 2000-03-02, tom.acton@enron.com): “They would like to drop the volume again to 4400.”
- `farmer-d/logistics/716` (line 6, 2000-01-25, timpowell@txu.com): “HPL Nomination for January 26, 2000”
- `farmer-d/logistics/816` (line 6, 2000-02-18, ami.chokshi@enron.com): “COPANO CHANGES FOR THE 19TH”
- `farmer-d/logistics/767` (line 31, 2000-02-08, ami.chokshi@enron.com): “(See attached file: egmnom-Feb.xls)”
- `farmer-d/logistics/820` (line 32, 2000-02-22, ami.chokshi@enron.com): “Attached are some revised volumes for March, 2000.  Please let me know if I”
- `farmer-d/logistics/921` (line 29, 2000-03-20, susan.trevino@enron.com): “Here's REVISED March 2000 (effective 3/21/00 9:00am cycle) setup for Josey:”
- `farmer-d/logistics/984` (line 5, 2000-03-28, susan.trevino@enron.com): “FW: 3rd rev Mar. 2000 Josey Ranch nom”
- `farmer-d/logistics/993` (line 30, 2000-03-29, susan.trevino@enron.com): “This is the estimated Josey Ranch nomination for the month of April 2000.”
- `farmer-d/logistics/980` (line 35, 2000-03-28, tom.acton@enron.com): “deal tickets should be created and entered into sitara based on the following information:”
- `farmer-d/logistics/1001` (line 31, 2000-04-03, tom.acton@enron.com): “I recently received this nomination and the total package of gas for the aforementioned changed as follows:”
- `farmer-d/logistics/1054` (line 17, 2000-04-19, ami.chokshi@enron.com): “My est. for Tufco is the same as last May's (1999) nom.”
- `farmer-d/logistics/1063` (line 23, 2000-04-20, ami.chokshi@enron.com): “Does this average represent a good estimate of the Calpine May nom?”
- `farmer-d/logistics/1053` (line 21, 2000-04-19, ami.chokshi@enron.com): “These are my estimates. The volumes for April at T-ville and Colorado RS are either spot or April only.”
- `farmer-d/logistics/1137` (line 17, 2000-05-24, ami.chokshi@enron.com): “i put in 35000 for the expected volume for the sale to SDS/TUFCO.”
- `farmer-d/logistics/1163` (line 27, 2000-05-31, robert.cotten@enron.com): “Will you approve revising the volume in Unify down to 2,300?  Please advise.  Thanks.”
- `farmer-d/logistics/1161` (line 19, 2000-05-31, robert.cotten@enron.com): “We have received a revised nomination as follows:”
- `farmer-d/logistics/1169` (line 20, 2000-06-02, robert.cotten@enron.com): “The C/P is Costilla Energy and the deal # is 125783.  Do you want me to adjust?  Please advise.”
- `farmer-d/logistics/1166` (line 17, 2000-06-01, aimee.lannou@enron.com): “Is there a reason there is a nom of 20.000/day at meter 385?  This is a non-allocatable meter.”
- `farmer-d/logistics/1151` (line 29, 2000-05-26, tom.acton@enron.com): “a nom change from 3,300 to 2,400 mmbtu/d at HPL Meter 98-6296 delivery @ HPL Thompsonville”
- `farmer-d/logistics/1239` (line 19, 2000-06-23, robert.cotten@enron.com): “Prize Energy revised their nom eff. 6/26 through 6/29 for the following meters:”
- `farmer-d/logistics/1239` (line 26, 2000-06-23, robert.cotten@enron.com): “Please advise if you want me to adjust.”
- `farmer-d/logistics/1242` (line 23, 2000-06-26, michael.mitcham@enron.com): “Enron Methanol nominates the following natural gas requirements for the Methanol Plant for July 2000:”
- `farmer-d/logistics/1245` (line 5, 2000-06-27, rickya@calpine.com): “Calpine Daily Gas Nomination and Monthly (JULY) Nomination”
- `farmer-d/logistics/1367` (line 23, 2000-08-25, michael.mitcham@enron.com): “Enron Methanol nominates the following natural gas requirements for the Methanol Plant for September 2000:”
- `farmer-d/logistics/1368` (line 32, 2000-08-25, lee.papayoti@enron.com): “So, I added 5,000 for September (#139057 @ GD) in addition to the 34,000 they nom'd.”
- `farmer-d/logistics/1370` (line 5, 2000-08-28, rickya@calpine.com): “Calpine Daily and Monthly Gas Nomination”
- `farmer-d/logistics/1504` (line 53, 2000-11-09, tom.acton@enron.com): “Please accept this transmission as nomination for gas flow on Southland Pipeline (Now Desoto Pipeline)”
- `farmer-d/logistics/1539` (line 21, 2000-11-27, rickya@calpine.com): “Aimee, I am still waiting on a transport number from lori Allen in your”
- `farmer-d/logistics/1532` (line 21, 2000-11-21, mary.johnson@enron.com): “Well- I have officially NOT heard from Hilcorp after numerous voice and email”
- `farmer-d/logistics/1530` (line 31, 2000-11-20, mary.johnson@enron.com): “If we don't hear by 4pm, we are supposed to bypass the gas...........”
- `farmer-d/logistics/2063` (line 45, 2001-01-31, aimee.lannou@enron.com): “Can I change the tickets or will you?  Attached is the confirmation spreadsheet from Valero.”
- `farmer-d/logistics/2043` (line 19, 2001-01-12, edward.terry@enron.com): “A suggestion was made (by Carlos) to centralize transport nominations we receive by email.”
- `farmer-d/logistics/2043` (line 25, 2001-01-12, edward.terry@enron.com): “If the file is still in the "inbox", it has not been addressed.”
- `farmer-d/logistics/2028` (line 24, 2001-01-03, sabrae.zajac@enron.com): “She has informed me that for this time period there should be no nominations at these points.”
- `farmer-d/logistics/193` (line 28, 2001-04-05, mjones7@txu.com): “As soon as we get a e-mail from Duke I will send it to you.”
- `farmer-d/logistics/152` (line 19, 2001-04-30, juliann.kemp@enron.com): “Can you give me deal numbers so I can confirm it.”
- `farmer-d/logistics/150` (line 17, 2001-05-01, juliann.kemp@enron.com): “What would you like to do with the two day outage on May 8th and 9th.”
- `farmer-d/logistics/158` (line 19, 2001-04-26, mary.poorman@enron.com): “FYI, check the purchase from Swift at the Tailgate (Meter 9643) and make sure to nom the correct quantity.”
- `farmer-d/logistics/180` (line 26, 2001-04-16, mark.mccoy@enron.com): “Notified by gas control that the Freeport delivery to Dow was increased to 10.0.”
- `farmer-d/logistics/148` (line 17, 2001-05-07, tom.acton@enron.com): “I need  deal ticket 745546 extended on both ends.   4/23 for flow of 35 and 5/1/ for flow of 132.”
- `farmer-d/logistics/131` (line 17, 2001-05-23, craig.breslau@enron.com): “Could we please make the appropriate nomination change and also let me know how we plan to price the buyback.”
- `farmer-d/logistics/121` (line 17, 2001-05-30, david.baumbach@enron.com): “I rolled 740208, 740209,740210 and 740235 into June.”
- `farmer-d/logistics/120` (line 18, 2001-06-01, rebecca.griffin@enron.com): “I want to confirm the May MidCon volumes for Mobil - I think it is 30,000 mmbtu/day?”

## 11. Daily P&L, DPR, officialization and origination checks

Each night the risk book owners run the calc and officialize every post id and basis position. They email the daily P&L and DPR with notes on held-back amounts and UA4, and they send Schedule C add or release notes to credit. They also reconcile origination granted against origination recognised by book. Darron Giron drives most of this for the gas desks, forwarding macros and reminders to his analysts and answering variance emails from P&L analysts. Missed books end up on a daily exception list that goes to senior management.

- **Who touches it:** bryan.hull@enron.com, darron.giron@enron.com
- **How often:** 3.92 occurrences/month (51 dated messages over 13 active months, 2000-03-07 → 2001-03-28)
- **Where it stalls:** Officializing depends on an admin remembering to do it, and the benchmark check misses books with no net position. Reports go out with the wrong or a missing attachment. Origination grants arrive late, so the same variance is reported again. The calc depends on the system being up. Protected DPR copies have to be re-requested.
- **Automation:** A nightly scheduled job that verifies every book and post id is officialized, including zero-position ones, and emails exceptions to each controller. After the calc, it would generate and distribute the daily P&L, DPR and Schedule C amounts automatically, and an automatic origination granted-versus-recognised comparison would flag only residual differences.
- **Estimate:** 20 min/occurrence × 50% automatable → 0.65 h/month → **$56/month**
- **Why that estimate:** Observer estimates range from 5 to 40 minutes with a median of 20 minutes per daily cycle. Checking, generation and distribution are mechanical, while explaining unusual P&L is not, so the fraction is set at the 0.5 median.

**Evidence**

- `giron-d/sent/703` (line 17, 2000-08-21, darron.giron@enron.com): “I held back $1,087,409 from the MEH book.”
- `giron-d/sent/694` (line 17, 2000-08-23, darron.giron@enron.com): “after I put in the deals, the system went down and I was not able to get them to calc.”
- `giron-d/sent/375` (line 17, 2000-12-21, darron.giron@enron.com): “The P&L is attached.  The total daily is $471,793 before any sharing.”
- `farmer-d/logistics/888` (line 17, 2000-03-07, bryan.hull@enron.com): “we attached both a consolidated p&l and an updated prudency schedule.”
- `giron-d/sent/765` (line 32, 2000-06-16, darron.giron@enron.com): “IM CENTRAL failed to recognize 468 (dollars) of the 9,488 that were granted to them by FT-Central on 06/15”
- `giron-d/sent/763` (line 27, 2000-06-19, darron.giron@enron.com): “you recognized 3.975 (thousand) of orig, and I did not see that coming out of any book. Could you let me know who granted that.”
- `giron-d/sent/762` (line 34, 2000-06-19, darron.giron@enron.com): “Can you update for transport?  Sitara #131389 (North Shore) and #131405 (Peoples).”
- `giron-d/sent/739` (line 20, 2000-07-18, darron.giron@enron.com): “Currently attached is the P&L that was signed off on last night.”
- `giron-d/sent/745` (line 19, 2000-07-10, darron.giron@enron.com): “Here is Agave for June.  I also made a change to May.”
- `giron-d/sent/722` (line 35, 2000-07-31, darron.giron@enron.com): “There is still a remaining difference of  771.00 dollars that IM Central  and/ or  Chicago have not recognized on their P&L.”
- `giron-d/sent/695` (line 33, 2000-08-23, darron.giron@enron.com): “Intracentral recognized $11,812 origination on their P&L that was not granted on the origination schedule.”
- `giron-d/sent/677` (line 33, 2000-08-29, darron.giron@enron.com): “Central origination claimed $750 more than what was granted to them.”
- `giron-d/sent/675` (line 19, 2000-08-30, darron.giron@enron.com): “Did you grant the $750 in orig from the ticket I gave you yesterday?”
- `giron-d/sent/691` (line 19, 2000-08-23, darron.giron@enron.com): “But the copies we receive have some sort of protection which I'm sure you are aware of.”
- `giron-d/sent/666` (line 17, 2000-09-06, darron.giron@enron.com): “Will you please send Richard Tomaski a version of yesterday's DPR that can be printed or forwarded.”
- `giron-d/sent/651` (line 20, 2000-09-14, darron.giron@enron.com): “He sent me a spreadsheet with deals but I cannot even come close to tying them out to what we have booked in Tagg.”
- `giron-d/sent/640` (line 22, 2000-09-20, darron.giron@enron.com): “I think the best thing to do is to simply start over and book the deals you tell me to.”
- `giron-d/sent/631` (line 45, 2000-09-27, darron.giron@enron.com): “Again this month, you are going to have to calculate your basis positions (officialize) twice.”
- `giron-d/sent/595` (line 24, 2000-10-16, darron.giron@enron.com): “If a postid has a net position and is not officialized, it will be caught using this procedure.”
- `giron-d/sent/586` (line 18, 2000-10-17, darron.giron@enron.com): “Please make sure we stay off the "list".  Thanks.”
- `giron-d/sent/596` (line 29, 2000-10-13, darron.giron@enron.com): “I would like each of your book admins using WeaponX to begin using the following procedures at least once/week”
- `giron-d/sent/582` (line 19, 2000-10-17, darron.giron@enron.com): “Use it to make sure all your postid's that need to be, are officialized each night.”
- `giron-d/sent/533` (line 19, 2000-11-02, darron.giron@enron.com): “we need to have the last person finished do it every day.”
- `giron-d/sent/533` (line 44, 2000-11-02, darron.giron@enron.com): “All regional controllers will receive a sheet at the end of the night, verifying that all books are officialized.”
- `giron-d/sent/580` (line 34, 2000-10-17, darron.giron@enron.com): “This one requires a comment in all post-id's to pull in only those.”
- `giron-d/sent/478` (line 18, 2000-11-16, darron.giron@enron.com): “I show a net open position of (15.9) contracts.”
- `giron-d/sent/476` (line 17, 2000-11-17, darron.giron@enron.com): “P&L is OK.  Open position is 39.0 contracts.”
- `giron-d/sent/442` (line 32, 2000-11-30, darron.giron@enron.com): “On the Benchmark, these traders basis positions were not rolled off.”
- `giron-d/sent/430` (line 31, 2000-12-04, darron.giron@enron.com): “Has everyone flashed?  Nagesh is waiting for me to give him the O.K. to create the CPR detail file that OA imports into their database.”
- `giron-d/sent/436` (line 50, 2000-11-30, darron.giron@enron.com): “Please plan on adjusting your PL for the following amount during the month of November...”
- `giron-d/sent/399` (line 17, 2000-12-12, darron.giron@enron.com): “We released $75M tonight.”
- `giron-d/sent/200` (line 18, 2001-02-23, darron.giron@enron.com): “We are taking $100M to Schedule C tonight.  I don't know when it may be released.”
- `giron-d/sent/191` (line 17, 2001-02-26, darron.giron@enron.com): “We are removing the $100M from Schedule C that was put there on Friday.”
- `giron-d/sent/109` (line 17, 2001-03-28, darron.giron@enron.com): “We added $75M so Schedule C tonight.”
- `giron-d/sent/374` (line 17, 2000-12-22, darron.giron@enron.com): “It would help if I attached the file.”
- `giron-d/sent/420` (line 31, 2000-12-06, darron.giron@enron.com): “we have not received the P&L top pages or curve shift reports for the following regions:  West Firm, FT Northwest and Mgmt. West.”
- `giron-d/sent/376` (line 5, 2000-12-21, darron.giron@enron.com): “12/21 Curves”
- `giron-d/sent/369` (line 19, 2000-12-26, darron.giron@enron.com): “The Central desk has the other side of the transaction and if I backed your portion out, then the loss would be double counted.”

## 12. Recurring hand-built operational report distribution

Several staff rebuild the same recurring report by hand and email it to a fixed list: Kimberly Vaughn's HL&P month-to-date flow spreadsheet, monthly storage and industrial reports, Michelle Lokay's Friday Transwestern California capacity report with Gas Daily prices, and the daily Energy Market Report and Gas and Power Daily PDFs. The figures are pulled from source systems and typed into an identical template each time. Recipient lists are kept by hand.

- **Who touches it:** bill.williams@enron.com, elizabeth.brown@enron.com, janet.wallis@enron.com, jill.chatterton@enron.com, kenneth.seaman@enron.com, kimberly.vaughn@enron.com, lisa.kinsey@enron.com, michelle.lokay@enron.com, rita.bianchi@enron.com, robert.lloyd@enron.com, theresa.villeggiante@enron.com
- **How often:** 1.71 occurrences/month (48 dated messages over 28 active months, 1999-12-21 → 2002-03-22)
- **Where it stalls:** Numbers are compiled and typed by hand every cycle, so late data delays the report. Files are requested from another person each time. Reports are resent with the wrong label or a missing attachment, and distribution list changes are handled by email.
- **Automation:** Scheduled report jobs that pull flow, throughput, delivery and price data from the source systems into the standard template, compute derived figures such as shortfalls against tolerance and utilisation, and email a maintained subscription list automatically when the data is published. This replaces manual compilation and forwarding.
- **Estimate:** 35 min/occurrence × 65% automatable → 0.65 h/month → **$55/month**
- **Why that estimate:** Observer estimates range from 10 minutes for forwarding to 45 minutes for compiling, with a median of about 35 minutes. Most reports follow a fixed template from system data, so the fraction is set high at the 0.65 median.

**Evidence**

- `farmer-d/logistics/603` (line 29, 1999-12-21, kimberly.vaughn@enron.com): “I have updated the HL&P flow MTD.   Jill told me that on the 18th,19 th and 20th the San Jac. nom  should be 29,209.”
- `farmer-d/logistics/644` (line 19, 2000-01-04, kimberly.vaughn@enron.com): “Attached is the best available for December.  I have split 3rd party noms and HPL noms.”
- `farmer-d/logistics/683` (line 21, 2000-01-12, janet.wallis@enron.com): “It is the pipelines decision on how to allocate between the shippers, however, If the pipeline allocates the shortage to ENA then we need to follow”
- `farmer-d/logistics/760` (line 19, 2000-02-07, kimberly.vaughn@enron.com): “Attached are the month to date flow volumes.”
- `farmer-d/logistics/821` (line 19, 2000-02-22, kimberly.vaughn@enron.com): “I have updated the flow volumes for HL&P”
- `farmer-d/logistics/852` (line 19, 2000-02-28, robert.lloyd@enron.com): “Can you please forward me the "Buyback/Deficiency"  Deals  for March' 2000.”
- `farmer-d/logistics/742` (line 20, 2000-02-02, lisa.kinsey@enron.com): “Attached is the worksheet showing your withdrawals for the month of January”
- `lokay-m/inbox/10` (line 22, 2001-10-26, michelle.lokay@enron.com): “Transwestern's average deliveries to California were 945 MMBtu/d (87%), with San Juan lateral throughput at 865 MMBtu/d.”
- `lokay-m/inbox/8` (line 34, 2001-10-29, elizabeth.brown@enron.com): “Please post the attached TW rate matrix, MATRIX200111.doc, effective 11/1/2001.”
- `lokay-m/inbox/7` (line 26, 2001-10-29, rita.bianchi@enron.com): “There is a new tab for each change in Current Shipper Rates.”
- `lokay-m/sent_items/18` (line 23, 2001-12-14, michelle.lokay@enron.com): “Transwestern's average deliveries to California were 1122 MMBtu/d (103%), with San Juan lateral throughput at 844 MMBtu/d.”
- `lokay-m/sent_items/67` (line 24, 2001-12-21, michelle.lokay@enron.com): “Transwestern's average deliveries to California were 1059 MMBtu/d (97%), with San Juan lateral throughput at 839 MMBtu/d.”
- `lokay-m/sent_items/63` (line 23, 2001-12-28, michelle.lokay@enron.com): “Transwestern's average deliveries to California were 959 MMBtu/d (88%), with San Juan lateral throughput at 827 MMBtu/d.”
- `lokay-m/sent_items/55` (line 23, 2002-01-04, michelle.lokay@enron.com): “Transwestern's average deliveries to California were 840 MMBtu/d (77%), with San Juan lateral throughput at 829 MMBtu/d.”
- `lokay-m/sent_items/46` (line 23, 2002-01-11, michelle.lokay@enron.com): “Sorry, the effective date for this new report is 01/07-01/11.”
- `lokay-m/sent_items/40` (line 8, 2002-01-18, michelle.lokay@enron.com): “California Capacity Report for Week of 01/14-01/18”
- `lokay-m/sent_items/30` (line 23, 2002-01-24, michelle.lokay@enron.com): “Transwestern's average deliveries to California were 933 MMBtu/d (86%), with San Juan lateral throughput at 864 MMBtu/d.”
- `lokay-m/sent_items/30` (line 8, 2002-01-24, michelle.lokay@enron.com): “California Capacity Report for Week of 01/21-01/25”
- `lokay-m/sent_items/35` (line 17, 2002-01-22, michelle.lokay@enron.com): “Due today at 5:00...hope you guys bid!”
- `lokay-m/sent_items/34` (line 17, 2002-01-22, michelle.lokay@enron.com): “Bids are due today at 5:00...hope you guys bid!”
- `williams-w3/inbox/62` (line 10, 2002-01-31, jill.chatterton@enron.com): “FW: Energy Market Report - 01/30/02”
- `williams-w3/sent_items/7` (line 19, 2002-01-31, bill.williams@enron.com): “Could you add DL-Portland Shift to this distribution. I would like the guys in Real-Time to be able to see this information when they come in.”
- `williams-w3/inbox/50` (line 32, 2002-02-04, theresa.villeggiante@enron.com): “They do not have Gas daily loaded yet, I will check back periodically, if and when it becomes available I will send it.”
- `williams-w3/inbox/67` (line 17, 2002-01-31, theresa.villeggiante@enron.com): “No problem, is it possible for you to give me a list of names as I am not sure who does what just yet.”
- `lokay-m/sent_items/86` (line 23, 2002-02-08, michelle.lokay@enron.com): “Transwestern's average deliveries to California were 1011 MMBtu/d (93%), with San Juan lateral throughput at 872 MMBtu/d.”
- `lokay-m/sent_items/110` (line 25, 2002-02-22, michelle.lokay@enron.com): “El Paso's average deliveries to California were 2063 MMBtu/d (70%):”
- `lokay-m/sent_items/117` (line 23, 2002-03-01, michelle.lokay@enron.com): “Transwestern's average deliveries to California were 815 MMBtu/d (75%), with San Juan lateral throughput at 879 MMBtu/d.”

## 13. Gas Sitara deal entry, transport and buyback ticket setup requests

Producer Services, traders, settlements and logistics email the gas desk (Tom Acton, Daren Farmer, schedulers) to key new spot or well deals into Sitara. Other requests ask to add meters or change points on existing deals, set up monthly transport usage and buyback or swing tickets for industrial customers, book processing-plant deals, or enter one-off sales such as storage. Each request is free text that someone re-types into Sitara, POPS or Unify before replying with the ticket number or a change notice. Rates are kept in both Unify and Sitara and have to be checked by hand each month.

- **Who touches it:** antoinette.beale@enron.com, brenda.herod@enron.com, bryce.baxter@enron.com, buddy.majorwitz@enron.com, carlos.rodriguez@enron.com, clem.cernosek@enron.com, d..winfree@enron.com, david.baumbach@enron.com, edward.gottlob@enron.com, f..smith@enron.com, fred.boas@enron.com, gary.lamphier@enron.com
- **How often:** 3.4 occurrences/month (85 dated messages over 25 active months, 1999-12-16 → 2001-12-12)
- **Where it stalls:** Details are re-typed from email, and errors such as a wrong price or missing deal number need a second email. Requesters do not know who owns a deal or has access, so mails bounce between intermediaries. Inactive counterparties or contracts block entry for weeks. Change notices are followed by several correction emails. Transport rates live in two systems and are corrected twice.
- **Automation:** A structured deal-request form and queue that validates counterparty, meter, contract status, price and dates, then writes the Sitara ticket draft for one-click approval and returns the ticket number automatically. Monthly transport usage, buyback and swing tickets would roll forward from the prior month, with only rate changes flagged against the rate matrix and Unify. Change notices would be generated from the deal-change log.
- **Estimate:** 30 min/occurrence × 35% automatable → 0.59 h/month → **$51/month**
- **Why that estimate:** Observer estimates range from 8 to 60 minutes with a median of 30 minutes, reflecting multi-party back-and-forth. Validation and ticket drafting can be automated, but many requests carry pricing or commercial judgement, so the fraction is set at the 0.35 median.

**Evidence**

- `farmer-d/logistics/1253` (line 20, 2000-06-29, pat.clynes@enron.com): “Please make sure that Gary gets a copy of the Industrial spreadsheet.”
- `farmer-d/logistics/662` (line 19, 2000-01-10, kenneth.seaman@enron.com): “Each meter is now to be treated seperately: Tickets have been created accordingly.”
- `farmer-d/logistics/645` (line 19, 2000-01-04, kenneth.seaman@enron.com): “Attached are the current buyback deals I'm aware of. If you have further information please let me know.”
- `farmer-d/logistics/702` (line 20, 2000-01-21, kenneth.seaman@enron.com): “Please let us know how the economics should be handled---- buyback, force majure, no deal, or what.”
- `farmer-d/logistics/706` (line 23, 2000-01-21, vance.taylor@enron.com): “Please create a spot ticket for gas that commence flowing on 1/14/00 at 8:30”
- `farmer-d/logistics/707` (line 23, 2000-01-21, vance.taylor@enron.com): “Oooops!  How about 100% IF/HSC LESS $0.10”
- `farmer-d/logistics/777` (line 23, 2000-02-09, tom.acton@enron.com): “The new Sitara ticket # is 165331”
- `farmer-d/logistics/789` (line 29, 2000-02-14, susan.smith@enron.com): “Please supply the sitara number once entered.  If you have any questions, please give me a call.”
- `farmer-d/logistics/857` (line 55, 2000-02-29, tom.acton@enron.com): “Just send me a lotus note with all the info that I will need,  then I can put”
- `farmer-d/logistics/867` (line 35, 2000-03-02, mary.smith@enron.com): “Right now we have not entered in or corrected rates in their transport usage tickets.”
- `farmer-d/logistics/874` (line 19, 2000-03-03, heidi.withers@enron.com): “I have a lot of PMA's for 1999 related to rates missing or incorrect.”
- `farmer-d/logistics/972` (line 20, 2000-03-28, sherlyn.schumack@enron.com): “I have provided Stacey with the daily allocation from PG&E Texas.”
- `farmer-d/logistics/958` (line 30, 2000-03-24, stacey.neuweiler@enron.com): “Please be advised that Contract No. Teco9121 shows in the Global Contract system as PG&E Texas Pipeline, L.P.”
- `farmer-d/logistics/1082` (line 22, 2000-05-01, kenny.soignet@enron.com): “Daren- Please enter Texas purchase from Cannon Interest and a Texas sale to the Storage Book in the sitara.”
- `farmer-d/logistics/1114` (line 20, 2000-05-17, stephanie.gomes@enron.com): “I see that the volume has not been scheduled, so therefore it is not pulling into unify for me to pay.”
- `farmer-d/logistics/1093` (line 21, 2000-05-08, torrey.moorer@enron.com): “I also wanted to let you have an electronic copy of the failed deals which need to be booked into SITARA.”
- `farmer-d/logistics/1136` (line 17, 2000-05-23, brenda.herod@enron.com): “Please make sure this is clearly understood by the schedulers.”
- `farmer-d/logistics/1019` (line 23, 2000-04-06, tom.acton@enron.com): “The ticket is in and the deal number is 237756. It doesn't seem to want to flow over to mops at the moment though.”
- `farmer-d/logistics/1257` (line 19, 2000-06-30, heidi.withers@enron.com): “I have input and updated transport usage tickets for July.”
- `farmer-d/logistics/1304` (line 58, 2000-07-25, lee.papayoti@enron.com): “Equistar invoice can not be drafted without this deal ticket.”
- `farmer-d/logistics/1317` (line 22, 2000-08-02, robert.lloyd@enron.com): “Will there be a Buyback ticket for Formosa during August 2000 activity.”
- `farmer-d/logistics/1275` (line 23, 2000-07-12, fred.boas@enron.com): “Please put the HPLC 012-41500-02-013 transport contract in POPS at meter 980692 for June 2000”
- `farmer-d/logistics/1514` (line 21, 2000-11-14, mary.poorman@enron.com): “I need HPL Sales and Purchases, back dated to 8/99 between HPL and TECO to book any processing revenue or losses.”
- `farmer-d/logistics/1518` (line 23, 2000-11-15, clem.cernosek@enron.com): “Deal #487040 has been setup with demand charge equally to the amounts that Teco paid HPL at Indian Spring for the following months:”
- `farmer-d/logistics/1534` (line 19, 2000-11-21, mary.poorman@enron.com): “HPL has elected to be kept whole with respect to processing during the month of December 2000 on its gas delivered from the Three Rivers Gathering System.”
- `farmer-d/logistics/1540` (line 19, 2000-11-28, edward.gottlob@enron.com): “Mary provided this to Brian, please check against your numbers ASAP”
- `farmer-d/logistics/2072` (line 17, 2001-02-01, mark.mccoy@enron.com): “I changed points on this deal from PGTT-TECO Waha 18002800 to PGTT-TECO”
- `farmer-d/logistics/2073` (line 17, 2001-02-01, mark.mccoy@enron.com): “OOOPS!   This is effective the 1st.”
- `farmer-d/logistics/2074` (line 17, 2001-02-01, mark.mccoy@enron.com): “Oh yeah, and that goes for deal 594596 Crosstex , also.”
- `farmer-d/logistics/2085` (line 23, 2001-02-20, mark.mccoy@enron.com): “So I went ahead and changed the AEC ticket to match up with the Aquila deal.”
- `farmer-d/logistics/103` (line 39, 2001-06-28, d..winfree@enron.com): “Let me know if you have any objections to me entering the deals”
- `farmer-d/logistics/100` (line 29, 2001-07-09, michael.olsen@enron.com): “I looked in Sitara and deal 70550 is still not released.”
- `farmer-d/logistics/98` (line 22, 2001-07-13, tnray@aep.com): “there is no sales draft in Unify for this sale.”
- `farmer-d/logistics/95` (line 17, 2001-07-20, megan.parker@enron.com): “I have not heard back from Mike Olsen on this. Can you extend this deal for me?”
- `farmer-d/logistics/96` (line 32, 2001-07-19, megan.parker@enron.com): “Can you verify how this deal should be priced?”
- `farmer-d/logistics/94` (line 17, 2001-07-23, megan.parker@enron.com): “We need to add TGPL meter 52-1087 to deal 895951.  We have some swing gas for May that we need to allocate.”
- `farmer-d/logistics/91` (line 18, 2001-07-27, megan.parker@enron.com): “I have a price issue with MGI Supply for January 2001.”
- `farmer-d/logistics/78` (line 19, 2001-08-14, valerie.vela@enron.com): “On day 18, did you intentionally enter 50,000 days or was it a slip of the fingers?”
- `farmer-d/logistics/86` (line 35, 2001-08-02, antoinette.beale@enron.com): “I input the purchase and sale deals that were not in the system.”
- `farmer-d/logistics/43` (line 27, 2001-10-16, stephen.swisher@enron.com): “If you need a copy of the statement, let me know.”
- `farmer-d/logistics/40` (line 32, 2001-10-19, richard.deming@enron.com): “Each has a relatively recent deal booked to it that need to be changed as described above”
- `farmer-d/logistics/39` (line 28, 2001-10-23, rita.wynne@enron.com): “this meter needs to be set up for May 2001 just as it was for April 2001.”
- `farmer-d/logistics/33` (line 21, 2001-10-30, buddy.majorwitz@enron.com): “Please set up a valid deal for March 2000 just like either one of these deals”
- `farmer-d/logistics/38` (line 28, 2001-10-23, michael.olsen@enron.com): “Please be advised that we have discrepancies with the  State and County information for the meter No. (s) listed on the attached spreadsheet.”
- `farmer-d/logistics/14` (line 27, 2001-11-30, michael.olsen@enron.com): “I need a deal entered into Sitra and pathed for the sale of the Centana Storage to AEP.”
- `farmer-d/logistics/12` (line 21, 2001-12-11, rita.wynne@enron.com): “Have the two of you been able to get the deal in for the sale of the Centana storage to AEP?”
- `farmer-d/logistics/11` (line 19, 2001-12-11, stephen.swisher@enron.com): “I am going to have them activate the old contracts so that Mike can finish pathing.”
- `farmer-d/logistics/9` (line 19, 2001-12-12, stephen.swisher@enron.com): “The deals have been pathed and I have just actualized and balanced them.”

## 14. System access, IT and directory requests

Staff request application access, trader IDs, book calc and print rights, TDS approvers, shared ISO logins, equipment, turrets and phones through email or the SRRS ticket system, then follow up when access is partial. During the UBS and Netco transition, IT and desk leads also chased each user for access methods and estate-account exceptions and coordinated database outages. A separate recurring irritant is the name collision between Bill Williams and Bill Williams III, which misroutes mail and access requests that then have to be forwarded and corrected.

- **Who touches it:** arsystem@ect.enron.com, arsystem@mailman.enron.com, bill.williams@enron.com, chris.mallory@enron.com, claudia.clark@enron.com, d..winfree@enron.com, dalton.hogan@enron.com, daniel.diamond@enron.com, darron.giron@enron.com, david.steiner@enron.com, information.management@enron.com, infrastructure.ubsw@enron.com
- **How often:** 4.21 occurrences/month (80 dated messages over 19 active months, 2000-08-16 → 2002-02-06)
- **Where it stalls:** Requests wait on approvers who are not the right ones. Grants arrive partially and need a second request. Each request triggers several automated emails that must be opened. Users do not answer surveys until chased. Shared credentials circulate by email. Senders keep choosing the wrong Bill Williams, so the same correction is repeated.
- **Automation:** A single access-request workflow with role-based access bundles, automatic routing to the correct data approver, status tracking and reminders, plus a managed credential store for shared logins. Directory aliases and distribution-list fixes would resolve the name collision once instead of message by message.
- **Estimate:** 15 min/occurrence × 50% automatable → 0.53 h/month → **$45/month**
- **Why that estimate:** Observer estimates range from 4 to 30 minutes with a median of 15 minutes per request including follow-ups. Routing and tracking are largely mechanical, so the fraction is set at the 0.5 median.

**Evidence**

- `farmer-d/logistics/1339` (line 31, 2000-08-16, yvette.connevey@enron.com): “You will be notified via eMail when your request has been processed.”
- `farmer-d/logistics/1407` (line 17, 2000-09-14, arsystem@ect.enron.com): “Please review and act upon this request. You have received this email because the requester specified you as their Manager.”
- `farmer-d/logistics/1361` (line 17, 2000-08-23, information.management@enron.com): “Additional Information for Security Resource Request  DJFR-4NGPA6 has been provided by Security.”
- `giron-d/sent/532` (line 19, 2000-11-02, darron.giron@enron.com): “I don't have access to run this book.  Will you please get me authorization?  Thanks.”
- `giron-d/sent/520` (line 18, 2000-11-07, darron.giron@enron.com): “I can calc postids for FT-NW but cannot print.  Please help.  Thanks.”
- `giron-d/sent/568` (line 18, 2000-10-20, darron.giron@enron.com): “I need to have access to calc all books on a minibook level.”
- `giron-d/sent/541` (line 17, 2000-10-31, darron.giron@enron.com): “Please add Carole Frank to the list.  Her NT username is cfrank2.”
- `giron-d/sent/573` (line 19, 2000-10-19, darron.giron@enron.com): “Please add them to Tagg.  Call me if you have any questions.”
- `williams-w3/sent_items/507` (line 18, 2001-06-12, bill.williams@enron.com): “Just want to make sure you have me as Bill Williams III.”
- `williams-w3/sent_items/492` (line 18, 2001-06-18, bill.williams@enron.com): “My address is Bill Williams III, Please make the correction.”
- `williams-w3/sent_items/489` (line 17, 2001-06-19, bill.williams@enron.com): “Please add Ainsley Gaddis and remove Daniel Kang from your list when sending the spreadsheets to EES.”
- `williams-w3/sent_items/468` (line 18, 2001-06-25, bill.williams@enron.com): “You must change your e-mail list for Bill Williams.  Please send this to bill.williams@enron.com.”
- `williams-w3/sent_items/448` (line 20, 2001-07-02, bill.williams@enron.com): “This needs to go to Bill Williams, not Bill Williams III.”
- `williams-w3/sent_items/437` (line 21, 2001-07-03, bill.williams@enron.com): “Please make the appropriate change to your address book.”
- `williams-w3/sent_items/429` (line 21, 2001-07-05, bill.williams@enron.com): “Please make the change in your address book.”
- `williams-w3/sent_items/450` (line 18, 2001-07-02, bill.williams@enron.com): “Try to make sure you get these to me rather than to my Dad.”
- `williams-w3/sent_items/350` (line 28, 2001-07-30, bill.williams@enron.com): “I received a message from Todd Bland over the weekend saying he is still unable to save deals using his own name.”
- `williams-w3/sent_items/323` (line 19, 2001-08-07, bill.williams@enron.com): “I would like only the members of the real-time group to have access.”
- `williams-w3/sent_items/368` (line 38, 2001-07-24, bill.williams@enron.com): “FYI- security requests are averaging 14 business days.”
- `farmer-d/logistics/87` (line 17, 2001-07-31, arsystem@mailman.enron.com): “You have received this email because you are listed as a data approver.”
- `williams-w3/sent_items/284` (line 18, 2001-08-27, bill.williams@enron.com): “We need to get a third turret in the mix at RT.”
- `williams-w3/sent_items/258` (line 18, 2001-09-12, bill.williams@enron.com): “Any word from PGE regarding a phone for Kate?”
- `farmer-d/logistics/65` (line 20, 2001-09-07, tommy.garza@enron.com): “I'm working on the PC you requested.  Can you provide me with the following information so I can start imaging your pc:”
- `williams-w3/sent_items/249` (line 19, 2001-09-14, bill.williams@enron.com): “I would like to cap per employee costs at $50 per month on the group calling plan.”
- `williams-w3/sent_items/213` (line 20, 2001-09-25, bill.williams@enron.com): “I think you intended to send this to Bill Williams in Technical Assets. Please note the difference in addresses and make the change.”
- `williams-w3/sent_items/184` (line 20, 2001-10-09, bill.williams@enron.com): “Please update your email list to read Bill Williams and not Bill Williams III.”
- `williams-w3/sent_items/243` (line 21, 2001-09-14, bill.williams@enron.com): “Please remove my name from whatever list you might have. I work in Portland and am not involved with security clearance or security access.”
- `williams-w3/sent_items/241` (line 22, 2001-09-15, bill.williams@enron.com): “I am not involved with security, in Houston or otherwise, and can not help you obtain a security badge.”
- `williams-w3/sent_items/70` (line 17, 2001-11-28, bill.williams@enron.com): “I do need those folks to have access”
- `williams-w3/sent_items/70` (line 45, 2001-11-28, bill.williams@enron.com): “Mike, I am not the approver for these rights.  Try Bill Williams.”
- `williams-w3/inbox/135` (line 21, 2001-12-08, chris.mallory@enron.com): “This New login, SC ID and password will take effect for scheduling Tuesday the 11th.”
- `williams-w3/sent_items/52` (line 20, 2001-12-11, bill.williams@enron.com): “I would like to request a password change for the following EPMI logins.”
- `williams-w3/sent_items/29` (line 32, 2002-01-09, bill.williams@enron.com): “The DBAs for the EnPower database want to take it down from 4 PM Friday afternoon”
- `williams-w3/inbox/110` (line 21, 2002-01-10, susan.amador@enron.com): “You must re-boot your machines following this shut down to access any EnPower applications.”
- `williams-w3/sent_items/24` (line 28, 2002-01-11, bill.williams@enron.com): “Please enter a few test deals on Saturday after the databases are brought back up.”
- `giron-d/inbox/114` (line 26, 2002-01-22, kam.keiser@enron.com): “I still need a list of people who need Netco Sitara access for the East and Central Regions.”
- `giron-d/inbox/50` (line 20, 2002-01-30, d..winfree@enron.com): “you may need to edit your Copy Physical Macro in your P&L's that are saved in the Netco/Regions folder”
- `giron-d/inbox/49` (line 18, 2002-01-30, kam.keiser@enron.com): “all physical weapon-X tabs are linking to an old east book.  I didn't touch that tab yet”
- `giron-d/inbox/66` (line 30, 2002-01-28, s..shively@enron.com): “Send me a final list of who will be trading on your desk.  Thanks.”
- `williams-w3/inbox/56` (line 28, 2002-02-01, daniel.diamond@enron.com): “If you're receiving this email its because we're still waiting on a response from you.  Please reply to this message ASAP.”
- `williams-w3/inbox/71` (line 30, 2002-01-31, daniel.diamond@enron.com): “Please reply to this message with either a corresponding "1" or a "2" in the subject field.”
- `giron-d/inbox/32` (line 20, 2002-02-01, russ.severson@enron.com): “The curve files for Netco will need to be modified before they are used in the new environment.”
- `giron-d/inbox/38` (line 17, 2002-01-31, arsystem@mailman.enron.com): “You have received this email because you are listed as a data approver.”
- `giron-d/inbox/12` (line 20, 2002-02-06, kam.keiser@enron.com): “There is a new directory for the curve files.  I am trying to request access to this for the traders so they can't see the rest of our files.”
- `williams-w3/inbox/21` (line 19, 2002-02-06, david.steiner@enron.com): “I need to know now who will need an exception to this. ASAP.”
- `williams-w3/inbox/18` (line 20, 2002-02-06, david.steiner@enron.com): “What do we need to do to make sure these accounts stay active past Sunday?”
- `giron-d/inbox/4` (line 19, 2002-02-06, stephanie.hopkins@enron.com): “Could you please let me know if there are any procedures that any UBS people are still running that should be run by the estate team?”

## 15. Gas pipeline outage, cut and on-call notice relay

Gas control, field staff, plant contacts and schedulers email long distribution lists about pipeline maintenance, meter shut-ins, plant upsets, capacity reductions and pipeline cuts. Weekend on-call staff also send narrative notes. Schedulers read each notice, work out which nominations are affected, and decide whether to zero volumes, buy back, cut, or negotiate with the producer. Updates come as repeated forwards that revise earlier notices.

- **Who touches it:** bill.williams@enron.com, charlotte.hawkins@enron.com, gary.hanks@enron.com, gary.lamphier@enron.com, jackie.young@enron.com, lauri.allen@enron.com, mandy.mackinnon@enron.com, maritta.mullet@enron.com, mark.mccoy@enron.com, mary.poorman@enron.com, michael.olsen@enron.com, pat.clynes@enron.com
- **How often:** 2.9 occurrences/month (58 dated messages over 20 active months, 1999-12-27 → 2001-07-24)
- **Where it stalls:** Notices are typed by hand and sent to 15 to 40 people. Each reschedule is a new forwarded chain that has to be re-read. The volume decision waits on someone mapping the notice to nominations, and producer notice letters are written by hand. On-call notes are free text or attachments with no body, and cuts are relayed after the fact.
- **Automation:** A shared outage and cut log keyed by meter and pipeline, populated from gas control and pipeline notices. It matches each event against open nominations, alerts the owning scheduler with a proposed volume change, auto-generates producer notice letters, and publishes a structured weekend on-call summary. This replaces the free-text broadcast emails and re-forwards.
- **Estimate:** 20 min/occurrence × 40% automatable → 0.39 h/month → **$33/month**
- **Why that estimate:** Observer estimates range from 10 to 30 minutes per notice across sender and readers, with a median of 20 minutes. Matching and distribution automate well, but the nomination decision remains a judgement call, so the fraction is set at the 0.4 median.

**Evidence**

- `farmer-d/logistics/631` (line 24, 1999-12-29, lauri.allen@enron.com): “Rather than cut these volumes, would you try to negotiate with Koch not to flow this gas during the outage”
- `farmer-d/logistics/636` (line 21, 1999-12-30, charlotte.hawkins@enron.com): “He agreed to hold the gas for us and batch it throughout the rest of January.”
- `farmer-d/logistics/671` (line 26, 2000-01-11, gary.hanks@enron.com): “If you have any questions please call me at 36449.”
- `farmer-d/logistics/959` (line 23, 2000-03-24, maritta.mullet@enron.com): “The MTBE plant had an upset early today and a steam boiler is being taken out of service.”
- `farmer-d/logistics/961` (line 23, 2000-03-26, maritta.mullet@enron.com): “The MTBE plant will continue operating at lower production rates of approximately 8 MBD to 9 MBD until April 6 or 7 at the earliest.”
- `farmer-d/logistics/905` (line 19, 2000-03-13, gary.lamphier@enron.com): “Please zero out the volumes until further notice.”
- `farmer-d/logistics/902` (line 22, 2000-03-13, robert.lloyd@enron.com): “Do you want to arrange a buyback for this activity.”
- `farmer-d/logistics/969` (line 20, 2000-03-27, gary.hanks@enron.com): “The following meters are in the affected section for the outage planned in April:”
- `farmer-d/logistics/1182` (line 19, 2000-06-07, mark.mccoy@enron.com): “Some of the gas purchased from Dynegy on gas day 6/6 was cut:”
- `farmer-d/logistics/1182` (line 28, 2000-06-07, mark.mccoy@enron.com): “I will enter in MOPS as estimates.”
- `farmer-d/logistics/1218` (line 19, 2000-06-19, mark.mccoy@enron.com): “FYI----------Here are the latest cuts:”
- `farmer-d/logistics/1177` (line 74, 2000-06-05, robert.lloyd@enron.com): “Pleas  check  meters:  6780, 71, 68  for  weekend scheduling changes.”
- `williams-w3/sent_items/369` (line 23, 2001-07-24, bill.williams@enron.com): “The most important thing to remember is to document everything and call with questions.”
- `farmer-d/logistics/1268` (line 21, 2000-07-10, gary.hanks@enron.com): “On Friday, July 7 2000, the field detected a leak on the Wilson Creek Lateral in Wharton Co.”
- `farmer-d/logistics/1272` (line 21, 2000-07-12, gary.hanks@enron.com): “Repairs to the Wilson Creek lateral were completed on Monday afternoon 7/10/00.”
- `farmer-d/logistics/1375` (line 27, 2000-08-29, gary.hanks@enron.com): “All producers are to be shut-in by 9:00 AM on September 12, 2000.”
- `farmer-d/logistics/1297` (line 24, 2000-07-24, maritta.mullet@enron.com): “The Methanol Plant is still on target to begin making spec methanol on Friday, July 28.”
- `farmer-d/logistics/1332` (line 20, 2000-08-11, gary.hanks@enron.com): “This is a reduction in total capacity from 528,000 to 400,000 at Station 809.”
- `farmer-d/logistics/1334` (line 9, 2000-08-14, robert.lloyd@enron.com): “On Call Notes for Weekend Dated ; August 12th thru 13th”
- `farmer-d/logistics/1369` (line 23, 2000-08-28, mary.poorman@enron.com): “Here are my notes, please let me know if you have any questions.”
- `farmer-d/logistics/1786` (line 31, 2000-09-07, sabrae.zajac@enron.com): “She has informed me that for this time period there should be no nominations at these points.”
- `farmer-d/logistics/1793` (line 26, 2000-09-12, sabrae.zajac@enron.com): “Meters 6040 and 584 are back up.  Intradays for 9/12/00 can be done.”
- `farmer-d/logistics/1418` (line 19, 2000-09-21, mary.poorman@enron.com): “Duke Energy Field Services will be reworking the Wilcox Plant on 9/26 f rom 7am to 12 noon”
- `farmer-d/logistics/1816` (line 30, 2000-09-21, sabrae.zajac@enron.com): “This will begin @ 2:00 A.M. on the 28th but PG&E will keep the noms whole for the 28th.”
- `farmer-d/logistics/1422` (line 19, 2000-09-25, mark.mccoy@enron.com): “Oasis made cut to WGR sale to HPL on Sunday 9/24 & Monday 9/25 for 5.0 /day”
- `farmer-d/logistics/1443` (line 21, 2000-10-05, mark.mccoy@enron.com): “In my absence Tom Acton will be handling the Oasis & Lonestar interconnects at Katy”
- `farmer-d/logistics/2021` (line 24, 2001-01-01, robert.cotten@enron.com): “Please see the attached file for On-Call Notes.”
- `farmer-d/logistics/2115` (line 22, 2001-03-12, robert.cotten@enron.com): “Please find attached the On-Call Notes for the weekend of 3/10 & 11/01.”
- `farmer-d/logistics/2050` (line 25, 2001-01-22, mary.poorman@enron.com): “Phone Lee in Gas Control regarding same.”
- `farmer-d/logistics/2110` (line 29, 2001-03-05, michael.olsen@enron.com): “I changed the confirm in Pops to reflect it.”
- `farmer-d/logistics/2126` (line 25, 2001-03-21, mary.poorman@enron.com): “Please email me a list of any meters/contracts that you are aware of.”
- `farmer-d/logistics/2127` (line 24, 2001-03-21, mary.poorman@enron.com): “Please verify, add or update the information based on your desk's activities.”
- `farmer-d/logistics/2108` (line 19, 2001-02-27, mark.mccoy@enron.com): “so I moved the deals to reflect this on WGR (Aquila Header ).”

## 16. Transport contract, amendment and OBA administration

Shippers email Transwestern's account director (Michelle Lokay) to raise contract quantity for a day or two, change receipt points, continue capacity or amend OBAs. She approves each request and forwards it to contract administration (Dennis Lee, Craig Buehler), who generate the amendment. Capacity-release billing adjustments and OBA cash-outs are tracked by forwarded email. On the HPL side, contract administration asks the desk to confirm active deals before terminating contracts and mails a periodic assignment, termination and expiration report.

- **Who touches it:** baveety@pplweb.com, cheryl.dudley@enron.com, craig.buehler@enron.com, dennis.lee@enron.com, dlsmith@pplweb.com, elsa.villarreal@enron.com, julie.meyers@enron.com, kimberlee.bennick@enron.com, marlene.hilliard@enron.com, michael.eiben@enron.com, michelle.lokay@enron.com
- **How often:** 1.96 occurrences/month (47 dated messages over 24 active months, 2000-04-10 → 2002-03-25)
- **Where it stalls:** One-day changes mean the same contract is re-requested, re-approved and re-forwarded several times. Customer revisions arrive after the original request. Contracts wait on missing CAFs, credit approval or legal. Status is compiled into emails by hand, and the sharing calculation for capacity-release billing is redone each month.
- **Automation:** A request-to-amendment workflow that captures contract, quantity, dates, points and rate in structured fields. It would route for approval and credit check and push the change to the contract system with status visible to all parties. It would also query active deals by contract before termination, generate the contract status and termination report on a schedule, and encode capacity-release sharing rules in billing.
- **Estimate:** 25 min/occurrence × 45% automatable → 0.37 h/month → **$31/month**
- **Why that estimate:** Observer estimates range from 10 minutes for a simple approval to 60 minutes for billing adjustments and reports, with a median of 25 minutes. Intake and routing automate well, and approvals stay human, so the fraction is set at 0.45.

**Evidence**

- `farmer-d/logistics/1028` (line 18, 2000-04-10, marlene.hilliard@enron.com): “Please let me know if there are any deals attached to these contracts before I terminate them in the system.”
- `farmer-d/logistics/1131` (line 27, 2000-05-23, cheryl.dudley@enron.com): “Does Praxair really need to remain under ENA or is it okay under HPLC?”
- `farmer-d/logistics/1127` (line 21, 2000-05-22, michael.eiben@enron.com): “Please supply these savings where your name is listed if you haven't already done so.”
- `farmer-d/logistics/1135` (line 19, 2000-05-23, julie.meyers@enron.com): “Last that I had, was that legal was reviewing the contract.  Which sounds like it has been forgotten.”
- `farmer-d/logistics/2114` (line 34, 2001-03-08, cheryl.dudley@enron.com): “I accidentally failed to do the report for March 2001.”
- `farmer-d/logistics/211` (line 32, 2001-03-24, cheryl.dudley@enron.com): “If you do not need to receive this report or if you know of someone else that should receive it, please let me know”
- `farmer-d/logistics/2120` (line 19, 2001-03-16, cheryl.dudley@enron.com): “I have re-checked Sitara & verified that the above deal was a Term, Firm”
- `farmer-d/logistics/2121` (line 21, 2001-03-16, kimberlee.bennick@enron.com): “A termination letter is being prepared to be faxed to Exxon with an original to follow for their records.”
- `lokay-m/sent_items/164` (line 21, 2001-11-28, michelle.lokay@enron.com): “Please generate amendments for PPL's Red Rock expansion contract #27641.  The Administrative Contract will also need to be updated.”
- `lokay-m/inbox/53` (line 21, 2001-11-28, baveety@pplweb.com): “Just a quick revision to Dave's note below.”
- `lokay-m/inbox/71` (line 24, 2001-11-27, dennis.lee@enron.com): “Contract Submitted to CAS for Capacity Approval”
- `lokay-m/inbox/72` (line 15, 2001-11-27, craig.buehler@enron.com): “December 1st Contract Status as of November 27th (at 4:50 pm)”
- `lokay-m/inbox/52` (line 17, 2001-11-26, michelle.lokay@enron.com): “Please set up the following points and combinations.”
- `lokay-m/sent_items/2` (line 19, 2001-12-10, michelle.lokay@enron.com): “Please increase the Total Quantity from 10000 to 23115 for TODAY.  Points remain the same.”
- `lokay-m/sent_items/3` (line 30, 2001-12-10, michelle.lokay@enron.com): “please increase our 27748 MDQ from 10,000 to 16,000 effective 12/11 for one day only.”
- `lokay-m/sent_items/4` (line 17, 2001-12-11, michelle.lokay@enron.com): “Approved. Additional 15,000 on top of the 10,000 that is there all month.”
- `lokay-m/sent_items/73` (line 19, 2001-12-17, michelle.lokay@enron.com): “Approved.  The contract number will remain the same, #27785.”
- `lokay-m/sent_items/5` (line 27, 2001-12-12, michelle.lokay@enron.com): “Williams Field Services signed their new OBA and returned it (CR 27760).”
- `lokay-m/sent_items/9` (line 17, 2001-12-12, michelle.lokay@enron.com): “Final approval received!  I have an executed document signed by Williams and Danny McCarty.”
- `lokay-m/sent_items/68` (line 19, 2001-12-21, michelle.lokay@enron.com): “This is the wire transfer that I have been looking for since last week.”
- `lokay-m/sent_items/60` (line 17, 2001-12-31, michelle.lokay@enron.com): “Approved.  Amendment to increase TQ by 10,000 for 2 days.”
- `lokay-m/sent_items/61` (line 19, 2001-12-31, michelle.lokay@enron.com): “This is the San Juan to San Juan contract, with alternates out of the path.  Same as December.”
- `lokay-m/sent_items/57` (line 19, 2002-01-03, michelle.lokay@enron.com): “Approved.  Please increase, on Amendment #4, the West Texas receipts from 14,265 to 18,000 effective Nov 2002-Feb 2003.”
- `lokay-m/sent_items/44` (line 27, 2002-01-17, michelle.lokay@enron.com): “a manual adjustment will need to occur on ENA's contract 24924.”
- `lokay-m/sent_items/20` (line 38, 2002-01-30, michelle.lokay@enron.com): “ENA demand invoice will be adjusted for a capacity release credit of $56,700”
- `lokay-m/sent_items/45` (line 18, 2002-01-17, michelle.lokay@enron.com): “Let's discuss this prior to billing.  I agree that ENA owes us money”
- `lokay-m/sent_items/150` (line 18, 2002-03-19, michelle.lokay@enron.com): “Contract Administration needs you to email them officially requesting a name change.  Thanks.”
- `lokay-m/sent_items/149` (line 18, 2002-03-19, michelle.lokay@enron.com): “Burlington has agreed to execute this outstanding OBA if the name on the contract is changed.”
- `lokay-m/sent_items/126` (line 25, 2002-03-05, michelle.lokay@enron.com): “We still need to bill Conoco the TCR II Surcharges on 20,000 MMBtu per day.”

## 17. Meeting, shift and coverage scheduling

Assistants, managers and desk leads arrange meetings, training classes, conference calls and travel by email: proposing slots, collecting reply-all availability and re-sending reschedule notices. Desk leads also distribute shift schedules, collect swaps, canvass volunteers for holiday and weather coverage, and send out-of-office notes naming who covers each pipeline or desk. Rosters are compiled by hand from individual replies.

- **Who touches it:** aimee.lannou@enron.com, audrey.robertson@enron.com, bill.rapp@enron.com, bill.williams@enron.com, brenda.herod@enron.com, carlos.rodriguez@enron.com, csulzer@grenergy.com, d..hogan@enron.com, darron.giron@enron.com, eddie.janzen@enron.com, f..calger@enron.com, ghills@br-inc.com
- **How often:** 2.64 occurrences/month (74 dated messages over 28 active months, 1999-12-22 → 2002-03-25)
- **Where it stalls:** Availability is polled reply by reply, and meetings are cancelled and rescheduled with each notice re-sent to the full list. Dial-in details are requested afterwards. Shift swaps must be both emailed and hand-marked on the posted schedule. Coverage notes are free text that the backup has to interpret.
- **Automation:** Calendar scheduling with availability polling, invites that carry the agenda and dial-in, and automatic reschedule notices. A shared shift and coverage roster would take swaps and volunteer sign-ups once, notify the manager automatically, and route questions to the named backup when someone is marked out.
- **Estimate:** 15 min/occurrence × 50% automatable → 0.33 h/month → **$28/month**
- **Why that estimate:** Observer estimates cluster at 10 to 15 minutes with a median of 15 minutes. Standard scheduling tools remove most of the back-and-forth, so the fraction is set at the 0.5 median.

**Evidence**

- `farmer-d/logistics/1269` (line 24, 2000-07-10, mark.mccoy@enron.com): “In my absense, my desk will be covered as follows:”
- `farmer-d/logistics/1547` (line 32, 2000-12-04, carlos.rodriguez@enron.com): “Aimee 3-0506 will be the point person for any questions but the following people will do some of my desk, thanks.”
- `farmer-d/logistics/1382` (line 26, 2000-09-01, robert.lloyd@enron.com): “In my absence please contact Mark McCoy at extension 3-3396.”
- `williams-w3/sent_items/123` (line 26, 2001-11-02, bill.williams@enron.com): “I will be out of the office on Friday November 2nd, I will return on Monday November 5th.”
- `farmer-d/logistics/705` (line 25, 2000-01-21, mary.weatherstone@enron.com): “Please let me know if you would be available for the above mtg on Tuesday,”
- `farmer-d/logistics/842` (line 21, 2000-02-24, yvette.connevey@enron.com): “Please hold Thursday, March 9th 11:30 - 5:00 pm as Tentative for the Follow”
- `farmer-d/logistics/788` (line 23, 2000-02-14, robert.superty@enron.com): “As you might already know we had to reschedule our second meeting that was”
- `farmer-d/logistics/829` (line 21, 2000-02-23, yvette.connevey@enron.com): “please provide me with your
monthly calendars showing your vital business days”
- `giron-d/sent/499` (line 30, 2000-11-13, darron.giron@enron.com): “Group 1 will meet this Wednesday @ 11:30am and Group 2 this Thursday @ 11:30am.”
- `giron-d/sent/503` (line 33, 2000-11-13, darron.giron@enron.com): “Can you meet today @ 2:00 to discuss this weeks class?”
- `giron-d/sent/421` (line 35, 2000-12-06, darron.giron@enron.com): “I have not had an opportunity to set anything up for this week, yet.”
- `giron-d/sent/397` (line 18, 2000-12-13, darron.giron@enron.com): “We really need to pick up again next week.”
- `farmer-d/logistics/1990` (line 25, 2000-12-20, mary.poorman@enron.com): “would like to have a minimum of three on staff, so I need two volunteers (one offsystem, just in  case).”
- `farmer-d/logistics/1997` (line 29, 2000-12-20, mary.poorman@enron.com): “The following Logistics personnel will be in the office on Tuesday:”
- `farmer-d/logistics/1552` (line 27, 2000-12-06, heather.choate@enron.com): “The Texas Desk has reserved 15 rooms at the Hyatt in preparation of this Inclement Weather.”
- `farmer-d/logistics/1991` (line 29, 2000-12-20, tom.acton@enron.com): “Mary since I will be on call I'll be in here.”
- `williams-w3/sent_items/237` (line 23, 2001-09-18, bill.williams@enron.com): “Please send Bert and I an email notifying us of the changes and be sure to write your changes on the schedule.”
- `williams-w3/sent_items/233` (line 23, 2001-09-19, bill.williams@enron.com): “All submissions will have to be faxed to the Power Pool as we do not have a working digital certificate.”
- `williams-w3/sent_items/222` (line 18, 2001-09-22, bill.williams@enron.com): “Please schedule 4 or 5 of them to go if possible.”
- `lokay-m/inbox/17` (line 21, 2001-10-15, audrey.robertson@enron.com): “Okay, let's move Steve's Strategy Meeting to 8:30a on the 23rd.”
- `giron-d/inbox/264` (line 25, 2001-10-26, csulzer@grenergy.com): “Please let me know (and reply all in your response) if one or both dates”
- `giron-d/inbox/265` (line 18, 2001-10-26, janet.bowers@enron.com): “But I would prefer an afternoon or a late morning (10:30 a.m. or after) meeting.”
- `williams-w3/sent_items/163` (line 18, 2001-10-19, bill.williams@enron.com): “I could meet with Britt at 3PM or at 9 AM.”
- `giron-d/inbox/374` (line 19, 2001-11-09, csulzer@grenergy.com): “I recommend a brief conference call at 10:00 Tuesday.”
- `giron-d/inbox/421` (line 22, 2001-11-02, csulzer@grenergy.com): “I was thinking that perhaps we should plan to have dinner on Monday evening.”
- `giron-d/inbox/379` (line 29, 2001-11-12, csulzer@grenergy.com): “Should I use 763-241-2490 as the number to use for our conference call?”
- `giron-d/inbox/439` (line 25, 2001-11-12, laura.luce@enron.com): “Please accept this invitation, as it will automatically populate onto your schedule.”
- `lokay-m/sent_items/52` (line 21, 2002-01-07, michelle.lokay@enron.com): “Are we still on tomorrow?  What are the calling instructions?  Thanks.”
- `lokay-m/inbox/51` (line 22, 2001-11-26, audrey.robertson@enron.com): “Please note, Paul has scheduled a meeting to discuss "Available Capacity" on tomorrow, Tuesday, November 27, 10:30 - 11:30, ECN-1336.”
- `williams-w3/sent_items/87` (line 19, 2001-11-20, bill.williams@enron.com): “Contact me as soon as you can if you think you may not be able to make it.”
- `lokay-m/sent_items/71` (line 19, 2001-12-18, michelle.lokay@enron.com): “FYI...this is the conference call that I'd mentioned during staff meeting yesterday.”
- `williams-w3/sent_items/13` (line 20, 2002-01-25, bill.williams@enron.com): “Please be sure to send me an email regarding changes, and write them on the schedule.”
- `williams-w3/inbox/95` (line 19, 2002-01-26, john.anderson@enron.com): “Traded 1/29 day shift for 2/1 night shift.  See schedule for details.”
- `williams-w3/inbox/85` (line 21, 2002-01-30, bill.williams@enron.com): “I'm sure this was meant for you rather than me.  Response required.”
- `williams-w3/sent_items/11` (line 19, 2002-01-30, bill.williams@enron.com): “Could you resend me the original with the attachment?”
- `williams-w3/sent_items/16` (line 21, 2002-01-24, bill.williams@enron.com): “The meeting this afternoon will be delayed until next week.”
- `lokay-m/sent_items/21` (line 17, 2002-01-30, michelle.lokay@enron.com): “TW has a weekly gas control meeting every Friday at 3:00.  Can your meeting be finished by 3:00, or should we start earlier?”
- `lokay-m/sent_items/118` (line 28, 2002-03-01, michelle.lokay@enron.com): “Is Monday Mar-4, 9-10 am or Tuesday-Mar-4, 9-10 am ( my office) good for you to discuss the Baker Field project?”
- `lokay-m/sent_items/153` (line 17, 2002-03-19, michelle.lokay@enron.com): “Let's schedule all the marketers:  me, Lorraine, TK, Paul, Mark, and Kim.”
- `lokay-m/inbox/34` (line 20, 2002-03-25, bill.rapp@enron.com): “has been cancelled due to recent personnel changes at Transwestern. Another meeting will be scheduled later this week.”
- `lokay-m/sent_items/124` (line 17, 2002-03-04, michelle.lokay@enron.com): “Is there still room in the 03/21 class?  Thanks.”

## 18. Standing procedure reminders and market notice broadcasts

Desk managers broadcast standing rules and market changes to their groups by email. On the real-time power desk these cover CAISO and FERC notices, price caps, path derates, tagging, congestion bidding, time zones and delivery points. In gas risk, Giron forwards Gossett's procedure memos to book administrators, and in gas logistics managers send reminders on EOL deal handling. The same rules are restated after each error because they live only in email.

- **Who touches it:** bill.williams@enron.com, darron.giron@enron.com, mark.mccoy@enron.com, mary.poorman@enron.com, pat.clynes@enron.com, victor.lamadrid@enron.com
- **How often:** 3.06 occurrences/month (55 dated messages over 18 active months, 2000-06-27 → 2001-11-21)
- **Where it stalls:** Each notice is forwarded separately to several people, sometimes weeks late or without its attachment. New staff repeat old errors, such as wrong tiered bids, wrong time zones or altered EOL deals, which produces disputes and after-hours re-pathing. Forwarding depends on one person seeing each notice.
- **Automation:** Auto-route CAISO and market notices to the desk distribution list with a summary and an acknowledgement tracker. Keep the desk rules on one maintained page, and encode the key rules as validation at deal entry: lock EOL-sourced tickets, check tier bids, time zones and delivery points, and require the physical flag. This replaces repeated broadcast reminders.
- **Estimate:** 10 min/occurrence × 45% automatable → 0.23 h/month → **$19/month**
- **Why that estimate:** Observer estimates range from 3 to 25 minutes with a median of 10 minutes per notice including reading and correcting. Routing is fully automatable, but interpretation is not, so the fraction is set at about the 0.45 median.

**Evidence**

- `farmer-d/logistics/1298` (line 27, 2000-07-24, pat.clynes@enron.com): “All EOL deals at Katy must stay at the tailgate of the Exxon Katy Plant #4132.”
- `farmer-d/logistics/1299` (line 20, 2000-07-24, pat.clynes@enron.com): “Please be careful of EOL deals.  I got a call on Friday evening about this deal being changed but you had already left.”
- `farmer-d/logistics/1302` (line 24, 2000-07-24, mark.mccoy@enron.com): “explained to her that any deal they make on EOL cannot be changed in any way”
- `giron-d/sent/381` (line 33, 2000-12-20, darron.giron@enron.com): “Please make sure that all physical deals with a finacial component are marked physical in TAGG.”
- `giron-d/sent/364` (line 30, 2000-12-27, darron.giron@enron.com): “could you please forward this to your intra-month book admins.”
- `giron-d/sent/410` (line 59, 2000-12-07, darron.giron@enron.com): “In the past few months, the procedures for setting up new curves and books have not been followed by everyone.”
- `giron-d/sent/384` (line 36, 2000-12-20, darron.giron@enron.com): “it is extremely important that any deal booked to the East is communicated quickly to someone on my team.”
- `williams-w3/sent_items/449` (line 27, 2001-07-02, bill.williams@enron.com): “The current price cap is $91.87. We should continue our practice of not selling over the cap”
- `williams-w3/sent_items/423` (line 22, 2001-07-09, bill.williams@enron.com): “Important, CAISO computers down at 2 PM. Submit HE 17 and HE 18 before 2 PM.”
- `williams-w3/sent_items/401` (line 21, 2001-07-13, bill.williams@enron.com): “The CAISO has a new website. The link below should take you there.”
- `williams-w3/sent_items/397` (line 19, 2001-07-13, bill.williams@enron.com): “I would like you to find this information and distill the relevant information from it.”
- `williams-w3/sent_items/422` (line 27, 2001-07-09, bill.williams@enron.com): “we fill out an outage report and send it to the Generation Outage Desk.”
- `williams-w3/sent_items/363` (line 32, 2001-07-26, bill.williams@enron.com): “After the Day ahead market ran, the branch group ISO Share (PNOB) TTC in the”
- `williams-w3/sent_items/361` (line 9, 2001-07-26, bill.williams@enron.com): “Correction to COI rerate message:”
- `williams-w3/sent_items/261` (line 24, 2001-09-10, bill.williams@enron.com): “we must begin adjust bidding for congestion at ALL tie points.”
- `williams-w3/sent_items/250` (line 24, 2001-09-14, bill.williams@enron.com): “We have developed a process for tiering our bids and should do so going forward.”
- `williams-w3/sent_items/262` (line 24, 2001-09-07, bill.williams@enron.com): “we should notify the services desk if it is during the day, and should email the services desk (and me) if it is after normal work hours.”
- `williams-w3/sent_items/270` (line 20, 2001-08-30, bill.williams@enron.com): “please allocate all Hour-Ahead Congestion charges or revenues to the ECTRT group.”
- `williams-w3/sent_items/244` (line 23, 2001-09-14, bill.williams@enron.com): “Please remember to put the Tag # in the inc sheet. Every schedule should now be tagged if it is outside of the CAISO.”
- `williams-w3/sent_items/238` (line 22, 2001-09-17, bill.williams@enron.com): “And here is the attachment”
- `williams-w3/sent_items/235` (line 23, 2001-09-18, bill.williams@enron.com): “When tiering adjustment bids, the CAISO system will not read more than 10 bids.”
- `williams-w3/sent_items/76` (line 17, 2001-11-21, bill.williams@enron.com): “Allegheny's SC is now APX 5. Contact numbers are below.”
- `williams-w3/sent_items/137` (line 24, 2001-10-30, bill.williams@enron.com): “These deals should be scheduled in MST on the deal scheduling portion of Enpower as well.”
- `williams-w3/sent_items/146` (line 23, 2001-10-29, bill.williams@enron.com): “Please specify Pacific time zone in your summary of your deal at the end of each phone call”
- `williams-w3/sent_items/172` (line 26, 2001-10-17, bill.williams@enron.com): “ONLY schedule the energy to or from the originally prescheduled delivery point.”
- `williams-w3/sent_items/166` (line 27, 2001-10-19, bill.williams@enron.com): “Please do not fill any sale to EnMax with MPC energy.”
- `williams-w3/sent_items/95` (line 17, 2001-11-14, bill.williams@enron.com): “Extra ST-SW transmission can be viewed in the Available Transmission Sheet.”
- `williams-w3/sent_items/92` (line 24, 2001-11-14, bill.williams@enron.com): “Our old BPA contract # was 96104 our new BPA Contract # is 10728.”
- `williams-w3/sent_items/124` (line 26, 2001-11-02, bill.williams@enron.com): “Do not sell to them, do not buy from them.”
- `williams-w3/sent_items/119` (line 46, 2001-11-05, bill.williams@enron.com): “Please send me a list of the real time traders who will be using FSP.”
- `williams-w3/sent_items/100` (line 23, 2001-11-13, bill.williams@enron.com): “Everything must be tagged both light load and heavy load.”

## 19. Bankruptcy and Netco separation bulk deal moves (episode)

After the bankruptcy filings and during the Netco separation, credit, legal and contracts staff repeatedly send spreadsheets of deals or counterparties that must be zeroed, killed or moved into bankruptcy books. The gas risk group (Love, Giron, Gossett) cross-checks each list against the books and sends move requests to IT (Cecilia Cheung), who runs book-move scripts and retranslates. Each move needs its parameters clarified by email.

- **Who touches it:** c..gossett@enron.com, c..kenne@enron.com, cecilia.cheung@enron.com, cyndie.balfour-flanagan@enron.com, elena.chilkina@enron.com, exchange.administrator@enron.com, jayant.krishnaswamy@enron.com, m..love@enron.com, mark.mcclure@enron.com, scott.palmer@enron.com, stacey.richardson@enron.com, tammy.jaquet@enron.com
- **How often:** 13.33 occurrences/month (40 dated messages over 3 active months, 2001-12-13 → 2002-02-06)
- **Where it stalls:** Lists arrive as updates, stragglers and corrections, so versions must be reconciled. Requests lack book ids, commodity code or cutoff date, which forces clarification rounds. The impact on Unify paths is questioned only after thousands of deals are announced for killing.
- **Automation:** A master deal-move list that is matched automatically against the books by counterparty and deal id, flagging gaps and duplicates. A parameterised move request would capture source and target book, commodity, cutoff date and Canadian or US logic once, and an impact check would run against Unify paths and volumes before the script executes, with completion sent automatically.
- **Estimate:** 45 min/occurrence × 50% automatable → 5.0 h/month → **$425/month**
- **Why that estimate:** Observer estimates were 40 to 60 minutes with a median of 45 minutes per list cycle. List matching and parameter capture automate well, but legal and credit decisions on scope stay human, so the fraction is set at 0.5.
- **Drafted artifacts:** `drafts/bankruptcy-and-netco-separation-bulk-deal-moves-template.md`

**Evidence**

- `farmer-d/logistics/5` (line 29, 2001-12-13, tammy.jaquet@enron.com): “If a deal is killed it poses a problem for us in Unify if there are any paths associated with the deal; therefore, we request the deals be zeroed out.”
- `farmer-d/logistics/4` (line 38, 2001-12-13, mark.mcclure@enron.com): “I would like to meet with you guys and get more detail on why we are doing this and determine the impact?”
- `farmer-d/logistics/1` (line 27, 2001-12-14, jayant.krishnaswamy@enron.com): “Here is a list of the 66 physical deals that were zeroed out from December 15 onwards”
- `farmer-d/logistics/3` (line 23, 2001-12-14, scott.palmer@enron.com): “More deals that will be moved to the Bankruptcy book in TAGG and zeroed out 12/01 forward in Sitara.”
- `giron-d/inbox/117` (line 26, 2002-01-18, scott.palmer@enron.com): “With the bankruptcy filing of ENA Upstream yesterday, please find a listing of auto-terminating deals that need to be moved into the bankruptcy books.”
- `giron-d/inbox/116` (line 25, 2002-01-18, stacey.richardson@enron.com): “Please start forwarding these requests to myself and Darron Giron.”
- `giron-d/inbox/115` (line 23, 2002-01-19, stacey.richardson@enron.com): “Based on that list, here are some deals that need to be moved into the bankruptcy books.”
- `giron-d/inbox/105` (line 22, 2002-01-22, stacey.richardson@enron.com): “Here are more deals that need to be moved into the bankruptcy books.  Please skim across the spreadsheet to the column for the date reported to risk.”
- `giron-d/inbox/95` (line 40, 2002-01-23, m..love@enron.com): “Is this the last list we are going to get?  Jeff Gossett wants to know if we are done so that we can assure Don Miller that all of the CP's have been taken care of.”
- `giron-d/inbox/93` (line 26, 2002-01-23, stacey.richardson@enron.com): “This evening, Cyndie Balfour-Flanagan will combine all our spreadsheets so that we are working off one document.”
- `giron-d/inbox/42` (line 20, 2002-01-31, m..love@enron.com): “can you tell me why EH6453.2 is not on the list?  We are moving EH6453.5, in the comments it says it is an unwind of leg 2.”
- `giron-d/inbox/84` (line 19, 2002-01-24, m..love@enron.com): “Please move only financial deals.  Please let me know when this is complete.  We need to have it done by the time we calc our books today - no exceptions.”
- `giron-d/inbox/82` (line 19, 2002-01-24, cecilia.cheung@enron.com): “2923 deals with NG-PRICE book attached have been moved to the Bankruptcy bookand retranslated successfully.”
- `giron-d/inbox/67` (line 26, 2002-01-28, cecilia.cheung@enron.com): “5. Please provide the cutoff date to determine active deals (e.g. instr_end_dt > ? 1-jan-2002?)”
- `giron-d/inbox/58` (line 21, 2002-01-28, cecilia.cheung@enron.com): “The deals have been moved to ENA-FT-WT-SOCAL and retranslated successfully.”
- `giron-d/inbox/44` (line 22, 2002-01-31, m..love@enron.com): “should be the exact same script as yesterday, just substitute FT_TERMIN-GD for the two books you were looking for yesterday.”
- `giron-d/inbox/39` (line 19, 2002-01-31, m..love@enron.com): “The list has 140 counterparties on it.  Please let me know if you are not going to be able to move these today by 3:30.”
- `giron-d/inbox/44` (line 60, 2002-01-31, m..love@enron.com): “Which Bankruptcy book you want to move the deals to? BANKRUPTCY (166660) or BANKRUPTCY-CAD (166762)?”
- `giron-d/inbox/43` (line 28, 2002-01-31, scott.palmer@enron.com): “Please fill out the book and trader name.”

## 20. Daily credit report forwarding and counterparty rebook actions (episode)

Each business day the credit group (Veronica Espinoza, Russell Diamond) emails a Credit Report listing counterparties to rebook and pending credit actions. Darron Giron forwards each one unchanged to a desk analyst (usually Carole Frank), who then performs the TAGG rebooks by hand. When he is out, the reports pile up and are forwarded in a batch days later.

- **Who touches it:** darron.giron@enron.com
- **How often:** 18.0 occurrences/month (72 dated messages over 4 active months, 2001-02-02 → 2001-05-09)
- **Where it stalls:** This is pure manual pass-along through one person. Reports are forwarded hours or days late and in lumps after absences, which delays the rebook actions. Rebooks are then keyed by hand in TAGG.
- **Automation:** Route the credit report automatically to the desk distribution list or shared mailbox when it is sent. Parse its rebook and pending table into a per-desk task list with TAGG deal numbers. This removes the forwarding step entirely.
- **Estimate:** 4 min/occurrence × 80% automatable → 0.96 h/month → **$82/month**
- **Why that estimate:** All four observers estimated 3 to 4 minutes per forward with 0.8 to 0.85 automatable. Forwarding is fully mechanical, while the rebook judgement stays human, so 4 minutes and 0.8 are used.

**Evidence**

- `giron-d/sent/255` (line 48, 2001-02-05, darron.giron@enron.com): “I apologize for the delay on the distribution, as we had systems issues.”
- `giron-d/sent/263` (line 49, 2001-02-02, darron.giron@enron.com): “AEP Communications, Inc.   q00902.1  Rebook to AEP Energy Services, Inc.”
- `giron-d/sent/255` (line 51, 2001-02-05, darron.giron@enron.com): “Please contact Walter Guidroz at x5-3595 if you have any questions on the Aquila COLW deal.”
- `giron-d/sent/154` (line 17, 2001-03-19, darron.giron@enron.com): “I don't know if you got any of these while I was out.”
- `giron-d/sent/153` (line 43, 2001-03-19, darron.giron@enron.com): “Amoco Oil Company    qW3725.1 Rebook to BP Amoco Corporation”
- `giron-d/sent/149` (line 53, 2001-03-19, darron.giron@enron.com): “PG&E Energy Trading, Canada Co qX4420.1  Rebook ENA to ECC, under the ISDA”
- `giron-d/sent/100` (line 19, 2001-04-03, darron.giron@enron.com): “From: Veronica Espinoza/ENRON@enronXgate on 04/03/2001 09:25 AM To: Janie Aguayo/HOU/ECT@ECT, Diane Anderson/NA/Enron@Enron”
- `giron-d/sent/75` (line 47, 2001-04-11, darron.giron@enron.com): “Bank of America Corporation   v28205.1  Rebook to Bank of America, NA”
- `giron-d/sent/61` (line 53, 2001-04-18, darron.giron@enron.com): “Idaho Power Company   v39821.A   Rebook to Idacorp Energy Solutions LP”
- `giron-d/sent/85` (line 19, 2001-04-06, darron.giron@enron.com): “From: Veronica Espinoza/ENRON@enronXgate on 04/02/2001 09:29 AM To: Janie Aguayo/HOU/ECT@ECT, Diane Anderson/NA/Enron@Enron”
- `giron-d/sent/19` (line 5, 2001-05-04, darron.giron@enron.com): “Credit Report--5/3/01”
- `giron-d/sent/16` (line 5, 2001-05-04, darron.giron@enron.com): “Credit Report--5/4/01”
- `giron-d/sent/14` (line 44, 2001-05-07, darron.giron@enron.com): “Rebook to Calpine Energy”
- `giron-d/sent/10` (line 5, 2001-05-09, darron.giron@enron.com): “Credit Report--5/9/01”

## Method

1. Deterministic parse of every file; duplicates removed by normalised sender+subject+body; invalid or out-of-range dates set to null.
2. Messages grouped into subject threads and packed into 28 batches, each read in full by one observer subagent that reported processes as JSON with verbatim quotes.
3. Every quote checked against the raw file by code; failures logged in `validation.json`.
4. A synthesizer merged per-batch processes into company-wide ones; its citations were checked again.
5. Hours and dollars computed by code from dated message counts and two model-supplied estimates (minutes per occurrence, automatable fraction), both shown beside each result.
6. A process counts as recurring when it has dated mail in at least 6 distinct months; shorter bursts are reported as episodes, outside the total.
7. Drafts produced only for recurring opportunities above the threshold ($100/month).
