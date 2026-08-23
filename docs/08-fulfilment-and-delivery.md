# 08 — Fulfilment & Delivery

What happens between a verified payment and the buyer having everything they paid for.

---

## 1. The delivery matrix

| Key | Product | Entitlement slug | Delivered as | Reachable at |
| --- | --- | --- | --- | --- |
| `FE` | The 2-Hour Cold Email System | `outbound-micro-course` | Portal course, 3 phases | `/micro-course` |
| `OB1` | Cold Email Copy Swipe File | `cold-email-swipe-file` | Notion page | External link + Offer Vault |
| `OB2` | 78-Page Implementation Guide | `outbound-implementation-guide` | Claude artifact | External link + Offer Vault |
| `OB3` | LinkedIn Outreach Automation | `linkedin-mini-course` | Portal course, 98 min | `/linkedin-mini-course` |
| `OTO1` | 1:1 Live Session | *(none)* | Cal.com booking → Zoom → recording | Cal.com |
| Bonus 1–4 | ICP skill, copy skill, map, calculator | *(rides on `FE`)* | Portal resources | `/micro-course` |
| Bonus 5 | Private VIP Community | *(rides on `FE`)* | WhatsApp invite | `/thank-you`, `/no-thanks`, email |

`OTO1` grants no entitlement because the deliverable is a human on a call, not content.
It is tracked instead through the portal's `consult.sessions_purchased` counter.

## 2. Why the document bumps still get entitlements

`OB1` and `OB2` are external links, so strictly they need no portal grant. They get one
anyway:

> Without an entitlement they existed only on the thank-you page and in the welcome email
> — so a buyer who navigated away or never got the mail had paid for something they could
> not reach again, and support had nothing to grant them. The vault now carries them like
> anything else bought.

## 3. The fulfilment sequence

```
Razorpay payment captured
        │
        ▼
POST /api/verify-payment          HMAC-SHA256 over order_id|payment_id,
        │                          constant-time compare
        │ verified
        ▼
POST /api/grant-access
        │
        ├─▶ Create (or find) the Supabase auth account
        │     └─ 18 URL-safe chars from a CSPRNG as the password
        │
        ├─▶ Write the order row
        │     orders.items · orders.bump_keys · orders.coupon_used · orders.source
        │
        ├─▶ Grant entitlements  (upsert on user_id, offer_slug)
        │     FE → outbound-micro-course
        │     OB1 → cold-email-swipe-file
        │     OB2 → outbound-implementation-guide
        │     OB3 → linkedin-mini-course
        │
        ├─▶ Fire the n8n webhook          (best effort)
        │     └─ welcome email + internal notification
        │
        ├─▶ Send the Meta CAPI Purchase   (best effort)
        │     └─ deduped against the browser pixel by shared event_id
        │
        └─▶ Fire the Pabbly Connect webhook per product   (best effort)
        │
        ▼
Redirect to /oto-1
```

**Best-effort steps never block fulfilment.** Account creation, entitlements and the
welcome email must not fail because an ads API was slow or down, so every tracking failure
is logged and swallowed.

## 4. The n8n workflow

**"Micro Offer — Fulfilment"** — workflow id `VKXE0JCwlSymA6l8`.

| Node | Type | Role |
| --- | --- | --- |
| Purchase Webhook | Webhook | Receives the verified cart from `api/grant-access.js` |
| Validate & Build Email | Code | Validates the payload; composes the welcome email from what was actually bought |
| Has Valid Email? | If | Branches on whether a usable email address is present |
| Send Welcome Email | Gmail | To the buyer — login details plus every purchased link |
| Notify Internally | Gmail | Internal sale notification |
| Respond OK | Respond to Webhook | 200 |
| Respond Bad Request | Respond to Webhook | 400 |

The workflow reads the same cart the server priced, so **the email only mentions what was
actually bought**. A buyer who skipped `OB3` is never sent a LinkedIn link.

**Security:** the webhook is authenticated by a shared secret that must match on both
sides. The workflow is optional — access is granted with or without it.

## 5. Reconciliation

`api/reconcile.js` runs hourly on Vercel Cron. It finds **captured payments with no order
row** and fulfils them.

This is the safety net for the case that matters most: money taken, nothing delivered. It
is authenticated by a shared secret (`RECONCILE_SECRET`); Vercel sets `CRON_SECRET` itself
for scheduled invocations.

## 6. The portal

| Attribute | Value |
| --- | --- |
| Origin | `https://course.intentledsales.com` |
| Vault | `/portal` |
| Login | `/login` |
| Forgot password | `/forgot-password` |
| Micro course | `/micro-course` · `/micro-course/:partId` |
| LinkedIn mini course | `/linkedin-mini-course` · `/linkedin-mini-course/:partId` |

