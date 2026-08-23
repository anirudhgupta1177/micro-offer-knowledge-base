# 04 — Implementation Checklist

A sequenced list to work through after the session.

**The order is the point.** Phases 2 and 3 run *while* the warm-up is going, not after it —
that's what turns a six-week timeline into a two-week one.

---

## Before you spend anything

- [ ] Run the **Cost + ROI Calculator**. Enter your target daily send volume and lead
      count. Know your monthly number before you buy a domain.
- [ ] Write down what you sell and who you sell it to, in one sentence each. You'll feed
      this to the ICP skill.
- [ ] Confirm this fits: are your buyers reachable at a **work email address**? If you sell
      to consumers or to local offline businesses, stop here — this isn't the right system.
- [ ] [Join the community](https://chat.whatsapp.com/L3ht1NZZvqqEEBlT3XML0b) and post an
      intro: what you sell, who you're targeting, what you've built so far.

---

## Day 1 — Phase 1 · Build the infrastructure

**Do this first, today.** The 14-day warm-up clock starts when you finish, and nothing
downstream can happen until it's done.

- [ ] Buy **dedicated sending domains** — separate from your primary business domain
- [ ] Create **US-IP mailboxes** on those domains
- [ ] Apply the **domain-to-mailbox ratio** from the session. Don't overload one domain
- [ ] Set **SPF, DKIM and DMARC** on every sending domain — automatically, not by hand
- [ ] Verify all three records resolve correctly before moving on
- [ ] **Start the 14-day warm-up** ⏰ ← *note today's date; you can launch 14 days from here*
- [ ] Confirm nothing points at your primary domain

> **The single most common mistake:** sending real campaign email during the warm-up
> window because the setup "looks ready". It isn't. Let the 14 days run.

---

## Days 1–3 — Phase 2 · Build the target list

Runs in parallel with the warm-up.

- [ ] Feed your business context into the **AI ICP Engine**
- [ ] Review the **5–10 ICPs** it returns. Cut the ones that don't feel real
- [ ] For each ICP you keep, confirm you have: the pain point, the buying logic, and hard
      filters you can actually scrape against
- [ ] Pick **one ICP to start with**. Not all of them — one
- [ ] Scrape the list against that ICP's filters
- [ ] Verify the emails from the same source
- [ ] Check accuracy. **~80% is the bar.** Below that, tighten the filters rather than
      adding another tool

> **The single most common mistake:** running all 5–10 ICPs at once. One segment, launched
> and measured, teaches you more than five launched blind.

---

## Days 3–5 — Phase 3 · Write and prepare

Still running in parallel with the warm-up.

- [ ] Feed the chosen ICP into the **Outbound Copywriting Skill**
- [ ] Check the output against **one rule**: does the first email ask for a call? If yes,
      rewrite it
- [ ] Replace the ask with something small — a free Loom, a short pilot, a resource
- [ ] Compare your copy against the [swipe file](https://navy-professor-355.notion.site/Best-Performing-Email-Copy-Examples-1cd26bb2645a46cab8e5cd970ef04259).
      Not to copy it — to check yours clears the same bar
- [ ] Build **spintext variations** so one email becomes five
- [ ] Run a **spam-check** and confirm inbox placement
- [ ] Load the sequence into the sending platform
- [ ] Set daily sending limits per mailbox
- [ ] Post your first email in the community for a second opinion before you send it

---

## Day 15 — Launch

- [ ] Confirm the **14-day warm-up is complete**
- [ ] Confirm SPF, DKIM and DMARC still resolve
- [ ] Send a test to your own inbox and check where it lands
- [ ] **Launch** to your first segment
- [ ] Keep warm-up running alongside the live campaign

---

## After launch

- [ ] Watch **delivery rate** first. Below ~95% means an infrastructure problem, not a copy
      problem — go back to Phase 1
- [ ] Then **reply rate**. Low replies with good delivery is a targeting or copy problem —
      go back to Phase 2, then 3
- [ ] Don't change more than one variable at a time
- [ ] Give it a full sequence cycle before judging it
- [ ] Use the **diagnostics section** of the
      [implementation guide](https://claude.ai/public/artifacts/d403a11f-86b5-42d3-b1d1-ba87f84b4e0f)
      to work out which layer is at fault
- [ ] Once email is running steadily, add **LinkedIn on the same list**

---

## Diagnosing what's wrong

Work top-down. Each layer depends on the one above it, so fixing copy while deliverability
is broken changes nothing.

| Symptom | Most likely layer | Where to look |
| --- | --- | --- |
| Low delivery rate | **Phase 1** — infrastructure | DNS records, warm-up length, domain-to-mailbox ratio |
| Good delivery, low open rate | **Phase 1 / 3** | Sending reputation, or subject lines |
| Good opens, no replies | **Phase 2 / 3** — list or ask | Is the ICP real? Is the first email asking for a call? |
| Replies, but all unqualified | **Phase 2** — targeting | The filters are too loose |
| Everything drops off suddenly | **Phase 1** — a domain got flagged | Check domain health; pause and diagnose before sending more |

---

## Realistic timeline

| When | What |
| --- | --- |
| Day 1 | Infrastructure built, warm-up started |
| Days 1–5 | List built, copy written, sequence loaded |
| Day 15 | Campaign launches |
| Days 15–20 | First replies land |
| Day 30+ | Infrastructure fully matured; volume can scale |

The build itself is one sitting. **Infrastructure maturity is the part that takes real
time** — roughly 30 days for domains to age and mailboxes to warm properly. Nothing about
this system is instant, and anyone telling you otherwise is selling you a burned domain.
