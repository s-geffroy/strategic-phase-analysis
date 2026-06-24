#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

REQUIRED_FILES = [
    "00_short_diagnostic.md",
    "01_full_analytical_fiche.md",
    "02_machine_output.yaml",
    "03_decision_synthesis.md",
    "04_evidence_notes.md",
    "05_validation_log.md",
]

def fail(msg):
    print(f"[FAIL] {msg}")
    return False

def ok(msg):
    print(f"[OK] {msg}")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_case.py <case_dir>")
        sys.exit(2)

    case_dir = Path(sys.argv[1])
    passed = True

    if not case_dir.exists():
        print(f"[FAIL] Case directory not found: {case_dir}")
        sys.exit(1)

    for name in REQUIRED_FILES:
        path = case_dir / name
        if path.exists():
            ok(f"Found {name}")
        else:
            passed = fail(f"Missing {name}") and passed

    yaml_path = case_dir / "02_machine_output.yaml"
    if yaml_path.exists():
        try:
            data = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
            ok("Machine YAML readable")
        except Exception as e:
            print(f"[FAIL] YAML parse error: {e}")
            sys.exit(1)

        required_keys = ["case_id", "dominant_phase", "confidence", "evidence_status", "analyst_validation"]
        for key in required_keys:
            if key in data:
                ok(f"YAML has {key}")
            else:
                passed = fail(f"YAML missing {key}") and passed

    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
