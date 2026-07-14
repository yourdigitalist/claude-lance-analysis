#!/usr/bin/env python3
"""
Meta ads compliance checker for Lance marketing copy.

Scans ad copy or a creative description (e.g. "screenshot showing $4,100 paid")
against Lance's known Meta compliance risk patterns and prints a risk rating
plus suggested fixes for anything flagged.

Usage:
    python3 check_compliance.py "ad copy text here"
    python3 check_compliance.py --file path/to/copy.txt
    echo "ad copy text" | python3 check_compliance.py
    python3 check_compliance.py "ad copy text" --json
"""

import argparse
import json
import re
import sys

RATING_ORDER = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}

DOLLAR_RE = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?")

SCARCITY_RE = re.compile(
    r"\bonly\s+\d+\b"
    r"|\b\d+\s+(spots?|seats?|spaces?|slots?)\s+(left|remaining)\b"
    r"|\blimited\s+(time|spots?|seats?|availability)\b"
    r"|\blast\s+chance\b"
    r"|\bact\s+now\b"
    r"|\bhurry\b"
    r"|\bwhile\s+supplies?\s+last\b",
    re.IGNORECASE,
)

# Unverified social-proof / stat patterns: "2,400+ freelancers", "10,000 users trust", "93% of clients"
STAT_CLAIM_RE = re.compile(
    r"\b\d[\d,]*\+?\s+(freelancers?|users?|clients?|customers?|people|teams?)\b"
    r"|\b\d+(\.\d+)?%\s+of\b"
    r"|\btrusted\s+by\s+\d",
    re.IGNORECASE,
)

TESTIMONIAL_RE = re.compile(
    r'"[^"]{15,}"'
    r"|\bsaid\b.{0,40}(freelancer|client|customer|user)\b"
    r"|\breview(s|ed)?\b.{0,20}\bstars?\b",
    re.IGNORECASE,
)

VAGUE_SAFE_RE = re.compile(
    r"\borgani[sz]ed\s+freelancers?\s+earn\s+more\b"
    r"|\bearn\s+more\b(?!\s+than\s+\$)"
    r"|\bget\s+paid\s+faster\b"
    r"|\blook\s+more\s+professional\b",
    re.IGNORECASE,
)


def find_all(pattern, text):
    return [m.group(0) for m in pattern.finditer(text)]


def check(text: str) -> dict:
    findings = []

    dollar_hits = find_all(DOLLAR_RE, text)
    if dollar_hits:
        findings.append({
            "category": "implied_earnings_claim",
            "rating": "HIGH",
            "matches": dollar_hits,
            "issue": (
                "Specific dollar figure(s) found. Per known pattern, these read as "
                "implied earnings claims even in obvious UI mockups or screenshots."
            ),
            "fix": (
                "Remove the specific figure(s) or replace with non-numeric language "
                "(e.g. 'get paid faster' instead of '$4,100 paid'). If a real figure "
                "must be shown, it needs Marina's sign-off and should be verifiable, "
                "not illustrative."
            ),
        })

    scarcity_hits = find_all(SCARCITY_RE, text)
    if scarcity_hits:
        findings.append({
            "category": "scarcity_claim",
            "rating": "HIGH",
            "matches": scarcity_hits,
            "issue": (
                "Scarcity language found. This is a known Meta rejection trigger and "
                "is only usable if the claim is literally true and enforced."
            ),
            "fix": (
                "Confirm with Marina whether the cap/limit is real and actively "
                "enforced. If not, remove the scarcity line or replace with evergreen "
                "phrasing that doesn't imply a countdown or limited inventory."
            ),
        })

    stat_hits = find_all(STAT_CLAIM_RE, text)
    if stat_hits:
        findings.append({
            "category": "unverified_stat_or_social_proof",
            "rating": "MEDIUM",
            "matches": stat_hits,
            "issue": (
                "Numeric claim about users/customers/percentage found. Per the voice "
                "rule, real proof only — never fabricate stats or user counts. If this "
                "number isn't confirmed real, it's a placeholder, not final copy."
            ),
            "fix": (
                "Confirm this number is real and current. If it's a placeholder, say "
                "so explicitly rather than shipping it as final copy, or remove the "
                "claim entirely until real data exists."
            ),
        })

    testimonial_hits = find_all(TESTIMONIAL_RE, text)
    if testimonial_hits:
        findings.append({
            "category": "testimonial_or_quote",
            "rating": "MEDIUM",
            "matches": testimonial_hits,
            "issue": (
                "Quote or testimonial-style language found. Testimonials must be real "
                "— never fabricated."
            ),
            "fix": (
                "Confirm this is a real, attributable testimonial with permission to "
                "use it. If invented for illustration, remove it or clearly label it "
                "as a placeholder/example."
            ),
        })

    vague_hits = find_all(VAGUE_SAFE_RE, text)
    if vague_hits and not findings:
        findings.append({
            "category": "vague_claim",
            "rating": "LOW",
            "matches": vague_hits,
            "issue": (
                "Vague, non-specific claim found. This is the lower-risk pattern "
                "compared to specific dollar figures or stats."
            ),
            "fix": "No action needed. This phrasing is on the safer end of the known risk spectrum.",
        })

    if not findings:
        overall = "LOW"
    else:
        overall = max((f["rating"] for f in findings), key=lambda r: RATING_ORDER[r])

    return {
        "input": text,
        "overall_risk": overall,
        "findings": findings,
        "note": (
            "No claims or stats detected. Personal-narrative format with no stats or "
            "claims has been the safest and most on-brand format so far."
            if not findings else None
        ),
    }


def format_report(result: dict) -> str:
    lines = []
    lines.append("# Meta Ads Compliance Check")
    lines.append("")
    lines.append(f"**Input:** {result['input']}")
    lines.append("")
    lines.append(f"**Overall risk: {result['overall_risk']}**")
    lines.append("")

    if not result["findings"]:
        lines.append("No known risk patterns detected.")
        if result.get("note"):
            lines.append("")
            lines.append(result["note"])
        return "\n".join(lines)

    lines.append("## Findings")
    lines.append("")
    for i, f in enumerate(result["findings"], 1):
        lines.append(f"{i}. **[{f['rating']}] {f['category']}** — matched: {', '.join(repr(m) for m in f['matches'])}")
        lines.append(f"   - Issue: {f['issue']}")
        lines.append(f"   - Suggested fix: {f['fix']}")
        lines.append("")

    lines.append("---")
    lines.append("Reminder: anything that spends money or goes live gets Marina's sign-off first.")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Check ad copy against Lance's Meta compliance risk patterns.")
    parser.add_argument("text", nargs="?", help="Ad copy or creative description to check")
    parser.add_argument("--file", help="Path to a file containing the ad copy")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of a formatted report")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as f:
            text = f.read()
    elif args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.error("Provide ad copy as an argument, --file, or via stdin.")
        return

    result = check(text.strip())

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_report(result))


if __name__ == "__main__":
    main()
