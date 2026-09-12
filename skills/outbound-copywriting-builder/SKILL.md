---
name: outbound-copywriting-skill
description: >
 Write complete cold email sequences for an ICP in the buying-intent format - 3 structurally
 different Email-1 variants (appetite ask / mechanism walkthrough / micro-POC), a threaded
 Email 2, a conditional-ask Email 3, plus spares - with offer menu, per-email reply forecast,
 intent score, fulfillment specs, and a measurement warning.
---

# Outbound Copywriting: sequences that book calls

> **Published version.** The worked example originally ran on a real client
> account. Company names and the named customer reference have been replaced
> with generic stand-ins so this can live in a public repo. The structure, the
> sequences and the format contract are unchanged.

Turn a **client product + one ICP + proof** into a complete, paste-ready email sequence in a fixed format.

The sequence's only job: **make every reply mean "I want what you sell."** Reply rate is a vanity metric - a positive reply from someone who wanted a free document costs money and calendar time. Optimise for what the yes commits them to.

Read `references/swipe-file.md` before writing anything. Read `references/worked-example.md` for the exact output format.

---

## Non negotiable: no em dashes

Never use an em dash or an en dash in any line of generated copy, subject
line or body. It is the single most obvious sign that a machine wrote the
email, and it costs credibility with exactly the buyers worth having.
Use a comma, a full stop, a colon, or restructure the sentence. Plain
hyphens are fine for ranges and compounds.

The examples in `references/` follow this rule. Match them.

---

## Inputs

| Input | Required? | If missing |
|---|---|---|
| Client product - what it is, what it replaces | **yes** | web-search the company; ground the copy in real capabilities, never invented ones |
| ICP - who, geography, titles, buying logic | **yes** | ask for it, or take it from the campaign angles doc |
| Proof - named clients + numbers | **yes** | if none exists, use sample-as-proof (see swipe file, Teardown 2) and say plainly the client just launched. Never invent a number or a logo. |
| Client constraints - compliance rules, banned claims, CTA rules | no | apply the defaults below |
| Existing sequence being rebuilt | no | skip the diagnosis section |

Don't stall on missing detail you can reasonably infer - state the assumption inline and keep going. The one thing you may never infer is proof.

---

## Workflow

### 1. Build the product model
Write the capability → what it kills table before any copy. Two columns: what the product does, and the specific work or cost it removes. Copy written without this table drifts into category language ("streamline incentive operations") instead of the thing the buyer feels.

If the client is a real company and the brief is thin, web-search their site and product pages. Ground every claim.

### 2. Read the buying logic and pick the vehicle
The ICP's buying logic decides which yes-vehicle leads. This is the highest-leverage decision in the whole sequence:

| Buying logic says... | Lead vehicle |
|---|---|
| "doesn't move without a proof of concept" | **micro-POC** - a built sample is a miniature POC |
| "already knows the category, pitched by competitors" | **mechanism walkthrough** - the job is differentiation, not education |
| "category-unaware, needs educating" | **mechanism walkthrough** - the video teaches and sells at once |
| "self-serve product, fast evaluation" | **trial/access**, paired with a doubt case |
| "long procurement, many stakeholders" | **walkthrough** - something they can forward internally |
| "regulated, cautious about sharing data" | micro-POC on a *described* input, never a requested file |

### 3. Build the offer menu
Seven labelled offers, mapped to slots. Each carries a name, type (Direct = no asset / Asset = something behind the yes), vehicle, and slot.

### 4. Write the emails against the skeletons
Skeletons are in `references/swipe-file.md`. Four to six lines each. Every email carries all six anatomy components.

### 5. Score, forecast, spec
Every email gets an intent score and a reply forecast. Every asset offer gets a fulfillment spec. The output ends with the measurement warning.

---

## The two gates: run on every email before it ships

**Gate 1 - The Yes Test.** Write the sentence the prospect agrees to when they reply. Try to finish it with "...and then I never speak to them again." If that lands cleanly, the email is broken.

**Gate 2 - The Detachment Test.** Three questions about whatever sits behind the yes. One yes and it's a lead magnet:
1. Is it still useful after they delete the email?
2. Could they get the rest without the client?
3. Does it *substitute* for the service instead of *sampling* it?

Documents fail all three. Recordings of the product, built samples, and product access fail none.

---

## Offer anatomy: all six, every email

| # | Component | Cut it and... |
|---|---|---|
| 1 | **Relevance** - why them, at category or role level | it reads as a blast |
| 2 | **Identity + mechanism** - the client's name and what the product actually does | nobody can want a thing they can't see |
| 3 | **Outcome** - the end-of-chain result | they weigh effort against nothing |
| 4 | **Proof** - a named client, a number, or the sample itself | the outcome isn't believable |
| 5 | **The yes-vehicle** - nothing / walkthrough / made sample / trial | the ask is abstract |
| 6 | **The micro-yes ask** - one word, no time commitment | resistance spikes |

