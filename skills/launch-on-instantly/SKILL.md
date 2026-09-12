# Skill: launch on Instantly

Load the sequence, connect the addresses, test, then send.

Needs `INSTANTLY_API_KEY` in `.env`.

---

## Build order

Leads go in **last**, because taking them out again is the painful part.

```
1. Check the copy        copy_qa.py, before anything is created
2. Create the campaign   created paused, nothing sends yet
3. House settings        tracking OFF, schedule, daily limit
4. Load the sequence     3 emails, waits between them, 5 spintax versions each
5. Attach the addresses  the fleet from step 1
6. Spam test             confirm it lands in the inbox
7. Leads LAST
8. Start it
```

---

## Run it

```python
import instantly_lib as inst

inst.accounts()                                  # your sending addresses
cid = inst.create_campaign("Ahmedabad recruitment", timezone="Asia/Kolkata")
inst.apply_house_settings(cid, daily_limit=30)   # tracking off, stop on reply
rows = inst.read_csv("leads.csv")
inst.add_leads(cid, rows)                        # last
```

---

## The settings that must be true before launch

| Setting | Value | Why |
| --- | --- | --- |
| Open tracking | **off** | A tracking pixel is a spam signal on cold mail |
| Link tracking | **off** | Rewritten links wreck a cold name's reputation. Separate flag from opens |
| Stop on reply | on | Otherwise you follow up on someone who already answered |
| Daily limit | ~30 per address | More volume means more addresses, never more per address |
| Schedule | the prospect's timezone | Not yours |
| Unsubscribe link | off | Cold email should not carry one |

---

## Things that will catch you out

**Editing the sequence on a live campaign pauses it.** Patch the sequence before
the leads go in, not after.

**Spintax is `{{RANDOM | a | b}}`.** Uppercase, spaces around the pipes. The
`{a|b}` form sends literal braces to the prospect.

**Lists page with `starting_after`, not page numbers.** `_page_all()` handles it.

**A `402 Payment Required` means the workspace has no active paid plan**, not
that your key is wrong. Check which workspace the key belongs to.

**Re-touching leads a campaign already contacted** needs a duplicate campaign
plus a move, not a re-upload. Re-uploading silently does nothing.

---

## Before you press send

- [ ] The 14 day warm-up is **finished**, not nearly finished
- [ ] SPF, DKIM and DMARC still resolve
- [ ] Open and click tracking both off
- [ ] One email sent to your own inbox, and you checked where it landed
- [ ] Live with **one group only**, warm-up still running alongside

Full API notes: [reference/instantly.md](../../reference/instantly.md)
