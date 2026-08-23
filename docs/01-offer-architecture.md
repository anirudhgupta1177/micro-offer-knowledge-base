# 01 — Offer Architecture

How the micro-offer funnel is put together: the routes, the offer ladder, and the
rules that govern what can be bought with what.

---

## 1. The ladder

| Stage | Product | Key | Price (ex-GST) | Purpose |
| --- | --- | --- | --- | --- |
| Front end | The 2-Hour Cold Email System | `FE` | ₹997 | The core offer. Everything else attaches to it. |
| Bump | Cold Email Copy Swipe File | `OB1` | ₹599 | Solves the "my copy might be wrong" objection at the moment of purchase. |
| Bump | 78-Page Outbound Implementation Guide | `OB2` | ₹699 | Solves "I'll lose the thread once the video ends". |
| Bump | LinkedIn Outreach Automation Training | `OB3` | ₹799 | Doubles touchpoints on a list the buyer already paid to build. |
| OTO | 1:1 Live Session With Anirudh | `OTO1` | ₹1,497 | Post-purchase. Sold on its own checkout, never bundled. |

## 2. Route map

The app is based at `/micro/`, but the sales page itself lives at
`/micro/cold-email-system`. `/micro` redirects there so older ad links keep working.

| Route | Page | Guard |
| --- | --- | --- |
| `/micro/cold-email-system` | Front-end sales page — 11 sections | Public |
| `/micro/oto-1` | OTO 1 sales page | Requires a purchase in session |
| `/micro/no-thanks` | Decline path + last-chance re-offer + full access | Requires a purchase in session |
| `/micro/call-booking` | Cal.com hand-off for the 1:1 session | Requires a purchase in session |
| `/micro/thank-you` | Access links, booking confirmation, next steps | Requires a purchase in session |

**There is no checkout route.** Every CTA on the sales page opens a popup checkout in
place. This is deliberate — it removes a full page transition from the highest-drop-off
step in the funnel.

The guarded routes redirect to the sales page unless funnel state exists in
`sessionStorage`. The guard is off in local dev, and `?preview=1` bypasses it on any
deployment that opts in with `VITE_ALLOW_PREVIEW=1` — never on production by default,
because an ungated query string would hand non-buyers the community invite and the paid
delivery links.

## 3. The flow

```
                     ┌──────────────────────────┐
   Ads / traffic ───▶│  /cold-email-system      │  11 sections:
                     │  Front-end sales page    │  hero · testimonials · myths ·
                     └────────────┬─────────────┘  3 phases · introduction ·
                                  │                bonuses · offer stack ·
                        every CTA │ opens          video proof · mentor ·
                                  ▼                guarantee · FAQ
                     ┌──────────────────────────┐
                     │   Popup checkout         │
                     │   + OB1 / OB2 / OB3      │──▶ Razorpay
                     └────────────┬─────────────┘
                                  │ payment verified (HMAC)
                                  ▼
                     ┌──────────────────────────┐
                     │   /oto-1                 │  1:1 Live Session, ₹1,497
                     └───────┬──────────┬───────┘
                       buy   │          │  decline
                             │          ▼
                             │   ┌──────────────────────┐
                             │   │  /no-thanks          │  Full access granted anyway
                             │   │  + last-chance offer │  + re-offer at same price
                             │   └──────┬───────────────┘
                             │     buy  │
                             ▼          ▼
                     ┌──────────────────────────┐
                     │   /call-booking          │  Cal.com
                     └────────────┬─────────────┘
                                  │ ?booked=1
                                  ▼
                     ┌──────────────────────────┐
                     │   /thank-you             │  Access links · booking confirmed ·
                     └──────────────────────────┘  3 next steps · community invite
```

## 4. Cart rules

These are enforced **server-side** in `micro-offer-funnel/api/_catalog.js`. The browser
sends product *keys*, never amounts, so a tampered client cannot change a price.

- **Primary keys** — `FE` and `OTO1`. Only these may be the primary item of an order.
- **Bump keys** — `OB1`, `OB2`, `OB3`. These may only ride along with a primary item.
- **Only `FE` accepts bumps.** The OTO checkout never sends them; anything arriving
  alongside `OTO1` is a malformed or tampered request and is ignored rather than charged,
  since a buyer reaching the OTO has already been offered the bumps once and may own them.
- **Duplicates are deduped.** A client sending `['OB1','OB1']` is charged once.
- **Unknown keys throw.** A key used in the wrong slot is an error, not a silent skip.

## 5. What the buyer sees at each step

| Step | Offered | Already owns |
| --- | --- | --- |
| Sales page | `FE` | — |
| Popup checkout | `FE` + optional `OB1`, `OB2`, `OB3` | — |
| `/oto-1` | `OTO1` only | `FE` + whichever bumps were taken |
| `/no-thanks` | `OTO1` re-offer at the same price | `FE` + bumps, plus full access already granted |
| `/thank-you` | Nothing | Everything purchased |

Access is granted on the `/no-thanks` page regardless of whether the OTO is declined —
declining the upsell never withholds what was already paid for.

## 6. Payment sequence

1. Browser POSTs `{ primary, bumps, customer }` to `/api/create-order`.
2. Server prices the cart from `api/_catalog.js` and creates a Razorpay order with
   `payment_capture: 1`.
3. Razorpay's popup collects payment.
4. Browser POSTs the returned ids to `/api/verify-payment`, which recomputes the
   HMAC-SHA256 signature over `order_id|payment_id` and compares it in constant time.
5. Only a **verified** payment sets funnel state and advances the customer.

A payment that succeeds but fails verification shows the buyer their payment ID and the
support address, rather than silently granting or denying access.

## 7. Technical stack

| Layer | Technology |
| --- | --- |
| Front end | React + Vite, Tailwind CSS v4 |
| API | Vercel serverless functions (`/micro/api/*`) |
| Payments | Razorpay |
| Accounts & entitlements | Supabase |
| Fulfilment email | n8n → Gmail |
| Booking | Cal.com |
| Hosting | Vercel (proxied from the course project at `/micro`) |
| Tracking | Meta Pixel (browser) + Meta Conversions API (server) |

Design tokens come from `IntentLedSales_Brand_Assets.pdf` v1.0: near-black `#0A0A0F`
backgrounds, cyan `#22D3EE` used sparingly for CTAs and emphasis, Plus Jakarta Sans
headings, Inter body, Playfair Display for editorial accents.
