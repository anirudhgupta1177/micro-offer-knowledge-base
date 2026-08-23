# 10 — Links Index

Every URL in the micro-offer system, in one place.

---

## Live surfaces

| What | URL |
| --- | --- |
| Funnel sales page | https://course.intentledsales.com/micro/cold-email-system |
| Funnel short link (redirects) | https://course.intentledsales.com/micro |
| Member portal | https://course.intentledsales.com |
| Portal — Offer Vault | https://course.intentledsales.com/portal |
| Portal — login | https://course.intentledsales.com/login |
| Portal — forgot password | https://course.intentledsales.com/forgot-password |

The funnel is deployed as its own Vercel project (`micro-offer-funnel.vercel.app`, built
with `VITE_BASE_PATH=/micro/`) and **proxied** by the course project at `/micro`. A domain
can only be attached to one Vercel project, and `course.intentledsales.com` belongs to the
course — so the two stay separate, and a bad funnel deploy can never take the course
checkout offline.

## Funnel routes

| Route | Page |
| --- | --- |
| `/micro/cold-email-system` | Front-end sales page |
| `/micro/oto-1` | OTO 1 — 1:1 Live Session |
| `/micro/no-thanks` | Decline path + last-chance re-offer |
| `/micro/call-booking` | Cal.com hand-off |
| `/micro/thank-you` | Access links and next steps |
| `/micro/thank-you?booked=1` | Same, with "Your Call Is Scheduled" confirmed |

## Portal routes

| Route | Content | Entitlement required |
| --- | --- | --- |
| `/portal` | Offer Vault | Any |
| `/micro-course` | The 2-Hour Cold Email System | `outbound-micro-course` |
| `/micro-course/:partId` | An individual phase | `outbound-micro-course` |
| `/linkedin-mini-course` | LinkedIn Outreach Automation Training | `linkedin-mini-course` |
| `/linkedin-mini-course/:partId` | An individual part | `linkedin-mini-course` |

## Product delivery

| Product | URL |
| --- | --- |
| **OB1** — Cold Email Copy Swipe File | https://navy-professor-355.notion.site/Best-Performing-Email-Copy-Examples-1cd26bb2645a46cab8e5cd970ef04259 |
| **OB2** — 78-Page Implementation Guide | https://claude.ai/public/artifacts/d403a11f-86b5-42d3-b1d1-ba87f84b4e0f |
| **OB3** — LinkedIn Training | https://course.intentledsales.com/linkedin-mini-course |
| **FE** — Micro course | https://course.intentledsales.com/micro-course |
| **Bonus 5** — Private VIP Community | https://chat.whatsapp.com/L3ht1NZZvqqEEBlT3XML0b |
| **OTO1** — Booking | https://cal.com/anirudh-gupta/consulting-call |

## API endpoints

All served as Vercel serverless functions under `/micro/api/*`, so they proxy through the
same rule as the app and never collide with the course project's own `/api/*`.

| Endpoint | Method | Role |
| --- | --- | --- |
| `/micro/api/create-order` | POST | Prices the cart server-side and creates a Razorpay order |
| `/micro/api/verify-payment` | POST | HMAC-SHA256 signature verification |
| `/micro/api/grant-access` | POST | Creates the account, writes the order, grants entitlements, fires webhooks |
| `/micro/api/reconcile` | POST | Hourly cron — fulfils captured payments with no order row |

## Repositories

| Repo | Contains |
| --- | --- |
| https://github.com/anirudhgupta1177/micro-offer-funnel | The funnel app — sales page, checkout, OTO, thank-you, APIs |
| https://github.com/anirudhgupta1177/outbound-training-LP | The member portal, main course, admin portal |
| *(this repo)* | Documentation and resource index |

## Operations

| What | Where |
| --- | --- |
| n8n fulfilment workflow | "Micro Offer — Fulfilment" · id `VKXE0JCwlSymA6l8` |
| Meta dataset & CAPI tokens | business.facebook.com → Events Manager |
| Pabbly Connect | One reporting workflow per product (`FE`, `OB1`, `OB2`, `OB3`, `OTO1`) |
| Razorpay | Same credentials as the course checkout |
| Supabase | Same project as the course — one account across both products |

## Contact

| What | Value |
| --- | --- |
| Support email | agent@theorganicbuzz.com |
| Legal entity | The Organic Buzz |
| Brand | IntentLedSales |
| Instructor | Anirudh Gupta ("Ani") |

## Environment variables

Names only — values live in Vercel, never in a repository.

### Server-only (never `VITE_` prefixed)

| Variable | Purpose |
| --- | --- |
| `RAZORPAY_KEY_ID` | Razorpay credentials — same as the course checkout |
| `RAZORPAY_KEY_SECRET` | Signs orders and verifies payment signatures |
| `SUPABASE_URL` | Portal project — same as the course |
| `SUPABASE_SERVICE_ROLE_KEY` | Creates buyer accounts and grants entitlements |
| `N8N_WEBHOOK_URL` | Fulfilment workflow endpoint |
| `N8N_WEBHOOK_SECRET` | Shared secret; must match on the n8n side |
| `META_CAPI_TOKEN` | Server-side conversion events |
| `META_DATASET_ID` | Optional — defaults to the browser pixel's dataset |
| `META_CAPI_TEST_CODE` | Optional — routes events to the Test Events tab |
| `PABBLY_WEBHOOK_FE` / `_OB1` / `_OB2` / `_OB3` / `_OTO1` | Sales reporting, one per product |
| `RECONCILE_SECRET` | Manual trigger for the reconciliation job |
| `CRON_SECRET` | Set by Vercel for scheduled invocations |

### Client (`VITE_` prefixed — **these are public**)

| Variable | Purpose |
| --- | --- |
| `VITE_PORTAL_URL` | Portal origin. Must match `api/grant-access.js`, or buyers and their welcome email go to different domains |
| `VITE_BOOKING_URL` | Cal.com link for the 1:1 session |
| `VITE_COMMUNITY_URL` | WhatsApp VIP community invite |
| `VITE_BASE_PATH` | `/micro/` when proxied under a sub-path. Unset for a standalone root deploy |
| `VITE_ALLOW_PREVIEW` | `1` on staging only — lets `?preview=1` bypass purchase guards |
| `VITE_META_DATASET_ID` | Meta pixel dataset. **No default** — unset means no pixel loads |
| `VITE_META_DISABLED` | `1` on staging, so it cannot pollute live attribution |

> ⚠️ `RAZORPAY_KEY_SECRET`, `SUPABASE_SERVICE_ROLE_KEY` and `META_CAPI_TOKEN` must **never**
> carry a `VITE_` prefix — Vite inlines `VITE_*` values into the browser bundle at build
> time, which would publish them.

> ⚠️ **`VITE_ALLOW_PREVIEW` must never be set in production.** Left ungated, a query string
> anyone could paste would hand non-buyers the community invite and the paid delivery links.
