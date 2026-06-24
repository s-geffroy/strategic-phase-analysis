# Method Corrections Log

## Objet

Ce fichier consigne les corrections et standardisations apportées à la méthode après son application aux cas P0. Si les cas P0 ne forcent aucune correction, c'est que la méthode n'a probablement pas été assez éprouvée.

Les entrées ci-dessous documentent les ajustements observés lors du **premier remplissage sourcé** des quatre cas P0 (au 2026-06-24). Aucune ne modifie les règles dures de la V1 : il s'agit de **conventions de structure** rendues explicites pour garantir la comparabilité et le passage des validateurs.

## Entrées

### Correction 1 — Forme de `secondary_phases`

- **Date :** 2026-06-24
- **Cas déclencheur :** les quatre cas P0 (tous polyphasés).
- **Problème observé :** la spécification décrit les phases secondaires sans figer la forme de l'objet YAML, d'où un risque d'hétérogénéité entre cas.
- **Règle affectée :** sortie `02_machine_output.yaml`, champ `secondary_phases`.
- **Correction :** chaque entrée est un objet `{ phase_id, applies_to, rationale }`. `applies_to` nomme la **couche** concernée (ex. « couche commerce/logistique », « couche militaire du détroit »), ce qui matérialise le caractère polyphasé.
- **Compatibilité ascendante :** oui (précision, pas de changement de règle).
- **Fichiers concernés :** `cases/p0_*/02_machine_output.yaml`, `templates/02_full_analytical_fiche_template.md` (section 8).
- **Questions ouvertes :** faut-il un score d'appui par couche en V1.1 ?

### Correction 2 — Champs de `transition_watch`

- **Date :** 2026-06-24
- **Cas déclencheur :** les quatre cas P0 (chacun avec une transition prioritaire).
- **Problème observé :** la liste des signaux et le niveau de risque n'étaient pas reliés à un schéma stable dans la sortie machine.
- **Règle affectée :** sortie `02_machine_output.yaml`, champ `transition_watch`.
- **Correction :** chaque entrée porte `{ transition_id, public_label_fr, from_phase, to_phase, risk_level, validation_status }`, avec `validation_status: under_review` tant que l'analyste n'a pas tranché, et le décompte des signaux porté dans `evidence_counts.transition_watch_documented_signals` (≥ 3).
- **Compatibilité ascendante :** oui.
- **Fichiers concernés :** `cases/p0_*/02_machine_output.yaml`, `scripts/validate_evidence_minimums.py` (déjà conforme).
- **Questions ouvertes :** gérer plusieurs transitions concurrentes avec priorité explicite (cas Ukraine : fissuration systémique + stabilisation post-crise).

### Correction 3 — Structure de `freshness_check`

- **Date :** 2026-06-24
- **Cas déclencheur :** les quatre cas P0 (tous `active_case: true`).
- **Problème observé :** la règle « cas actif → contrôle de fraîcheur obligatoire » ne précisait pas le contenu minimal du bloc.
- **Règle affectée :** `source_pack.freshness_check`.
- **Correction :** bloc non vide normalisé en `{ latest_source_date, oldest_source_date, stale_risk }` (dates ISO `YYYY-MM-DD`). `validate_evidence_minimums.py` exige déjà un bloc non vide pour un cas actif.
- **Compatibilité ascendante :** oui.
- **Fichiers concernés :** `cases/p0_*/02_machine_output.yaml`.
- **Questions ouvertes :** automatiser un avertissement de péremption au-delà d'un seuil d'âge en V1.1.

### Correction 4 — Convention de `case_id`

- **Date :** 2026-06-24
- **Cas déclencheur :** divergence entre nom de dossier (`p0_hormuz`) et `case_id` (`hormuz`).
- **Problème observé :** ambiguïté possible entre l'identifiant logique du cas et le préfixe de criticité du dossier.
- **Règle affectée :** identité des cas.
- **Correction :** `case_id` = identifiant **sans** préfixe de criticité (ex. `hormuz`, `red_sea_bab_el_mandeb`) ; le dossier conserve le préfixe `p0_` qui encode la criticité. `export_comparative_matrix.py` retombe sur le nom de dossier si `case_id` est absent.
- **Compatibilité ascendante :** oui.
- **Fichiers concernés :** `cases/p0_*/02_machine_output.yaml`, `scripts/export_comparative_matrix.py`.
- **Questions ouvertes :** aucune.

## Feuille de route V1.1

Pistes identifiées par l'application des cas P0, sans engagement de calendrier :

- **Validation analyste** : passer les quatre cas P0 de `analyst_review_required` à `analyst_validated` (action humaine, hors LLM), en renseignant les `05_validation_log.md`.
- **Scoring par couche** : envisager des scores d'appui différenciés par couche pour les cas fortement polyphasés (Taïwan, Ukraine).
- **Transitions concurrentes** : modéliser explicitement plusieurs `transition_watch` avec priorité et probabilité relative.
- **Fraîcheur automatisée** : avertissement de péremption des sources au-delà d'un seuil d'âge pour les cas actifs.
- **Schémas exécutables** : convertir les schémas indicatifs de `schemas/` en validation structurelle stricte (JSON Schema / pydantic) intégrée aux validateurs.
- **Nouveaux cas** : étendre au-delà des P0 (cas P1/P2, théâtres régionaux, chaînes de dépendance critiques).
