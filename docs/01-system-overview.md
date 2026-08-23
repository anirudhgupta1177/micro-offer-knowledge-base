# 01 — System Overview

The outbound system, end to end.

---

## Why most cold email fails

Not because cold email is dead. Because almost everyone starts at the wrong end.

The usual attempt: send from your main inbox, to a list pulled from a free tool, opening
with "do you have 15 minutes for a call this week?" Every one of those three choices is a
failure on its own. Together, they guarantee nothing lands.

The three phases fix them **in dependency order**. Great copy sent from a cold domain
lands in spam. A perfect domain setup sending to the wrong list gets ignored. Order matters
more than effort.

---

## Six things worth unlearning

| The common belief | What actually holds up |
| --- | --- |
| Cold email is dead | Well-written, personalised email still works — **if the infrastructure is built right** |
| You need a huge tech stack to run outbound | **80% list accuracy and the right sequence** beats an expensive stack every time |
| Send low volume to "stay safe" | Low volume is what kills you. **40+ warmed mailboxes are safer than 1 inbox** sending 50 emails a day |
| Personalisation at volume is impossible | AI-built ICPs and copy make "personalised at scale" the default, not the exception |
| "I can figure this out myself" | You probably already tried. What's missing isn't effort — it's infrastructure, **the part no tutorial shows you** |
| "My industry is different" | It's usually not the offer. It's that the last attempt skipped **the deliverability work that makes the offer land in an inbox at all** |

> The people quietly booking 30+ calls a month aren't working harder than you. They fixed
> the one thing nobody tells you to fix first — infrastructure.

---

## Phase 1 · BUILD — Deliverability that doesn't burn

**The problem:** send cold email from your main inbox and you can blacklist your primary
domain within days. That domain also carries your invoices, your client threads and your
password resets. It is not recoverable in any useful timeframe.

**What you build:**

| Step | Detail |
| --- | --- |
| Dedicated domains | Separate from your primary business domain. Never send cold from the domain you run your business on |
| US-IP mailboxes | Where the sending actually happens |
| DNS — SPF, DKIM, DMARC | The three authentication records. Set up **automatically**, not by hand |
| Domain-to-mailbox ratio | A specific ratio keeps the setup from tripping spam filters. Overloading one domain is what gets it flagged |
| 14-day warm-up | Automated sending between mailboxes to build a sending reputation before any real campaign goes out |

**What you end up with:** infrastructure capable of **1,000+ emails a day** that never
touches your primary domain's reputation.

**The one thing people get wrong:** treating the 14-day warm-up as optional. It is the
long pole in the whole system — it is the reason to build Phase 1 on day one rather than
after you've finished planning everything else. You cannot compress it.

---

## Phase 2 · TARGET — The AI ICP engine

**The problem:** wrong targeting kills a campaign before copy matters at all. Most people
skip straight to "who has this job title" and call that an ICP.

**What you build:**

```
Your business context
        │
        ▼
┌───────────────────────┐
│  AI ICP skill file    │
└───────────┬───────────┘
            ▼
  5–10 distinct ICPs, each with:
    · the pain point they actually feel
    · the buying logic that gets budget approved
    · hard filters you can scrape against
            │
            ▼
   Scrape + verify against those filters
            │
            ▼
   A list that's ~80% accurate
```

**Why one tool instead of four:** free and cheap data sources tend to hand you a list with
roughly a **50% bad-email rate**, which pushes people into stacking three or four
verification tools on top. One tool that pulls *and* verifies replaces the stack.

**The bar that matters:** 80% list accuracy. Chasing 95% costs more than the extra
accuracy returns, and 80% plus the right sequence outperforms an expensive stack anyway.

**The one thing people get wrong:** writing copy before the ICP exists. Copy written
against a vague list reads generic no matter how good the writing is, because it has
nothing specific to be about.

---

## Phase 3 · LAUNCH — Low-resistance copy

**The problem:** even a perfect list fails with the wrong ask. "Book a call" on a first
email asks a stranger for 30 minutes before you've given them anything.

**The governing rule: never ask for a call first.**

Ask for something small instead — something that costs the recipient one word to accept:

| Instead of | Ask for |
| --- | --- |
| "Do you have 15 minutes this week?" | "Want me to send a free Loom breaking down what I'd change?" |
| "Let's hop on a quick call" | "Want to try a small pilot on one segment?" |

**What you build:**

| Step | Detail |
| --- | --- |
| Copy from the ICP | An AI skill trained on real emails that got replies — not template libraries |
| Spintext | Variations so one email becomes five, which is what keeps volume from looking like volume |
| Spam-check | Test inbox placement **before** launch, not after the first 1,000 sends |
| Launch | Sequence configured and sent |

**What the live campaign returned:** 2,000 leads reached · 90 replies · 19 qualified — in
2 days. 4–5 meetings booked within the first 48 hours.

**The one thing people get wrong:** sending the same email to everyone at volume. Without
spintext, high volume is the fastest way to get pattern-matched into spam.

---

## The whole thing in sequence

```
  Week 0    Calculate what the setup will cost to run
              │
              ▼
  Day 1     PHASE 1 — buy domains, create mailboxes, set DNS
              │        start the 14-day warm-up  ◀── clock starts here
              │
              ├──────────────────────────────┐
              ▼                              │  (warm-up runs in the background)
  Day 1-3   PHASE 2 — run the ICP skill      │
              │        scrape + verify list  │
              ▼                              │
  Day 3-5   PHASE 3 — generate copy          │
              │        spintext + spam-check │
              ▼                              │
  Day 15    ◀────────────────────────────────┘
            LAUNCH — warm-up complete, campaign goes live
              │
              ▼
  Day 15+   Replies start landing
```

Phases 2 and 3 run *during* the warm-up, not after it. That's what makes a two-week
timeline a two-week timeline instead of a six-week one.

---

## Who this works for

**Works well:**
- B2B or SaaS, where buyers are reachable at a work email address
- Freelancers, agency owners, consultants, founders
- Targeting the US, Europe or India
- Starting from zero — arguably the better case, because you build it right the first time
  instead of undoing a burned domain later

**Doesn't work:**
- Local, offline businesses
- Selling directly to individual consumers
- Anything where the buyer doesn't use email professionally

---

## The numbers behind the system

| Metric | Figure |
| --- | --- |
| Live campaign in the session | 2,000 leads reached · 90 replies · 19 qualified in 2 days |
| A running client campaign | 6,785 contacted · 97.9% delivery · 26.5% reply rate |
| At scale | 247.8K emails → 918 opportunities |
| Sending capacity per setup | 1,000+ emails/day |
| Volume run monthly at Intent Led Sales | 1M+ emails |
