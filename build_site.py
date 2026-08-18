#!/usr/bin/env python3
"""Build the Bill Von Fumetti / Booming Bookkeeping swipe site.

Rebuilt 2026-08-01 onto the shared builder so it matches every other competitor
in the swipe file. The previous standalone version is in _superseded/ — it was a
copy of the Shelby template with only two nav links and its own shell.

Run: python3 build_site.py
"""
import sys, os, glob, json, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/BILL_VON_FUMETTI_Swipe")

ORDER = ["Preparty", "Day1", "Day2", "Day3", "Day4", "Day5", "BonusDay6"]


def _rank(p):
    b = os.path.basename(p)
    for i, o in enumerate(ORDER):
        if b.startswith(o):
            return i
    return 99


challenge = sorted(glob.glob(os.path.join(PKG, "Transcript/challenge/*.md")), key=_rank)
funnel_vids = sorted(glob.glob(os.path.join(PKG, "Transcript/bvf_*.md")))

# --- video library, read off disk -------------------------------------------
# The replay hub was captured 1 Aug, hours before Bill's own email said it came
# down ("before it goes away Sunday night"). Durations and sizes are probed
# rather than typed so this page cannot drift from what is actually in
# Recording/ as further sessions land.
BLURBS = {
    "Preparty":   "Warm-up the night before day one. Sets the rules of the week.",
    "Day1":       "The opportunity — market size and why bookkeeping, why now.",
    "Day2":       "The skill. Live QuickBooks teaching with a certification attached.",
    "Day3":       "Bulletproofing — de-risking the model against the obvious objections.",
    "Day4":       "Client acquisition. Two marketing methods, worked end to end.",
    "Day5_PITCH": "<b>The pitch.</b> Value stack, $17,000 anchor, $4,997 price, "
                  "$997 deposit mechanics, deadline and the first-50 bonus.",
    "BonusDay6":  "<b>The second close.</b> A free bonus day that re-stacks the value "
                  "and re-runs the offer at everyone who did not buy on day five.",
    "bvf_909612633": "Welcome / registration confirmation. The night-terrors origin story.",
    "bvf_909822828": "Member testimonial, used to sell the VIP tier.",
    "bvf_909619779": "Facebook group onboarding and next steps.",
}


def _probe(path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", path],
            capture_output=True, text=True, timeout=60).stdout.strip()
        return int(float(out))
    except Exception:
        return 0


