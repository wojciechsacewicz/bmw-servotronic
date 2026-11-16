#!/usr/bin/env python3
"""Check the publication tree without opening a vehicle connection."""

import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = {"README.md", "AGENTS.md", "RIGHTS.md", ".gitignore"}
PRIVATE_PATTERNS = {
    "vehicle identifier": r"\bW[A-HJ-NPR-Z0-9]{16}\b",
    "home directory": r"/(?:home|Users)/[A-Za-z0-9_.-]+/",
    "Windows user directory": r"[A-Za-z]:\\Users\\[^\\\s]+",
    "session identifier": r"\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b",
    "private thread link": r"t3[-]thread://|provider[-]thread:|run:thread[:]",
    "common credential": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{24,})\b",
    "email address": r"\b[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
}


def private_findings(text):
    return [name for name, pattern in PRIVATE_PATTERNS.items()
            if re.search(pattern, text, re.IGNORECASE)]


def heading_slug(text):
    text = text.lower().replace("`", "")
    text = "".join(c for c in text if c in " -_" or
                   unicodedata.category(c)[0] in "LN")
    return text.replace(" ", "-")


def allowed(path):
    relative = path.relative_to(ROOT)
    return (str(relative) in ROOT_FILES or
            relative.parent == Path("docs") and path.suffix == ".md" or
            str(relative) in {"data/attempts.json", "scripts/check_repository.py"})


def check():
    errors = []
    files = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts:
            continue
        if path.is_symlink():
            errors.append(f"{relative}: symlinks are outside the publication boundary")
        elif path.is_file():
            files.append(path)
            if not allowed(path):
                errors.append(f"{relative}: unexpected publication file")
            if path.stat().st_size > 1_000_000:
                errors.append(f"{relative}: unexpectedly large file")
    for name in ROOT_FILES | {"docs/agent-guide.md", "docs/evidence.md",
                             "docs/attempts.md", "data/attempts.json"}:
        if not (ROOT / name).is_file():
            errors.append(f"{name}: missing required file")

    for path in files:
        relative = path.relative_to(ROOT)
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"{relative}: unreadable text or binary artifact")
            continue
        for finding in private_findings(text):
            errors.append(f"{relative}: possible {finding}")
        if "\u2014" in text:
            errors.append(f"{relative}: long dash in generated prose")
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not linked.is_relative_to(ROOT) or not linked.is_file():
                errors.append(f"{relative}: missing or external local link {target}")
            elif parsed.fragment:
                headings = {heading_slug(h) for h in
                            re.findall(r"^#+\s+(.+)$", linked.read_text(), re.MULTILINE)}
                if unquote(parsed.fragment) not in headings:
                    errors.append(f"{relative}: missing heading {target}")

    try:
        attempts = json.loads((ROOT / "data/attempts.json").read_text())
        ids = [entry["id"] for entry in attempts]
        if ids != [f"A{i:03}" for i in range(1, 115)]:
            errors.append("attempt dataset must preserve ordered IDs A001 through A114")
        ledger = (ROOT / "docs/attempts.md").read_text()
        for entry in attempts:
            for key in ("id", "title", "action", "result", "status", "limits", "next_question"):
                if not isinstance(entry.get(key), str) or not entry[key]:
                    errors.append(f"{entry.get('id')}: missing field {key}")
            if f"## {entry['id']} {entry['title']}" not in ledger:
                errors.append(f"{entry['id']}: missing ledger heading")
            for key in ("action", "result", "limits", "next_question"):
                if entry[key] not in ledger:
                    errors.append(f"{entry['id']}: ledger differs from dataset field {key}")
            for key in ("superseded_by", "followed_by"):
                if any(value not in ids for value in entry.get(key, [])):
                    errors.append(f"{entry['id']}: unknown related attempt")
    except (OSError, ValueError, TypeError, KeyError) as error:
        errors.append(f"invalid attempt dataset or ledger: {error}")

    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"PASS: {len(files)} publication files; 114 attempts; links, ledger, and privacy patterns checked.")
    print("This checks repository hygiene, not vehicle compatibility or steering safety.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
