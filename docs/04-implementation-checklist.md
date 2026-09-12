# 04 - Implementation checklist

Work down this list in order. **The order is the point.** Steps 2, 3 and 4 run
*while* the warm-up is going, which is what turns six weeks into two.

---

## Before you spend anything

- [ ] Work out the monthly cost. Three tools, roughly ₹26,500 a month.
- [ ] Write down what you sell and who buys it, one sentence each. Claude needs this.
- [ ] Confirm this fits: **is your buyer reachable at a work email address?**
      If you sell to consumers or to small local shops, stop here.
- [ ] `cp .env.example .env` and paste in the three keys.

---

## Day 1 - Step 1, set up sending

**Do this first, today.** The 14 day clock starts when you finish, and nothing
downstream can launch until it is done.

- [ ] Buy 3 or 4 **new website names**, separate from your business name
- [ ] Create **3 mailboxes per name**, on US servers
- [ ] Let InboxKit write **SPF, DKIM, DMARC and MX**. Never by hand
- [ ] Confirm all four records resolve before moving on
- [ ] **Start the 14 day warm-up.** Note today's date, you can launch 14 days from here
- [ ] Pick ONE warm-up source, InboxKit's or Instantly's. Never both
- [ ] Confirm nothing points at your main business name

> **The most common mistake:** sending real campaign email during the warm-up
> because the setup "looks ready". It looks ready on day three. It is not.

---

## Days 1-3 - Step 2, who and what

Runs in parallel with the warm-up.

- [ ] Give Claude your business context, get **5 to 10 types of buyer** back
- [ ] Cut the ones that do not feel real
- [ ] For each one you keep, confirm you have: the pain, the buying logic, and
      **filters you can actually search against**
- [ ] **Pick one** to start with. Not all of them. One
- [ ] Write the emails for that one, using the three part structure
- [ ] Check it against one rule: **does email one ask for a call?** If yes, rewrite
- [ ] Confirm every email is **under 100 words**
- [ ] Run the copy scan: `python3 skills/write-the-copy/scripts/copy_qa.py your_copy.txt`

> **The most common mistake:** running all ten buyer types at once. One segment,
> launched and measured, teaches you more than five launched blind.

---

## Days 3-5 - Step 3, build the list

- [ ] Put the filters into the count. **It is free**
- [ ] Wrong number? Change a filter and count again. Still free
- [ ] Only when the count looks right, pull the list
- [ ] Let the same tool find and check the addresses
- [ ] Check accuracy. **8 in 10 is the bar.** Below that, tighten filters rather
      than adding another tool

```bash
S=skills/build-the-list/scripts/enrich_so.py
python3 $S count --title "Director" --city Ahmedabad
python3 $S build --title "Director" "Operations Manager" \
                 --city Ahmedabad --limit 75 --out leads.csv --free-only
```

> **The most common mistake:** buying a cheap list from a data seller. Half the
> addresses bounce, and bouncing is what gets your own addresses blocked.

---

## Days 5-8 - Step 4, load the campaign

Still in parallel with the warm-up.

- [ ] Connect the mailboxes from step 1 into Instantly
- [ ] Load the sequence: email, wait 3 days, email, wait 4 days, email
- [ ] Add **five spintax versions** of each email
- [ ] **Turn open tracking OFF. Turn click tracking OFF**
- [ ] Set the sending window to **the prospect's** working hours
- [ ] Set the daily limit to around **30 per address**
- [ ] Run a **spam test** and confirm it lands in the inbox
- [ ] Load the leads **last.** Removing them afterwards is painful
- [ ] Run the pre-launch check

---

## Day 15 - Launch

- [ ] Confirm the **14 day warm-up is complete**, not nearly complete
- [ ] Confirm SPF, DKIM and DMARC still resolve
- [ ] Send one email to your own inbox and see where it lands
- [ ] **Launch to one group only**
- [ ] Keep the warm-up running alongside the live campaign

---

## After launch

- [ ] Watch **delivery rate** first. Below 95% is a step 1 problem, not a copy problem
- [ ] Then **reply rate.** Good delivery with low replies is a step 2 or 3 problem
- [ ] **Reply to every reply within a few hours.** Speed is most of the win
- [ ] Change **one thing at a time**
- [ ] Give it a full sequence cycle before judging it

---

## Realistic timeline

| When | What |
| --- | --- |
| Day 1 | Sending set up, warm-up started |
| Days 1-8 | Buyer chosen, copy written, list built, sequence loaded |
| Day 15 | Campaign launches |
| Days 15-20 | First replies land |
| Day 30+ | Setup fully matured, volume can scale |

The build itself is one sitting. **Maturity is the part that takes real time**,
roughly 30 days for names to age and addresses to warm properly. Nothing about
this is instant, and anyone telling you otherwise is selling you a burned domain.
