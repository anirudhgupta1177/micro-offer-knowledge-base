# The 2-Hour Cold Email System — Knowledge Base

The complete reference for the **micro-offer funnel**: the front-end micro course, all
three order bumps, all five bonuses, the one-time offer, every tool referenced, and
the fulfilment machinery that delivers it.

This repository is **documentation only**. The application code lives in
[`micro-offer-funnel`](https://github.com/anirudhgupta1177/micro-offer-funnel) (the funnel)
and [`outbound-training-LP`](https://github.com/anirudhgupta1177/outbound-training-LP)
(the member portal that hosts the training).

---

## The offer at a glance

| Key | Product | Price (ex-GST) | Anchor | Slot |
| --- | --- | --- | --- | --- |
| `FE` | The 2-Hour Cold Email System | ₹997 | ₹9,997 | Front-end |
| `OB1` | The Best-Performing Cold Email Copy Swipe File | ₹599 | ₹2,000 | Order bump |
| `OB2` | The 78-Page Outbound Implementation Guide | ₹699 | ₹4,000 | Order bump |
| `OB3` | LinkedIn Outreach Automation Training | ₹799 | ₹7,000 | Order bump |
| `OTO1` | 1:1 Live Session With Anirudh (60 min) | ₹1,497 | ₹15,000 | One-time offer |

Every listed price is **exclusive of 18% GST**, which is added at checkout.
Maximum realisable order value: **₹5,417** inc. GST — see [Pricing & GST](docs/07-pricing-and-gst.md).

## The five bonuses (included free with `FE`)

| # | Bonus | Stated value |
| --- | --- | --- |
| 1 | The AI ICP Engine — Claude Skill File | ₹5,000 |
| 2 | The Outbound Copywriting Skill | ₹7,000 |
| 3 | Whimsical Implementation Map | ₹10,000 |
| 4 | The Cold Email Cost + ROI Calculator | ₹4,000 |
| 5 | Private VIP Community | Priceless |

## The funnel

```
Ads / traffic
 └─▶ /micro/cold-email-system          Front-end sales page (11 sections)
      │                                Every CTA opens a popup checkout — there is no checkout route
      └─▶ Popup checkout · 3 order bumps · Razorpay
           └─▶ /oto-1                  OTO 1 — 1:1 Live Session, ₹1,497
                ├─ Buy ─────────────▶ /call-booking ─▶ /thank-you
                └─ Decline ─▶ /no-thanks   Last-chance re-offer (+ full access)
                                  └─ Buy ─▶ /call-booking ─▶ /thank-you
```

---

## Contents

| Doc | What's in it |
| --- | --- |
| [01 — Offer architecture](docs/01-offer-architecture.md) | The full funnel map, every route, the offer ladder, cart rules |
| [02 — The micro course](docs/02-micro-course.md) | The 2-Hour Cold Email System: all 3 phases, the promise, the curriculum |
| [03 — Order bumps](docs/03-order-bumps.md) | OB1, OB2 and OB3 in full — positioning, contents, delivery |
| [04 — Bonuses](docs/04-bonuses.md) | All 5 bonuses in full — what each is, why it exists, how it's delivered |
| [05 — OTO: 1:1 session](docs/05-oto-1on1-session.md) | The one-time offer, the decline path, the re-offer |
| [06 — Tools reference](docs/06-tools-reference.md) | **Every tool referenced**, split into the stack taught and the stack that runs the funnel |
| [07 — Pricing & GST](docs/07-pricing-and-gst.md) | The catalogue, GST maths, every cart combination, coupons |
| [08 — Fulfilment & delivery](docs/08-fulfilment-and-delivery.md) | Entitlement slugs, portal routes, n8n workflow, delivery links |
| [09 — Asset inventory](docs/09-asset-inventory.md) | Every proof shot, mockup, illustration and clip, and where it's used |
| [10 — Links index](docs/10-links-index.md) | Every URL in the system, in one table |
| [11 — Source map](docs/11-source-map.md) | Which file in which repo is the authority for each fact here |

---

## How to read this

Facts here are **sourced**. Where a claim comes from a specific file, that file is
cited inline as `repo/path/to/file.js`. Where something is genuinely not recorded in
any repository, it is marked **`TBD — not recorded`** rather than guessed at.
[11 — Source map](docs/11-source-map.md) lists every authority.

## Contacts

- **Support:** agent@theorganicbuzz.com
- **Legal entity:** The Organic Buzz
- **Brand:** IntentLedSales
- **Instructor:** Anirudh Gupta ("Ani")
