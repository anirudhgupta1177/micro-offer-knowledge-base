# 03 — The Tool Stack

What the system runs on, phase by phase.

The stack is deliberately small. A big part of the argument in the session is that most
people over-tool outbound — stacking four data providers to fix a data problem that one
good source solves.

---

## Phase 1 · Infrastructure

| What you need | Role | Notes |
| --- | --- | --- |
| **Domain registrar** | Buying dedicated sending domains | Separate from your primary business domain. Never send cold from the domain that runs your business |
| **Mailbox provider (US IPs)** | Hosting the sending mailboxes | US IPs matter for deliverability into US inboxes |
| **DNS records — SPF, DKIM, DMARC** | Authenticating every sending domain | Set up **automatically** rather than by hand. Doing these wrong is one of the most common silent failures |
| **Warm-up** | Building sending reputation before you send anything real | 14 days. Not skippable, not compressible |
| **Instantly.ai** | Sending platform — campaigns, sequences, analytics | Where the campaign is configured, launched and measured |

> The exact registrar and mailbox provider used in the live build are named on screen in
> the session. Any provider that gives you dedicated domains and US-IP mailboxes with
> automated DNS will work — the ratio and the warm-up matter far more than the vendor.

---

## Phase 2 · Targeting

| What you need | Role | Notes |
| --- | --- | --- |
| **Claude** | Runs the AI ICP skill file | The skill file does the work; Claude is the environment it runs in |
| **AI ICP Engine** (skill file) | Business context → 5–10 ICPs with hard filters | See [02 — Resources](02-resources.md) |
| **Lead sourcing + verification tool** | Pulls the contact list *and* verifies the emails | One tool doing both is the point — see below |

### Why one tool instead of four

The common path: pull a list from a cheap data source, discover roughly **half the emails
bounce**, then bolt on three or four verification tools to clean it. You end up paying for
four subscriptions to fix one bad list.

A single source that pulls *and* verifies replaces that stack. **80% list accuracy is the
bar** — and 80% plus the right sequence beats an expensive four-tool stack every time.

---

## Phase 3 · Copy & launch

| What you need | Role | Notes |
| --- | --- | --- |
| **Claude** | Runs the copywriting skill file | |
| **Outbound Copywriting Skill** | ICP → sequence copy | Trained on real emails that got replies |
| **Spintext** | One email becomes five variations | Built into most sending platforms. This is what keeps volume from looking like volume |
| **Spam-check** | Testing inbox placement before launch | Run it **before** the first thousand sends, not after |
| **Instantly.ai** | Campaign configuration and launch | |
| **Loom** | The low-resistance ask itself | Offering a free Loom is often the small ask that replaces "book a call" |

---

## Optional · LinkedIn, in parallel

| What you need | Role |
| --- | --- |
| **LinkedIn** | The second channel — same list, no extra sourcing cost |
| **LinkedIn automation tool** | Connection and message sequencing, within safe daily limits |

Add this **after** email is live, not alongside setting it up. Two half-built channels
perform worse than one finished one.

---

## What it costs to run

The tools are a real recurring cost, and it's worth being honest about that up front:
domains, mailboxes and a sending platform are the actual cost of running outbound.

**Run the Cost + ROI Calculator before you buy anything.** Plug in your mailbox count and
lead volume and you'll see your real monthly cost and what the campaign needs to return to
justify it — before you spend a rupee.

The main variables:

| Cost driver | Scales with |
| --- | --- |
| Domains | How many mailboxes you're running (the ratio sets this) |
| Mailboxes | Your target daily send volume |
| Sending platform | Usually contacts or mailboxes, depending on the plan |
| Lead data | Volume of contacts pulled and verified |

Sending capacity scales roughly linearly with mailbox count — which is why the answer to
"how do I send more?" is more mailboxes, not more emails per mailbox.

---

## What you don't need

Two things worth naming explicitly, because they come up every time:

| Tool | Why it's not here |
| --- | --- |
| **Large multi-tool enrichment stacks** | The "you need a huge tech stack to run outbound" belief is the single most expensive myth in the list. 80% list accuracy and the right sequence outperforms it |
| **Four separate verification tools** | You only need these if your data source is bad. Fix the source instead |

You also don't need technical skills. Domain purchases, DNS, warm-up, ICP building and
copywriting are all walked through step by step, and the two AI skill files handle the
heaviest lifting.
