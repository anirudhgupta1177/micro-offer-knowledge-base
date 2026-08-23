# 07 — Pricing & GST

`micro-offer-funnel/api/_catalog.js` is the **only** source of truth for what a customer
is charged. The browser sends product *keys*, never amounts, so a tampered client cannot
lower a price.

---

## 1. The catalogue

All prices are INR major units (rupees) and are **TAX-EXCLUSIVE**.

| Key | Name | Price | Compare-at | Slot |
| --- | --- | --- | --- | --- |
| `FE` | The 2-Hour Cold Email System | ₹997 | ₹9,997 | Primary |
| `OB1` | The Best-Performing Cold Email Copy Swipe File | ₹599 | ₹2,000 | Bump |
| `OB2` | The 78-Page Outbound Implementation Guide | ₹699 | ₹4,000 | Bump |
| `OB3` | LinkedIn Outreach Automation Training | ₹799 | ₹7,000 | Bump |
| `OTO1` | 1:1 Live Session With Anirudh (60 minutes) | ₹1,497 | ₹15,000 | Primary |

Total compare-at across the front-end cart: **₹22,997** against ₹3,094 actually charged.

## 2. GST

**18% GST is added on top of every line** — the front-end offer, all three order bumps
and the OTO session. ₹997 is charged as **₹1,176**.

Because the listed price and the charged price differ, **every surface that shows a price
has to say "+ GST"**. The sales page CTA carries the note *"Prices exclude 18% GST, added
at checkout."*

`GST_RATE = 0.18` is declared in **two** files — `api/_catalog.js` (bundled into the
serverless functions) and `src/data/gst.js` (bundled into the browser). They cannot import
from each other, so **if one moves the other must move with it**. The server value is the
one that decides what is actually charged.

> ⚠️ **Known stale doc.** The `## Pricing` section of `micro-offer-funnel/README.md` still
> says prices are "tax-**inclusive** … ₹997 is exactly what is charged". That is wrong and
> contradicts `api/_catalog.js`, `src/data/gst.js` and the on-page tax note. Prices are
> **ex-GST**. Fix the README, not the catalogue.

## 3. Every cart combination

Computed exactly as `priceCart()` does it: GST is `round(taxable × 0.18)` on the **cart
subtotal**, not per line.

### Front-end carts

| Cart | Subtotal | GST 18% | **Charged** |
| --- | --- | --- | --- |
| `FE` | ₹997 | ₹179 | **₹1,176** |
| `FE` + `OB1` | ₹1,596 | ₹287 | **₹1,883** |
| `FE` + `OB2` | ₹1,696 | ₹305 | **₹2,001** |
| `FE` + `OB3` | ₹1,796 | ₹323 | **₹2,119** |
| `FE` + `OB1` + `OB2` | ₹2,295 | ₹413 | **₹2,708** |
| `FE` + `OB1` + `OB3` | ₹2,395 | ₹431 | **₹2,826** |
| `FE` + `OB2` + `OB3` | ₹2,495 | ₹449 | **₹2,944** |
| `FE` + all three bumps | ₹3,094 | ₹557 | **₹3,651** |

### OTO cart

| Cart | Subtotal | GST 18% | **Charged** |
| --- | --- | --- | --- |
| `OTO1` | ₹1,497 | ₹269 | **₹1,766** |

### Maximum realisable value per buyer

| | Ex-GST | Inc. GST |
| --- | --- | --- |
| Front-end cart (all bumps) | ₹3,094 | ₹3,651 |
| OTO | ₹1,497 | ₹1,766 |
| **Total** | **₹4,591** | **₹5,417** |

That is **4.6× the ₹997 entry price** — the whole point of the bump-and-OTO structure.

## 4. Pricing logic

`priceCart(primaryKey, bumpKeys, couponCode)` in `api/_catalog.js`:

1. Reject any `primaryKey` not in `PRIMARY_KEYS` (`FE`, `OTO1`).
2. Add the primary item.
3. Add bump items **only** if the primary is `FE` — dedupe, and skip anything not in
   `BUMP_KEYS`.
