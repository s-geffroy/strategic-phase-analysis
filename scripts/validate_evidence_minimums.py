#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

def count_table_rows(markdown_text, section_title):
    # Simple heuristic: count markdown table data rows after a section title.
    idx = markdown_text.lower().find(section_title.lower())
    if idx == -1:
        return 0
    chunk = markdown_text[idx: idx + 2500]
    rows = [line for line in chunk.splitlines() if line.strip().startswith("|") and "---" not in line]
    # subtract header row when present
    return max(0, len(rows) - 1)

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_evidence_minimums.py <case_dir>")
        sys.exit(2)

    case_dir = Path(sys.argv[1])
    yaml_path = case_dir / "02_machine_output.yaml"
    evidence_path = case_dir / "04_evidence_notes.md"

    if not yaml_path.exists() or not evidence_path.exists():
        print("[FAIL] Missing 02_machine_output.yaml or 04_evidence_notes.md")
        sys.exit(1)

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
    evidence_text = evidence_path.read_text(encoding="utf-8")

    criticality = data.get("criticality", "P0")
    source_count = data.get("source_pack", {}).get("source_count", 0)
    min_sources = {"P0": 10, "P1": 5, "P2": 3, "Lab": 0}.get(criticality, 3)

    passed = True

    if source_count < min_sources:
        print(f"[FAIL] source_count={source_count}, minimum for {criticality} is {min_sources}")
        passed = False
    else:
        print(f"[OK] source_count={source_count} meets {criticality} minimum")

    dominant_evidence_count = data.get("evidence_counts", {}).get("dominant_phase_evidence_items", 0)
    if dominant_evidence_count < 3:
        print(f"[FAIL] dominant phase evidence items={dominant_evidence_count}, minimum is 3")
        passed = False
    else:
        print(f"[OK] dominant phase evidence items={dominant_evidence_count}")

    transition_signal_count = data.get("evidence_counts", {}).get("transition_watch_documented_signals", 0)
    has_transition_watch = bool(data.get("transition_watch"))
    if has_transition_watch and transition_signal_count < 3:
        print(f"[FAIL] transition watch signals={transition_signal_count}, minimum is 3")
        passed = False
    elif has_transition_watch:
        print(f"[OK] transition watch signals={transition_signal_count}")

    if data.get("active_case") is True:
        freshness = data.get("source_pack", {}).get("freshness_check", {})
        if not freshness:
            print("[FAIL] active case requires freshness_check")
            passed = False
        else:
            print("[OK] freshness_check present")

    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
