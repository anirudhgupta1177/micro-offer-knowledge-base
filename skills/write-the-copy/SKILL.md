# Skill: write the copy

Write the emails, then prove they are safe to send.

---

## The three parts

Every first email that works has exactly these, in this order:

1. **One line about them.** Something true you could only know if you looked.
   Not "I loved your website".
2. **The problem that line points to.** The headache that fact implies. This is
   the part everyone skips, and it is the part that earns the reply.
3. **One small question.** Something they can accept with a single word.

**Under 100 words. Always.**

---

## Never ask for a call in the first email

You are asking a stranger for 30 minutes before you have given them anything.
In a crowded market, give value first and ask for time later.

| Instead of | Ask for |
| --- | --- |
| "Do you have 15 minutes this week?" | "Want me to send a three minute video breaking down what I would change?" |
| "Let's hop on a quick call" | "Want to try a small pilot on one segment?" |

---

## What most people send, and why it fails

> Hi Anirudh, I'm the founder of Intent Led Sales. We are a lead generation
> agency that helps B2B companies scale their outbound with AI powered
> personalisation, verified data and multi channel sequences. We have worked
> with 50+ clients... Would you have 15 minutes for a quick call this week?

112 words, every one of them about the sender, and it asks for 30 minutes.

**The one line fix:** delete every sentence that starts with "We". Whatever
survives that is about them becomes your first line.

## What gets replies

> Hi Rahul, saw you supply to both Zomato and Swiggy.
>
> Most suppliers running on both portals lose two or three days a month just
> matching orders between the two.
>
> Want me to send a three minute video showing how our clients cut that to an hour?

46 words. Opens about them, names the pain, asks for a video.

---

## Spintax

One email becomes five, so volume does not look like volume. In Instantly the
syntax is uppercase with spaces:

```
{{RANDOM | Hi | Hey}} {{firstName}}, {{RANDOM | saw | noticed}} {{companyName}}...
```

The `{a|b}` form other tools use does **nothing** here. It sends the braces to
the prospect. Aim for 5 or more distinct versions per email.

Merge tags are camelCase: `{{firstName}}`, `{{companyName}}`. A tag that is not
set on every lead renders **empty**, which reads worse than no personalisation.

---

## Check it before it ships

```bash
python3 skills/write-the-copy/scripts/copy_qa.py my_email.txt
python3 skills/write-the-copy/scripts/copy_qa.py my_email.txt --preview 5
```

It blocks on spam words, banned characters, wrong spintax and any first email
that asks for a call. It warns on shouting, long copy and thin spintax.

---

## Characters

Never use em dashes or en dashes. It is the most obvious sign a machine wrote
the email, and it costs you credibility with exactly the buyers worth having.
Use commas, full stops, or a plain hyphen. `copy_qa.py` normalises them for you.
