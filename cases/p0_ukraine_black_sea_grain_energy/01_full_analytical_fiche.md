# Full Analytical Fiche — Ukraine / mer Noire / céréales / énergie

## 1. Object analyzed

- `case_id`: ukraine_black_sea_grain_energy
- `criticality`: P0
- `scale`: crisis, corridor, chokepoint
- `active_case`: true

## 2. Strategic composition

Acteurs principaux : Ukraine (Kyiv) et Fédération de Russie (Moscou) en conflit ouvert prolongé ; arrière-plan de soutien occidental (OTAN sous Mark Rutte, Union européenne, États-Unis) et médiation ponctuelle (États-Unis pour les pourparlers de Genève, AIEA pour la sûreté nucléaire). La Turquie est un acteur de seuil (détroits du Bosphore et des Dardanelles, proximité des attaques maritimes).

Institutions et dispositifs : Conseil de sécurité de l'ONU (briefings humanitaires récurrents), FAO (sécurité alimentaire et plan triennal de protection agricole), AIEA (sûreté de la centrale occupée de Zaporijjia, trêves techniques), Union européenne (régime de sanctions, 19e paquet et propositions ultérieures, plafond du prix du pétrole russe).

Interdépendances et corridors : corridor céréalier maritime de la mer Noire (ports d'Odessa, Tchornomorsk, Pivdenny), routes terrestres de solidarité de l'UE, exportations pétrolières russes via la « flotte fantôme » et le détroit de Kertch comme ligne logistique vers la Crimée occupée.

Infrastructures critiques : réseau électrique ukrainien (cible des frappes russes), centrale nucléaire de Zaporijjia (occupée, alimentation externe répétitivement coupée), raffineries et terminaux pétroliers russes (cibles des frappes ukrainiennes par drones).

Contraintes historiques : invasion de 2022, suspension de la Black Sea Grain Initiative en 2023, capture de Pokrovsk début 2026, accumulation d'incidents nucléaires (douze pertes d'alimentation hors-site).

## 3. Geopolitical temperature

- Score: 5
- Rationale: activité cinétique soutenue et quotidienne (ex. 105 drones et 4 missiles russes en une nuit ; 90 drones la nuit du 18-19 juin), front actif, escalade simultanée sur les volets énergétique et maritime.
- Evidence references: S1, S2, S15, S16
- Uncertainty: intensité variable d'une nuit à l'autre ; pas de bascule vers une escalade qualitative (armes stratégiques) à ce stade.

## 4. Geopolitical carbon

- Score: 4
- Rationale: forte accumulation de contraintes durcissantes et peu réversibles — sanctions structurelles, découplage énergétique, occupation d'infrastructures, attrition logistique répétée — qui rigidifient durablement la configuration.
- Evidence references: S10, S11, S5, S15
- Uncertainty: une reprise négociée pourrait commencer à dissoudre une partie de cette charge accumulée, mais aucun signal fort en ce sens.

## 5. Cooling / option closure

- Score: 4
- Mode: frozen_conflict (tendance) avec épisodes incomplete_metastable (trêves techniques)
- Rationale: les fenêtres de désescalade existent uniquement sous forme technique et révocable (trêve AIEA du 5 juin, échanges humanitaires) ; le volet politique reste bloqué sur le statut du Donbass et le rejet russe des conditions de Kyiv. Les trêves générales de mai 2026 ont été violées.
- Evidence references: S2, S3, S14, S19

## 6. Historical treatments

Chocs antérieurs majeurs : invasion de 2022 ; mise en place puis suspension (2023) de la Black Sea Grain Initiative ; reconstitution unilatérale d'un corridor maritime ukrainien. Stabilisations partielles : trêves techniques répétées autour de Zaporijjia (six depuis 2022). Contraintes répétées : frappes hivernales récurrentes sur le réseau électrique, attrition du front, accumulation d'incidents nucléaires. Tensions résiduelles non résolues : revendications territoriales russes sur le Donbass et la Crimée, refus d'adhésion de l'Ukraine à l'OTAN exigé par Moscou, absence de garanties de sécurité crédibles pour Kyiv.

## 7. Dominant phase

- `phase_id`: brittle_coercive_order
- `short_label_fr`: phase cassante
- `full_label_fr`: ordre coercitif cassant
- Rationale: configuration rigidifiée par choc prolongé, forte polarisation, fermeture des options diplomatiques, prédominance de la coercition (militaire, énergétique, maritime, financière) et risque élevé de rupture localisée (sûreté nucléaire, choc énergétique).
- Minimum 3 evidence items:
  1. Négociations politiques en pause depuis mars 2026 et rejet russe (7 juin) des conditions de paix de Kyiv/UE (S2, S19).
  2. Coercition dominante et croissante : frappes ukrainiennes sur raffineries/ports russes, frappes russes sur réseau et corridor (S15, S16, S6).
  3. Sanctions devenues structurelles (19e paquet, flotte fantôme, plafond pétrolier maintenu) (S10, S11).
  4. Trêves générales de mai 2026 violées des deux côtés (S14).

## 8. Secondary phases

- phase_id: localized_coercive_nodes
  - applies_to: centrale nucléaire occupée de Zaporijjia, Crimée occupée (carburant rationné), détroit de Kertch comme point de verrouillage logistique
  - rationale: points de contrainte dure et infrastructures sous contrôle/contrainte coercitive localisée, gérés par dispositifs techniques d'exception
  - evidence: S3, S5, S1

