#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    files = sorted((root / "schema").rglob("*.graphql"))
    if not files:
        print("no graphql files", file=sys.stderr); return 1
    for p in files:
        text = p.read_text(encoding="utf-8")
        if text.count("{") != text.count("}"):
            print(f"{p}: unbalanced braces", file=sys.stderr); return 1
        if not re.search(r"\b(type|input|enum|scalar|interface|union|query|mutation|subscription)\b", text):
            print(f"{p}: no SDL definition", file=sys.stderr); return 1
    print(f"graphql validation ok ({len(files)} files)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
