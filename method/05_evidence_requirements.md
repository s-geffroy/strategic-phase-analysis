# Evidence Requirements V1

## Principe

Une phase sans preuve n’est pas un diagnostic. C’est une impression.

## Exigences minimales

```yaml
source_requirements_v1:
  any_case_min_sources: 3
  p0_min_sources: 10
  dominant_phase_min_evidence_items: 3
  transition_watch_min_documented_signals: 3
  critical_score_4_or_5_requires_rationale: true
  dated_sources_required: true
  freshness_check_required_for_active_cases: true
```

## Criticité documentaire

| Criticité | Sources minimales | Usage |
|---|---:|---|
| P0 | 10–20 | crise active, chokepoint mondial, corridor systémique |
| P1 | 5–10 | cas important mais moins systémique |
| P2 | 3–5 | cas secondaire, historique ou exploratoire |
| Lab | variable | hypothèse interne non validée |

## Source pack P0

Un P0 doit couvrir autant que possible :

- sources institutionnelles ;
- déclarations officielles ;
- données opérationnelles ou suivi d’incidents ;
- données commerce / logistique ;
- indicateurs financiers ou assurance si pertinents ;
- presse fiable ;
- analyses spécialisées ;
- sources régionales ;
- contradiction ou lecture alternative.

## Evidence status

| Status | Définition |
|---|---|
| weak | preuve rare, indirecte, ancienne ou fortement contestée |
| partial | preuve suffisante pour soutenir le jugement mais incertitude matérielle |
| strong | preuves multiples, fiables, convergentes et peu contredites |

## Confidence

| Niveau | Définition |
|---|---|
| low | jugement fragile |
| medium | jugement plausible, soutenu mais contestable |
| high | jugement solidement appuyé et relativement stable |

## Interdictions

- Phase dominante sans 3 preuves.
- Transition watch sans 3 signaux.
- Score critique sans justification.
- Confiance haute avec preuve faible.
- Contradiction ignorée.
