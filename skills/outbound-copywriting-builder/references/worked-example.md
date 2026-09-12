# Worked Example: the format contract

> A complete run, start to finish. This is the format every output follows: same sections, same order, same metadata blocks. Client: **Northwind**, a no-code sales commission platform. ICP: **BFSI - Insurance & Insurance Broking, India**. This run was a rebuild, so it includes the diagnosis section; omit that section when writing a sequence from scratch.

---

# Northwind: ICP 1
## BFSI: Insurance & Insurance Broking (India)

Sequence built against the swipe file. Honours the client's constraints: no absolute outcome claims, one yes/no CTA per email, no scraped signal voiced as an observation about the recipient, one proof name per email.

---

## What the product actually is

| Capability | What it kills |
|---|---|
| No-code plan builder - rules, qualifiers, rates, drag-and-drop | the IT/vendor dependency on every plan change |
| End-to-end calculation automation | Excel-based payout cycles and the people tied to them |
| **our AI agent** - AI incentive agent; plain-English questions, dispute investigation, plan-change tracing, source-backed | days spent reconstructing how a payout was derived |
| Rep-facing dashboards, what-if calculators, self-service portal | payout queries landing on the ops team |
| Granular audit trail, compliance-first architecture | audit exposure in a regulated sector |
| Typical go-live in ~4 weeks depending on scope | the six-month platform project objection |

**Confirmed proof for this ICP:** A pan-India life insurer: agent incentive calculations previously run entirely in Excel; typically 5-6 days of manual work a month recovered across two full-time roles, with admins retaining control to adjust plans.

**Buying logic that shapes the offer:** highly regulated, multiple stakeholders, **doesn't move without a proof of concept**, buyer function varies by sub-sector. External agents are most of the incentive-eligible population.

> That last point drives the whole build. If the segment won't move without a POC, the strongest cold offer is a **miniature POC** - not a benchmark document.

*(Note how the product model is written before any copy, and how a single line of buying logic picks the lead vehicle. Do this every time.)*

---

## Diagnosis of the current sequence

| Old offer | Verdict | Why |
|---|---|---|
| The Process Question | **Rebuild** | Bare symptom question. Never names the product, no proof, no reason for the email. A yes means "I'll discuss my process" - a conversation, not a buyer. |
| Payout Explainability | **Rebuild** | Same shape. Right pain, no product, no proof. |
| The Sector Benchmark | **Kill** | Fails all three detachment questions: useful after they delete the email, gettable elsewhere, unconnected to anything the client sells. This is the variant that harvests resource-hunters. |
| The Network Snapshot | **Kill** | Detachable, and it dresses a firmographic scrape up as value. |
| The Peer Proof | **Rebuild** | Right asset, wrong packaging. "Want the details?" is vague; a case study is information they can take. Convert to a walkthrough of how the setup was built. |
| The Phased Start Offer | **Rebuild** | Closest to a real offer. Needs the product named and a sharper conditional ask than "worth a look?" |

**The structural problem:** every Email-1 variant asked about the prospect's pain and none said what the product is. Three variants, three questions, zero product. The A/B test could only ever reveal which question people liked answering.

---

## Offer menu

| Label | Name | Type | Vehicle | Slot |
|---|---|---|---|---|
| 1A | The Plan Change Appetite | Direct | none | Email 1 - Variant A |
| 1B | Payout Explainability | Asset | mechanism walkthrough | Email 1 - Variant B |
| 1C | The One Rule Build | Asset | made sample (micro-POC) | Email 1 - Variant C |
| 1D | The Peer Walkthrough | Asset | mechanism walkthrough | Email 2 |
| 1E | The Phased Start | Direct | none | Email 3 |
| 1F | The Audit Trace | Asset | mechanism walkthrough | Spare |
| 1G | The Dispute Rebuild | Asset | made sample | Spare |

**The A/B/C test is structural, not cosmetic.** Variant A is appetite-only, B is a walkthrough, C is a micro-POC - three vehicles against one ICP, so the winner transfers to the client's other segments.

---