4. Sum to a subtotal.
5. Apply a coupon, if any, to the **taxable value** — so GST is charged on what is
   actually paid for the goods, not on the pre-discount list price.
6. `gst = round(taxable × 0.18)`, `total = taxable + gst`.
7. Return `amountSmallest` in paise, because Razorpay takes the smallest currency unit.

### Discount types

| Type | Behaviour |
| --- | --- |
| `percent` | Takes a percentage off the subtotal, before GST |
| `fixed_off` | Subtracts an amount from the subtotal, before GST |
| `fixed_total` | **Overrides the gross outright.** The tax is derived back *out* of it rather than added on — so a ₹1 code charges exactly ₹1, not ₹1 + 18% |

**Floor:** Razorpay rejects anything under ₹1, so ₹1 is the floor on every path. Nothing
can reach zero — a "free" code is really a ₹1 code.

## 5. Coupons

There is **no visible coupon field** on either checkout. It was removed deliberately: the
funnel does not run public discounts, and an empty "Have a coupon?" box mostly teaches
buyers to leave and go hunting for one.

A code may still be passed on the URL as `?coupon=CODE`. This is not a security boundary
and does not need to be — the server has always been the only thing that decides whether a
code is real, what it is worth, and how many times it may be used.

### Active coupons

| Code | Type | Value | Purpose |
| --- | --- | --- | --- |
| `TESTFUNNEL1` | `fixed_total` | ₹1 | Internal end-to-end test of the live funnel: real Razorpay flow, real portal provisioning, ₹1 charged |

`TESTFUNNEL1` exercises the whole chain — order → signature check → portal account →
entitlements → welcome email — for one rupee.

> **Operational rule:** keep max redemptions low, rotate the code if it ever leaks, delete
> or rename it before scaling ad spend, and **never put it in copy**. It is a live discount
> on a live checkout.

## 6. B2B invoicing (GSTIN)

Supplying a GSTIN changes **only whether an invoice is raised**. It never changes the
amount charged.

| Field | Detail |
| --- | --- |
| GSTIN format | 15 characters: 2 state digits + PAN + entity + `Z` + checksum |
| Validation | `GSTIN_RE` in `src/data/gst.js` |
| State code fallback | The first two digits of the GSTIN **are** the state code |
| Captured | Business name, business state, business state code |

**Why state codes matter:** the invoice generator compares the buyer's state code with the
seller's to decide **CGST + SGST** (same state) vs **IGST** (inter-state). Getting it wrong
produces a legally incorrect invoice, which is why the state list is kept identical to the
main course's rather than re-typed.

The field set and state codes are copied from the course checkout so that
`outbound-training-LP/api/admin/generate-invoices.js` can raise invoices for micro-funnel
orders without a second code path.

## 7. Display vs. charge

Two things quote a price, and they must agree:

| File | Bundled into | Used for |
| --- | --- | --- |
| `api/_catalog.js` | Serverless functions | **The authority.** What is actually charged |
| `src/data/prices.js` | Browser | Rendering a figure before the server has answered; valuing a `ViewContent` that has no cart |

`localQuote()` in `src/data/gst.js` mirrors `priceCart()` exactly, **including its
rounding**, so the buyer sees the real payable figure from the moment the checkout opens
rather than a pre-tax number that jumps when the gateway loads.

`prices.js` exists because `FE_PRICE` and `OTO_PRICE` were previously declared in both
checkout modals — which is exactly how a price ends up changed in one place and not the other.

## 8. Value anchoring on the page

| Element | Anchor | Price |
| --- | --- | --- |
| Front-end offer stack | ₹9,997 | **Just ₹997** |
| Bonus 1 — AI ICP Engine | ₹5,000 | Included |
| Bonus 2 — Outbound Copywriting Skill | ₹7,000 | Included |
| Bonus 3 — Whimsical Implementation Map | ₹10,000 | Included |
| Bonus 4 — Cost + ROI Calculator | ₹4,000 | Included |
| Bonus 5 — Private VIP Community | Priceless | Included |
| OTO — 1:1 Live Session | ₹15,000 | **₹1,497** (90% off) |

Stated bonus value alone (₹26,000) is **26× the entry price**.
