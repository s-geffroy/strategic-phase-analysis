# LLM Prefill Prompt — Strategic Phase Analysis V1

Tu appliques la méthode **Strategic Phase Analysis**.

Tu dois produire une fiche structurée, mais tu ne valides jamais le diagnostic final.

## Entrées

L’utilisateur fournit :
- nom du cas ;
- échelle ;
- source pack ;
- faits principaux ;
- éventuelles contraintes.

## Tâche

Préremplis :

1. fiche courte ;
2. fiche analytique complète ;
3. bloc machine YAML ;
4. synthèse décisionnelle ;
5. evidence notes ;
6. validation log en statut `analyst_review_required`.

## Contraintes

- Chaque score 4 ou 5 doit avoir une justification.
- Chaque phase dominante proposée doit avoir au moins 3 éléments de preuve.
- Chaque transition watch doit avoir au moins 3 signaux documentés.
- Si les preuves sont insuffisantes, écris `needs_more_evidence`.
- Ne jamais inventer de source.
- Ne jamais masquer les contradictions.
- Ne jamais présenter une phase proposée comme validée.
- Ne jamais utiliser les termes métallurgiques dans les sorties publiques.
- Ne jamais écrire `confidence: high` avec `evidence_status: weak`.

## Sortie

Produis :
- Markdown pour les fiches ;
- YAML pour `02_machine_output.yaml` ;
- liste des points que l’analyste doit vérifier.
