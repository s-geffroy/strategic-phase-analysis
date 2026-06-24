# Changelog

Toutes les modifications notables de ce projet sont documentées dans ce fichier.

Le format s'appuie sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/)
et le projet suit un versionnage par paliers de méthode (V1, V1.1, …).

## [Non publié]

### Ajouté
- Réorganisation du pack de spécification en projet livrable (`source/` = archive, `impl/` = dépôt).
- Socle Docker : `Dockerfile`, `docker-compose.yml` (services `validate`, `build`, `serve`), `requirements.txt` (PyYAML, mkdocs-material, pytest).
- Outillage Python : 5 validateurs repris + `run_all_validations.py` (orchestrateur) + suite de tests `pytest`.
- Remplissage sourcé des 4 cas P0 (Mer Rouge / Bab el-Mandeb, Ormuz, Taïwan, Ukraine / mer Noire), statut `analyst_review_required`, données au 2026-06-24.
- Site de documentation MkDocs Material généré par `scripts/build_site.py` ; bijection métallurgique confinée à une annexe scientifique.
- CI GitHub Actions : `validate.yml` (tests + validateurs) et `deploy-pages.yml` (build + déploiement GitHub Pages).
