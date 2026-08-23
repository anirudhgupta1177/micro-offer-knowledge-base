# 11 — Source Map

Which file, in which repository, is the authority for each fact in this knowledge base.

Use this before changing anything: **update the source, then update the doc** — never the
other way round.

---

## 1. The authorities

| Fact | Authority | Repo |
| --- | --- | --- |
| **What a customer is charged** | `api/_catalog.js` | `micro-offer-funnel` |
| Every word of on-page copy | `src/data/copy.js` | `micro-offer-funnel` |
| Proof-asset manifest + intrinsic dimensions | `src/data/assets.js` | `micro-offer-funnel` |
| Deployment URLs, toggles, delivery links | `src/data/config.js` | `micro-offer-funnel` |
| Display prices (browser-side mirror) | `src/data/prices.js` | `micro-offer-funnel` |
| GST rate, GSTIN validation, state codes | `src/data/gst.js` | `micro-offer-funnel` |
| Route paths and base-path handling | `src/lib/paths.js` | `micro-offer-funnel` |
| Funnel state (sessionStorage) | `src/lib/funnel.js` | `micro-offer-funnel` |
| Razorpay create → pay → verify flow | `src/lib/razorpay.js` | `micro-offer-funnel` |
| Pixel + CAPI event ids | `src/lib/track.js` | `micro-offer-funnel` |
| Entitlement slugs, account creation, order rows | `api/grant-access.js` | `micro-offer-funnel` |
| Signature verification | `api/verify-payment.js` | `micro-offer-funnel` |
| Server-side conversion events | `api/_meta.js` | `micro-offer-funnel` |
| Pabbly reporting webhooks | `api/_webhooks.js` | `micro-offer-funnel` |
| Reconciliation job | `api/reconcile.js` | `micro-offer-funnel` |
| Fulfilment email content | `n8n/micro-offer-fulfilment.json` | `micro-offer-funnel` |
| Illustration sources | `design/*.html` | `micro-offer-funnel` |
| Environment variable names | `.env.example` | `micro-offer-funnel` |
| Portal offer slugs | `src/services/offersService.js` | `outbound-training-LP` |
| Portal routes and gating | `src/App.jsx` | `outbound-training-LP` |
| Offer Vault schema | `supabase/portal-offers-schema.sql` | `outbound-training-LP` |
| Order schema | `supabase/orders-schema.sql` | `outbound-training-LP` |
| GST invoice generation | `api/admin/generate-invoices.js` | `outbound-training-LP` |
| Brand tokens | `src/index.css` (`@theme` block) | `micro-offer-funnel` |
| Brand system source | `IntentLedSales_Brand_Assets.pdf` v1.0 | Input folder |
| Source copy document | `Anirudh Funnel Copy.pdf` | Input folder |

## 2. Facts that live outside any repository

These cannot be verified from source. They are held in live systems or in the training
recording itself.

| Fact | Where it actually lives |
| --- | --- |
| The **portal course structure** — modules, lessons, resources for `outbound-micro-course` and `linkedin-mini-course` | Supabase (the Offer Vault), authored through the admin portal. Not seeded in any migration |
| **Domain registrar** used in Phase 1 | Named on screen in the training recording only |
| **Mailbox provider** (US IPs) used in Phase 1 | Named on screen in the training recording only |
| **Lead sourcing + verification tool** in Phase 2 — "the single tool that replaces all of them" | Named on screen in the training recording only |
| **Spam-check tool** in Phase 3 | Named on screen in the training recording only |
| **LinkedIn automation tool** in OB3 | Named on screen in the OB3 training only |
| The contents of the **OB1 swipe file** | The Notion page |
| The 25 sections of the **OB2 guide** | The Claude artifact |
| The **Whimsical map** (Bonus 3) | The Whimsical board |
| The **ROI calculator** (Bonus 4) | The spreadsheet |

To complete the tool reference in [06 — Tools Reference](06-tools-reference.md), the five
`TBD` entries need someone to watch the recording and write down what appears on screen.

## 3. Duplicated values that must move together

Places where the same number or string is declared twice on purpose, because the two
bundles cannot import from each other.

