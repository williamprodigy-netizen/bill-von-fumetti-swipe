#!/usr/bin/env python3
"""Bill Von Fumetti / Booming Bookkeeping — the whole business, wired.

The 5-day challenge transcripts (Preparty through Day 5 pitch, plus a bonus
Day 6 second close) were captured 30 July and live in data/transcripts.json.
This board wires the funnel around them.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build, X

REPO = os.path.dirname(os.path.abspath(__file__))
S = os.path.expanduser("~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS")
P = f"{S}/Bill_Von_Fumetti - Keyboard_Rich_5-Day_Challenge - 2026-07-30/02_Pages"

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · pages 31 July 2026 · sessions 30 July 2026",
    "TITLE": "Bill Von Fumetti — the whole business, wired",
    "BLURB": "A five-day live challenge run inside a Facebook group rather than a webinar room, "
             "with a paid VIP tier layered on top. The full previous cohort is captured &mdash; "
             "<b>12h 16m and 135,840 words</b>, including a 170-minute pitch day and a bonus "
             "day six second close.",

    "SHOTS": {
        "optin": {
            "col": 1, "y": 120, "lane": "event", "step": "Entry",
            "title": "Challenge opt-in",
            "url": "thebookkeepingchallenge.com/live-1",
            "img": f"{P}/01_Live_opt-in/20260730T110254Z__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "&ldquo;5 days, just 90 minutes a day.&rdquo; First name, email, phone "
                    "&mdash; and the phone field's own placeholder reads <b>&ldquo;for text "
                    "reminders, we will NEVER call you&rdquo;</b>.",
        },
        "vip": {
            "col": 2, "y": 120, "lane": "back", "step": "Upsell",
            "title": "VIP upgrade",
            "url": "keyboardrichchallenge.com/vipfc-1",
            "img": f"{P}/02_VIP_TY_page/20260730T110306Z__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "Paid VIP tier offered straight after registration, sold with a "
                    "<b>member testimonial video</b> rather than founder assertion.",
        },
        "group": {
            "col": 3, "y": 120, "lane": "ever", "step": "Onboard",
            "title": "Facebook group / next steps",
            "url": "keyboardrichchallenge.com/nextstepsfc-2",
            "img": f"{P}/03_Facebook_group_next_steps/20260730T110325Z__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "Routes registrants into the group. The challenge lives there, not in a "
                    "webinar room, so attendance becomes social and the asset persists.",
        },
    },

    "DATA": {
        "days": {
            "col": 4, "y": 120, "lane": "event", "step": "The challenge",
            "title": "Five days + a bonus day",
            "kv": [("Preparty", "45m · 8,772 w"),
                   ("Day 1 Opportunity", "94m · 18,874 w"),
                   ("Day 2 QuickBooks", "97m · 15,042 w"),
                   ("Day 3 Bulletproof", "100m · 17,744 w"),
                   ("Day 4 Client acq.", "91m · 18,724 w"),
                   ("Day 5 <b>PITCH</b>", "170m · 30,117 w"),
                   ("Day 6 second close", "139m · 26,567 w")],
            "note": "Teach for four days, pitch on day five for nearly three hours, then run a "
                    "second close on a bonus day six.",
        },
        "offer": {
            "col": 5, "y": 120, "lane": "paid", "step": "Close",
            "title": "The offer",
            "kv": [("Pitched", "Day 5, from ~01:48"),
                   ("Templates", "&ldquo;$997 value&rdquo;"),
                   ("Access", "one full year"),
                   ("Included", "support, coaches, him"),
                   ("Price", "see Day 5 transcript")],
            "note": "The full stack and close are in the captured Day 5 transcript on the "
                    "transcripts page of this site.",
        },
        "next": {
            "col": 6, "y": 120, "lane": "event", "step": "Next cohort",
            "title": "Aug 3&ndash;7 cohort — registered",
            "kv": [("Dates", "Mon 3 &ndash; Fri 7 Aug"),
                   ("Time", "9:00 AM PT daily"),
                   ("Length", "90 min/day"),
                   ("Zoom", "j/81705832147"),
                   ("Zoom 2", "j/82304411625"),
                   ("Live?", "genuinely live")],
            "note": "Registered on the research identity. Real Zoom meetings, so these have to "
                    "be captured on the day.",
        },
    },

    "EDGES": [
        ("optin", "vip"), ("vip", "group"), ("group", "days"),
        ("days", "offer"), ("offer", "next"),
    ],

    "LABELS": [
        {"x": X[1], "y": 60, "t": "Challenge funnel"},
        {"x": X[1], "y": 1600, "t": "Routing logic"},
    ],

    "BRANCH": [
        {"id": "b_phone", "x": X[1] + 10, "y": 1660, "state": "yes",
         "cond": "Phone field → objection killed in the placeholder",
         "body": "<b>&ldquo;Phone (for text reminders &mdash; we will NEVER call you)&rdquo;.</b> "
                 "He names the exact fear the field creates and kills it inside the placeholder "
                 "text. Every other funnel in this swipe file takes the number under autodial "
                 "consent and says nothing. Cheapest conversion fix in the whole set, and "
                 "directly testable on our own opt-in.",
         "ev": "VERIFIED · form inspected live 31 Jul"},
        {"id": "b_group", "x": X[3] + 10, "y": 1660, "state": "yes",
         "cond": "Registers → routed into a Facebook group",
         "body": "The challenge is delivered in a group rather than a webinar room. Attendance "
                 "becomes social, peer proof accumulates in public where prospects can see it, "
                 "and the asset persists after the week ends. Our masterclass evaporates the "
                 "moment the Zoom closes.",
         "ev": "VERIFIED · next-steps page + welcome video transcript"},
        {"id": "b_vip", "x": X[5] + 10, "y": 1660, "state": "yes",
         "cond": "VIP is sold by a member, not the founder",
         "body": "The VIP page leads with a member describing the experience &mdash; watching "
                 "questions answered live and getting her own answered. At the exact moment he "
                 "asks for more money, the voice is not his.",
         "ev": "VERIFIED · transcript of the VIP page testimonial video"},
        {"id": "b_second", "x": X[7] + 10, "y": 1660, "state": "yes",
         "cond": "Did not buy on Day 5 → a bonus Day 6 second close",
         "body": "A 139-minute bonus day runs after the pitch day, functioning as a second close "
                 "on everyone who did not convert. 26,567 words of it are captured. Our own "
                 "masterclass has one shot and no structured second pass.",
         "ev": "VERIFIED · Day 6 transcript captured 30 Jul"},
    ],

    "LEGEND": [("event", "Challenge"), ("ever", "Community"),
               ("paid", "Close"), ("back", "VIP upsell")],
}

if __name__ == "__main__":
    build(CONFIG)
