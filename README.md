# Strategic Phase Analysis

[![validate](https://github.com/s-geffroy/strategic-phase-analysis/actions/workflows/validate.yml/badge.svg)](https://github.com/s-geffroy/strategic-phase-analysis/actions/workflows/validate.yml)
[![deploy-pages](https://github.com/s-geffroy/strategic-phase-analysis/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/s-geffroy/strategic-phase-analysis/actions/workflows/deploy-pages.yml)

**Nom public FR :** Analyse des phases géopolitiques
**Nom public EN :** Strategic Phase Analysis

Méthode autonome de diagnostic géopolitique produisant des fiches **comparables, auditables et réutilisables**. Ce dépôt contient la méthode, les schémas, les templates, l'outillage de validation, les 4 cas P0 et le site de documentation publié via GitHub Pages.

> 📖 **Site publié :** https://s-geffroy.github.io/strategic-phase-analysis/

## Cas P0

1. Mer Rouge / Bab el-Mandeb
2. Ormuz
3. Taïwan / semi-conducteurs / mer de Chine
4. Ukraine / mer Noire / céréales / énergie

> Les cas sont préremplis avec sources datées mais conservent le statut `analyst_review_required` : conformément à la méthode, **le LLM ne valide jamais une phase finale**, seul un analyste humain valide.

## Structure

```text
method/       Spécification de méthode, taxonomie, scoring, transitions, preuve, validation
templates/    Templates Markdown pour les fiches
schemas/      Schémas YAML indicatifs
prompts/      Prompts LLM (préremplissage, implémentation, articles)
publication/  Explications pour publication scientifique et grand public
validation/   Règles qualité et termes interdits
scripts/      Validateurs Python + build du site
cases/        Dossiers des 4 cas P0
outputs/      Matrices comparatives générées
docs/         Site MkDocs (généré par scripts/build_site.py — non versionné)
```

## Utilisation (tout via Docker — aucune installation locale)

```bash
# Construire l'image
docker compose build

# Valider l'outillage et les cas (pytest + 4 validateurs + export matrice)
docker compose run --rm validate

# Construire le site (build_site.py + mkdocs build --strict)
docker compose run --rm build

# Prévisualiser le site sur http://localhost:8000
docker compose up serve
```

## Validation d'un cas individuel

```bash
docker compose run --rm base python scripts/validate_case.py cases/p0_red_sea_bab_el_mandeb
docker compose run --rm base python scripts/validate_public_terms.py cases/p0_red_sea_bab_el_mandeb
docker compose run --rm base python scripts/validate_scores.py cases/p0_red_sea_bab_el_mandeb/02_machine_output.yaml
docker compose run --rm base python scripts/validate_evidence_minimums.py cases/p0_red_sea_bab_el_mandeb
```

## Règles dures V1

- Aucun diagnostic final automatique ; validation humaine obligatoire.
- Pas de vocabulaire métallurgique dans les sorties publiques (annexe scientifique uniquement).
- Pas de score critique 4–5 sans justification.
- Pas de phase dominante sans au moins 3 preuves.
- Pas de transition watch sans au moins 3 signaux documentés.
- Aucun P0 sans 10 sources datées.
- Les contradictions doivent rester visibles.

## Contribuer

Voir [`CONTRIBUTING.md`](CONTRIBUTING.md). Tout passe par Docker (aucune installation locale).

## Licence

Projet sous **double licence** :

- **Code** (`scripts/`, tests, `Dockerfile`, `docker-compose.yml`, workflows GitHub Actions) — [MIT](LICENSE).
- **Contenu** (méthode, cas, templates, schémas, prompts, publications, site `docs/`) — [Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE-CONTENT.md).
