#!/usr/bin/env python3
"""Enrich.so v3: count free, pull, find emails, verify, write a SendKit-ready CSV.

  python3 enrich_so.py count --title "Head of Sales" --city "San Francisco"
  python3 enrich_so.py build --title "Head of Sales" --city "San Francisco" \
                             --limit 60 --out leads.csv

WHICH HOST: there are two Enrich APIs and only one takes an `sk_` key.
  api.enrich.so   legacy v1/v2, wants a JWT. An sk_ key here returns
                  {"code":401,"message":"jwt malformed"} on every route.
  dev.enrich.so   the current v3 API. This is the one. Despite the hostname
                  it is production.

CREDIT MODEL (checked live, not from docs):
  lead-finder/count    FREE. meta carries no creditsUsed at all.
  lead-finder/search   first 3 pages FREE (meta.freePageLimit), then 1 per record
  email-finder         10 per lead. Lead Finder does NOT return email addresses,
                       only emailDomain, so this step is mandatory
  email-validation     1 per email
  reverse-lookup/phones 500 per number. Not used here on purpose
"""
import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

BASE = "https://dev.enrich.so/api/v3"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# Only these keys are accepted inside `filters`. Anything else is a 400
# "Unrecognized key", which is at least loud rather than silent.
#   arrays: jobTitle, jobFunction, firstName, lastName, linkedinUrl,
#           city, companyName, domain, skills
#   number: employeeCount
ARRAY_FILTERS = ("jobTitle", "jobFunction", "firstName", "lastName",
                 "linkedinUrl", "city", "companyName", "domain", "skills")


def _find_env():
    here = os.path.abspath(__file__)
    for _ in range(8):
        here = os.path.dirname(here)
        cand = os.path.join(here, ".env")
        if os.path.exists(cand):
            return cand
    return None


def env(name):
    if os.environ.get(name):
        return os.environ[name]
    path = _find_env()
    if not path:
        raise RuntimeError("no .env found")
    for line in open(path, encoding="utf-8", errors="ignore"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip() == name:
            return v.strip().strip('"').strip("'")
    raise RuntimeError("%s not set in %s" % (name, path))


_KEY = None


def key():
    global _KEY
    if _KEY is None:
        _KEY = env("ENRICH_API_KEY")
    return _KEY


def call(method, path, body=None, tries=4):
    url = BASE + path
    for attempt in range(tries):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, method=method, data=data)
        req.add_header("x-api-key", key())
        req.add_header("Accept", "application/json")
        req.add_header("User-Agent", UA)
        if body is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", "replace")
            if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            # v3 speaks RFC 9457 problem+json, so `detail` is the useful field
            try:
                p = json.loads(raw)
                raise RuntimeError("%s %s: %s" % (e.code, p.get("title", ""), p.get("detail", raw)[:300]))
            except ValueError:
                raise RuntimeError("%s %s" % (e.code, raw[:300]))
        except Exception:
            if attempt < tries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            raise
    raise RuntimeError("unreachable")


def balance():
    return call("GET", "/wallets/balance")["data"]


# ──────────────────────────────────────────────────────────── lead finder
def count(filters):
    """How many people match. Costs nothing, so run it before every pull."""
    d = call("POST", "/lead-finder/count", {"filters": filters})["data"]
    return d


# NOTE: `limit` is sent but the API returns a fixed page of 25 regardless.
# Ask for 5 and you still get 25 (all free inside the first 3 pages), so slice
# client-side rather than trusting the parameter.
def search(filters, limit=25, page=1):
    out = call("POST", "/lead-finder/search",
               {"filters": filters, "limit": limit, "page": page})
    return out["data"].get("results", []), out.get("meta", {}), out["data"].get("pagination", {})


def search_many(filters, want, page_size=25, free_only=False):
    """Pull `want` records. free_only stops at the free page limit."""
    rows, page = [], 1
    while len(rows) < want:
        recs, meta, _ = search(filters, limit=page_size, page=page)
        if not recs:
            break
        rows.extend(recs)
        free_limit = meta.get("freePageLimit")
        if free_only and free_limit and page >= free_limit:
            print("  stopped at the free page limit (%d pages)" % free_limit)
            break
        page += 1
        time.sleep(0.3)
    return rows[:want]


# ───────────────────────────────────────────────────── email find + verify
def find_emails(leads, poll=6, timeout=900):
    """leads: [{firstName,lastName,domain}] -> {(f,l,d): email}. 10 credits each."""
    if not leads:
        return {}
    sub = call("POST", "/email-finder/batch", {"leads": leads})["data"]
    bid = sub["batchId"]
    waited = 0
    while waited < timeout:
        st = call("GET", "/email-finder/batch/%s" % bid)["data"]
        if st.get("status") in ("completed", "failed"):
            break
        time.sleep(poll)
        waited += poll
    found, page = {}, 1
    while True:
        res = call("GET", "/email-finder/batch/%s/results?page=%d&limit=1000" % (bid, page))["data"]
        items = res.get("results") or []
        for r in items:
            if r.get("email"):
                found[(r.get("firstName", ""), r.get("lastName", ""), r.get("domain", ""))] = r
        if len(items) < 1000:
            break
        page += 1
    return found