**Pain is a setup line, never the ask.** Pain opens the email to establish relevance. The ask is always about appetite for the outcome.

---

## The three legal vehicles

| Vehicle | Behind the yes | Why it filters |
|---|---|---|
| **Mechanism walkthrough** | 3-6 min recording of the product doing the thing, made once per ICP | consuming it means watching a pitch |
| **Made sample / micro-POC** | one unit of the real deliverable, built for them | they can't produce unit two |
| **Trial / access** | the product, time-boxed | setup effort is the qualification |

**Banned as assets** (all fail Gate 2): benchmarks, reports, audits, teardowns, checklists, templates, guides, PDFs, competitor gap lists, snapshots, primers, roadmaps, calculators, scorecards. Renaming an audit doesn't change what it does - it's the artifact that's wrong, not the word.

**Host the asset, don't hand over the file.** Recordings, live links, hosted demos. The moment it becomes a document, it detaches.

---

## Sequence architecture: the fixed slot structure

### Email 1: Day 0, net-new. Three variants, three *different vehicles*.

This is the signature move. Variants test structure, not phrasing:

| Variant | Offer type | Vehicle | What it tells you |
|---|---|---|---|
| **A** | Direct | none - appetite ask only | whether the outcome alone pulls |
| **B** | Asset | mechanism walkthrough | whether they'll watch |
| **C** | Asset | made sample / micro-POC | whether they'll engage at POC depth |

Whatever wins transfers to every other ICP for that client. Three phrasings of the same question tell you nothing; three vehicles tell you how the market buys.

### Email 2: Day 3, threaded reply, no subject line.
The **peer walkthrough**: the closest named case, converted from a case study into a recording of *how that setup was actually built*. Anchors on proof, ends in a permission ask.

### Email 3: Day 7, new thread, new subject.
The **conditional transaction** ask (Direct, no asset) - the highest-intent form in the swipe file. *"If we did X, without Y, and you saw it running before committing - would that be worth a look this quarter?"* Costs nothing to answer; a yes is appetite for the actual project. Optional graceful-out P.S.

### Spares: two, held in reserve.
Trigger-specific angles for when a signal is confirmed: the compliance/audit angle, the failure-mode angle, or a competitor-confirmed differentiation angle. Same rules, same format.

---

## Default constraints (client constraints override these)

- **No absolute outcome claims.** Every number hedged: "typically", "up to", "depending on scope". Never "eliminates", "down to zero", "guarantees".
- **One CTA per email**, framed as a yes/no.
- **No call or meeting ask in Emails 1 and 2.** Email 3 may ask for appetite, still time-free.
- **Never voice a scraped signal as an observation about the recipient.** Hiring data, review data and firmographics pick the list and shape the angle - they never appear as "I noticed you're...". State the category-level implication instead.
- **One proof name per email, never stacked.**
- **Only confirmed proof.** Named clients must be client-supplied or published. No invented logos, no invented numbers.
- **Ask for a description, not a document** in regulated segments. "Tell me the rule that gives you trouble" clears compliance where "send me your plan" doesn't.

---

## Writing rules

1. Name the client's company and what it sells, before the ask, in every email.
2. State the implication, not the signal.
3. Proof carries a number or a name - hedged.
4. No time commitment in any ask.
5. No deliverable jargon: audit, report, analysis, assessment, review, teardown, scan, diagnostic. Use plain verbs: I recorded, we'll build, I put together, mind if I send.
6. No AI vocabulary: pivotal, crucial, enhance, underscore, landscape, testament, foster, delve, showcase, leverage, robust, seamless, unlock, elevate, empower, streamline, holistic, cutting-edge, game-changer, navigate, realm, dive.
7. No contrast structures - no "It's not X, it's Y."
8. Sentences under 16 words. Four to six lines per email.
9. If a line could apply to 1,000 other companies, delete it.
10. Comparison over explanation for novel categories: "sort of like if X and Y came together."
11. **Subject lines**: 3-5 words, lowercase or sentence case, naming their company or their outcome - *"plan changes at {{company_name}}"*, *"{{company_name}} exit options"*, *"one rule, built for you"*. No `$` amounts. "free" is a soft avoid, not a ban.
12. **Variables**: `{{first_name}}`, `{{company_name}}`, `{{proof_name_1}}`. Use a real client name inline where one is confirmed; reserve the placeholder for ICPs where it isn't. List variables used at the end.

---

## Intent scorecard

Score 0-2 each. **Ship at 8+. Any 0 on criteria 2 or 3 is an automatic rewrite.**

| # | Criterion |
|---|---|
| 1 | Product named before the ask |
| 2 | A yes can only mean "I want the outcome" |
| 3 | The asset is useless without the client (or there is no asset) |
| 4 | Proof present and hedged |
| 5 | Ask is a one-word yes with no time commitment |

