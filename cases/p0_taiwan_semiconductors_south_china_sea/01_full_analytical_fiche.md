# Full Analytical Fiche — Taïwan / semi-conducteurs / mer de Chine méridionale

## 1. Object analyzed

- `case_id`: taiwan_semiconductors_south_china_sea
- `criticality`: P0
- `scale`: crisis, corridor, chokepoint
- `active_case`: true

## 2. Strategic composition

Le cas articule trois théâtres imbriqués autour d'un point de verrouillage mondial : le détroit de Taïwan, l'industrie taïwanaise des semi-conducteurs et les zones contestées de mer de Chine méridionale.

- **Acteurs principaux** : République populaire de Chine (Pékin, Armée populaire de libération, Bureau des affaires de Taïwan) ; Taïwan (président Lai Ching-te, ministère de la Défense nationale) ; États-Unis (Department of War, BIS / Department of Commerce, Indo-Pacific Command) ; Philippines (garde-côtes, conseil de sécurité nationale), liées à Washington par un traité de défense mutuelle.
- **Dépendance critique** : TSMC concentre environ 70 % de la fonderie mondiale, près de 90 % des semi-conducteurs avancés et près de 99 % des puces d'entraînement de l'IA de pointe. Les semi-conducteurs représentent une part majeure des exportations taïwanaises et un goulot d'étranglement systémique pour l'économie mondiale.
- **Corridors et points de verrouillage** : détroit de Taïwan, zone d'identification de défense aérienne (ADIZ), ligne médiane du détroit, Scarborough Shoal et voies maritimes de mer de Chine méridionale.
- **Instruments** : exercices militaires de grande ampleur (blocus simulé), incursions ADIZ, coercition maritime (garde-côtes, barrières flottantes), contrôles à l'exportation de technologies (régime de licences, plafonds, tarifs), canaux militaires de déconfliction.
- **Contraintes historiques** : rhétorique chinoise de « réunification », fenêtre de capacité militaire 2027, héritage des crises du détroit (notamment 2022) et instauration en 2025 d'une « Journée de la reconquête de Taïwan ».

## 3. Geopolitical temperature

- Score: 4
- Rationale: Tension active et soutenue — record d'incursions ADIZ 2025, exercice de blocus le plus vaste depuis 2022, face-à-face naval à Scarborough en juin 2026, rhétorique de souveraineté et de réunification croisées. Pas de conflit ouvert déclaré, d'où 4 plutôt que 5.
- Evidence references: S1, S2, S3, S4, S14
- Uncertainty: distinction entre pression rituelle/graduée et préparation opérationnelle.

## 4. Geopolitical carbon

- Score: 5
- Rationale: Énergie stratégique accumulée maximale — objectif militaire chinois 2027, montée structurelle des moyens de l'APL, dépendance mondiale quasi monopolistique aux puces avancées, coût modélisé d'une rupture autour de 10,6 T$ (~10 % du PIB mondial). Le potentiel de transformation brutale du système est très élevé.
- Evidence references: S1, S6, S11, S12
- Uncertainty: vitesse réelle de libération de cette énergie (gradualisme vs. choc).

## 5. Cooling / option closure

- Score: 3 (cf. score `cooling_option_closure`)
- Mode: incomplete_metastable
- Rationale: Les options de désescalade existent encore (canaux militaires ouverts en novembre 2025, NDS 2026 prônant la stabilité stratégique, ouverture conditionnelle de Lai au dialogue), mais elles sont fragilisées par la purge de la CMC et la répétition des exercices coercitifs. L'équilibre est provisoire et réactivable.
- Evidence references: S5, S7, S8

## 6. Historical treatments

Crises répétées du détroit de Taïwan, point culminant en 2022 (manœuvres post-visite Pelosi). Séquence d'exercices nommés de plus en plus larges (Joint Sword 2024, Strait Thunder 2025A, Justice Mission-2025) traduisant une contrainte répétée et une accoutumance au stress. Stress résiduel non résolu : statut politique de Taïwan, ligne médiane érodée, sanctions technologiques cumulatives. La cohésion interne des canaux mil-mil chinois est dégradée par les purges de 2025-2026.

## 7. Dominant phase

- `phase_id`: stratified_interdependence_order
- `short_label_fr`: phase stratifiée
- `full_label_fr`: ordre d'interdépendance stratifiée
- Rationale: Coopération et rivalité coexistent en couches distinctes — interdépendance économique et technologique encore fonctionnelle et gérée d'un côté, rivalité militaire et symbolique en durcissement de l'autre. Aucune rupture systémique n'est intervenue ; les flux de semi-conducteurs et les canaux de crise persistent malgré la coercition.
- Minimum 3 evidence items:
  1. Maintien des flux de semi-conducteurs et réautorisation conditionnelle du H200 alors que la rivalité militaire s'intensifie (S7, S9, S11).
  2. Interdépendance critique TSMC ~70 % fonderie / ~90 % puces avancées structurant une dissuasion économique mutuelle (S11, S12).
  3. Canaux militaires de déconfliction ouverts et NDS 2026 axé sur la stabilité stratégique, signe de mécanismes de gestion encore actifs (S7, S8).

