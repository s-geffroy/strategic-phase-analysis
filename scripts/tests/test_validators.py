"""Tests des validateurs : un cas valide de référence, puis une violation par règle dure."""
from pathlib import Path
import textwrap

import pytest
import yaml

from conftest import run_validator

PUBLIC_FILES = ["00_short_diagnostic.md", "01_full_analytical_fiche.md", "03_decision_synthesis.md"]
OTHER_MD = ["04_evidence_notes.md", "05_validation_log.md"]


def valid_machine_output():
    """YAML d'un cas P0 actif conforme à toutes les règles dures."""
    return {
        "schema_version": "spa_v1",
        "case_id": "test_case",
        "criticality": "P0",
        "active_case": True,
        "method_name": "strategic_phase_analysis",
        "scale": ["crisis", "corridor"],
        "dominant_phase": {
            "phase_id": "brittle_coercive_order",
            "short_label_fr": "phase cassante",
            "full_label_fr": "ordre coercitif cassant",
        },
        "secondary_phases": [],
        "modifiers": ["metastable"],
        "support_scores": {
            "geopolitical_temperature": 4,
            "geopolitical_carbon": 3,
            "cooling_option_closure": 4,
            "coercion_density": 4,
            "institutional_ductility": 2,
            "diplomatic_option_space": 2,
            "logistical_stress": 3,
            "economic_interdependence": 3,
            "strategic_rivalry": 4,
            "historical_residual_stress": 3,
            "resilience": 2,
            "fissure_risk": 3,
        },
        "transition_watch": [{"transition_id": "brittle_to_systemic_fissure"}],
        "source_pack": {"source_count": 12, "freshness_check": {"latest_source_date": "2026-06-20"}},
        "evidence_counts": {
            "dominant_phase_evidence_items": 4,
            "transition_watch_documented_signals": 3,
        },
        "analyst_validation": {"required": True, "status": "analyst_review_required"},
        "confidence": "medium",
        "evidence_status": "partial",
    }


def write_case(case_dir: Path, data: dict):
    case_dir.mkdir(parents=True, exist_ok=True)
    (case_dir / "02_machine_output.yaml").write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    for name in PUBLIC_FILES + OTHER_MD:
        (case_dir / name).write_text(f"# {name}\n\nContenu géopolitique de test.\n", encoding="utf-8")


@pytest.fixture
def valid_case(tmp_path):
    case_dir = tmp_path / "p0_test_case"
    write_case(case_dir, valid_machine_output())
    return case_dir


# --- Cas de référence : tout doit passer ---

def test_valid_case_passes_all(valid_case):
    for script, arg in [
        ("validate_case.py", valid_case),
        ("validate_public_terms.py", valid_case),
        ("validate_scores.py", valid_case / "02_machine_output.yaml"),
        ("validate_evidence_minimums.py", valid_case),
    ]:
        rc, out = run_validator(script, arg)
        assert rc == 0, f"{script} a échoué de façon inattendue:\n{out}"


# --- validate_case : fichier manquant ---

def test_missing_required_file_fails(valid_case):
    (valid_case / "03_decision_synthesis.md").unlink()
    rc, out = run_validator("validate_case.py", valid_case)
    assert rc == 1
    assert "Missing 03_decision_synthesis.md" in out


# --- validate_public_terms : terme métallurgique interdit ---

def test_forbidden_metallurgical_term_fails(valid_case):
    (valid_case / "00_short_diagnostic.md").write_text(
        "# Diagnostic\n\nLa structure est martensitic sous contrainte.\n", encoding="utf-8"
    )
    rc, out = run_validator("validate_public_terms.py", valid_case)
    assert rc == 1
    assert "martensitic" in out.lower()


# --- validate_scores : hors plage, et confidence/evidence incohérents ---

def test_score_out_of_range_fails(valid_case):
    data = valid_machine_output()
    data["support_scores"]["coercion_density"] = 7
    (valid_case / "02_machine_output.yaml").write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    rc, out = run_validator("validate_scores.py", valid_case / "02_machine_output.yaml")
    assert rc == 1
    assert "Invalid score" in out


def test_high_confidence_with_weak_evidence_fails(valid_case):
    data = valid_machine_output()
    data["confidence"] = "high"
    data["evidence_status"] = "weak"
    (valid_case / "02_machine_output.yaml").write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    rc, out = run_validator("validate_scores.py", valid_case / "02_machine_output.yaml")
    assert rc == 1
    assert "forbidden" in out.lower()


def test_critical_score_flagged_for_review(valid_case):
    rc, out = run_validator("validate_scores.py", valid_case / "02_machine_output.yaml")
    # Les scores 4 sont signalés [REVIEW] mais ne font pas échouer (cas valide).
    assert rc == 0
    assert "[REVIEW]" in out


# --- validate_evidence_minimums : seuils P0 ---

def test_p0_insufficient_sources_fails(valid_case):
    data = valid_machine_output()
    data["source_pack"]["source_count"] = 8
    (valid_case / "02_machine_output.yaml").write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    rc, out = run_validator("validate_evidence_minimums.py", valid_case)
    assert rc == 1
    assert "source_count" in out


def test_insufficient_dominant_evidence_fails(valid_case):
    data = valid_machine_output()
    data["evidence_counts"]["dominant_phase_evidence_items"] = 2
    (valid_case / "02_machine_output.yaml").write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    rc, out = run_validator("validate_evidence_minimums.py", valid_case)
    assert rc == 1
    assert "dominant phase evidence" in out


def test_transition_watch_insufficient_signals_fails(valid_case):
    data = valid_machine_output()
    data["evidence_counts"]["transition_watch_documented_signals"] = 2
    (valid_case / "02_machine_output.yaml").write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    rc, out = run_validator("validate_evidence_minimums.py", valid_case)
    assert rc == 1
    assert "transition watch signals" in out


def test_active_case_without_freshness_fails(valid_case):
    data = valid_machine_output()
    data["source_pack"]["freshness_check"] = {}
    (valid_case / "02_machine_output.yaml").write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    rc, out = run_validator("validate_evidence_minimums.py", valid_case)
    assert rc == 1
    assert "freshness" in out.lower()