def validate_emails(emails, poll=6, timeout=900):
    """-> {email: status}. 1 credit each."""
    if not emails:
        return {}
    bid = call("POST", "/email-validation/batch", {"emails": emails})["data"]["batchId"]
    waited = 0
    while waited < timeout:
        st = call("GET", "/email-validation/batch/%s" % bid)["data"]
        if st.get("status") in ("completed", "failed"):
            break
        time.sleep(poll)
        waited += poll
    out, page = {}, 1
    while True:
        res = call("GET", "/email-validation/batch/%s/results?page=%d&limit=1000" % (bid, page))["data"]
        items = res.get("results") or []
        for r in items:
            out[r["email"]] = r.get("status")
        if len(items) < 1000:
            break
        page += 1
    return out


# ───────────────────────────────────────────────────────────── pipeline
def build(filters, want, out_path, free_only=False, verify=False):
    print("balance:", balance().get("balance"), "credits")

    c = count(filters)
    print("count: %s match (searched %s)%s"
          % (c.get("count"), c.get("searchedTotalResult"),
             " [approximate]" if c.get("isApproximate") else ""))
    if not c.get("count"):
        print("nothing matches. Widen the filters before spending anything.")
        return

    people = search_many(filters, want, free_only=free_only)
    print("pulled: %d" % len(people))

    # Lead Finder gives the person and the company domain but never the email,
    # so every row has to go through the finder before it is worth anything.
    leads = [{"firstName": p.get("firstName") or "", "lastName": p.get("lastName") or "",
              "domain": p.get("emailDomain") or p.get("domain") or ""}
             for p in people if (p.get("firstName") and (p.get("emailDomain") or p.get("domain")))]
    print("finding emails for %d (10 credits each)..." % len(leads))
    found = find_emails(leads)
    print("found: %d" % len(found))

    rows = []
    for p in people:
        k = (p.get("firstName") or "", p.get("lastName") or "",
             p.get("emailDomain") or p.get("domain") or "")
        hit = found.get(k)
        if not hit or not hit.get("email"):
            continue
        rows.append({
            "email": hit["email"],
            "isCatchAll": "yes" if hit.get("isCatchAll") else "",
            "firstName": p.get("firstName") or "",
            "lastName": p.get("lastName") or "",
            "companyName": p.get("companyName") or "",
            "jobTitle": p.get("jobTitle") or "",
            "city": p.get("city") or "",
            "domain": k[2],
            "linkedinUrl": p.get("linkedinUrl") or "",
            "employeeCount": p.get("employeeCount") or "",
            "confidence": hit.get("confidence") or "",
            "verification": "",
        })

    # The email finder ALREADY verifies the mailbox ("Verified mailbox exists"),
    # so a second validation pass is opt-in. Running it by default and keeping
    # only status=="valid" throws away perfectly good catch-all rows and drops
    # a real list to near zero - measured, not theoretical.
    if verify and rows:
        print("second-pass verifying %d addresses (1 credit each)..." % len(rows))
        verdicts = validate_emails([r["email"] for r in rows])
        for r in rows:
            r["verification"] = verdicts.get(r["email"], "unknown")
        before = len(rows)
        rows = [r for r in rows if r["verification"] != "invalid"]
        print("dropped %d explicitly invalid, kept %d" % (before - len(rows), len(rows)))

    if not rows:
        print("nothing survived. Nothing written.")
        return
    cols = ["email", "firstName", "lastName", "companyName", "jobTitle",
            "city", "domain", "employeeCount", "linkedinUrl", "confidence",
            "isCatchAll", "verification"]
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print("wrote %d rows -> %s" % (len(rows), out_path))
    print("SendKit only stores email, firstName, lastName and companyName. "
          "The rest of these columns are for your own segmentation.")


def filters_from_args(a):
    f = {}
    if a.title:
        f["jobTitle"] = a.title
    if a.city:
        f["city"] = a.city
    if a.company:
        f["companyName"] = a.company
    if a.domain:
        f["domain"] = a.domain
    if a.skills:
        f["skills"] = a.skills
    if a.employees:
        f["employeeCount"] = a.employees
    if not f:
        sys.exit("give at least one filter, e.g. --title 'Head of Sales'")
    return f


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["count", "search", "build", "balance"])
    ap.add_argument("--title", nargs="*")
    ap.add_argument("--city", nargs="*")
    ap.add_argument("--company", nargs="*")
    ap.add_argument("--domain", nargs="*")
    ap.add_argument("--skills", nargs="*")
    ap.add_argument("--employees", type=int)
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--out", default="enrich_leads.csv")
    ap.add_argument("--free-only", action="store_true",
                    help="stop at the free page limit, spend nothing on search")
    ap.add_argument("--verify", action="store_true",
                    help="optional second validation pass (1 credit each). The finder\n"
                         "already verifies mailboxes, so this is rarely needed.")
    a = ap.parse_args()

    if a.mode == "balance":
        print(json.dumps(balance(), indent=2))
        return
    f = filters_from_args(a)
    if a.mode == "count":
        print(json.dumps(count(f), indent=2))
    elif a.mode == "search":
        recs, meta, _ = search(f, limit=a.limit)
        print(json.dumps({"meta": meta, "sample": recs[:3], "n": len(recs)}, indent=2)[:3000])
    else:
        build(f, a.limit, a.out, free_only=a.free_only, verify=a.verify)


if __name__ == "__main__":
    main()
