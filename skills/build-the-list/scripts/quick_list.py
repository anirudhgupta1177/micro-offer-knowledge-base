#!/usr/bin/env python3
"""Workshop list build: 100 real emails in about 3 minutes.

Two API calls per stage, nothing else. No verification pass, no headcount
filtering, no enrichment. Designed to be run live in front of a room.

    python3 quick_list.py                          # 100 leads, the workshop ICP
    python3 quick_list.py --limit 50               # fewer
    python3 quick_list.py --title Director --city Ahmedabad
    python3 quick_list.py --count-only             # free, just the number

Why it is fast, where the old script was slow:
  * search pages are fetched in parallel. The API ignores `limit` and always
    returns 25 a page, so 100 leads is ~16 pages. Sequentially that was the
    whole delay.
  * ONE email-finder batch for every candidate at once, not chunks of 500.
  * rows with a blank first or last name are dropped BEFORE submitting. The
    API rejects the entire batch over a single blank name, which is what
    killed the earlier 4,800 record run.
"""
import argparse, csv, json, os, ssl, sys, time
import urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

BASE = "https://dev.enrich.so/api/v3"
CTX = ssl.create_default_context()

# Cloudflare in front of the API rejects a default urllib agent with 403 / 1010.
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36")

# The workshop ICP. Ops decision makers in Ahmedabad and Gandhinagar.
ICP_TITLES = ["Director", "Operations Manager", "General Manager"]
ICP_CITIES = ["Ahmedabad", "Gandhinagar"]

# Search yields ~43% with a usable company domain, and the finder hits on
# ~36% of those. So ~6.5 pulled per email. 8x gives comfortable headroom.
OVERPULL = 8


def find_env():
    here = os.path.abspath(__file__)
    for _ in range(6):
        here = os.path.dirname(here)
        p = os.path.join(here, ".env")
        if os.path.exists(p):
            return p
    return None


def key():
    k = os.environ.get("ENRICH_API_KEY")
    if k:
        return k.strip()
    p = find_env()
    if p:
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line.startswith("ENRICH_API_KEY"):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("No ENRICH_API_KEY. Put it in .env at the repo root.")


def call(method, path, body=None, tries=3):
    data = json.dumps(body).encode() if body is not None else None
    for attempt in range(tries):
        req = urllib.request.Request(BASE + path, data=data, method=method)
        req.add_header("x-api-key", key())
        req.add_header("Accept", "application/json")
        req.add_header("User-Agent", UA)
        if data is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=90, context=CTX) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            raw = e.read().decode()[:300]
            if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                time.sleep(2 * (attempt + 1)); continue
            sys.exit("HTTP %s on %s: %s" % (e.code, path, raw))
        except Exception:
            # transient DNS / network blips killed the previous run, so retry
            if attempt < tries - 1:
                time.sleep(3 * (attempt + 1)); continue
            raise
    return {}


def count(filters):
    # v3 nests the payload under "data"
    return call("POST", "/lead-finder/count", {"filters": filters})["data"].get("count", 0)


def page(filters, n):
    try:
        r = call("POST", "/lead-finder/search",
                 {"filters": filters, "limit": 25, "page": n})
        return r["data"].get("results", [])
    except SystemExit:
        return []


def search(filters, want):
    """Fetch pages in parallel. The API returns 25 per page and ignores limit."""
    pages = max(1, (want + 24) // 25)
    out = []
    with ThreadPoolExecutor(max_workers=10) as ex:
        for rows in ex.map(lambda n: page(filters, n), range(1, pages + 1)):
            out.extend(rows)
    return out


def find_emails(leads, poll=5, timeout=240):
    """One batch for everything. 10 credits per lead."""
    sub = call("POST", "/email-finder/batch", {"leads": leads})["data"]
    bid = sub["batchId"]
    waited = 0
    while waited < timeout:
        st = call("GET", "/email-finder/batch/%s" % bid)["data"]
        if st.get("status") in ("completed", "failed"):
            break
        time.sleep(poll); waited += poll
    found, pg = {}, 1
    while True:
        res = call("GET", "/email-finder/batch/%s/results?page=%d&limit=1000" % (bid, pg))["data"]
        items = res.get("results") or []
        for r in items:
            if r.get("email"):
                found[(r.get("firstName", ""), r.get("lastName", ""), r.get("domain", ""))] = r
        if len(items) < 1000:
            break
        pg += 1
    return found


COLS = ["email", "firstName", "lastName", "companyName", "jobTitle", "city",
        "domain", "employeeCount", "linkedinUrl", "confidence"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", nargs="*", default=ICP_TITLES)
    ap.add_argument("--city", nargs="*", default=ICP_CITIES)
    ap.add_argument("--limit", type=int, default=100, help="emails wanted")
    ap.add_argument("--out", default="workshop_leads.csv")
    ap.add_argument("--count-only", action="store_true", help="free, no spend")
    a = ap.parse_args()

    filters = {"jobTitle": a.title, "city": a.city}
    t0 = time.time()

    n = count(filters)
    print("pool: %d match %s in %s  (counting is free)" % (n, a.title, a.city), flush=True)
    if a.count_only:
        return
    if not n:
        sys.exit("Nothing matches. Widen the filters and count again, still free.")

    rows = search(filters, a.limit * OVERPULL)
    print("pulled %d records in %.0fs" % (len(rows), time.time() - t0), flush=True)

    # Drop anything the finder would reject or cannot use. A single blank
    # name fails the whole batch, so this filter is not optional.
    cands, seen = [], set()
    for r in rows:
        f = (r.get("firstName") or "").strip()
        l = (r.get("lastName") or "").strip()
        d = (r.get("emailDomain") or r.get("domain") or "").strip()
        if not (f and l and d):
            continue
        k = (f.lower(), l.lower(), d.lower())
        if k in seen:
            continue
        seen.add(k)
        cands.append({"firstName": f, "lastName": l, "domain": d, "_src": r})

    print("%d have a name and a company domain, looking up emails..." % len(cands), flush=True)
    if not cands:
        sys.exit("No usable rows. In India avoid Founder and CEO, they have no domain.")

    found = find_emails([{k: c[k] for k in ("firstName", "lastName", "domain")} for c in cands])

    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        cw = csv.DictWriter(fh, fieldnames=COLS)
        cw.writeheader()
        w = 0
        for c in cands:
            if w >= a.limit:
                break
            hit = found.get((c["firstName"], c["lastName"], c["domain"]))
            if not hit:
                continue
            s = c["_src"]
            cw.writerow({"email": hit["email"], "firstName": c["firstName"],
                         "lastName": c["lastName"], "companyName": s.get("companyName", ""),
                         "jobTitle": s.get("jobTitle", ""), "city": s.get("city", ""),
                         "domain": c["domain"], "employeeCount": s.get("employeeCount", ""),
                         "linkedinUrl": s.get("linkedinUrl", ""),
                         "confidence": hit.get("confidence", "")})
            w += 1

    print("\n%d emails -> %s   in %.0fs" % (w, a.out, time.time() - t0), flush=True)
    print("First four columns are what the sending tool wants: email, firstName, lastName, companyName.")
    if w < a.limit:
        print("Short of %d. Run again with --limit %d to pull deeper." % (a.limit, a.limit * 2))


if __name__ == "__main__":
    main()
