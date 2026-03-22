def main():
    print("-------- WELCOME TO SQUARE PRINTER -------")
    print("\nDo you want a full square or an empty square ?")
    while True:
        type_of_square = input("\n\nType 'full', 'empty' or 'end' to quit: ").strip()    
        if type_of_square == "full":
            full_square()
        elif type_of_square == "empty":
            empty_square()
        elif type_of_square == "end":
            print("Thanks for squaring.")
            break            

def full_square():
    (L , l) = what_is_size()
    full_block(L , l)

def empty_square():
    (L , l) = what_is_size()
    empty_block(L , l)

def what_is_size():
    while True:
        L_input = (input("- What is L ?: "))
        l_input = (input("- What is l ?: "))
        if L_input.isdigit() and l_input.isdigit():
            return int(L_input) , int(l_input)
        print("Error : please enter valid integers.")

def full_block(L , l):
    for brick in range(L):
        print("#" * l)

def empty_block(L , l):
    for brick in range(L):
        if brick == 0 or brick == L - 1:
            print("#" * l) 
        else: 
            print("#" + " " * (l - 2) + "#")

main()