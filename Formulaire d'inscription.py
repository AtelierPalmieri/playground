# EXERCICE : FORMULAIRE D'INSCRIPTION SIMPLIFIÉ
#
# Scénario : 
# Tu dois créer un script qui nettoie le nom d'un utilisateur et traite 
# son inscription selon son âge.
#
# Objectifs :
# 1. Créer une variable globale 'liste_inscrits' (une chaîne de caractères vide "").
# 2. Écrire une fonction 'formater_nom(nom)' :
#    - Elle doit retirer les espaces au début et à la fin.
#    - Elle doit renvoyer le nom propre (Return value).
# 3. Écrire une fonction 'traiter_inscription(nom_propre, age)' :
#    - Elle utilise l'instruction 'global' pour modifier 'liste_inscrits'.
#    - Utiliser 'match' sur la variable 'age' pour les cas suivants :
#        - 0 | 1 | 2 | 3 | 4 | 5 : Affiche "Trop jeune".
#        - 18 : Affiche "Bienvenue (Tout juste majeur !)".
#        - _ (cas par défaut) : Ajoute le nom_propre à 'liste_inscrits' 
#          suivi d'une virgule et affiche "Inscrit avec succès".

# --- TES OUTILS (FONCTIONS) ---
# On les définit une seule fois en haut du fichier
def formater_nom(nom):
    return nom.strip().lower()

def traiter_inscription(nom_propre, age):
    global liste_inscrits
    # ... le bloc match ici ...
    liste_inscrits += nom_propre + " "

# --- TON PROGRAMME PRINCIPAL ---
liste_inscrits = ""

while True:
    saisie = input("Nom (ou 'quitter') : ")
    
    # 1. Condition de sortie
    if saisie.lower() == "quitter":
        break
        
    # 2. Utilisation de tes outils
    age_saisie = int(input("Âge : "))
    nom_propre = formater_nom(saisie)
    traiter_inscription(nom_propre, age_saisie)

# --- RÉSULTAT FINAL ---
print(f"Voici tous les inscrits : {liste_inscrits}")