Every course route is wrapped in `ProtectedRoute` (authenticated?) then `OfferGate`
(entitled?). **Deep linking is safe before sign-in** — `ProtectedRoute` remembers the
intended destination and sends the buyer there after login rather than dropping them on
the vault.

> **Config trap, now fixed:** `VITE_PORTAL_URL` used to default to
> `portal.intentledsales.com` in the funnel and `course.intentledsales.com` in
> `grant-access.js`. With the variable unset, the funnel sent buyers to one domain and
> their welcome email to another. Both now default to `course.intentledsales.com`.

## 7. What the buyer sees on `/thank-you`

> **You're In. Here's Everything You Just Unlocked.**
> Your access details are on their way to your inbox right now. Bookmark this page — every
> link below works immediately.

Plus a spam-folder prompt: *"Can't find the email? Check spam and promotions, then add
{email} to your contacts so nothing else gets filtered."*

If the OTO was purchased and Cal.com returned with `?booked=1`:

> **Your 1:1 Session Is Confirmed** — pick the slot that works for you below. You'll get a
> calendar invite and a Zoom link the moment you book.

### The three next steps

| # | Instruction | Why |
| --- | --- | --- |
| 1 | **Watch Phase 1 first, and build as you watch.** | Do not binge all three phases. Phase 1 sets up domains and mailboxes, and the **14-day warm-up starts the moment you finish it** — so the earlier you do it, the earlier you can send |
| 2 | **Run the ICP skill before you touch copy.** | Feed it your business context and let it hand you the filters. **Copy written against a vague list is what kills most first campaigns** |
| 3 | **Post an intro in the VIP community.** | Tell everyone what you sell and who you're targeting. That's usually where the first useful correction comes from |

These are sequenced against the real constraint in the system — the 14-day warm-up is the
long pole, so it gets started first.

**Support:** *"Email agent@theorganicbuzz.com and a real person will get back to you."*

## 8. Reporting

Every order records what was actually bought:

```sql
select customer_email, amount, bump_keys, coupon_used,
       (select array_agg(offer_slug) from user_entitlements e
         where e.user_id = o.user_id) as portal_access
from orders o
where source = 'micro-offer-funnel'
  and 'OB3' = any(bump_keys);   -- everyone who took the LinkedIn training
```

| Column | Meaning |
| --- | --- |
| `orders.source` | Which funnel — `micro-offer-funnel` |
| `orders.items` | The full priced cart |
| `orders.bump_keys` | Which bumps were taken |
| `orders.coupon_used` | Which coupon, if any |
| Product line | `outbound-micro-course` (has `FE`) or `micro-oto-session` (has `OTO1`) |

## 9. Failure handling

| Failure | Behaviour |
| --- | --- |
| Payment succeeds, signature fails | Buyer is shown their **payment ID and the support address** — never silently granted or denied |
| Entitlement write fails | **Fails loud.** A silent failure locks a paying buyer out |
| n8n webhook fails | Logged and swallowed. Access is already granted; the Offer Vault is the durable copy |
| Meta CAPI fails or times out | Logged and swallowed. 4-second abort |
| Pabbly webhook fails | Logged and swallowed |
| Order row missing entirely | Caught by the hourly reconciliation job |

> ⚠️ **Known stale assumption in the course repo.**
> `outbound-training-LP/api/create-contact.js` says its entitlement write is
> "non-blocking … Outbound Mastery is also flagged unlocked-by-default." **That is no
> longer true** — Outbound Mastery is now locked behind an entitlement so micro-offer
> buyers cannot reach it. A failed write there genuinely locks a course buyer out. That
> grant should be made fail-loud, the way the funnel's `api/grant-access.js` does it.

## 10. Live delivery links

| Item | URL |
| --- | --- |
| OB1 — Swipe File | https://navy-professor-355.notion.site/Best-Performing-Email-Copy-Examples-1cd26bb2645a46cab8e5cd970ef04259 |
| OB2 — 78-Page Guide | https://claude.ai/public/artifacts/d403a11f-86b5-42d3-b1d1-ba87f84b4e0f |
| OB3 — LinkedIn Training | `course.intentledsales.com/linkedin-mini-course` (portal) |
| Bonus 5 — VIP Community | https://chat.whatsapp.com/L3ht1NZZvqqEEBlT3XML0b |
| OTO — Booking | https://cal.com/anirudh-gupta/consulting-call |
| Micro course | `course.intentledsales.com/micro-course` (portal) |
