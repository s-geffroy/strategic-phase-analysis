# LLM Implementation Prompt — Build Strategic Phase Analysis V1 Pack

Tu es un assistant d’implémentation logiciel senior. Tu dois implémenter un dépôt sobre pour la méthode **Strategic Phase Analysis V1**.

## Objectif

Créer un repo local qui permet de produire, valider et versionner des fiches de diagnostic géopolitique comparables, auditables et réutilisables.

## Contraintes d’architecture

- Pas de base de données en V1.0.
- Pas d’interface.
- Markdown + YAML comme source de vérité.
- Git comme historique.
- Python standard library autant que possible.
- PyYAML autorisé comme seule dépendance externe.
- Scripts simples, lisibles, testables manuellement.
- Aucun scoring automatique définitif.
- Validation humaine obligatoire.

## Arborescence attendue

```text
strategic-phase-analysis-v1/
  method/
  templates/
  schemas/
  prompts/
  publication/
  validation/
  scripts/
  cases/
  outputs/
```

## Scripts à produire

1. `validate_case.py`
   - vérifie les fichiers obligatoires ;
   - vérifie que `02_machine_output.yaml` existe ;
   - vérifie statut, phase dominante, confidence, evidence_status.

2. `validate_public_terms.py`
   - inspecte les sorties publiques d’un cas ;
   - interdit les termes internes métallurgiques.

3. `validate_scores.py`
   - vérifie scores 0–5 ;
   - vérifie cohérence confidence/evidence_status ;
   - signale scores 4–5.

4. `validate_evidence_minimums.py`
   - vérifie minimum sources ;
   - vérifie preuves minimales déclarées ;
   - vérifie signaux de transition déclarés.

5. `export_comparative_matrix.py`
   - lit les YAML des cas ;
   - exporte une matrice CSV et Markdown.

## Règles métier

- V1.0 démarre avec 4 cas P0 :
  - Red Sea / Bab el-Mandeb ;
  - Hormuz ;
  - Taiwan / semiconductors / South China Sea ;
  - Ukraine / Black Sea / grain / energy.

- Aucun P0 sans 10 sources.
- Aucune phase dominante sans 3 preuves.
- Aucune transition watch sans 3 signaux.
- Aucun score 4–5 sans justification.
- Aucun diagnostic final sans validation humaine.

## Livrable

Produis les fichiers, puis donne :
- commandes d’installation ;
- commandes de validation ;
- limites connues ;
- prochaines étapes V1.1.
