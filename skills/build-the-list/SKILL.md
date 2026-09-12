# Skill: build the list

Turn the filters from step 2 into a CSV of real, verified email addresses.

Uses **Enrich.so**. Needs `ENRICH_API_KEY` in `.env`.

---

## The one rule

**Count before you pull.** Counting is free and unlimited. Pulling costs money.
Almost every wasted rupee in list building comes from pulling before the filters
were right.

---

## Run it

```bash
S=skills/build-the-list/scripts/enrich_so.py

python3 $S balance                                  # credits left
python3 $S count --title "Director" --city Ahmedabad
python3 $S build --title "Director" "Operations Manager" \
                 --city Ahmedabad Gandhinagar \
                 --limit 75 --out leads.csv --free-only
```

`--free-only` stops at the free page limit so the pull costs nothing.

The CSV's first four columns are exactly what a sending tool accepts:
`email, firstName, lastName, companyName`.

---

## The filters that exist

Anything else is rejected with `Unrecognized key`, which is at least loud.

| Filter | Type |
| --- | --- |
| `jobTitle`, `jobFunction` | list |
| `firstName`, `lastName`, `linkedinUrl` | list |
| `city`, `companyName`, `domain`, `skills` | list |
| `employeeCount` | single number, exact match |

There is **no** country, industry, seniority, revenue or headcount-range filter.
Work with city and job title.

---

## What it costs

| Step | Credits |
| --- | --- |
| Count | **0, always** |
| Search, first 3 pages | **0** |
| Search after that | 1 per record |
| Find an email address | 10 |
| Verify an address | 1 |

---

## Things that will confuse you

**The search returns no email address.** Only the company's domain. Every row
goes through the email finder afterwards, so budget 10 credits per lead.

**Your key looks broken on `api.enrich.so`.** That is the old API and it wants a
JWT. The right host is `dev.enrich.so/api/v3`. The script already points there.

**Do not run a second verification pass by default.** The email finder already
checks the mailbox. Adding a verification pass and keeping only `valid` throws
away good catch-all addresses and can take a real list to zero. That is why
`--verify` is opt-in.

**In India, do not target "Founder" or "CEO".** Measured in Ahmedabad, only 8% of
Founder records and 0% of CEO records have a company domain attached, and no
domain means no email is findable. Director and Operations Manager run at 72%
and 76%. This is the single biggest yield lever on an Indian list.

---

## Realistic yield

```
25 pulled  ->  9 with a company domain  ->  4 emails found
```

About 16% of pulled records end up contactable. To get 500 leads, plan to pull
roughly 3,200 records.

Full API notes: [reference/enrich-so.md](../../reference/enrich-so.md)
