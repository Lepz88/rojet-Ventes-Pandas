# 🛒 Analyse de Ventes - Boutique Dakar

Ce projet est une analyse de données de ventes pour une boutique locale à Dakar.
L'objectif est de nettoyer un fichier de ventes "sale" (erreurs de saisie, doublons) pour calculer le chiffre d'affaires réel.

## 🚀 Fonctionnalités (Phase 1)
- **Audit des données :** Détection des valeurs manquantes et incohérentes.
- **Nettoyage (Data Cleaning) :**
  - Suppression des doublons.
  - Correction des fautes de frappe (ex: "Riz" vs "riz").
  - Gestion des prix négatifs et manquants.
- **Export :** Génération d'un fichier propre `rapport_ventes_final.csv`.

  ## 📊 Résultats de l'analyse (Aperçu)
Après exécution du script, voici les indicateurs clés découverts :

* **Lignes traitées :** 10 lignes brutes -> 7 lignes nettes.
* **Chiffre d'Affaires Total :** 360 000 FCFA.
* **Top Produit :** Le Riz (Leader des ventes).
* **Fichier de sortie :** Le rapport propre est généré sous `rapport_ventes_final.csv`.

## 🛠️ Outils utilisés
- **Python** (Langage principal)
- **Pandas** (Manipulation de données)

## 📅 Prochaines étapes
- Phase 2 : Visualisation des données avec Matplotlib (Graphiques des ventes).
  
