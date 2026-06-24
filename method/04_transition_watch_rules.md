# Transition Watch Rules V1

## Principe

Une transition n’est jamais déclarée automatiquement en V1. Elle est suspectée par signaux faibles, rattachée à une trajectoire typée, puis validée ou rejetée par l’analyste.

## Trajectoires typées V1

| transition_id | De | Vers | Libellé FR |
|---|---|---|---|
| absorptive_to_stratified_politicization | phase absorbante | phase stratifiée | politisation de l’interdépendance |
| absorptive_to_transformative_activation | phase absorbante | phase transformative | activation stratégique |
| stratified_to_brittle_delamination | phase stratifiée | phase cassante | délamination coercitive |
| stratified_to_resilient_security_stabilization | phase stratifiée | phase résiliente | sécurisation stabilisée |
| transformative_to_resilient_security_stabilization | phase transformative | phase résiliente | stabilisation sécuritaire |
| transformative_to_brittle_rapid_hardening | phase transformative | phase cassante | durcissement coercitif rapide |
| brittle_to_resilient_post_crisis_stabilization | phase cassante | phase résiliente | stabilisation post-crise |
| brittle_to_systemic_fissure | phase cassante | désorganisation | fissuration systémique |
| local_coercive_to_brittle_contagion | phase coercitive locale | phase cassante | contagion coercitive |
| brittle_to_stratified_controlled_reopening | phase cassante | phase stratifiée | réouverture contrôlée |

## Signaux vers phase cassante

- fermeture des canaux diplomatiques ;
- hausse du langage coercitif ;
- durcissement militaire ;
- sanctions devenant structurelles ;
- découplage économique ;
- récits de menace existentielle ;
- dégradation des hotlines de crise ;
- hausse de densité d’incidents ;
- rétrécissement de l’espace de compromis ;
- verrouillage par audiences internes.

## Signaux vers phase résiliente

- cessez-le-feu ou accord limité qui tient ;
- garanties de sécurité ;
- réouverture de canaux de crise ;
- stabilisation militaire sans escalade ;
- normalisation partielle des flux ;
- mécanismes de vérification ;
- baisse de fréquence des incidents ;
- dissuasion plus prévisible ;
- retour de routines institutionnelles.

## Règle V1

Une `transition_watch` doit avoir au moins 3 signaux documentés dans `04_evidence_notes.md`.
