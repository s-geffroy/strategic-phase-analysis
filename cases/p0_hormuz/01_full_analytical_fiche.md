# Full Analytical Fiche — Détroit d'Ormuz (chokepoint énergétique mondial)

## 1. Object analyzed

- `case_id`: hormuz
- `criticality`: P0
- `scale`: crisis, corridor, chokepoint
- `active_case`: true

## 2. Strategic composition

Le détroit d'Ormuz relie le golfe Persique au golfe d'Oman et constitue le principal point de passage maritime pour les hydrocarbures du Golfe. En 2024-2025, environ 20 millions de barils/jour de pétrole et produits y transitaient, soit près de 25 % du commerce maritime pétrolier mondial et environ un cinquième de la consommation mondiale de pétrole ; le détroit achemine aussi près d'un cinquième du commerce mondial de GNL, dominé par le Qatar (≈93 % de ses exportations) et les Émirats arabes unis (S1, S2, S3).

Acteurs : l'Iran, riverain nord, qui détient une capacité de nuisance déterminante (mines, vedettes rapides de l'IRGC, missiles côtiers, brouillage GNSS) ; les États du Golfe exportateurs (Arabie saoudite, EAU, Qatar, Koweït, Irak) ; les États-Unis (CENTCOM, Ve Flotte basée à Bahreïn) garants de la liberté de navigation ; Israël, partie au conflit avec l'Iran ; les grands importateurs asiatiques (Chine, Inde, Japon, Corée du Sud), avec une dépendance chinoise particulière au brut iranien.

Dépendances et infrastructures critiques : couloir maritime unique aux marges de manœuvre étroites ; oléoducs de contournement (East-West saoudien ; Habshan-Fujairah/ADCOP émirati ~1,5 Mb/j) offrant 2,6 à 5,5 Mb/j de capacité de réacheminement, très inférieure au volume transité et non éprouvée à pleine échelle (S1, S3, S14, S15). Coussins systémiques : capacité de production excédentaire mondiale > 4 Mb/j (T4 2025) et stocks stratégiques des membres de l'AIE (S3).

## 3. Geopolitical temperature

- Score: 3
- Rationale: Température élevée pendant le pic du conflit 2025-2026, désormais en retrait après accord et réouverture, mais loin d'un retour à froid : incidents résiduels, dispositif militaire lourd, accord fragile.
- Evidence references: S6, S7, S12, S13, S9.
- Uncertainty: Sensibilité à toute reprise des hostilités Iran-Israël-EU.

## 4. Geopolitical carbon

- Score: 4
- Rationale: Forte charge de contraintes accumulées et de leviers coercitifs « stockés » : mines posées (dont certaines non récupérées), sanctions, capacité de brouillage, dispositif de blocus/escortes. Le potentiel de réactivation reste haut.
- Evidence references: S4, S9, S10, S13.
- Uncertainty: Part exacte du dispositif démantelé après accord.

## 5. Cooling / option closure

- Score: 2
- Mode: incomplete_metastable
- Rationale: Le refroidissement post-crise est réel mais incomplet et provisoire ; l'accord est à durée déterminée et le calme dépend d'une présence militaire active plutôt que d'une détente structurelle. Les options diplomatiques restent partiellement ouvertes (canal EU-Iran, médiation), ce qui justifie un score de fermeture des options modéré-faible.
- Evidence references: S12, S13, S16.

## 6. Historical treatments

Chocs antérieurs majeurs : guerre des tankers (1984-1988) dans le Golfe, escortes navales US (opération Earnest Will) ; saisies et attaques de pétroliers (2019) ; menaces récurrentes de fermeture utilisées comme levier ; vote non contraignant du Parlement iranien en faveur du blocage (juin 2025) après les frappes US sur les sites nucléaires ; conflit Israël/EU-Iran et perturbations du détroit (2025-2026) suivis d'un accord et d'une réouverture. Stress résiduel non résolu : défiance structurelle Golfe-Iran (« trust gap »), militarisation permanente, dépendance énergétique mondiale inchangée (S4, S5, S11, S13, S14).

## 7. Dominant phase

- `phase_id`: resilient_security_order
- `short_label_fr`: phase résiliente
- `full_label_fr`: ordre de sécurité résiliente
- Rationale: Après un choc majeur, le corridor est revenu à une configuration stabilisée mais plus sécurisée et durcie, encore gouvernable par institutions, garanties navales, canaux diplomatiques et équilibre de dissuasion. La stabilité repose sur un dispositif sécuritaire actif et sur des coussins matériels (capacité excédentaire, stocks), non sur une détente.
- Minimum 3 evidence items:
  1. Réouverture après accord et reprise du trafic commercial sous escortes navales US (S12, S13).
  2. Volumes pétroliers revenus près des niveaux pré-conflit en juin 2026 (S12, S18).
  3. Précédent de désescalade rapide (cessez-le-feu juin 2025, prix revenus au niveau pré-conflit) (S6, S7).
  4. Coussins systémiques : capacité excédentaire > 4 Mb/j, stocks stratégiques AIE (S3).

## 8. Secondary phases

