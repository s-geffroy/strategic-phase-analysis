# Python Validation Rules Spec

## validate_case.py

Input: case directory.

Checks:
- required files exist ;
- machine output YAML readable ;
- case_id present ;
- dominant_phase present ;
- confidence present ;
- evidence_status present ;
- analyst_validation present.

## validate_public_terms.py

Input: case directory.

Checks public files:
- 00_short_diagnostic.md
- 01_full_analytical_fiche.md
- 03_decision_synthesis.md

Fails if forbidden internal terms appear.

## validate_scores.py

Input: YAML file.

Checks:
- support_scores exists ;
- all score values are integers 0–5 ;
- no confidence high with evidence_status weak ;
- scores 4–5 are listed for manual rationale check.

## validate_evidence_minimums.py

Input: case directory.

Checks machine output and evidence notes for:
- source_count ;
- dominant_phase_evidence_count ;
- transition_watch_signal_count ;
- active case freshness check.

## export_comparative_matrix.py

Reads all case YAML outputs and exports:
- outputs/comparative_matrix_p0.csv ;
- outputs/comparative_matrix_p0.md.
