#!/usr/bin/env python3
from pathlib import Path
import sys

FORBIDDEN = [
    "ferritic", "austenitic", "pearlitic", "bainitic", "martensitic", "cementitic",
    "ferritique", "austénitique", "perlitique", "bainitique", "martensitique", "cémentitique",
]

PUBLIC_FILES = [
    "00_short_diagnostic.md",
    "01_full_analytical_fiche.md",
    "03_decision_synthesis.md",
]

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_public_terms.py <case_dir>")
        sys.exit(2)

    case_dir = Path(sys.argv[1])
    passed = True

    for filename in PUBLIC_FILES:
        path = case_dir / filename
        if not path.exists():
            print(f"[WARN] Missing public file: {filename}")
            continue

        text = path.read_text(encoding="utf-8").lower()
        for term in FORBIDDEN:
            if term.lower() in text:
                print(f"[FAIL] Forbidden internal term '{term}' found in {filename}")
                passed = False

    if passed:
        print("[OK] No forbidden internal terms found in public outputs.")
    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