- phase_id: localized_coercive_nodes
  - applies_to: le point de passage lui-même (zone de brouillage, mines, présence IRGC)
  - rationale: Le détroit reste un noyau de contrainte dure localisée, militarisé et instrumenté comme levier malgré la réouverture.
  - evidence: mines et attaques IRGC, brouillage GNSS sur ~1 000 navires/jour, protocole maritime imposé (S4, S9, S10).
- phase_id: stratified_interdependence_order
  - applies_to: la dimension économico-énergétique mondiale du corridor
  - rationale: Coopération commerciale/énergétique (flux vers l'Asie) et rivalité sécuritaire (sanctions, présence navale) coexistent en couches distinctes.
  - evidence: flux soutenus vers Chine/Inde/Asie, dépendance chinoise au brut iranien (S2, S16, S17, S19).

## 9. Modifiers

- modifier_id: metastable
  - rationale: Équilibre provisoire, réactivation possible ; accord à durée déterminée, calme dépendant d'un dispositif militaire.
  - evidence: S12, S13.
- modifier_id: hardened_by_repeated_stress
  - rationale: Perte progressive de souplesse : militarisation permanente, défiance accrue, contournement structurel recherché.
  - evidence: S13, S14, S15.
- modifier_id: polyphased
  - rationale: Plusieurs régimes coexistent (résilient au plan systémique, coercitif local au point de passage, stratifié au plan économique).
  - evidence: S4, S16, S9.

## 10. Transition watch

- transition_id: transformative_to_brittle_rapid_hardening
  - public_label_fr: durcissement coercitif rapide
  - from_phase: resilient_security_order
  - to_phase: brittle_coercive_order
  - observed signals: hausse de densité d'incidents (brouillage GNSS persistant, attaques résiduelles) ; durcissement militaire et dispositif coercitif maintenu (blocus/escortes, protocole maritime, mines non récupérées) ; accord fragile et récits de méfiance (« trust gap » Golfe-Iran, accord à durée déterminée).
  - risk level: high
  - validation status: under_review

## 11. Support scores

| Score | Value | Rationale | Evidence |
|---|---:|---|---|
| geopolitical_temperature | 3 | Tension retombée après accord mais incidents résiduels et dispositif lourd | S6, S7, S12, S9 |
| geopolitical_carbon | 4 | Forte charge de leviers coercitifs « stockés » (mines, sanctions, brouillage, blocus) | S4, S9, S10, S13 |
| cooling_option_closure | 2 | Refroidissement incomplet/métastable ; options diplomatiques partiellement ouvertes | S12, S13, S16 |
| coercion_density | 4 | Mines, attaques IRGC, brouillage massif, blocus/escortes : coercition dense et instrumentée | S4, S9, S10, S13 |
| institutional_ductility | 2 | Capacité d'absorption institutionnelle réelle mais limitée et sous tutelle militaire | S12, S13 |
| diplomatic_option_space | 2 | Espace diplomatique étroit mais non nul (canal EU-Iran, médiation, accord) | S5, S13, S16 |
| logistical_stress | 4 | Volume immense concentré sur un point unique ; contournement plafonné et non éprouvé | S1, S2, S3, S14, S15 |
| economic_interdependence | 5 | ≈25 % du commerce maritime pétrolier, ≈1/5 du GNL, dépendances croisées Asie/Iran | S1, S2, S16, S17, S19 |
| strategic_rivalry | 4 | Rivalité structurelle Iran/EU/Israël/Golfe, sanctions, présence navale permanente | S4, S13, S16 |
| historical_residual_stress | 4 | Guerre des tankers, menaces récurrentes, vote 2025, conflit 2026, défiance durable | S4, S5, S11 |
| resilience | 3 | Coussins matériels (capacité excédentaire, stocks) et désescalade rapide, mais dépendants d'un dispositif coûteux | S3, S6, S12 |
| fissure_risk | 3 | Lignes de rupture visibles (incidents, accord fragile) sans rupture systémique en cours | S9, S13, S18 |

## 12. Uncertainties

- Durabilité de l'accord/réouverture 2026 (à durée déterminée).
- Capacité iranienne de fermeture durable vs simple capacité de nuisance.
- Capacité réelle de contournement par oléoduc sous stress soutenu (non éprouvée).
- Chronologie exacte de l'escalade 2026 selon des sources partiellement divergentes.

## 13. Contradictions / ambiguous signals

- « Fermeture » déclarée par l'Iran vs trafic substantiel maintenu et démentis US (« l'Iran ne contrôle pas le détroit ») : guerre des récits autant que blocage matériel (S18, S5).
- L'Iran entrave les exportations voisines tout en continuant d'exporter son propre brut vers la Chine (S16, S17).
- Vote parlementaire iranien non contraignant : intention affichée vs retenue effective (S5).
- Reprise rapide des flux vs durcissement durable du dispositif (stabilisation sous tension).

## 14. Analyst validation

- status: analyst_review_required
- validated phase: (à statuer par l'analyste)
- rejected alternatives: phase cassante (brittle_coercive_order) écartée comme phase dominante actuelle car le détroit est rouvert et les flux normalisés ; conservée comme cible de transition à risque élevé.
- confidence: medium (proposé)
- evidence_status: strong (proposé)
- analyst rationale: (à compléter) — pondérer stabilisation réelle vs risque de réactivation ; confirmer que la phase coercitive locale reste secondaire et non dominante.