| Value | Declared in | And in | Consequence of drift |
| --- | --- | --- | --- |
| `GST_RATE = 0.18` | `api/_catalog.js` (serverless) | `src/data/gst.js` (browser) | The quoted total stops matching the charged total |
| `FE` / `OTO1` prices | `api/_catalog.js` | `src/data/prices.js` | The checkout renders one price and charges another |
| Portal origin | `src/data/config.js` (`VITE_PORTAL_URL`) | `api/grant-access.js` | Buyers and their welcome email go to different domains |
| Indian state codes | `src/data/gst.js` | `outbound-training-LP` checkout | Invoices split CGST/SGST vs IGST incorrectly |
| Entitlement slugs | `api/grant-access.js` (`ENTITLEMENTS`) | `outbound-training-LP/src/services/offersService.js` | A buyer is granted a slug the portal does not gate on, so they see nothing |

**The server value always wins.** `api/_catalog.js` decides what is charged; everything
else is display.

## 4. Known documentation defects

Recorded here so this knowledge base does not repeat them.

| Defect | Where | Correct position |
| --- | --- | --- |
| "All prices are INR and **tax-inclusive** — ₹997 is exactly what is charged" | `micro-offer-funnel/README.md`, `## Pricing` | **Wrong.** Prices are ex-GST. ₹997 is charged as ₹1,176. See `api/_catalog.js` and the on-page tax note |
| "Non-blocking … Outbound Mastery is also flagged unlocked-by-default" | `outbound-training-LP/api/create-contact.js` | **Wrong.** Outbound Mastery is now locked behind an entitlement. A failed write there genuinely locks a course buyer out; the grant should be made fail-loud |
| Ashutosh's testimonial stored as `ankit.mp4` / `ankit.jpg` | `public/testimonials/` | Filenames are historical and do not match the on-page name. Harmless, but confusing |
| Bonus 3 renders `assets/phases/phase1.png` | `src/data/copy.js` | The Whimsical board built in this training is the correct asset. The other board in the library is from the Clay course — wrong product, and it would contradict the page's own "you don't need Clay" section |

## 5. Open items on the funnel itself

From the funnel README's "before you go live" checklist. Done:

- Real student clips (Ashutosh, Arjun, Pritham), carried over from the course
- Live URLs — Cal.com booking, WhatsApp community, portal
- Razorpay + Supabase credentials set in Vercel
- Fulfilment — `api/grant-access.js` provisions the portal account and entitlements; n8n sends the welcome email and the internal notification
- Outbound Mastery locked behind an entitlement so micro-offer buyers cannot reach it

Outstanding:

| Item | Detail |
| --- | --- |
| **VSL videos** | Every id in `VIDEOS` is empty on purpose. They must never point at the training Looms — that footage *is* the product. Until filled, the hero shows real proof instead |
| **Booking redirect** | Set Cal.com → Event type → Advanced → *Redirect on booking* to `https://course.intentledsales.com/micro/thank-you?booked=1`. Without it the flow is manual, and the page will not claim "Your Call Is Scheduled" |
| **Booking form questions** | Add qualifying questions to the Cal.com event (what they sell, who to, what they have built, revenue so far) so the session starts with context instead of discovery |
| **One live ₹1 test** | End to end with coupon `TESTFUNNEL1` |
| **Rotate credentials** | The Vercel API token and the n8n API key that were shared in chat during setup |

## 6. How to keep this knowledge base current

| If you change… | Update… |
| --- | --- |
| A price | `api/_catalog.js` **and** `src/data/prices.js`, then [07 — Pricing & GST](07-pricing-and-gst.md) |
| Any on-page wording | `src/data/copy.js`, then docs [02](02-micro-course.md), [03](03-order-bumps.md), [04](04-bonuses.md) or [05](05-oto-1on1-session.md) |
| A delivery link | `src/data/config.js` (`DELIVERY_LINKS`), then [08](08-fulfilment-and-delivery.md) and [10](10-links-index.md) |
| An entitlement slug | `api/grant-access.js` **and** `outbound-training-LP/src/services/offersService.js`, then [08](08-fulfilment-and-delivery.md) |
| A tool in the training | [06 — Tools Reference](06-tools-reference.md) |
| An asset | `src/data/assets.js`, then [09 — Asset Inventory](09-asset-inventory.md) |
