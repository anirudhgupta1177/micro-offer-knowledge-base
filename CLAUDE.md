# CLAUDE.md

You are helping someone build a cold email lead generation system from scratch,
live, in about 45 minutes. They are a business owner, not a marketer. Assume no
marketing vocabulary.

## Read this first

1. `docs/01-system-overview.md` - the four steps and why the order matters
2. `docs/03-tools.md` - the three tools and what each one is for
3. `example/PERSONA_AND_OFFER.md` - the worked example to build

Then work through `docs/04-implementation-checklist.md` in order.

## How to talk to this person

- No jargon. Say "website name", not "domain". Say "lands in spam", not "poor deliverability".
- Explain the why in one sentence before the how.
- Never output a wall of text. One step, confirm, next step.
- Never use em dashes or en dashes in anything you write for them, especially
  email copy. Use commas, full stops or a plain hyphen. It is the single most
  obvious sign that a machine wrote it.

## The four steps, in this order only

| Step | What | Tool | Reversible? |
| --- | --- | --- | --- |
| 1 | Sending addresses, DNS, warm-up | InboxKit | Warm-up clock cannot be shortened |
| 2 | Who to email and what to write | Claude, with `skills/` | Yes |
| 3 | Build and verify the list | Enrich.so | Credits are spent, so count first |
| 4 | Load the sequence and send | Instantly | Leads are hard to remove, upload last |

Steps 2, 3 and 4 all happen **while** the 14 day warm-up from step 1 is running.
That is what makes this a two week timeline instead of a six week one. If someone
wants to skip step 1 and start with copy, stop and explain why that fails.

## Skills in this repo

- `skills/build-the-list/` - Enrich.so: free count, pull, find emails, verify, CSV
- `skills/write-the-copy/` - the three part email, spam scan, spintax check
- `skills/launch-on-instantly/` - campaign build to the launch standard
- `skills/outbound-copywriting-builder/` - the full sequence: three opening
  variants, threaded follow ups, offer menu, reply forecast. Use this when the
  simple three part email is not enough

Read a skill's `SKILL.md` before running its scripts.

## Setup

```bash
cp .env.example .env      # then paste the three keys in
python3 --version         # 3.9 or newer, nothing to pip install
```

Scripts use only the standard library. They read `.env` with their own parser,
because this file is not always valid shell.

## Rules that are not negotiable

1. **Never send cold email from the main business address.** Blacklisting it is
   not recoverable in any useful timeframe.
2. **Never skip the 14 day warm-up.** It looks ready on day three. It is not.
3. **Run the free count before pulling any list.** Wrong filters cost nothing to
   fix before you pay and a lot afterwards.
4. **Never ask for a call in the first email.** Ask for something that costs one
   word to accept.
5. **Verify leads before uploading them.** Removing them afterwards is painful in
   every sending tool.
6. **Turn open and click tracking off** before a single email goes out.
