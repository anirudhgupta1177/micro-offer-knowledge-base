# Enrich.so

People search, email finding and email verification. Replaces a three-tool
stack: it finds the person AND the address AND checks it.

## Which host, and why the key looks broken

There are **two** Enrich APIs. Only one takes an `sk_` key.

| Host | Version | Auth | Use it? |
| --- | --- | --- | --- |
| `api.enrich.so` | legacy v1/v2 "Enrich Labs API" | **JWT** | No |
| `dev.enrich.so` | **current v3** | `x-api-key: sk_...` | **Yes** |

Sending an `sk_` key to `api.enrich.so` returns `{"code":401,"message":"jwt
malformed"}` on every route, and sending it with any other header name returns
`"No auth token"`. Neither error hints that you are simply on the wrong host.
Despite the name, `dev.enrich.so` is production.

```bash
BASE=https://dev.enrich.so/api/v3
curl "$BASE/wallets/balance" -H "x-api-key: $ENRICH_API_KEY"
```

`Authorization: Bearer sk_...` works too. Responses are
`{success, data, meta:{requestId, creditsUsed, creditsRemaining}}`; errors are
RFC 9457 problem+json where **`detail`** carries the useful message.

Key lives in `.env` as `ENRICH_API_KEY`.

## Endpoints that matter

| Route | Method | Credits |
| --- | --- | --- |
| `/wallets/balance` | GET | 0 |
| `/lead-finder/count` | POST | **0, always free** |
| `/lead-finder/search` | POST | **0 for the first 3 pages**, then 1 per record |
| `/email-finder` | POST | 10 |
| `/email-finder/batch` (+ `/{id}`, `/{id}/results`) | POST/GET | 10 each, up to 500k |
| `/email-validation` | POST | 1 |
| `/email-validation/batch` | POST | 1 each, up to 500k |
| `/reverse-lookup/lookup` | POST | 10, refunded if not found |
| `/reverse-lookup/phones` | GET | **500**, refunded if not found |

## Lead Finder

```json
POST /lead-finder/count   {"filters": {"jobTitle": ["Director"], "city": ["Ahmedabad"]}}
-> {"count": 19505, "searchType": "unified", "isApproximate": false, "searchedTotalResult": 19505}
```

**Only these filter keys exist.** Anything else is a 400 `Unrecognized key`:

- arrays: `jobTitle`, `jobFunction`, `firstName`, `lastName`, `linkedinUrl`, `city`, `companyName`, `domain`, `skills`
- number: `employeeCount` (exact match, so no ranges)

There is no country, industry, seniority, revenue or headcount-range filter.
`count` caps at 500,000.

## Gotchas that cost real time

- **Search returns NO email address**, only `emailDomain`. Every row has to go
  through `/email-finder` afterwards. Budget 10 credits per lead, not 1.
- **`limit` on search is ignored.** It always returns a page of 25. Slice client side.
- **The email finder already verifies the mailbox** (`"Verified mailbox exists"`).
  A second `/email-validation` pass and a `status == "valid"` filter will throw
  away good catch-all rows and can take a real list to zero. Keep `found: true`
  and only drop what validation calls explicitly `invalid`.
- **Indian "Founder" and "CEO" records mostly have no company domain** (8% and 0%
  measured in Ahmedabad, against 72-76% for Director and Operations Manager).
  No domain means no email is possible. Target Director-level titles in India.
- `revenue` and `industryNaicsDescription` are mostly empty for Indian records.
  `employeeCount`, `companyName` and `linkedinUrl` are reliable.

## Script

```bash
S=skills/build-the-list/scripts/enrich_so.py
python3 $S balance
python3 $S count --title "Director" --city Ahmedabad
python3 $S build --title "Director" "Operations Manager" --city Ahmedabad \
                 --limit 75 --out leads.csv --free-only
```

`build` runs the whole pipeline: free count, pull, email finder, optional
verification, then a CSV whose first four columns are exactly what SendKit
accepts.