---

## Output format

Follow `references/worked-example.md` exactly. Section order:

```markdown
# [Client]: [ICP name] Sequence
## [Segment descriptor, geography]

[One line on what this is and which constraints it honours]

## What the product actually is
[capability → what it kills table]
**Confirmed proof for this ICP:** [named client + hedged numbers]
**Buying logic that shapes the offer:** [the constraint that picked the vehicle]
> [the one-line reason the lead vehicle was chosen]

## Diagnosis of the current sequence ← only when rebuilding
[table: old offer | Kill / Rebuild | why]
**The structural problem:** [one paragraph]

## Offer menu
[table: label | name | type | vehicle | slot]
**The A/B/C test is structural, not cosmetic.** [one line on what each variant tests]

## Email 1: Day 0, net-new
### Variant A: [label]: [name] *(Direct, no asset)*
**Subject:** [3-5 words]
> [email body, blockquoted, 4-6 lines]
- **A yes means:** ...
- **Says no:** ...
- **Score:** x/10 - [one line]

### Variant B: ... *(Asset - mechanism walkthrough)*
[same, plus:]
- **Behind the yes:** ...
- **Detachment check:** ...

### Variant C: ... *(Asset - made sample / micro-POC)*
[same]

## Email 2: Day 3, threaded
### [label]: [name] *(Asset: mechanism walkthrough)*
*(threaded reply, no subject)*
> [body]
[metadata block]

## Email 3: Day 7, new thread
### [label]: [name] *(Direct: conditional transaction)*
**Subject:** [...]
> [body]
[metadata block]

## Spares
[2 offers, same shape, compressed]

## Fulfillment specs
[walkthrough table: build | deliver | trigger]
[made-sample table: intake | build | deliver | bridge | capacity]
**Killed:** [any old assets that no longer need building]

## What to measure: read this before the first send
[the warning, below]

## Variables used
[list]
```

**The measurement warning is mandatory in every output.** Reply rate will likely fall, especially on Variant C - that's the freebie collectors leaving by design. Appointments per positive reply should rise. Rank variants on **calls booked per 1,000 sent**, never on reply rate, or the highest-intent variant gets killed first. Hold any existing send-volume floor before drawing conclusions.

---

## Running this across many ICPs

One run per ICP. Across a client's full ICP set:

- **Reuse** the product model, the proof bank, and - wherever the vehicle repeats - the actual recordings. One walkthrough often covers three ICPs.
- **Vary** at least one real variable per ICP: the outcome named, the pain in the setup line, the proof point, or the vehicle. If two ICPs' sequences blur on a skim, the segments should merge.
- **Re-pick the vehicle per ICP** from the buying-logic table. Don't inherit the previous ICP's choice by default.
- Close the batch with a short note on which ICPs the micro-POC will hit hardest and why.

---

## Validation checklist

```
[ ] Product model table written before any copy
[ ] Vehicle chosen from the ICP's buying logic, with the reason stated
[ ] Email 1 has 3 variants testing 3 different vehicles, not 3 phrasings
[ ] Every email names the client's product before the ask
[ ] Every email carries proof - named or hedged number - one name per email
[ ] Gate 1 run on all 5+ emails; no yes completes with "...and I never speak to them again"
[ ] Gate 2 run on every asset; nothing detachable
[ ] No banned assets (benchmark/report/snapshot/primer/roadmap/gap list/checklist)
[ ] Assets are hosted recordings, built samples, or product access - never documents
[ ] Pain appears only as a setup line, never as the ask
[ ] No meeting ask in Emails 1-2; no time commitment anywhere
[ ] No scraped signal voiced as an observation about the recipient
[ ] All outcome claims hedged
[ ] Every email scored; nothing under 8/10; no 0s on criteria 2 or 3
[ ] Reply forecast (a yes means / says no) written for every email
[ ] Fulfillment specs written for every asset offer
[ ] Measurement warning included
[ ] Subject lines 3-5 words, naming their company or outcome
[ ] Variables listed
```

---

## Reference library

| File | Read it when... |
|---|---|
| `references/swipe-file.md` | **Before writing anything.** Seven proven emails torn down, the shared DNA, the skeletons to write against, subject-line patterns, and the before/after conversions. |
| `references/worked-example.md` | **For the format contract.** A complete run (Northwind → Indian insurance & broking) showing every section, the metadata blocks, the fulfillment specs, and the measurement warning. |

## Related skills
- `offer-strategy` - designs the offer menu this skill turns into copy; deeper theory on vehicles and gates
- `outbound-campaign-builder` - lists, volume, intent signals, and the campaign this sequence plugs into
- `campaign-copywriting` - the stepwise, confirm-as-you-go alternative; use that one when the user wants to approve direction before seeing copy, this one when they want the finished sequence in a single pass
- `icp-creation-skill` - define the ICP before writing the sequence
