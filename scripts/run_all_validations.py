#!/usr/bin/env python3
"""Orchestrateur de validation : pytest + 4 validateurs sur chaque cas + export matrice.

Conçu pour tourner dans le conteneur (`docker compose run --rm validate`) et en CI.
Code de sortie non nul si une vérification échoue. Les scores critiques 4–5 sont
signalés `[REVIEW]` par validate_scores mais ne font pas échouer la validation.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
CASES = ROOT / "cases"


def run(label, cmd):
    print(f"\n=== {label} ===")
    result = subprocess.run([sys.executable, *cmd], cwd=ROOT)
    return result.returncode == 0


def main():
    failures = []

    # 1) Tests unitaires des validateurs
    print("=== pytest ===")
    pytest_rc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(SCRIPTS / "tests")], cwd=ROOT
    ).returncode
    if pytest_rc != 0:
        failures.append("pytest")

    # 2) Validateurs sur chaque cas
    case_dirs = sorted(p for p in CASES.iterdir() if p.is_dir())
    for case_dir in case_dirs:
        rel = case_dir.relative_to(ROOT)
        checks = [
            (f"validate_case {rel}", ["scripts/validate_case.py", str(rel)]),
            (f"validate_public_terms {rel}", ["scripts/validate_public_terms.py", str(rel)]),
            (
                f"validate_scores {rel}",
                ["scripts/validate_scores.py", str(rel / "02_machine_output.yaml")],
            ),
            (
                f"validate_evidence_minimums {rel}",
                ["scripts/validate_evidence_minimums.py", str(rel)],
            ),
        ]
        for label, cmd in checks:
            if not run(label, cmd):
                failures.append(label)

    # 3) Export de la matrice comparative
    if not run("export_comparative_matrix", ["scripts/export_comparative_matrix.py", str(ROOT)]):
        failures.append("export_comparative_matrix")

    print("\n" + "=" * 50)
    if failures:
        print(f"[FAIL] {len(failures)} vérification(s) en échec :")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("[OK] Toutes les vérifications sont passées.")
    sys.exit(0)


if __name__ == "__main__":
    main()
