# CONSIGNE : Le "Robot Barman" 🤖🥤
# Imagine que tu codes un petit robot qui sert des boissons. 
# Le robot reçoit une commande sous forme de texte et doit décider quoi faire.
# Écris une structure match qui vérifie la variable commande :
# Si c'est "café", affiche : "Je prépare un expresso bien chaud !"
# Si c'est "thé", affiche : "L'eau bout, votre thé arrive."
# Si c'est "jus", affiche : "Voulez-vous orange ou pomme ?"
# Cas par défaut (si la commande n'est pas reconnue) : 
# Affiche "Désolé, je ne connais pas cette boisson."
import time

print("Bonjour, je suis votre robot serveur, vous pouvez m'appeler Robert !")
time.sleep(1)
commande = input("Qu'est-ce que je vous sers ? :").lower().strip()

match commande :
    case "un café" | "un chocolat chaud" | "un thé":
        print("Très bien, je vous prépare une boisson bien chaude !")
    case "de l'eau" | "une bière" :
        print("Entendu, je vous apporte une boisson désaltérante !")
    case _:
        print("Je ne connais pas cette boisson :(")