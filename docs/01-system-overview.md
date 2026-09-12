# 01 - System overview

The whole system, in the order it has to be built.

---

## Why most cold email fails

Not because cold email stopped working. Because almost everyone starts at the
wrong end: they send from their main inbox, to a list pulled from a free tool,
opening with "do you have 15 minutes for a call this week?"

Each of those three is fatal on its own. Together, nothing lands.

The four steps fix them **in dependency order.** Great copy sent from a cold
address goes to spam. A perfect setup sending to a wrong list gets ignored.
Order matters more than effort.

---

## Step 1 - Set up sending (InboxKit)

**The problem:** send cold email from your main business address and you can
blacklist it within days. That address also carries your invoices, your client
threads and your password resets. It does not come back.

**What you build:**

| | |
| --- | --- |
| New website names | Bought only for sending. Around ₹800 a year each |
| Mailboxes on US servers | Email from an Indian internet address is treated as suspicious far more often |
| SPF, DKIM, DMARC, MX | The records that prove the email is really from you. Set automatically, never by hand |
| Domain to mailbox ratio | Three addresses per name. More and spam filters notice |
| 14 day warm-up | The addresses quietly email each other to build trust, like a new phone number nobody recognises yet |

**You end up with:** the ability to send 1,000+ emails a day without ever
touching your business address.

**How much you can send is a multiplication:**

```
14 website names  ×  3 addresses each  =  42 addresses
42 addresses      ×  30 emails a day   =  1,260 a day
```

To send more, add addresses. Never push one address harder.

**What people get wrong:** treating the 14 days as optional. It is the longest
pole in the whole build, which is exactly why it starts on day one.

---

## Step 2 - Who and what (Claude)

**The problem:** wrong targeting kills a campaign before copy matters. Most
people stop at "who has this job title" and call that a buyer.

**What you build:** 5 to 10 types of buyer, each with the pain they feel, the
logic that gets it approved, and filters you can actually search against. Then
the emails, for **one** of them.

See [skills/write-the-copy/](../skills/write-the-copy/).

### Every email that works has three parts

1. **One line about them.** Something you could only know if you looked.
2. **The problem that line points to.** The headache it tells you they have.
3. **One small question.** Something they can accept with a single word.

Under 100 words. Always.

**Never ask for a call in the first email.** You are asking a stranger for 30
minutes before giving them anything.

| Instead of | Ask for |
| --- | --- |
| "Do you have 15 minutes this week?" | "Want me to send a three minute video breaking down what I would change?" |
| "Let's hop on a quick call" | "Want to try a small pilot on one segment?" |

**What people get wrong:** writing copy before they know who it is for. It reads
generic no matter how good the writing is, because it has nothing to be about.

---

## Step 3 - Build the list (Enrich.so)

**The problem:** cheap lists have roughly half their addresses dead. Every dead
address bounces, and bouncing is what tells email providers you are a spammer.
A ₹2,000 list can cost you every sending address you own.

**What you build:**

```
Paste the filters in
        |
        v
  Count, for free      <- change a filter, count again, still free
        |
        v
  Pull the list        <- first 3 pages free, then 1 credit per record
        |
        v
  Find the emails      <- the search gives you the person, not the address
        |
        v
  A list around 8 in 10 correct
```

**The bar is 8 in 10.** Going to 9.5 in 10 costs more than the extra half is
worth. Below 8, tighten the filters rather than adding another tool.

See [skills/build-the-list/](../skills/build-the-list/).

**What people get wrong:** emailing the whole list on day one. If the list is
wrong you find out after burning all of it.

---

## Step 4 - Send and reply (Instantly)

**The problem:** a newsletter tool will get you banned. Mailchimp and Mail Merge
are built for people who signed up for your list. Use one for strangers and your
account goes, your website name gets blacklisted, and everything lands in spam.

**What you build:**

| | |
| --- | --- |
| Addresses connected | The fleet from step 1 plugs in |
| Three emails, spread over a week | Day 0, day 3, day 7 |
| Five versions of each | Same message, different words, so volume does not look like volume |
| Open and click tracking OFF | Both are spam signals on cold mail |
| Sending window | The prospect's working hours, not yours |
| Spam test | Before the first thousand sends, not after |

See [skills/launch-on-instantly/](../skills/launch-on-instantly/).

**What people get wrong:** judging it after two days. Most replies come from the
second and third email.

---

## The whole thing in sequence

```
  Day 1     STEP 1   buy names, create addresses, set DNS
              |      start the 14 day warm-up   <- clock starts here
              |
              +----------------------------+
              v                             |  (warm-up runs in the background)
  Day 1-3   STEP 2   who to email           |
              |      write the emails       |
              v                             |
  Day 3-5   STEP 3   count, pull, verify    |
              |                             |
              v                             |
  Day 5-8   STEP 4   load the sequence      |
              |      run the spam test      |
              v                             |
  Day 15    <---------------------------------+
            LAUNCH   warm-up done, one group goes live
              |
              v
  Day 15+   replies start landing
```

---

## If it is not working, check in this order

Each step sits on the one above it. Fixing copy while the addresses are broken
changes nothing.

| Symptom | The layer at fault | Where to look |
| --- | --- | --- |
| Emails are not arriving | **Step 1** | DNS records, warm-up length, addresses per name |
| Arriving, but nobody opens | **Step 1 or 2** | Sending reputation, or the subject line |
| Good opens, no replies | **Step 2** | Is the buyer real? Does email one ask for a call? |
| Replies, but the wrong people | **Step 3** | The filters are too loose |
| Everything stops suddenly | **Step 1** | A name got flagged. Pause and diagnose before sending more |

Change one thing at a time, and give it a full cycle before judging it.

---

## Six things worth unlearning

| The common belief | What actually holds up |
| --- | --- |
| Cold email is dead | It works, **if the sending setup is built right** |
| You need a big tech stack | **Three tools and the right order** beats an expensive stack |
| Send low volume to stay safe | Low volume is what kills you. **40 warmed addresses are safer than one inbox** sending 50 a day |
| Personalisation at volume is impossible | The filters and the copy skill make it the default |
| I can figure this out myself | You probably tried. What is missing is not effort, it is **the infrastructure nobody shows you** |
| My industry is different | Usually it is not. It is that the last attempt skipped **the part that gets the email into an inbox at all** |
