#!/usr/bin/env python3
from pathlib import Path
import sys
import csv
import yaml

FIELDS = [
    "case_id", "criticality", "dominant_phase", "confidence", "evidence_status",
    "geopolitical_temperature", "geopolitical_carbon", "cooling_option_closure",
    "coercion_density", "diplomatic_option_space", "logistical_stress",
    "resilience", "fissure_risk"
]

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    cases_dir = root / "cases"
    outputs_dir = root / "outputs"
    outputs_dir.mkdir(exist_ok=True)

    rows = []
    for yaml_path in cases_dir.glob("*/02_machine_output.yaml"):
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        scores = data.get("support_scores", {})
        dominant = data.get("dominant_phase", {})
        row = {
            "case_id": data.get("case_id", yaml_path.parent.name),
            "criticality": data.get("criticality", ""),
            "dominant_phase": dominant.get("phase_id", ""),
            "confidence": data.get("confidence", ""),
            "evidence_status": data.get("evidence_status", ""),
            "geopolitical_temperature": scores.get("geopolitical_temperature", ""),
            "geopolitical_carbon": scores.get("geopolitical_carbon", ""),
            "cooling_option_closure": scores.get("cooling_option_closure", ""),
            "coercion_density": scores.get("coercion_density", ""),
            "diplomatic_option_space": scores.get("diplomatic_option_space", ""),
            "logistical_stress": scores.get("logistical_stress", ""),
            "resilience": scores.get("resilience", ""),
            "fissure_risk": scores.get("fissure_risk", ""),
        }
        rows.append(row)

    csv_path = outputs_dir / "comparative_matrix_p0.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    md_path = outputs_dir / "comparative_matrix_p0.md"
    with md_path.open("w", encoding="utf-8") as f:
        f.write("# Comparative Matrix P0\n\n")
        f.write("| " + " | ".join(FIELDS) + " |\n")
        f.write("| " + " | ".join(["---"] * len(FIELDS)) + " |\n")
        for row in rows:
            f.write("| " + " | ".join(str(row.get(field, "")) for field in FIELDS) + " |\n")

    print(f"[OK] Exported {csv_path}")
    print(f"[OK] Exported {md_path}")

if __name__ == "__main__":
    main()