## Email 1: Day 0, net-new

### Variant A: 1A: The Plan Change Appetite *(Direct, no asset)*

**Subject:** plan changes at {{company_name}}

> Hey {{first_name}},
>
> Would your team want a mid-quarter commission rule change live the same week, without an IT ticket or a vendor request?
>
> That's what Northwind is built for - a no-code commission platform where ops teams change the plan rules themselves. One pan-India life insurer moved agent incentive calculations off Excel onto it, and typically get back 5-6 days of manual work a month across two full-time roles.
>
> Worth exploring at {{company_name}} this year?

- **A yes means:** they want the capability and there's appetite to look inside a real timeframe.
- **Says no:** teams mid-implementation elsewhere, or with no plan-change pain.
- **Score:** 9/10 - product named, proof specific and hedged, appetite ask with a genuine no available in the timing.

### Variant B: 1B: Payout Explainability *(Asset - mechanism walkthrough)*

**Subject:** agent payout disputes

> Hey {{first_name}},
>
> Most agent payout disputes aren't calculation problems. They're explanation problems - the number is usually right, but showing how it was derived takes days.
>
> Northwind is a no-code commission platform for teams paying large agent networks. Our AI agent, the agent, traces any payout back to the rule and the transaction behind it, in plain English, with the source attached.
>
> I recorded a short video of it working through a live dispute. Want me to send it over?

- **Behind the yes:** one 3-4 minute recording, made once for this ICP, of the agent resolving a dispute end to end.
- **Detachment check:** a recording of our product doing our thing. Nothing to extract, nothing to reuse.
- **A yes means:** they've agreed to watch a product demo. · **Says no:** anyone not evaluating.
- **Score:** 10/10.

### Variant C: 1C: The One Rule Build *(Asset - made sample / micro-POC)*

**Subject:** one rule, built for you

> Hey {{first_name}},
>
> Tell me the one commission rule that gives your team the most trouble - the one with all the exceptions - and we'll build it in Northwind and send you a recording of it calculating.
>
> We're a no-code commission platform used by insurers and broking firms paying large agent networks. One pan-India life insurer runs agent incentives on us now, after years of doing it in Excel.
>
> Takes us a couple of days and costs you nothing. Want to try it?

- **Behind the yes:** their real rule, built in our builder, running on sample data, delivered as a recording plus a live link.
- **Detachment check:** it lives in our platform. They cannot take it, rebuild it, or run rule two without us.
- **A yes means:** they described a real rule to a vendor - the highest-effort yes in the sequence, and the closest thing to the POC this segment needs before it moves.
- **Says no:** everyone not seriously evaluating, which is the point.
- **Score:** 10/10 - **expect the lowest reply rate and the highest call rate of the three.**

> **Ask for a description, not a file.** In a regulated segment, "tell me the rule" clears compliance where "send me your plan document" does not.

---

## Email 2: Day 3, threaded

### 1D: The Peer Walkthrough *(Asset: mechanism walkthrough)*

*(threaded reply, no subject)*

> Hey {{first_name}},
>
> The closest case to your setup is a pan-India life insurer that ran agent incentive calculations entirely in Excel.
>
> They moved onto Northwind and typically save 5-6 days of manual work a month across two full-time roles, with their own admins still adjusting the plans when rules change.
>
> I recorded a walkthrough of how their setup was built and what the first few weeks looked like. Want me to send it?

- **Behind the yes:** one recording per ICP covering the peer build - architecture, plan logic, rollout sequence.
- **Detachment check:** our implementation method. Useless to anyone not considering us.
- **A yes means:** they want to see how the peer result was produced - evaluation behaviour, not curiosity.
- **Score:** 10/10.

---

## Email 3: Day 7, new thread

### 1E: The Phased Start *(Direct: conditional transaction)*

**Subject:** before the data is clean

> {{first_name}},
>
> If we automated your highest-value agent calculations first, without waiting for the rest of the data to be clean, and you saw it running on your own plan before committing to a full rollout - would that be worth a look this quarter?
>
> That's how we start insurance rollouts at Northwind. One pan-India life insurer began the same way, and now runs agent incentives on us instead of Excel.
>
> P.S. if this isn't for you, just reply "no" and I'll close the file.

