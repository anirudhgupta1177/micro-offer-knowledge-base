# Workshop demo: the persona and offer to build live

Everything here was measured against the live Enrich.so v3 API on 2026-09-12,
not guessed. The counts and yields below are what the room will actually see.

---

## The offer

**Recruitment support for growing Ahmedabad businesses.**
You fill one role on a success fee. No retainer, no exclusivity.

Chosen because it is the most universally understood service in an Indian BNI
room, it works for a 7-person agency and a 350-person manufacturer alike, and
every variable it needs is present in the data at a 100% fill rate.

**Swap-in alternatives** that use the identical persona and filters: managed IT
support (AMC), group health insurance, corporate catering, facility management.
All four are priced per head, so the same `employeeCount` variable drives them.

---

## The persona

| | |
| --- | --- |
| **Who** | Director, Operations Manager or General Manager |
| **Where** | Ahmedabad and Gandhinagar |
| **Company** | 3 to 400 people, has its own website domain |
| **The pain** | Hiring eats the operations person's week. No in-house recruiter at this size |
| **The buying logic** | A success fee is a line item they can approve without a board |

### Paste-ready Enrich filters

```json
{
  "jobTitle": ["Director", "Operations Manager", "General Manager"],
  "city": ["Ahmedabad", "Gandhinagar"]
}
```

```bash
python3 skills/build-the-list/scripts/enrich_so.py count \
  --title "Director" "Operations Manager" "General Manager" \
  --city Ahmedabad Gandhinagar
# -> {"count": 30372}   costs nothing
```

---

## Why NOT "Founder" or "CEO"

This is the most useful thing to show the room, and it is counterintuitive.
Measured domain-fill rate across 25 pulled records per persona:

| Title, Ahmedabad | Records with a company domain |
| --- | --- |
| Operations Manager | **76%** |
| Director | **72%** |
| Plant Head / Production Manager (Gujarat) | 48% |
| Founder, Mumbai | 12% |
| **Founder, Ahmedabad** | **8%** |
| Marketing Manager | 4% |
| **CEO, Ahmedabad** | **0%** |

Indian "Founder" and "CEO" profiles are overwhelmingly solo or unlinked to a
company record, and **no domain means the email finder cannot run at all**.
Everyone in the room will instinctively target "Founder". Showing them that it
returns almost nothing usable, live, is the moment the lesson lands.

---

## What the data actually gives you

100% filled on usable rows: `firstName`, `jobTitle`, `city`, `employeeCount`,
`linkedinUrl`, `companyName`, `emailDomain`.

Weak, do not build on it: `employeeOnLinkedinGrowthRateOrg` is 0 to 7 for almost
every Gujarat company, so "I saw you are growing fast" is not supportable.
`revenue` and `industryNaicsDescription` are mostly empty in India.

So the personalisation line has to come from **company name plus headcount**.

---

## The email, in the three parts

**Subject:** `{{random|Hiring at {{companyName}}?|{{companyName}} and your next hire|Quick one about hiring}}`

```
{{random|Hi|Hey}} {{firstName}},

{{random|saw|noticed}} {{companyName}} is around 16 people in Ahmedabad.

{{random|At that size|At that headcount}} there is usually no in-house recruiter,
so hiring lands on whoever is running operations. That is normally you.

{{random|Want me to send|Can I send you}} two shortlisted CVs for the role you
are hiring next, free, so you can see the quality before deciding anything?
```

47 words. Opens about them, names the pain the headcount points to, and asks for
two CVs rather than a call. That is the exact structure on slide 08.

> Note: the headcount is stated in the copy as an example. SendKit only stores
> `firstName`, `lastName`, `companyName` and `email`, so a live headcount merge
> tag is not possible. Either segment the list into headcount bands and write one
> version per band, or keep the line generic.

---

## Yield maths, measured

From a real run of this exact persona:

```
25 pulled (free)  ->  9 had a company domain  ->  4 emails found
```

| Stage | Rate | Cost |
| --- | --- | --- |
| Count | free | 0 |
| Search, first 3 pages | free | 0 (75 records) |
| Search after that | 1 credit per record | |
| Has a usable domain | ~36% of pulled | |
| Email found | ~44% of those with a domain | 10 credits each |
| **End to end** | **~16% of pulled records** | |

**To get 500 contactable leads:** pull roughly 3,200 records, which is about
3,200 search credits plus 11,500 finder credits, so **under 15,000 credits**.
The account holds 7,602,779. Cost is not the constraint here, the domain-fill
rate is.

---

## Live demo running order

```
1. count with "Founder"  -> big number, then show 8% have domains   (the trap)
2. count with "Director" -> 30,372, and 72% are usable             (the fix)
3. build --limit 25      -> real CSV with real Ahmedabad emails
4. feed the CSV into the SendKit campaign                          (skills/launch-on-instantly/)
5. the pre-launch check        -> it BLOCKS on 0 mailboxes                (the point)
```

Step 5 failing on purpose is the strongest moment in the demo: it proves the
checks are real and that infrastructure is genuinely step one.

---

## About the sample file

`sample_leads_ahmedabad.csv` shows the exact column layout the pipeline
produces. The rows are fictional on purpose: this is a public repo, and
real prospects' work email addresses do not belong in one. Your own run
will produce the same columns with real data.
