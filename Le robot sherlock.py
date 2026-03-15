# CONSIGNE : Le Robot Sherlock 🕵️‍♂️
# 1. Demande une commande à l'utilisateur.
# 2. Utilise un match commande :
# 3. Crée un case avec une variable de copie (ex: case c)
# 4. Ajoute un "if" qui vérifie deux choses :
#    Si "café" est dans c ET si la longueur de c est > 20 caractères.
# 5. Si c'est le cas, affiche : "C'est une bien longue phrase pour un simple café !"
# 6. Ajoute un cas par défaut pour les commandes normales.

import time

print("--- Ouverture de l'Auberge du Sherlock ---")

while True:
    print("\n[Robert attend un nouveau client...]")
    time.sleep(1)
    commande = input("Que désirez-vous ? (ou tapez 'quitter') : ").lower().strip()

    match commande:
        case "quitter" | "stop" | "fin":
            print("Robert ferme boutique. À bientôt !")
            break  # Cette instruction casse la boucle et arrête le programme
            
        case c if "café" in c and len(c) > 30:
            print("C'est une bien longue phrase pour un simple café...")
            time.sleep(1)
            print("Mais soit ! Un espresso, un !")
            
        case c if "café" in c:
            print("☕ Très bon choix, voici votre café !")
            
        case _:
            print("❌ Désolé, Sherlock ne sert que du café ici !")

print("--- Programme terminé ---")