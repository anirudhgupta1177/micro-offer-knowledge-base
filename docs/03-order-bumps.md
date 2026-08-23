# 03 — The Three Order Bumps

All three bumps are offered **only** on the front-end popup checkout, alongside `FE`.
They are never offered on the OTO checkout — a buyer who reaches the OTO has already
been shown them once and may own them, so `api/_catalog.js` ignores any bump key that
arrives with `OTO1` rather than charging for it.

Each is a single checkbox labelled **"YES! Add This To My Order!"**.

| Key | Product | Price | Anchor | Discount | Delivery |
| --- | --- | --- | --- | --- | --- |
| `OB1` | The Best-Performing Cold Email Copy Swipe File | ₹599 | ₹2,000 | 70% | Notion link |
| `OB2` | The 78-Page Outbound Implementation Guide | ₹699 | ₹4,000 | 83% | Claude artifact link |
| `OB3` | LinkedIn Outreach Automation Training | ₹799 | ₹7,000 | 89% | Member portal |

Combined bump value if all three are taken: **₹2,097 ex-GST** on top of the ₹997 front
end — a maximum front-end cart of **₹3,094 ex-GST / ₹3,651 inc. GST**.

---

## OB1 — The Best-Performing Cold Email Copy Swipe File

**₹599** · was ₹2,000

### The pitch

> Your targeting can be perfect and your campaign can still fail, because a great list
> means nothing if the words don't land. This is a bank of real cold emails that were
> **actually sent and actually got replies** — so instead of guessing whether your copy
> is good, you have proof of what already works to compare it against.

### What's inside

- Cold opens that actually get read
- **20+ real, sent emails**, annotated to show why each one worked
- Real performance data on select campaigns, so you're copying what's proven
- Spintext variations shown live, so one email becomes five
- A close match for almost any offer you're selling

### The close

> **IMPORTANT** — A cold email copywriter at this level charges thousands of dollars a
> month. This gives you the reference bank for a one-time small investment.

### Delivery

| Attribute | Value |
| --- | --- |
| Entitlement slug | `cold-email-swipe-file` |
| Delivered as | Notion page, emailed by n8n and listed on `/thank-you` |
| Link | https://navy-professor-355.notion.site/Best-Performing-Email-Copy-Examples-1cd26bb2645a46cab8e5cd970ef04259 |

The entitlement exists even though delivery is an external link. Without one, the bump
lived only on the thank-you page and in the welcome email — so a buyer who navigated away
or never received the mail had paid for something they could not reach again, and support
had nothing to grant them. The Offer Vault now carries it like anything else bought.

### Why it converts here

It attacks the objection that surfaces the instant someone commits to the front end:
*"the system is fine, but is my writing good enough?"* It is the cheapest of the three
bumps and the least effortful to consume.

---

## OB2 — The 78-Page Outbound Implementation Guide

**₹699** · was ₹4,000 · also referred to as the *Outbound Field Manual*

### The pitch

> This is **the 78-page document we keep open ourselves** while building campaigns for
> real clients — covering everything from targeting to infrastructure to what to fix when
> a campaign underperforms.

### What's inside

25 sections, covering:

- The exact ICP framework for building a target list that doesn't waste sends
- Every deliverability rule for domains, mailboxes and warm-up, so nothing burns
- The complete offer and copywriting rules, laid out step by step
- A full diagnostics section for what's broken and how to fix it
- Every number and benchmark in one place, so you're never guessing

### The close

> **Note** — This one-time offer disappears once you leave this page. Don't miss out.

### Delivery

| Attribute | Value |
| --- | --- |
| Entitlement slug | `outbound-implementation-guide` |
| Delivered as | Claude artifact, emailed by n8n and listed on `/thank-you` |
| Link | https://claude.ai/public/artifacts/d403a11f-86b5-42d3-b1d1-ba87f84b4e0f |

### Why it converts here

It solves the fear that arrives right after watching a 2-hour build: *"I'll lose the
thread the moment the video ends."* It is the reference layer under the video, and the
diagnostics section is what makes it re-openable months later.

> The same 78-page guide appears in the main course's offer stack at a stated value of
> ₹3,000. Here it is anchored at ₹4,000. Both are value anchors, not prices.

---

## OB3 — LinkedIn Outreach Automation Training

**₹799** · was ₹7,000 · **the highest-taking bump**

### The pitch

> **95% of people choose this upgrade** because they're already running cold email to a
> list, and LinkedIn is the exact same prospect, sitting right there, untouched. This
> training walks you through automating LinkedIn outreach so it runs alongside your email
> campaign, **doubling your touchpoints on contacts you've already paid to find**.

### What's inside

- Connection and message sequencing that doesn't look automated
- Safe daily limits so your account never gets flagged
- Account-safety rules that keep LinkedIn running long-term
- How to run LinkedIn and email in parallel, on the same list
- **98 minutes of training**, delivered instantly

### The close

> **NOTE** — Most people either skip LinkedIn entirely or risk their account running it
> wrong. This training is normally taught as part of a much larger program. Today, it's
> yours for a one-time investment of ₹799.

### Delivery

| Attribute | Value |
| --- | --- |
| Entitlement slug | `linkedin-mini-course` |
| Delivered as | Full course inside the member portal |
| Portal route | `/linkedin-mini-course` (and `/linkedin-mini-course/:partId`) |
| Runtime | 98 minutes |

This is the only bump delivered as portal content rather than a link, which is why it is
the only one that gets a real gated route.

### Why it converts here

It is the strongest of the three because it is **marginal-cost framing**: the buyer has
already paid to find these contacts, and LinkedIn is a second channel to the same list for
no additional sourcing cost. The economics do the persuading, not the copy.

### Creative note

The bump illustration deliberately carries **no LinkedIn brand mark** — it is an abstract
render of the mechanic (one contact list feeding two parallel sequences that converge),
built in `design/bump-linkedin.html`.

---

## Reporting on bumps

Every micro-offer order records what was actually bought, so resource delivery is
answerable after the fact:

```sql
select customer_email, amount, bump_keys, coupon_used,
       (select array_agg(offer_slug) from user_entitlements e
         where e.user_id = o.user_id) as portal_access
from orders o
where source = 'micro-offer-funnel'
  and 'OB3' = any(bump_keys);   -- everyone who took the LinkedIn training
```

`api/grant-access.js` writes `orders.items`, `orders.bump_keys`, `orders.coupon_used` and
`orders.source`, then grants the portal entitlements. The n8n workflow reads the same cart
and only mentions what was actually bought.
