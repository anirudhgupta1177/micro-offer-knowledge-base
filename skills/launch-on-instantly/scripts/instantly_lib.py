"""Instantly v2 API client, plus the settings every campaign must have.

    import instantly_lib as inst
    inst.whoami()
    inst.accounts()                    # your connected sending addresses
    inst.campaigns()
    cid = inst.create_campaign("Name")
    inst.apply_house_settings(cid, timezone="Asia/Kolkata")

Base https://api.instantly.ai, header `Authorization: Bearer <INSTANTLY_API_KEY>`.
Lists page with `starting_after`, not page numbers.
"""
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.instantly.ai/api/v2"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
_KEY = None


def _find_env():
    here = os.path.abspath(__file__)
    for _ in range(8):
        here = os.path.dirname(here)
        cand = os.path.join(here, ".env")
        if os.path.exists(cand):
            return cand
    return None


def env(name):
    """Read from .env by hand. Do not `source` it, it is not always valid shell."""
    if os.environ.get(name):
        return os.environ[name]
    path = _find_env()
    if not path:
        raise RuntimeError("no .env found. Run: cp .env.example .env")
    for line in open(path, encoding="utf-8", errors="ignore"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip() == name:
            v = v.strip().strip('"').strip("'")
            if v:
                return v
    raise RuntimeError("%s is empty in %s" % (name, path))


def key():
    global _KEY
    if _KEY is None:
        _KEY = env("INSTANTLY_API_KEY")
    return _KEY


def call(method, path, body=None, tries=4):
    url = path if path.startswith("http") else BASE + path
    for attempt in range(tries):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, method=method, data=data)
        req.add_header("Authorization", "Bearer " + key())
        req.add_header("Accept", "application/json")
        req.add_header("User-Agent", UA)
        if body is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                raw = r.read().decode("utf-8", "replace")
            return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", "replace")
            if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            raise RuntimeError("%s %s -> %s" % (method, path, raw[:400]))
        except Exception:
            if attempt < tries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            raise
    raise RuntimeError("unreachable")


def _page_all(path, limit=100):
    """Instantly pages with `starting_after`, carrying the last id forward."""
    out, cursor = [], None
    while True:
        sep = "&" if "?" in path else "?"
        url = "%s%slimit=%d" % (path, sep, limit)
        if cursor:
            url += "&starting_after=" + urllib.parse.quote(str(cursor))
        payload = call("GET", url)
        items = payload.get("items") or payload.get("data") or []
        out.extend(items)
        cursor = payload.get("next_starting_after")
        if not cursor or not items:
            return out


# ───────────────────────────────────────────────────────────── reads
def whoami():
    return call("GET", "/accounts?limit=1")


def accounts():
    """Your connected sending addresses."""
    return _page_all("/accounts")


def campaigns():
    return _page_all("/campaigns")


def find_campaign(name):
    for c in campaigns():
        if c.get("name") == name:
            return c
    return None


# ───────────────────────────────────────────────────────────── writes
def create_campaign(name, timezone="Asia/Kolkata", start="09:00", end="17:00"):
    """Create a campaign. It is created paused; nothing sends until you start it."""
    body = {
        "name": name,
        "campaign_schedule": {
            "schedules": [{
                "name": "Working hours",
                "timing": {"from": start, "to": end},
                "days": {"1": True, "2": True, "3": True, "4": True, "5": True},
                "timezone": timezone,
            }]
        },
    }
    out = call("POST", "/campaigns", body)
    return out.get("id") or out.get("campaign_id")


# House standard. Tracking OFF is the one people forget, and both flags are
# separate: turning opens off does not turn clicks off.
def apply_house_settings(cid, daily_limit=30):
    return call("PATCH", "/campaigns/" + cid, {
        "open_tracking": False,
        "link_tracking": False,
        "stop_on_reply": True,
        "daily_limit": daily_limit,
    })


def add_leads(cid, rows, chunk=500):
    """rows: [{email, firstName, lastName, companyName}, ...]

    Upload LAST. Removing leads from a campaign afterwards is painful, and a
    campaign that has already contacted someone needs a duplicate plus a move
    to re-touch them, not a re-upload.
    """
    added = 0
    for i in range(0, len(rows), chunk):
        batch = rows[i:i + chunk]
        out = call("POST", "/leads/list", {
            "campaign_id": cid,
            "leads": [{
                "email": r["email"],
                "first_name": r.get("firstName", ""),
                "last_name": r.get("lastName", ""),
                "company_name": r.get("companyName", ""),
            } for r in batch],
        })
        added += out.get("total_sent", len(batch))
        time.sleep(0.5)
    return {"added": added}


def read_csv(path):
    import csv
    with open(path, newline="", encoding="utf-8") as fh:
        return [r for r in csv.DictReader(fh) if r.get("email")]