- **A yes means:** they'd evaluate a phased implementation on a real timeline - a sales conversation, not a chat.
- **Score:** 9/10. The conditional frame costs nothing to answer and a yes is appetite for the actual project. The P.S. is optional; drop it under strict one-CTA rules.

---

## Spares

**1F - The Audit Trace** *(Asset - walkthrough; use where audit findings are the trigger)*

**Subject:** payouts from eight months ago

> Hey {{first_name}},
>
> When an auditor asks how a specific agent payout was calculated eight months ago, is that a same-day answer at {{company_name}} or a week of reconstruction?
>
> Northwind keeps the rule, the transaction and the plan version behind every payout, so the trail is already there when someone asks.
>
> I recorded a short video showing an old payout traced back to source. Want it?

**1G - The Dispute Rebuild** *(Asset - made sample)*

**Subject:** that one disputed payout

> Hey {{first_name}},
>
> Describe one payout dispute your team had to reconstruct by hand and we'll rebuild the same shape of case in Northwind, then send you a recording of the agent walking it back to the rule that produced it.
>
> We're a no-code commission platform for insurers and broking firms paying large agent networks - a pan-India life insurer runs on us after years in Excel.
>
> Want to send one over?

---

## Fulfillment specs

**Mechanism walkthroughs (1B, 1D, 1F)** - three recordings, made once, reused across all contacts in the ICP.

| | Build | Deliver | Trigger |
|---|---|---|---|
| 1B Dispute video | screen recording: dispute → the agent traces to rule + transaction → source shown. 3-4 min. | hosted page, view tracking, pixelled | reply "yes" → reply agent sends link |
| 1D Peer walkthrough | how the a pan-India life insurer setup is structured, plan logic, weeks 1-4. 4-6 min. | same | same |
| 1F Audit trace | pulling an eight-month-old payout back to its rule and plan version. 3 min. | same | same |

Route anyone who watches past 80% to a human follow-up - view depth qualifies better than the reply itself.

**Made samples (1C, 1G)** - the micro-POC.

| Step | Detail |
|---|---|
| Intake | one sentence describing the rule or dispute, captured in the reply. No documents, no data. |
| Build | configure the rule in the no-code builder against synthetic data. Target 48 hours. |
| Deliver | screen recording of it calculating + a live link, hosted in our environment. |
| Bridge | "this is one rule on sample data - running your full agent plan on live data is the phased start we'd propose. Want to see what that looks like?" |
| Capacity | cap at ~10 builds a week; treat the queue as qualification, not a bottleneck. |

**Killed:** the Sector Benchmark and Network Snapshot pre-filled pages. Nothing to build, nothing to maintain.

---

## What to measure: read this before the first send

- **Positive reply rate will likely fall**, especially on Variant C. The old benchmark variant collected yeses from people who wanted a free document. Those replies are gone by design.
- **Appointments per positive reply should rise sharply.** That's the metric that matters.
- **Rank variants on calls booked per 1,000 sent, never on reply rate.** Rank on reply rate and you will kill Variant C - the variant most likely to produce the POC this segment needs to buy.
- Hold the existing send-volume floor before drawing conclusions.

**Confirm before launch:** whether ops can commit to the 48-hour turnaround on Variant C builds. The offer only works if fulfillment is fast and good - a slow build burns the highest-intent lead in the sequence.

---

## Variables used

`{{first_name}}`, `{{company_name}}` throughout. `{{proof_name_1}}` not needed - a pan-India life insurer is confirmed for this ICP and used inline.

---

## Notes on reading this example

- Every email is 4-6 lines and names the product before the ask.
- Every metadata block answers *a yes means* and *says no*. Asset offers add *behind the yes* and *detachment check*.
- Scores appear on every email; nothing under 8 ships.
- The measurement warning is not optional - without it, a client ranking on reply rate kills the best variant in week two.
