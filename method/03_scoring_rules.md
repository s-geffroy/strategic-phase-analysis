# Scoring Rules V1

## Principe

Les scores ne produisent pas la phase. Ils appuient un jugement analytique. La V1 utilise une phase dominante qualitative, des phases secondaires, des modificateurs, puis des scores d’appui.

## Échelle 0–5

| Score | Sens |
|---:|---|
| 0 | absent ou négligeable |
| 1 | faible |
| 2 | modéré-faible |
| 3 | significatif |
| 4 | élevé |
| 5 | critique |

## Scores centraux V1

```yaml
support_scores:
  geopolitical_temperature: 0-5
  geopolitical_carbon: 0-5
  cooling_option_closure: 0-5
  coercion_density: 0-5
  institutional_ductility: 0-5
  diplomatic_option_space: 0-5
  logistical_stress: 0-5
  economic_interdependence: 0-5
  strategic_rivalry: 0-5
  historical_residual_stress: 0-5
  resilience: 0-5
  fissure_risk: 0-5
```

## Règles

- Tout score 4 ou 5 exige une justification explicite.
- Aucun score ne peut être présenté comme une preuve autonome.
- `confidence: high` est interdit avec `evidence_status: weak`.
- Les scores doivent être liés à des observations ou preuves dans `04_evidence_notes.md`.

## Lecture correcte

Mauvais :
> La phase est cassante car le score vaut 4.

Correct :
> La phase cassante est proposée parce que plusieurs scores d’appui convergent : fermeture diplomatique élevée, coercition dominante, ductilité faible et risque de fissure élevé.
