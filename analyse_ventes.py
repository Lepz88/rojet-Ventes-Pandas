import pandas as pd
import os

# 1. Chargement intelligent du fichier
# On récupère le dossier où se trouve ce script
dossier_projet = os.path.dirname(os.path.abspath(__file__))
# On construit le chemin vers le fichier de données
chemin_fichier = os.path.join(dossier_projet, 'data', 'ventes_dakar_brutes.csv')

print(f"📂 Chargement du fichier : {chemin_fichier}")

# 2. Lecture du CSV
try:
    df = pd.read_csv(chemin_fichier, encoding='latin-1')
    print("✅ Fichier chargé avec succès !\n")
except FileNotFoundError:
    print("❌ Erreur : Fichier introuvable. Vérifie que tu as bien créé le dossier 'data' et le fichier csv dedans.")
    exit()
  
print("--- 1. Dimensions du fichier (Lignes, Colonnes) ---")
print(df.shape)
print("")

print("\n--- 2. Valeurs manquantes ---")
print(df.isna().sum())
print("")

print("\n--- 3. Statistiques rapides (Pour voir les prix bizarres) ---")

print(df.describe())
print("")

print("\n--- 🧹 DÉBUT DU NETTOYAGE ---")

# 1. Supprimer les doublons (La ligne Lait en double)
# On garde la première, on jette les copies
df = df.drop_duplicates()
print(f"Doublons supprimés. Nouvelles dimensions : {df.shape}")

# 2. Standardiser le texte (Riz, riz , RIZ -> riz)
# On nettoie les espaces (strip) et on met tout en minuscules (lower)
df['Produit'] = df['Produit'].str.strip().str.lower()
print("Texte standardisé (tout en minuscules).")

# 3. Gérer les prix bizarres (Le Pain à -150)
# On ne garde que les lignes où le prix est positif (> 0)
df = df[df['Prix_Unitaire'] > 0]
print("Prix négatifs supprimés.")

# 4. Gérer les vides (Le Sucre sans prix)
# S'il n'y a pas de prix, on ne peut pas analyser la vente donc On supprime la ligne
df = df.dropna(subset=['Prix_Unitaire'])

# Pour la Catégorie (Savon), c'est moins grave, on remplit par "Inconnu"
df['Categorie'] = df['Categorie'].fillna('Inconnu')
print("Valeurs manquantes gérées.")

print("\n--- ✅ FIN DU NETTOYAGE ---")
print(f"Dimensions finales du tableau propre : {df.shape}")

print("\n--- 💰 ANALYSE BUSINESS ---")

# 1. Créer une nouvelle colonne : Total par vente
# Formule : Prix x Quantité
df['Total_Vente'] = df['Prix_Unitaire'] * df['Quantite']

# 2. Calculer le Chiffre d'Affaires total
ca_total = df['Total_Vente'].sum()
print(f"Chiffre d'Affaires Total : {ca_total} FCFA")

# 3. Le Top Produit (Qu'est-ce qui se vend le mieux ?)
# On groupe par produit et on additionne les montants
top_produit = df.groupby('Produit')['Total_Vente'].sum().sort_values(ascending=False)

print("\n🏆 Classement des ventes par produit :")
print(top_produit)

print("\n--- 💾 EXPORT FINAL ---")
# On sauvegarde le résultat propre pour le patron
df.to_csv('rapport_ventes_final.csv', index=False)
print("✅ Rapport sauvegardé sous 'rapport_ventes_final.csv' !")