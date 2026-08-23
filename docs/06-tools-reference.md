# 06 — Tools Reference

Every tool referenced anywhere in the micro-offer system, in two groups:

- **[Part A](#part-a--the-outbound-stack-taught-in-the-training)** — the outbound stack the training teaches the buyer to build
- **[Part B](#part-b--the-stack-that-runs-the-funnel)** — the stack that sells, delivers and tracks the offer

A third section, **[Part C](#part-c--tools-named-but-not-taught)**, covers tools the copy
names in order to argue *against* them.

> **Sourcing.** Where the repositories name a tool explicitly, it is stated plainly.
> Where the training refers to a tool by role but never names it in any file, it is marked
> **`TBD — not recorded`**. Nothing here is inferred from outside the repositories.

---

## Part A — The outbound stack (taught in the training)

### Phase 1 — Infrastructure

| Tool / component | Role | Named in repo? | Notes |
| --- | --- | --- | --- |
| **Domain registrar** | Buying dedicated sending domains, separate from the primary business domain | Role only — **TBD** | The exact domain-to-mailbox ratio is taught live |
| **Mailbox provider (US IPs)** | Hosting the sending mailboxes | Role only — **TBD** | US-IP mailboxes are a stated requirement |
| **DNS: SPF, DKIM, DMARC** | Authentication records for every sending domain | Yes | Taught as **automatically handled**, not configured by hand |
| **Warm-up** | 14-day mailbox warm-up before any campaign sends | Yes | Starts the moment Phase 1 finishes — the reason buyers are told to build Phase 1 first |
| **Instantly.ai** | Sending platform, campaign management, analytics | **Yes** | Also the instructor's employer; used for the live build and the proof screenshots |

**Target output of Phase 1:** infrastructure capable of **1,000+ emails/day** without ever
touching the primary domain's reputation. The page argues **40+ warmed mailboxes are safer
than 1 inbox sending 50 emails/day**.

### Phase 2 — Targeting

| Tool / component | Role | Named in repo? | Notes |
| --- | --- | --- | --- |
| **Claude** (Anthropic) | Runs the AI ICP Engine skill file | **Yes** | "the outbound AI skill file generating ICPs and copy inside Claude" |
| **AI ICP Engine** (Bonus 1) | Claude skill file → 5–10 ICPs with pain points, buying logic, hard filters | **Yes** | Included free with `FE`. See [04 — Bonuses](04-bonuses.md) |
| **Lead sourcing + verification tool** | Pulls and verifies the contact list against the ICP filters | Role only — **TBD** | Described as **"the single tool that replaces all of them"** — i.e. replaces Apollo plus 3–4 verification tools. The name is shown on screen in the training but is not written into any file in the repositories |

**Governing claim:** 80% list accuracy plus the right sequence beats an expensive 4-tool
stack every time. Apollo's data quality is cited as what forces people into 3–4 extra
tools and a ~50% bad-email rate.

### Phase 3 — Copy & launch

| Tool / component | Role | Named in repo? | Notes |
| --- | --- | --- | --- |
| **Claude** (Anthropic) | Runs the Outbound Copywriting skill file | **Yes** | |
| **Outbound Copywriting Skill** (Bonus 2) | ICP → sequence copy, trained on real emails that got replies | **Yes** | Included free with `FE` |
| **Spintext** | One email becomes five variations | **Yes** | Taught as a deliverability measure at volume |
| **Spam-check** | Pre-launch inbox-placement check | Role only — **TBD** | "the spintext and spam-check process that keeps you out of the spam folder even at high volume" |
| **Instantly.ai** | Campaign configuration and launch | **Yes** | "the real client campaign being configured and launched inside Instantly" |
| **Loom** | The *low-resistance ask* — offering a free Loom instead of a call | **Yes** | Also the video host for the training itself |

**Copy rule:** never ask for a call on a first email. Ask for something small — a free
Loom, a quick pilot.

### Bonus tooling

| Tool | Role | Bonus |
| --- | --- | --- |
| **Claude** (skill files) | The two AI skills that do the heavy lifting | 1 and 2 |
| **Whimsical** | The implementation map covering all three phases, in order | 3 |
| **Spreadsheet** (cost + ROI calculator) | Mailbox count + lead volume → real monthly cost and ROI | 4 |
| **WhatsApp** | The private VIP community | 5 |

### OB3 — LinkedIn stack

| Tool / component | Role | Named in repo? | Notes |
| --- | --- | --- | --- |
| **LinkedIn** | The second channel, run in parallel with email on the same list | **Yes** | |
| **LinkedIn automation tool** | Connection + message sequencing, safe daily limits | Role only — **TBD** | The bump illustration deliberately carries no LinkedIn brand mark |

Covered in the 98-minute training: sequencing that doesn't look automated, safe daily
limits, account-safety rules, running LinkedIn and email in parallel on one list.

### Cost of running the stack

The tools are a **real recurring cost, separate from the ₹997**. The FAQ is explicit:

> "You'll need domains, mailboxes and a sending platform — that's the actual cost of
> running outbound, and it's separate from what you pay here. The exact stack is picked
> out for you during the build, and **Bonus #4, the Cold Email Cost + ROI Calculator**, is
> the same one used for every number in the video."

The calculator is meant to be run **before buying a single domain**.

---

## Part B — The stack that runs the funnel

### Commerce

| Tool | Role | Notes |
| --- | --- | --- |
| **Razorpay** | Sole payment provider | Orders created with `payment_capture: 1`; payment verified by HMAC-SHA256 over `order_id\|payment_id`, compared in constant time. Minimum charge ₹1 |
| **Supabase** | Auth, member accounts, entitlements, orders | Same project as the main course, so a buyer of both has one account |
| **Vercel** | Hosting for the SPA and the serverless `/api/*` functions | The funnel is a separate Vercel project, proxied by the course project at `/micro` |

### Fulfilment

| Tool | Role | Notes |
| --- | --- | --- |
| **n8n** | Fulfilment workflow — *"Micro Offer — Fulfilment"* | Welcome email + internal notification. Optional: access is granted with or without it |
| **Gmail** | Send transport for both n8n emails | |
| **Notion** | Hosts the OB1 swipe file | External link, emailed and listed on `/thank-you` |
| **Claude Artifacts** | Hosts the OB2 78-page guide | Public artifact link |
| **Cal.com** | Booking for the OTO 1:1 session | Redirects to `/thank-you?booked=1` on booking; embedded in an iframe |
| **Zoom** | Where the 1:1 session actually happens | |
| **WhatsApp** | The private VIP community | |
| **Loom** | Video hosting for the training and the sales VSLs | |

### Tracking & reporting

| Tool | Role | Notes |
| --- | --- | --- |
| **Meta Pixel** | Browser-side conversion tracking | Fails closed — no dataset id means no pixel loads, deliberately |
| **Meta Conversions API** | Server-side copy of every conversion | Sent from `api/grant-access.js` after signature verification. Best-effort: fulfilment never fails because an ads API was slow. Deduplicated against the browser pixel by a shared `event_id` |
| **Meta Events Manager** | Where datasets and CAPI tokens are managed | A test-event code routes events to the test bucket instead of live attribution |
| **Pabbly Connect** | Sales reporting webhooks, one workflow per product | `FE`, `OB1`, `OB2`, `OB3`, `OTO1` each have their own |
| **Vercel Cron** | Hourly reconciliation job | Finds captured payments with no order row and fulfils them |

> **Tracking note:** the funnel once briefly reported into a dataset owned by an outside
> ads agency. There is now no default dataset id anywhere in the source — an unset value
> means no pixel loads at all. Losing tracking is recoverable; tracking into someone
> else's ad account is not.

### Build & design

| Tool | Role |
| --- | --- |
| **React 19** + **Vite 7** | SPA framework and build tool |
| **Tailwind CSS v4** | Styling, with brand tokens in an `@theme` block |
| **React Router 7** | Routing, base-path aware for the `/micro` proxy |
| **Framer Motion** | Scroll reveals and transitions |
| **Lucide React** | Icon set |
| **ESLint** | Linting |

**Brand system** — from `IntentLedSales_Brand_Assets.pdf` v1.0:

| Token | Value |
| --- | --- |
| Background | `#0A0A0F` (near-black) |
| Accent | `#22D3EE` (cyan) — used sparingly, for CTAs and emphasis |
| Surface | `#111118` |
| Card | `#1A1A24` |
| Headings | Plus Jakarta Sans (700/600) |
| Body | Inter (400/500) |
| Editorial accent | Playfair Display |
| Borders | `rgba(255,255,255,0.05)` |

---

## Part C — Tools named but not taught

These appear in the copy specifically as the thing the system replaces or avoids.

| Tool | How it's positioned |
| --- | --- |
| **Apollo** | "Why Apollo's data quality forces you into 3–4 extra tools and the single tool that replaces all of them with verified emails." Cited as the source of a ~50% bad-email rate |
| **Clay** | "You need a huge tech stack like Clay to run outbound" is listed as a **myth**. The counter-position: 80% list accuracy and the right sequence beats an expensive stack every time |

> **Note for content reuse:** the wider IntentLedSales course *does* teach Clay,
> Make.com, n8n, Smartlead, Apify, PhantomBuster, HeyReach, Expandi, Findymail, Sales
> Navigator, Cursor + Claude Code and others. Those belong to a different, larger product.
> Do not pull them into micro-course material — the micro course's positioning is
> explicitly that you do **not** need that stack, and mixing them contradicts the sales page.

---

## Quick index — every tool, alphabetical

| Tool | Group | Where it appears |
| --- | --- | --- |
| Apollo | C | Named as what gets replaced |
| Cal.com | B | OTO booking |
| Claude (Anthropic) | A | The two AI skill files (Bonuses 1 & 2), Phases 2 and 3 |
| Claude Artifacts | B | OB2 delivery |
| Clay | C | Named as the stack you don't need |
| ESLint | B | Build |
| Framer Motion | B | Build |
| Gmail | B | n8n send transport |
| Instantly.ai | A | Phases 1 and 3 — sending, launch, analytics |
| LinkedIn | A | OB3 |
| Loom | A, B | The low-resistance ask; training video host |
| Lucide React | B | Build |
| Meta CAPI / Pixel / Events Manager | B | Conversion tracking |
| n8n | B | Fulfilment workflow |
| Notion | B | OB1 delivery |
| Pabbly Connect | B | Sales reporting |
| Razorpay | B | Payments |
| React / Vite / Tailwind / React Router | B | Build |
| Supabase | B | Accounts and entitlements |
| Vercel (+ Cron) | B | Hosting, reconciliation |
| WhatsApp | A, B | Bonus 5 — VIP community |
| Whimsical | A | Bonus 3 — implementation map |
| Zoom | B | The 1:1 session |
| *Domain registrar* | A | **TBD — not recorded** |
| *Mailbox provider (US IP)* | A | **TBD — not recorded** |
| *Lead sourcing + verification tool* | A | **TBD — not recorded** |
| *Spam-check tool* | A | **TBD — not recorded** |
| *LinkedIn automation tool* | A | **TBD — not recorded** |

The five `TBD` entries are named on screen inside the training but are not written into
any file in the funnel or portal repositories. Filling them in requires watching the
recording — see [11 — Source map](11-source-map.md).
