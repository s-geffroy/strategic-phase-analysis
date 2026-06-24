# Contribuer

Merci de contribuer à **Strategic Phase Analysis**. Tout passe par **Docker** : aucune installation locale n'est requise ni souhaitée.

## Prérequis

- Docker + Docker Compose.
- Construire l'image une fois : `docker compose build`.

## Boucle de travail

```bash
# Valider l'outillage et les cas (pytest + 4 validateurs + export matrice)
docker compose run --rm validate

# Construire le site (build_site.py + mkdocs build --strict)
docker compose run --rm build

# Prévisualiser le site sur http://localhost:8000
docker compose up serve
```

## Ajouter un cas

1. Créer un dossier `cases/<criticité>_<case_id>/` (ex. `cases/p1_suez/`).
2. Y produire les **6 fichiers** en suivant les `templates/` :
   `00_short_diagnostic.md`, `01_full_analytical_fiche.md`, `02_machine_output.yaml`,
   `03_decision_synthesis.md`, `04_evidence_notes.md`, `05_validation_log.md`.
3. Respecter la structure YAML attendue (voir un cas P0 existant et `method/09_method_corrections_log.md`).
4. Si le cas doit apparaître sur le site, l'ajouter à `CASE_TITLES` dans `scripts/build_site.py` et à la nav `mkdocs.yml`.
5. Lancer `docker compose run --rm validate` jusqu'au vert.

## Règles dures à respecter

- Aucun diagnostic final automatique : **validation humaine obligatoire** (statut `analyst_review_required` tant qu'un analyste n'a pas validé ; le LLM ne valide jamais).
- Aucune source inventée ; sources **datées**, contrôle de fraîcheur pour les cas actifs.
- Phase dominante : **≥ 3 preuves** ; transition watch : **≥ 3 signaux** ; P0 : **≥ 10 sources**.
- Tout score critique (4–5) **justifié** ; `confidence: high` **interdit** avec `evidence_status: weak`.
- **Vocabulaire géopolitique uniquement** dans les pages publiques ; le lexique d'origine reste confiné à l'annexe scientifique (le garde-fou de `build_site.py` fait échouer le build en cas de fuite).
- Rendre les **contradictions visibles**.

## Documentation

Mettre à jour le `CHANGELOG.md` à chaque évolution de la documentation ou de la méthode.
