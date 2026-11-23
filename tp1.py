import random
while(True):
    
     joueur = input("Enter une ses choix (pierre , papier ,ciseaux)").lower()

     ordinateur = random.choice(["pierre" ,"papier" , "ciseaux"])
     print("joueur = " , joueur)
     print("ordinateur = " , ordinateur)
     if joueur not in ["pierre" ,"papier" , "ciseaux"]:
        print("choix invalide")
        continue
     elif joueur == ordinateur :
        print("Egalite")
     elif (joueur == "pierre" and ordinateur == "ciseaux" ) or (joueur == "papier" and ordinateur == "pierre" ) or (joueur == "ciseaux" and ordinateur == "papier" ) :
        print("vous avais gagne")
     else :
        print("vous avais perdu")
     rejouer = input("Volez-vous rejouer repondez par 'oui' ou 'nom'").lower()
     if rejouer != "oui" :
              break
print("Fin du jeu")
