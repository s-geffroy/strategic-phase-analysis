#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_scores.py <machine_output.yaml>")
        sys.exit(2)

    yaml_path = Path(sys.argv[1])
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
    scores = data.get("support_scores", {})
    passed = True

    if not isinstance(scores, dict) or not scores:
        print("[FAIL] Missing or empty support_scores")
        sys.exit(1)

    for key, value in scores.items():
        if not isinstance(value, int) or value < 0 or value > 5:
            print(f"[FAIL] Invalid score {key}: {value}. Expected integer 0–5.")
            passed = False
        elif value >= 4:
            print(f"[REVIEW] Critical score requires rationale: {key}={value}")
        else:
            print(f"[OK] {key}={value}")

    confidence = data.get("confidence")
    evidence_status = data.get("evidence_status")
    if confidence == "high" and evidence_status == "weak":
        print("[FAIL] confidence: high is forbidden with evidence_status: weak")
        passed = False

    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