## 8. Secondary phases

- phase_id: brittle_coercive_order
  - applies_to: couche militaire et symbolique du détroit de Taïwan
  - rationale: Polarisation, langage coercitif et fermeture du compromis dominants sur cette couche (blocus simulé, « réunification inéluctable »).
  - evidence: S2, S3
- phase_id: localized_coercive_nodes
  - applies_to: zones contestées de mer de Chine méridionale (Scarborough Shoal)
  - rationale: Verrouillage coercitif localisé via garde-côtes, barrières flottantes et présence navale, sans extension systémique pour l'instant.
  - evidence: S14

## 9. Modifiers

- modifier_id: polyphased
  - rationale: Plusieurs régimes coexistent dans le même cas — stratification économique, durcissement militaire, noyaux coercitifs maritimes.
  - evidence: S2, S9, S14
- modifier_id: metastable
  - rationale: Équilibre provisoire maintenu par dissuasion économique et canaux de crise, mais réactivation rapide possible.
  - evidence: S7, S13
- modifier_id: hardened_by_repeated_stress
  - rationale: Séquence d'exercices de plus en plus larges traduisant une perte progressive de souplesse et une accoutumance à la pression.
  - evidence: S1, S2

## 10. Transition watch

- transition_id: stratified_to_brittle_delamination
- public_label_fr: délamination coercitive
- from_phase: stratified_interdependence_order
- to_phase: brittle_coercive_order
- observed signals:
  1. Hausse de densité d'incidents (3 764 incursions ADIZ en 2025, +22,4 %) — S1.
  2. Durcissement militaire et langage coercitif (« Justice Mission-2025 », « réunification inéluctable ») — S2, S3.
  3. Sanctions devenant structurelles (contrôles export centraux, expiration du régime VEU) — S9, S10.
  4. Dégradation des canaux de crise (purge de la CMC) — S8.
  5. Verrouillage coercitif localisé contagieux à Scarborough — S14.
- risk level: high
- validation status: under_review

## 11. Support scores

| Score | Value | Rationale | Evidence |
|---|---:|---|---|
| geopolitical_temperature | 4 | Tension active soutenue sans conflit ouvert | S1, S2, S14 |
| geopolitical_carbon | 5 | Énergie stratégique accumulée maximale (objectif 2027, dépendance puces, coût ~10,6 T$) | S1, S6, S11, S12 |
| cooling_option_closure | 3 | Désescalade encore possible mais fragilisée — métastable incomplet | S5, S7, S8 |
| coercion_density | 4 | Coercition militaire et maritime élevée et croissante | S1, S2, S14 |
| institutional_ductility | 2 | Souplesse institutionnelle réduite (purges CMC, exercices ritualisés) mais canaux non rompus | S7, S8 |
| diplomatic_option_space | 2 | Espace de compromis étroit (positions souveraineté/réunification figées) mais non nul | S3, S5 |
| logistical_stress | 3 | Pression sur corridors maritimes et chaîne d'approvisionnement des puces | S2, S12, S14 |
| economic_interdependence | 5 | Interdépendance critique aux semi-conducteurs (TSMC ~70 %/~90 %) | S11, S12 |
| strategic_rivalry | 5 | Rivalité USA-Chine systémique multi-domaines | S3, S5, S6, S9 |
| historical_residual_stress | 4 | Crises répétées du détroit, statut non résolu, ligne médiane érodée | S2, S6 |
| resilience | 3 | Dissuasion économique et alliances (Japon, Philippines, dépendance puces) amortissent encore | S4, S12, S14 |
| fissure_risk | 4 | Lignes de rupture visibles mais amorties | S2, S9, S14 |

## 12. Uncertainties

- Posture chinoise : coercition graduée (statu quo modifié) vs. préparation d'une action de force avant 2027.
- Durabilité des canaux militaires de novembre 2025 après la purge de la CMC.
- Constance de l'engagement américain et instrumentation commerciale des contrôles export.

## 13. Contradictions / ambiguous signals

- Escalade militaire (incursions record, blocus simulé) vs. désescalade diplomatique (canaux mil-mil, ton conciliant de Hegseth).
- Durcissement technologique (fin du régime VEU, extension extraterritoriale) vs. assouplissement (réautorisation du H200, thèse du refroidissement des contrôles).
- Lectures probabilistes basses d'invasion/blocus 2026 (Polymarket, Swift Centre, ASPI/GMF) contre une lecture de rupture imminente.
- « Silicon shield » contesté : risque dominant possiblement un contrôle coercitif plutôt qu'une invasion.

## 14. Analyst validation

- status: analyst_review_required
- validated phase: à confirmer (proposé : phase stratifiée)
- rejected alternatives: phase cassante comme phase dominante (rejet proposé : pas de rupture systémique ni fermeture totale des canaux à ce jour) ; phase absorbante (rejet proposé : coercition trop dense pour une simple absorption institutionnelle)
- confidence: medium (proposé)
- evidence_status: partial (proposé)
- analyst rationale: à compléter par l'analyste — la qualification stratifiée vs. cassante dépend de l'appréciation du poids relatif de la couche militaire et de la durabilité des canaux de crise.