- phase_id: stratified_interdependence_order
  - applies_to: corridor céréalier de la mer Noire et coopération fonctionnelle de sûreté (AIEA)
  - rationale: coopération minimale (flux alimentaires, sûreté nucléaire) coexiste, en couches distinctes, avec la coercition militaire
  - evidence: S9, S3, S8

## 9. Modifiers

- modifier_id: hardened_by_repeated_stress
  - rationale: perte progressive de souplesse sous frappes et sanctions répétées
  - evidence: S5, S10, S15

- modifier_id: metastable
  - rationale: équilibre provisoire (front stabilisé, trêves techniques) susceptible de réactivation à tout moment
  - evidence: S17, S3, S14

- modifier_id: polyphased
  - rationale: coexistence d'une phase cassante dominante, de noyaux coercitifs locaux et de couches d'interdépendance
  - evidence: S9, S5, S3

## 10. Transition watch

- transition_id: brittle_to_systemic_fissure
  - public_label_fr: fissuration systémique
  - from_phase: brittle_coercive_order
  - to_phase: désorganisation
  - observed signals: 12e perte d'alimentation externe à Zaporijjia et diesels sursollicités ; escalade maritime (attaques sur pétroliers, primes de guerre relevées, Tuapse -91 %) ; intensification des frappes énergétiques réciproques
  - risk level: high
  - validation status: under_review

- transition_id: brittle_to_resilient_post_crisis_stabilization
  - public_label_fr: stabilisation post-crise
  - from_phase: brittle_coercive_order
  - to_phase: resilient_security_order
  - observed signals: trêve technique AIEA tenue localement (5 juin) ; volet militaire « constructif » à Genève (Ukraine prête à monitorer un cessez-le-feu) ; front russe enrayé ; architecture de garanties de sécurité en discussion (Rutte, trois niveaux)
  - risk level: medium
  - validation status: under_review

## 11. Support scores

| Score | Value | Rationale | Evidence |
|---|---:|---|---|
| geopolitical_temperature | 5 | Frappes quotidiennes, front actif, double escalade énergie/maritime | S1, S2, S15, S16 |
| geopolitical_carbon | 4 | Contraintes durcissantes accumulées, peu réversibles | S10, S11, S5, S15 |
| cooling_option_closure | 4 | Refroidissement vers conflit gelé, trêves seulement techniques et violées | S2, S3, S14, S19 |
| coercion_density | 5 | Coercition dominante et croissante sur tous les vecteurs | S6, S10, S13, S15 |
| institutional_ductility | 2 | Institutions (ONU, AIEA, FAO) actives mais capacité d'absorption faible, limitée à des trêves techniques | S3, S6, S7 |
| diplomatic_option_space | 1 | Espace de compromis fortement rétréci, seuls canaux techniques actifs | S2, S3, S19 |
| logistical_stress | 4 | Réseau, corridor et logistique russe en Crimée sous contrainte | S5, S9, S1 |
| economic_interdependence | 2 | Interdépendance résiduelle (céréales, énergie via tiers) mais découplage Russie/Occident avancé | S8, S9, S10 |
| strategic_rivalry | 5 | Rivalité existentielle Russie/Ukraine, structurée par l'enjeu OTAN/UE/US | S20, S21 |
| historical_residual_stress | 4 | Revendications territoriales, refus OTAN, contentieux non résolus depuis 2022 | S2, S19, S20 |
| resilience | 3 | Ukraine maintient corridor et défense ; Russie absorbe sanctions ; marges entamées des deux côtés | S9, S15, S17 |
| fissure_risk | 4 | Rupture possible via sûreté nucléaire ou choc énergétique/maritime | S5, S12, S13 |

## 12. Uncertainties

- Trajectoire des négociations (pause prolongée vs reprise sous pression américaine).
- Ampleur et durée réelles des pénuries de carburant russes.
- Solidité assurantielle du corridor céréalier si les attaques maritimes s'intensifient.
- Faisabilité d'une force de réassurance européenne et de garanties de sécurité crédibles.

## 13. Contradictions / ambiguous signals

- Corridor céréalier robuste (7 800 navires) vs hausse des primes de guerre et attaques maritimes croissantes.
- Trêve AIEA réussie et volet militaire « constructif » vs rejet politique russe et trêves générales violées.
- Indice FAO globalement stable : pas de reproduction du choc alimentaire mondial de 2022, ce qui relativise la dimension « alimentaire systémique » tout en maintenant la criticité régionale et sécuritaire.
- Front russe enrayé : lecture d'impasse pouvant mener soit à un gel négocié, soit à une escalade compensatoire.

## 14. Analyst validation

- status: analyst_review_required
- validated phase: (à valider) brittle_coercive_order proposé
- rejected alternatives: resilient_security_order (prématuré — pas de cessez-le-feu durable ni de garanties) ; active_transformation_order (le système est rigidifié, non en recomposition rapide)
- confidence: medium (proposé)
- evidence_status: strong (proposé)
- analyst rationale: à compléter par l'analyste. La convergence des scores d'appui (température, densité coercitive, fermeture diplomatique, faiblesse de l'espace de compromis) soutient la phase cassante ; les poches de coopération et les trêves techniques justifient les phases secondaires et la double surveillance de transition.
