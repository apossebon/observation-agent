---
title: Request to the deal owner for a meter flowing without a valid deal
opportunity: Meter flow without a valid deal: extension, new-deal and write-off requests
type: email
why_this_artifact: Requesters re-type a one-meter email to the deal owner every time, and requests stall when the meter, days, volume or prior deal are missing, so a standard message with the fields filled in is the change that works tomorrow.
---

# Email: meter flowing with no valid deal

Send one email per meter, to the deal owner (Daren Farmer in the archive). Fill every `{field}` before sending. A request that omits the meter, month or prior deal number forces a round trip. The same meters come back the next month (corpus/farmer-d/logistics/879, line 19).

Say in the subject which action you want. Subjects in the archive usually give only the meter and month, for example "Meter 1431 - Nov 1999" (corpus/farmer-d/logistics/590, line 20).

## Subject
`Meter {meter #} - {month/year} - {extend | new deal | write-off} needed`

## Body

Daren,

There is flow at meter {meter #} for {month/year} with no active Sitara deal. {Counterparty / contract, if known}.

- Flow: {volume in MMBtu} over {days or date range}
- Prior deal: #{deal #}, which {expired on {date} | missed its evergreen roll | is parked on the Strangers Gas contract | none, this is a new meter}
- What is blocked: {allocation | accounting arrangement | invoice} for {month/year}. {Allocation close is {date}.}

Please do ONE of the following:

1. **Extend or roll** deal #{deal #} through {end date}. "Can you please extend the deal thru 2-1-00 to cover this small volume?" is the form this takes (corpus/farmer-d/logistics/755, line 22). Another example: "Could you please extend deal #169625 for meter 1520 for..." (corpus/farmer-d/logistics/898, line 19).
2. **Create a new deal** for {sale | purchase} on contract {contract #} for {volume} MMBtu (corpus/farmer-d/logistics/596, line 19), or a spot ticket for {counterparty} at meter {meter #} for {month} (corpus/farmer-d/logistics/638, line 21).
3. **Approve a write-off** to Unaccounted for Gas. The signed original is attached or on its way: {printed form attached | will send the original}.

Please reply with the deal number you used, or tell me if the deal belongs to another desk ({desk / owner if known}).

Reason this is needed: Settlements cannot draft an invoice for this deal until it is extended or a new deal is set up (corpus/farmer-d/logistics/590, line 20). Volume management would rather have a deal than set up an accounting arrangement (corpus/farmer-d/logistics/751, line 20).

Thanks,
{name, role}

## Variant: chaser (send after {2} business days, same thread)

Daren, following up on meter {meter #} for {month/year}, requested on {date}. Still needed: {extend deal #{deal #} | new deal | write-off signature}. {Allocation close is {date}.} Reply to this message so the history stays in one thread. The first request was: "{paste the one-line ask}". (The archive shows reminders sent as "If you had forgotten, this can serve as reminder", corpus/farmer-d/logistics/748, line 26.)

## Variant: error forwarded by a third party

If you are forwarding a bridgeback or feedback error (corpus/farmer-d/logistics/749, line 38), do not forward the full quoted thread. Fill in the main template. Add the error text as one line: `Error: {text}`. Send it straight to the deal owner and copy the person who raised it. This avoids the hop through four or five people. A feedback error has the same form: "This deal expired 12/31/99" (corpus/farmer-d/logistics/881, line 19).

## Before you send, check

- One meter per email, with the month.
- Prior deal number checked. Deals sometimes sit with another desk.
- Counterparty is not suspended and the contract has not expired. Either one blocks the fix.
- For a write-off, the signed original is attached or the courier or mail step is noted.

## Not covered

The daily exception list (meters with flow and no deal), electronic write-off approval and automatic reminders from the opportunity description are an automation build. They are not part of this email. The email standardises the request until that exists.