def video_library():
    """(name, seconds, human size, blurb) for every mp4 actually on disk."""
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/*.mp4")), key=_rank):
        stem = os.path.splitext(os.path.basename(p))[0]
        mb = os.path.getsize(p) / 1e6
        size = f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB"
        rows.append((os.path.basename(p), _probe(p), size,
                     BLURBS.get(stem, "Captured from the replay hub.")))
    return rows

CONFIG = {
    "SITE": "Bill Von Fumetti — Booming Bookkeeping Business",
    "CREATOR": "Bill Von Fumetti",
    "ADS_KEY": "bill_von_fumetti",
    "FUNNEL_IDS": ["F086"],
    "CAPTURED": "challenge 30 July 2026 · funnel 31 July 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/BILL_VON_FUMETTI_Swipe",
    "BLURB": "A five-day live challenge run inside a Facebook group, closing at <b>$4,997</b> "
             "against a $17,000 anchor. The deepest capture in this swipe file — the entire "
             "previous cohort including a 170-minute pitch day and a bonus day six second "
             "close. <b>12h 16m, 135,840 words.</b>",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "The 5 days"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Price", "$4,997"),
        ("Anchor", "$17,000"),
        ("Deposit", "$997"),
        ("Captured", "12h 16m"),
        ("Words", "135,840"),
        ("Sessions", "7"),
        ("Pitch day", "170 min"),
        ("Active ads", "190"),
    ],

    "OFFER": [
        ("Product", "Booming Bookkeeping Business mentorship"),
        ("Front end", "Keyboard Rich Challenge — 5 days, 90 min/day, free"),
        ("Price", "<b>$4,997</b> one payment, or 3 &times; $1,997"),
        ("Anchor", "$17,000 — &ldquo;you can see why it&rsquo;s a good deal financially at "
                   "$17,000&rdquo; (Day 5, 01:49:40)"),
        ("Deposit", "$997 at keyboardrich.com/yes, then a DocuSign, then a separate page for "
                    "the balance"),
        ("Plan honesty", "He says outright the plan costs more: &ldquo;the payment plan is more "
                         "expensive due to the fact that hey interest we&rsquo;ve got "
                         "people&rsquo;s credit cards… we have to administer the payment "
                         "plan&rdquo;"),
        ("Close", "Enrollment shuts Sunday midnight Pacific"),
        ("First 50", "Lifetime access instead of one year"),
        ("Value stack", "Coaching calls &ldquo;$1,997 value&rdquo;, QuickBooks certification "
                        "&ldquo;$997&rdquo;, community &ldquo;$997&rdquo;. Running total called "
                        "out live at $7,991 then $11,982"),
        ("Venue", "Facebook group, with live Zoom sessions"),
    ],

    "FINDINGS": [
        ("The phone objection is killed inside the placeholder",
         "His opt-in field reads <b>&ldquo;Phone (for text reminders — we will NEVER call "
         "you)&rdquo;</b>. He names the exact fear the field creates, in the field itself. Every "
         "other funnel in this swipe file takes the number under autodial consent and says "
         "nothing. Six words against a known drop-off point — the cheapest test on our own "
         "opt-in."),
        ("A bonus Day 6 that is a second close",
         "After the 170-minute pitch on Day 5 he runs a further <b>139-minute</b> session that "
         "re-stacks the value and re-runs the close on everyone who did not buy. 26,567 words of "
         "it are captured. Our masterclass gets one shot and has no structured second pass."),
        ("The deposit splits the decision",
         "$997 holds the spot. Then a DocuSign. Then a separate page for the balance. The buyer "
         "commits small, signs, and only then faces the real number — materially easier to say "
         "yes to than $4,997 up front."),
        ("He admits the payment plan costs more",
         "Most operators bury financing markup. He explains it out loud as an interest and "
         "administration cost. It reads as honesty and makes paying in full feel like the "
         "buyer&rsquo;s own idea."),
        ("Run the event where the community already is",
         "The challenge is delivered in a Facebook group, not a webinar room. Attendance becomes "
         "social, peer proof accumulates in public, and the asset persists after the week ends. "
         "Ours evaporates when the Zoom closes."),
        ("Risk-aversion lead, not an income claim",
         "His ads open &ldquo;I knew I wanted to start my own business but everything felt risky "
         "— until I found this&rdquo; and frame bookkeeping as an <i>overlooked skill</i>. The "
         "most restrained voice of the seven, and he still runs 190 active ads."),
        ("Engagement is issued as a numbered task",
         "His first Facebook post is headed <b>&ldquo;TASK #1: IMPORTANT - START HERE&rdquo;</b> "
         "and instructs members to watch the entire video and <i>then like the post when "
         "you&rsquo;ve finished</i>. The like is not asked for as a favour, it is the "
         "completion marker for an assignment &mdash; which also tells him exactly who "
         "finished."),
        ("All five days added to the calendar in one click",
         "The same post carries a single AddEvent link that drops <b>all five trainings</b> "
         "into the registrant&rsquo;s calendar at once, before day one. We ask for one "
         "calendar add per session."),
    ],

    "FUNNEL": [
        ("Challenge opt-in", "thebookkeepingchallenge.com/live-1",
         "First name, email, phone — with the reassurance microcopy inside the field."),
        ("VIP upgrade", "keyboardrichchallenge.com/vipfc-1",
         "Paid VIP tier, sold with a <b>member testimonial video</b> rather than founder "
         "assertion."),
        ("Facebook group / next steps", "keyboardrichchallenge.com/nextstepsfc-2",
         "Routes registrants into the group where the challenge actually runs."),
        ("5 live sessions", "boomingbookkeeping.zoom.us/j/81705832147",
         '<span class="tag good">genuinely live</span> Aug 3–7, 9:00 AM PT. Registered; '
         'recorder scheduled. The July cohort is already captured end to end — see the '
         'video library.'),
        ("Replay hub", "keyboardrichchallenge.com/challengereplay",
         'All seven sessions, Vimeo-hosted, gated only by having registered. Pulled 1 Aug; '
         'Bill&rsquo;s own day-five email says it comes down Sunday night.'),
        ("Checkout", "keyboardrich.com/yes",
         "$997 deposit &rarr; DocuSign &rarr; balance page. Never submitted."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("The challenge — 7 sessions, 12h 16m, 135,840 words", challenge),
        ("Funnel videos", funnel_vids),
    ],

    "SLIDE_PAGES": [],

    # Webinar decks only, and slides only — the talking-head frames are stripped
    # before the PPTX is built. Day 6 keeps just 44 of 521 frames because that
    # session is mostly Bill on camera answering questions; Day 5 is the real
    # presentation and keeps 331.
    "DECKS": [
        ("Preparty (46m) — screen-share of the Facebook group, not slides", 18,
         "https://docs.google.com/presentation/d/1t22KH5GOt9MvmCaEW4vJ6uscROUU1jvEOQbkE6pbwAQ/edit"),
        ("Day 1 — the opportunity (94m)", 354,
         "https://docs.google.com/presentation/d/1WvjLGbuUqwUSl2ccAgG5sn7xNb4LtyLlQuMU5K2mBLI/edit"),
        ("Day 2 — the skill, live QuickBooks (97m)", 459,
         "https://docs.google.com/presentation/d/1noG0U894OvmW5_JILG4mbI0O9znY_-BANfW-CQefbBI/edit"),
        ("Day 3 — bulletproofing (100m)", 721,
         "https://docs.google.com/presentation/d/1Knoh-L-5PjNW2M5kFMFfP55GmYLwfpKFtryRdCm4FwM/edit"),
        ("Day 4 — client acquisition (91m)", 712,
         "https://docs.google.com/presentation/d/1XpOb7cokGIp9w_88RNy1sfPQJdhBndRIzLc6LiVcnh8/edit"),
        ("Day 5 — THE PITCH (170m)", 250,
         "https://docs.google.com/presentation/d/1PvZH19iBqeDXRAtnEe-ljIfDRhguwAlZESlYBWyV5hA/edit"),
        ("Bonus Day 6 — the second close (139m)", 44,
         "https://docs.google.com/presentation/d/1x4BfaOjJhcfTcJLSA093BVczT4uprEaVgf51j87CxjI/edit"),
    ],

    "VIDEOS": video_library(),

    "ANALYSIS": """
<div class="note"><b>Why this is the deepest capture we have.</b> Every other competitor here is
captured at the funnel and the pitch. Bill Von Fumetti is captured across an entire five-day
cohort <i>plus</i> a bonus second-close day — 12 hours 16 minutes and 135,840 words, including
the full 170-minute pitch. If you want to study how a challenge actually converts, this is the
one to read.</div>

<h2 class="sec">How the five days are structured</h2>
<div class="tablewrap"><table>
<tr><th>Session</th><th>Length</th><th>Words</th><th>Job</th></tr>
<tr><td>Preparty</td><td>45m</td><td>8,772</td><td>Warm the room before day one</td></tr>
<tr><td>Day 1 — Opportunity</td><td>94m</td><td>18,874</td><td>The market, the why-now</td></tr>
<tr><td>Day 2 — Skill / QuickBooks</td><td>97m</td><td>15,042</td><td>Teach a real, checkable skill</td></tr>
<tr><td>Day 3 — Bulletproof</td><td>100m</td><td>17,744</td><td>De-risk the model</td></tr>
<tr><td>Day 4 — Client acquisition</td><td>91m</td><td>18,724</td><td>Where the money comes from</td></tr>
<tr><td><b>Day 5 — PITCH</b></td><td><b>170m</b></td><td><b>30,117</b></td><td>Value stack, price, close</td></tr>
<tr><td>Bonus Day 6 — second close</td><td>139m</td><td>26,567</td><td>Re-close everyone who did not buy</td></tr>
</table></div>
<p style="margin-top:12px">Four days of teaching, then a pitch day nearly twice the length of a
normal session, then a bonus day that is a second close in all but name. The teaching days are
not filler — Day 2 teaches an actual certifiable skill, and that is what earns him the right to
ask $4,997 on Day 5.</p>

<h2 class="sec">The close, beat by beat</h2>
<div class="tablewrap"><table>
<tr><th>Time</th><th>Beat</th><th>What he does</th></tr>
<tr><td>01:40</td><td>Value stack</td><td>Coaching calls at &ldquo;$1,997 value&rdquo;, certification &ldquo;$997&rdquo;, community &ldquo;$997&rdquo;</td></tr>
<tr><td>01:43</td><td>Running total</td><td>Calls it out live: $7,991, then $11,982</td></tr>
<tr><td>01:48</td><td>ROI frame</td><td>&ldquo;Getting back 50, 75 or 100 every single year… you can&rsquo;t find that in the stock market or bitcoin&rdquo;</td></tr>
<tr><td>01:49</td><td>Anchor</td><td><b>$17,000</b> — &ldquo;you can see why it&rsquo;s a good deal financially&rdquo;</td></tr>
<tr><td>01:52</td><td>Price</td><td><b>$4,997</b> once, or 3 &times; $1,997</td></tr>
<tr><td>01:52</td><td>Deposit</td><td>$997 at keyboardrich.com/yes holds the spot</td></tr>
<tr><td>01:54</td><td>Mechanics</td><td>Deposit &rarr; DocuSign &rarr; balance page, spelled out step by step</td></tr>
<tr><td>02:03</td><td>Deadline + bonus</td><td>Sunday midnight Pacific; first 50 get lifetime access</td></tr>
<tr><td>02:18+</td><td>Repetition</td><td>The deposit URL is repeated at least five more times before the session ends</td></tr>
</table></div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Defuse the phone field in the placeholder</h3><p><i>&ldquo;for text reminders
— we will NEVER call you.&rdquo;</i> Our opt-in asks for a number and says nothing. Six words
against a measurable drop-off, and it costs nothing to test.</p></div>
<div class="card"><h3>Build in a second close</h3><p>His bonus Day 6 exists purely to re-close
non-buyers, and it runs 139 minutes — not a token follow-up. We have no structured second pass
at all after the masterclass.</p></div>
<div class="card"><h3>Split the payment decision</h3><p>A small deposit, a signature, then the
balance. Commitment escalates in three steps instead of one. Directly applicable to our own
checkout.</p></div>
<div class="card"><h3>Teach something certifiable</h3><p>Day 2 is a real QuickBooks skill with a
certification attached. It converts &ldquo;free challenge&rdquo; into &ldquo;I already got
something of value&rdquo; before any money is asked for.</p></div>
</div>

<h2 class="sec">Read carefully</h2>
<p>Whisper renders his prices without the thousands separator — <b>$4,997</b> appears as
&ldquo;49.97&rdquo; and <b>$1,997</b> as &ldquo;1997&rdquo;. Worse, &ldquo;1997&rdquo; is also a
value-stack figure in the same pitch (&ldquo;those coaching calls are a 1997 value&rdquo;), so
the same token means two different things. The price here is verified because it is stated three
separate times — Day 5 at 01:52:45 and 02:02:01, and Day 6 at 01:21:29 — and all three agree.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
