# DevTools_project

# Natural Selection Simulation - Projet Git 2020

# Introduction

## L'équipe

Le groupe d'étude est formé de **Alexandre YANG**, **Amandine THIVET** et **Alexandre DAVOINE** étudiants en 3AL2 & 3IABD2 à l'ESGI.

## Fonctionnalité de l'application

Nous avons choisi de créer un programme permettant de simuler une selection naturelle.

- Individus + Interface :
    - Class Being
    - Run
    - Interface graphique
    - Save / Load
- Reproduction & génome : 
    - Caractéristiques à définir
    - Reproduction --> c'est couple d'individu qui permettent de calculer une moyenne, pas un individu seul
- Génération du monde : 
    - Class World : tableau dobjet Square
     - Class Square : contient plusieurs caractéristique par ex son niveau d'humidité
     - Class Biotop : cohérence des cases [Prairie(température modérée, terrain plat, climat agréable, nourriture+), Montagne(escapé, avec grosse diff de température, neige à implémenter(optionnel), nourriture-), Littoral(optionnel), forêt(très humide, très riche, nourriture++)] 
     - Gestion de nourriture(var qui dit qu'il y a + ou - de nourriture)

## Versionning

Feature branch : En effet nous avont a peu près tous le même niveau et c'est un petit projet. C'est donc plus adapté de faire une branche par fonctionnalité.

Nous avons donc fait des branches par grandes fonctionnalité avec un ou plusieurs commit par branches. On a pu faire des push directement depuis les branches local pour avoir une trace au fur et à mesure.  