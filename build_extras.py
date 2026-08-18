#!/usr/bin/env python3
"""Add the funnel-pages gallery and copy bank to the Bill Von Fumetti site.

His index/transcripts pages predate the shared builder, so they are left alone.
This only adds the two Shelby-standard pages he was missing.

Run: python3 build_extras.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import shell
import extras, json as _j

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/BILL_VON_FUMETTI_Swipe")

CFG = {
    "SITE": "Bill Von Fumetti — Keyboard Rich Bookkeeping",
    "CREATOR": "Bill Von Fumetti",
    "CAPTURED": "31 July 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/BILL_VON_FUMETTI_Swipe",
    "PAGES": [
        ("index.html", "Overview"),
        ("board.html", "Board"),
        ("transcripts.html", "The 5 days"),
    ],
}

if __name__ == "__main__":
    pages = extras.collect_pages(CFG["CREATOR"], REPO)
    if not pages:
        print("no captured pages found")
        sys.exit(1)
    open(os.path.join(REPO, "pages.html"), "w", encoding="utf-8").write(
        extras.page_pages(CFG, shell, pages))
    tx = sorted(glob.glob(os.path.join(PKG, "Transcript", "*.md")))
    banks = extras.mine_copy(pages, tx)
    open(os.path.join(REPO, "copybank.html"), "w", encoding="utf-8").write(
        extras.page_copybank(CFG, shell, banks))
    b, method = extras.ads_for("bill_von_fumetti")
    if b:
        allb = _j.load(open(extras.ADS_JSON))["brands"]
        peers = sorted(((v.get("brand_name") or k, v.get("active_ads"), v.get("top_score"))
                        for k, v in allb.items()), key=lambda t: -(t[1] or 0))
        CFG["PAGES"].append(("ads.html", "Ads"))
        open(os.path.join(REPO, "ads.html"), "w", encoding="utf-8").write(
            extras.page_ads(CFG, shell, b, method, peers, extras.deep_for("bill_von_fumetti")))
        print("ads.html written")
    print(f"pages.html ({len(pages)} pages) + copybank.html "
          f"({sum(len(v) for v in banks.values())} lines) -> {REPO}")
