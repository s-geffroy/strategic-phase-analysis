# Validation Rules V1

## Statuts

```yaml
validation_status:
  draft_llm_prefill: "prérempli par LLM, non validé"
  analyst_review_required: "revue humaine obligatoire"
  analyst_validated: "validé par analyste avec preuves suffisantes"
  rejected: "diagnostic rejeté ou insuffisamment prouvé"
  needs_more_evidence: "diagnostic plausible mais preuve insuffisante"
```

## Rôle du LLM

Le LLM peut :
- préremplir les fiches ;
- proposer phases, scores, transitions et incertitudes ;
- signaler contradictions ;
- rédiger des synthèses provisoires.

Le LLM ne peut pas :
- valider la phase finale ;
- attribuer une confiance finale sans revue humaine ;
- inventer des sources ;
- retirer les contradictions ;
- transformer un score en certitude.

## Validation analyste obligatoire

L’analyste doit valider :
- phase dominante ;
- phases secondaires ;
- scores critiques ;
- transition watch ;
- evidence_status ;
- confidence ;
- sortie publique finale.

## Alternatives rejetées

Chaque phase dominante validée doit inclure au moins une alternative rejetée quand le cas est ambigu.

Exemple :
```yaml
rejected_alternatives:
  - phase_id: active_transformation_order
    reason: "Options still exist but coercive closure is already dominant."
```
