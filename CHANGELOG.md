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
- Articles de publication : `publication/03_article_scientifique.md` (10 sections, vocabulaire géopolitique, renvoi à l'annexe) et `publication/04_article_grand_public.md` (8 sections, 4 cas courts), exposés sur le site.
- Double licence : `LICENSE` (MIT, code) et `LICENSE-CONTENT.md` (CC BY 4.0, contenu) ; section Licence + badges de build dans le README.
- `method/09_method_corrections_log.md` : journal des standardisations issues des 4 cas P0 + feuille de route V1.1, ajouté à la nav du site.
- `CONTRIBUTING.md` : guide de contribution (workflow Docker, ajout de cas, règles dures).

### Notes
- L'avertissement GitHub Actions « Node 20 forcé sur Node 24 » est informatif ; les actions utilisées sont déjà à leur dernier major (`actions/checkout@v4`, `actions/deploy-pages@v4`). Aucun changement requis.
