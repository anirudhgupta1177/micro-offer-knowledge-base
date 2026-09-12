#!/usr/bin/env python3
"""Check cold email copy before it goes anywhere near a campaign.

    python3 copy_qa.py my_email.txt
    python3 copy_qa.py my_email.txt --preview 5      # see what the spintax renders as
    echo "Hi {{firstName}}..." | python3 copy_qa.py -

Checks: banned characters, spam words, shouting, word count, merge tags that
will render empty, and whether the spintax is balanced and actually varied.

Exit code 1 if anything BLOCKS, so it can gate a launch.
"""
import argparse
import random
import re
import sys

# ─────────────────────────────────────────────── character standard
# Applied at build time, never by hand-editing strings, so a banned character
# cannot creep back in from a fragment edited later.
REPLACEMENTS = {
    "\u2014": "-",   # em dash: the single most obvious sign a machine wrote it
    "\u2013": "-",   # en dash
    "\u2212": "-",   # minus sign
    "\u201c": '"', "\u201d": '"',
    "\u2018": "'", "\u2019": "'",
    "\u2026": "...",
    "\u00a0": " ", "\u202f": " ",
}


def normalize(s):
    for a, b in REPLACEMENTS.items():
        s = s.replace(a, b)
    return s


SPAM_WORDS = [
    "100% free", "free trial", "no cost", "risk free", "risk-free", "guarantee",
    "guaranteed", "act now", "urgent", "limited time", "hurry", "don't miss",
    "once in a lifetime", "order now", "buy now", "cheap", "discount",
    "lowest price", "special promotion", "best price", "save big",
    "amazing", "incredible", "revolutionary", "breakthrough", "miracle",
    "unbelievable", "exclusive offer", "congratulations", "winner", "prize",
    "bonus", "jaw-dropping", "life-changing",
    "call now", "click here", "click below", "sign up free", "apply now",
    "increase sales", "extra income", "make money", "earn per week",
    "double your", "cash bonus", "no credit check",
    "this is not spam", "no obligation", "no strings attached", "dear friend",
    "dear sir", "dear madam", "opt out", "unsubscribe",
]

CAPS_ALLOW = {"PS", "CEO", "CFO", "COO", "CTO", "CRO", "VP", "HR", "IT", "CRM",
              "ERP", "SAAS", "GST", "VAT", "SMS", "API", "USD", "INR", "AED",
              "ROI", "TAM", "ICP", "OK", "QSR", "FMCG", "BFSI", "APAC", "UAE"}

# Instantly merge tags are camelCase. Anything not mapped on the lead renders
# EMPTY on every send, which reads worse than not personalising at all.
COMMON_TAGS = {"firstName", "lastName", "companyName", "email", "website",
               "phone", "title", "city"}

# Instantly spintax is {{RANDOM | one | two}}. Uppercase, spaces around pipes.
# The {one|two} form that other tools use does nothing here, it just sends the
# braces to the prospect.
SPIN = re.compile(r"\{\{\s*RANDOM\s*\|(.+?)\}\}", re.S)
BAD_SPIN = re.compile(r"(?<!\{)\{[^{}]*\|[^{}]*\}(?!\})")


def findings(text, allow_caps=None):
    out = []
    t = text.lower()
    for w in SPAM_WORDS:
        if w in t:
            out.append(("BLOCK", "spam word", w))

    allow = CAPS_ALLOW | {x.upper() for x in (allow_caps or set())}
    plain = re.sub(r"\{\{[^}]*\}\}", " ", re.sub(r"<[^>]+>", " ", text))
    for w in set(re.findall(r"\b[A-Z]{4,}\b", plain)):
        if w.upper() not in allow:
            out.append(("WARN", "shouting", w))
    if plain.count("!") > 1:
        out.append(("WARN", "punctuation", "%d exclamation marks" % plain.count("!")))
    for ch, nm in (("\u2014", "em dash"), ("\u2013", "en dash"), ("\u2212", "minus sign")):
        if ch in text:
            out.append(("BLOCK", "banned character", nm))

    for tag in sorted(set(re.findall(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}", text))):
        if tag not in COMMON_TAGS and tag.upper() != "RANDOM":
            out.append(("WARN", "unusual merge tag",
                        "{{%s}} renders empty unless it is set on every lead" % tag))

    if BAD_SPIN.search(text):
        out.append(("BLOCK", "wrong spintax",
                    "found {a|b}. Instantly needs {{RANDOM | a | b}}"))

    n = len(plain.split())
    out.append(("ok" if n <= 100 else "WARN", "word count",
                "%d words%s" % (n, "" if n <= 100 else ", house rule is under 100")))

    spins = SPIN.findall(text)
    combos = 1
    for block in spins:
        combos *= max(1, len([x for x in block.split("|") if x.strip()]))
    if not spins:
        out.append(("WARN", "no spintax",
                    "every prospect gets identical words. Add {{RANDOM | a | b}} blocks"))
    else:
        out.append(("ok" if combos >= 5 else "WARN", "spintax",
                    "%d blocks, %d distinct versions%s"
                    % (len(spins), combos, "" if combos >= 5 else ", aim for 5+")))

    low = text.lower()
    if re.search(r"\b(quick call|hop on a call|15 minutes|30 minutes|book a call|schedule a call)\b", low):
        out.append(("BLOCK", "asks for a call",
                    "never in the first email. Ask for something that costs one word"))
    return out


def render(text, seed=None):
    rnd = random.Random(seed)
    while True:
        m = SPIN.search(text)
        if not m:
            return text
        opts = [o.strip() for o in m.group(1).split("|") if o.strip()]
        text = text[:m.start()] + rnd.choice(opts) + text[m.end():]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="file with the copy, or - for stdin")
    ap.add_argument("--preview", type=int, default=0, help="show N rendered versions")
    ap.add_argument("--brand", nargs="*", default=[], help="brand names allowed in caps")
    a = ap.parse_args()

    raw = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    text = normalize(raw)
    if text != raw:
        print("note: normalised banned characters (em dashes, curly quotes)\n")

    blocked = 0
    for level, kind, detail in findings(text, set(a.brand)):
        mark = {"ok": "  ok ", "WARN": " WARN", "BLOCK": "BLOCK"}[level]
        print(" %s  %-20s %s" % (mark, kind, detail))
        if level == "BLOCK":
            blocked = 1

    if a.preview:
        print("\n" + "-" * 66)
        for i in range(a.preview):
            print("\nversion %d:\n%s" % (i + 1, render(text, seed=i)))

    print("\n%s" % ("READY" if not blocked else "BLOCKED, fix the BLOCK lines above"))
    return blocked


if __name__ == "__main__":
    sys.exit(main())
