# EXERCICE : LE TRADUCTEUR D'ANIMAUX
#
# Consigne :
# Utilise 'match' sur la variable 'cri' pour afficher :
# - "C'est un chat" si le cri est "miaou"
# - "C'est un chien" si le cri est "ouaf"
# - "Je ne connais pas cet animal" pour tout le reste (_)

print("Bienvenue dans le traducteur")
print("Taper 'quitter' pour quitter.")
print()

while True:

    cri = input("L'animal fait miaou ou ouaf ? ").strip().lower()

    match cri:
        case "miaou":
            print("C'est un chat!")
        case "ouaf":
            print("C'est un chien!")
        case "quitter":
            print("Au revoir")
            break
        case _:
            print("Drôle d'animal...")
