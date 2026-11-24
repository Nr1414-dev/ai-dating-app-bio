#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes one dating-app bio line to /output/entry.txt.

Line (93 chars, 93 bytes UTF-8):
    I will fact-check your fishing stories mid-date. Sorry in advance.
    The fish was not that big.
"""
import sys
import unicodedata
from pathlib import Path

BIO = "I will fact-check your fishing stories mid-date. Sorry in advance. The fish was not that big."
OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"
MAX_CHARS = 180


def _fail(message):
    print(f"entry check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def _validate(text):
    if not 1 <= len(text) <= MAX_CHARS:
        _fail(f"length {len(text)} is outside 1-{MAX_CHARS} characters")
    if "\n" in text or "\r" in text:
        _fail("entry must be a single line")
    if text.strip() != text:
        _fail("entry must not start or end with whitespace")
    for ch in text:
        if unicodedata.category(ch).startswith("C"):
            _fail(f"control character U+{ord(ch):04X} is not allowed")


def _verify_written():
    written = OUT_FILE.read_bytes()
    if written != BIO.encode("utf-8"):
        _fail("bytes on disk differ from the bio line")


def run():
    _validate(BIO)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(BIO)
    OUT_FILE.chmod(0o644)
    _verify_written()


if __name__ == "__main__":
    run()
