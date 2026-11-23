import random 
def tirer_nombre() :
            secret = random.randint(1 , 100)
            return secret

def demander_proposition():
            essai = int(input("ecrivez la valeur que vous propose il doit etre compris entre 1 et 100 : "))
            return essai
def comparer(secret , essai) :
            if secret > essai :
                print("Trop petit")
            elif secret < essai :
                print("Trop grand")
            else :
                 print("Trouve")
secret = tirer_nombre()
while (True) :

    
    essai = demander_proposition()
    if 1 <= essai <= 100 :
        comparer(secret , essai)
        if secret == essai :
            break
    else :
           print("le nombre sesir doit etre compris entre 1 et 100")

