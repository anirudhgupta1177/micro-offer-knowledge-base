# 05 — OTO 1: The 1:1 Live Session

**1:1 Live Session With Anirudh** — `OTO1` · ₹1,497 ex-GST · anchor ₹15,000 · **90% off**

Shown once, immediately after a verified front-end purchase, on `/oto-1`.

---

## 1. The offer

> **"1:1 Live Session With Anirudh"**
> A focused 60-minute working session — together on a Zoom call.
>
> I'll personally go through your business, what you've built so far, what's working and
> what's not, and hand you a prioritized action plan for implementing the system, step by
> step.

Two badges carry the framing:

- **This is a real working session, not a sales call**
- **Only 3 spots available this week**

## 2. The hook

> Would you want me to personally look at your business, your setup, and your next move?
>
> I'll personally audit your business and hand you a **personalized action plan**, so you
> know exactly how to turn this outbound system into booked calls.
>
> Instead of guessing what to do next or figuring it out alone over the next few months,
> book a 60-minute working session and walk away with **a clear, prioritized plan built
> specifically for your business**.

Framed as **for new members only**, one time offer.

## 3. What the session covers

The letter section commits to three things, in order:

| # | Step | What happens |
| --- | --- | --- |
| 1 | **Audit** | Where you're actually at right now. What you've tried, what's built, what's missing or wrong. |
| 2 | **Diagnosis** | What you've done so far — what's actually going to work, and what's going to waste your time or budget. |
| 3 | **Roadmap** | A specific, sequenced plan for implementing this inside your business, so you leave knowing exactly what to do next, and in what order. |

## 4. What's included

Shown inside the OTO popup checkout, so the buyer sees exactly what ₹1,497 covers at the
moment of payment:

- A focused **60-minute** working session, one to one, on Zoom
- A full audit of where you actually are — what you have tried, what is built, what is missing
- A diagnosis of what will work and what will waste your time or budget
- A specific, sequenced roadmap you can start executing the same day
- **Lifetime access to the recording** of the call

## 5. The decline path

Declining is deliberately worded to make the cost of declining explicit:

> "No thanks, I'll figure it out myself, even if it takes longer to get there."

Short form used elsewhere: *"No thanks, I'll figure out my next steps on my own."*

Declining routes to `/no-thanks` — where **full access is granted regardless**. Refusing
the upsell never withholds what was already paid for.

## 6. `/no-thanks` — the last-chance re-offer

The page opens with a hard warning bar — **"DO NOT CLOSE OR REFRESH THIS PAGE!"** — then
does two jobs in order:

### First: deliver what was bought

> **Congrats & Welcome To The 2-Hour Cold Email System**
>
> Check your email to get the login details for everything you ordered, then click below
> to join the private VIP community.

Primary CTA: **Join The Private VIP Community**.

### Then: re-offer

> Did you not upgrade to the **"1:1 Live Session With Anirudh"**?
>
> Ouch… you might want to reconsider that, because this is your final chance to unlock it.
>
> Let's be honest. If you're serious about getting this system live and actually booking
> calls from it, the fastest way is having someone who runs it every day look at your
> specific setup and tell you what to fix.

**The re-offer is at the same ₹1,497** — it is a last chance, not a further discount.

### The expanded list on the re-offer

The `/no-thanks` page lists more than the OTO page does, adding three specifics that
address exactly what a buyer who just watched the training would now be unsure about:

| | Item |
| --- | --- |
| 1 | A full audit of where you actually are — what you have tried, what is built, what is missing or wrong |
| 2 | A diagnosis of what will work and what will waste your time or budget |
| 3 | **Your ICP reviewed** against what is converting in live campaigns right now |
| 4 | **Your infrastructure checked** for the setups that get flagged |
| 5 | **Your copy read** against what is landing replies and what is getting ignored |
| 6 | A specific, sequenced roadmap you can start executing the same day |
| 7 | A real working session, not a sales call — 60 minutes, one to one, on Zoom |
| 8 | Lifetime access to the recording of the call |

Items 3, 4 and 5 map one-to-one onto the three phases of the training. That is the
mechanism: the session is positioned as a review of the buyer's own Phase 1, 2 and 3 output.

### The scarcity close

> Once you leave this page, this price is gone and the session goes back to full price.

A **15-minute countdown** (`OTO_TIMER_MINUTES`) runs on the final CTA.

## 7. Booking

| Attribute | Value |
| --- | --- |
| Platform | Cal.com |
| Link | https://cal.com/anirudh-gupta/consulting-call |
| Route | `/call-booking` hands off to Cal.com |
| Return | Cal.com redirects to `/thank-you?booked=1` on booking |
| Fallback | An "Already booked?" link on `/call-booking` reaches `/thank-you` manually |

The thank-you page only claims **"Your Call Is Scheduled"** when `?booked=1` is present —
so a buyer who reached it by the fallback link is not told something untrue.

**Embedding:** `EMBED_BOOKING = true` embeds the calendar in an iframe on the thank-you
page rather than only linking out. Both Cal.com and Calendly allow framing.

**Booking form questions** — the Cal.com event should carry qualifying questions (what
they sell, who to, what they have built, revenue so far) so the session starts with
context instead of discovery.

## 8. Cart rules

`OTO1` is a **primary key**, not a bump. It has its own checkout and is never bundled
with `FE`. `PRIMARIES_ACCEPTING_BUMPS` contains only `FE`, so any bump key arriving with
`OTO1` is ignored rather than charged — a buyer at this stage has already been offered
the bumps once and may own them.

## 9. Fulfilment

| Attribute | Value |
| --- | --- |
| Entitlement slug | **None** — `OTO1` grants nothing in the portal |
| Product line (reporting) | `micro-oto-session` |
| Delivered as | Cal.com booking + Zoom call + recording |
| Consult tracking | The portal's `consult.sessions_purchased` counter |

The reason there is no entitlement: the deliverable is a human on a call, not content.
`'expert-call'` needs no grant.

## 10. Pricing

| | Amount |
| --- | --- |
| Anchor value | ₹15,000 |
| Price | ₹1,497 |
| Discount | 90% off |
| 18% GST | ₹269 |
| **Charged** | **₹1,766** |

## 11. The signature block

| Field | Value |
| --- | --- |
| Name | Anirudh Gupta |
| Role | Ran Outbound For Instantly.ai, $1.2M ARR/Month |

## 12. Proof used on the OTO page

Four screenshots of real 1:1 sessions, used to demonstrate that these calls actually
happen rather than being a promise:

| Asset | Session |
| --- | --- |
| `call-ceejay.jpg` | Ceejay & Bhushan — founder and operations lead |
| `call-gangel.jpg` | Lilla, Gábor & Sebastian — founding team reviewing their outbound |
| `call-saeed.jpg` | Saeed — one-to-one going through a client setup |
| `call-shrey.jpg` | Shrey — one-to-one reviewing a live email sequence |

Plus written reviews (`words-*.jpg`) from Shuvasree Bhadra, Nihal Prasad and Anant Kumar
Maurya, and a client message reporting a first booked meeting on day one.
