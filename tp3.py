
print("Bienvenue dans notre jeu Tic Tac Toe !")


grille = [" "] * 9


combinaisons = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

def afficher_grille():
    print(grille[0], "|", grille[1], "|", grille[2])
    print("----------")
    print(grille[3], "|", grille[4], "|", grille[5])
    print("----------")
    print(grille[6], "|", grille[7], "|", grille[8])


joueur = "X"

# Boucle principale
while True:

    afficher_grille()

    print("Tour du joueur", joueur)

    # Demander un choix valide
    while True:
        try:
            choix = int(input("Choisissez une case entre 0 et 8 : "))

            if choix < 0 or choix > 8:
                print("Choisissez un nombre entre 0 et 8.")

            elif grille[choix] != " ":
                print("Cette case est déjà occupée.")

            else:
                break

        except ValueError:
            print("Veuillez entrer un nombre valide.")

   
    grille[choix] = joueur

    gagne = False

    for a, b, c in combinaisons:
        if grille[a] == grille[b] == grille[c] == joueur:
            gagne = True
            break

    if gagne:
        afficher_grille()
        print("Le joueur", joueur, "a gagné !")
        break
    if " " not in grille:
        afficher_grille()
        print("Match nul !")
        break

  
    if joueur == "X":
        joueur = "O"
    else:
        joueur = "X"




