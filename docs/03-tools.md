# 03 - The tools

Three tools plus Claude. The stack is deliberately small: most people over-tool
outbound, stacking four data providers to fix a problem one good source solves.

| Tool | What it does | Per month |
| --- | --- | --- |
| **Claude** | Works out who to email, writes the emails, runs the scripts | Your existing plan |
| **InboxKit** | Website names, mailboxes on US servers, DNS, warm-up | ₹12,500 |
| **Enrich.so** | The list, email finding, verification | ₹5,000 |
| **Instantly** | Sequences, sending, replies | ₹9,000 |
| | **Total** | **₹26,500** |

---

## InboxKit

Buys the sending names and creates the mailboxes, on US IPs, with SPF, DKIM,
DMARC and MX written automatically through Cloudflare in under a minute.

Doing this by hand is the most common silent failure in outbound, and doing it
from an Indian internet connection is the second.

- Key: `INBOXKIT_API_KEY` (a JWT, starts `eyJ`). It is a session token, so a
  `401` usually means it expired rather than that it is wrong.
- Three mailboxes per website name.
- Pick **one** warm-up source, InboxKit's or Instantly's. Running both at the
  same time causes deliverability dips.
- It exports mailboxes straight into Instantly, so you never handle passwords.

---

## Enrich.so

Finds the people AND their email addresses AND checks them. One subscription
instead of a data tool plus three verifiers.

### Use the right host

This is the thing that wastes an afternoon. There are **two** Enrich APIs.

| Host | Auth | Use it? |
| --- | --- | --- |
| `api.enrich.so` | a JWT | **No.** Your `sk_` key returns `jwt malformed` here |
| `dev.enrich.so/api/v3` | `x-api-key: sk_...` | **Yes.** Despite the name it is production |

### What things cost

| Call | Credits |
| --- | --- |
| Count how many match | **free, always** |
| Search, first 3 pages | **free** |
| Search after that | 1 per record |
| Find an email address | 10 |
| Verify an address | 1 |
| Find a phone number | 500 |

**The search does not return email addresses**, only the company's domain, so
every row needs the email finder afterwards. Budget 10 credits per lead, not 1.

Full API notes: [reference/enrich-so.md](../reference/enrich-so.md).

---

## Instantly

Where the campaign is configured, launched and measured.

- Base `https://api.instantly.ai`, header `Authorization: Bearer <key>`, API v2.
- Key: `INSTANTLY_API_KEY`.
- Spintax is `{{RANDOM | one | two}}`, uppercase, with spaces around the pipes.
  The `{one|two}` form does nothing.
- Merge tags are camelCase: `{{firstName}}`, `{{companyName}}`.
- Editing a sequence on a live campaign **pauses it automatically.** Patch the
  sequence before the leads go in.
- Open and click tracking must be turned off before launch.

Full API notes: [reference/instantly.md](../reference/instantly.md).

---

## What you do not need

| | Why not |
| --- | --- |
| A big enrichment stack | "You need a huge tech stack" is the most expensive myth here. Eight in ten correct, plus the right sequence, beats it |
| Four separate verification tools | You only need those if your data source is bad. Fix the source |
| A newsletter tool like Mailchimp | Built for people who opted in. Using one for cold email gets you banned and your name blacklisted |
| Technical skills | Domain setup, DNS, warm-up and the scripts are all walked through. The two AI skills do the heaviest lifting |

---

## What it costs to run

Work out your monthly number **before** you buy anything. The drivers:

| Cost driver | Scales with |
| --- | --- |
| Website names | How many addresses you run (the ratio sets this) |
| Mailboxes | Your target daily volume |
| Sending platform | Contacts or mailboxes, depending on plan |
| List data | Contacts pulled and emails found |

Sending capacity scales almost linearly with mailbox count, which is why the
answer to "how do I send more" is always more addresses.
