import csv
import sys
# # ===== With DictReader =====
# with open("Notes_SGBD.csv", "r") as f :
#     reader = csv.DictReader(f , delimiter= ";")
#     matricule = input("Input your ID for you get your note in th SGBD :")
#     for row in reader :
        
#         if row["ï»¿matriculeEtudiant"] == matricule :
                    
#                     print(f"Your name is : {row['nomprenom']}")
#                     print(f"your note of DS is : {row['DS']}")
#                     print(f"your note of Examen pratique is : {row['Examen pratique']}")
#                     print(f"your note of Tp is : {row['Tp']}")
#                     print(f"your note of Cp is : {row['CP']}")
#                     sys.exit(0) 
#         print("Your ID is not found")
#         sys.exit(1)
# ===== With Reader ======
with open("Notes_SGBD.csv", "r") as f :
    reader = csv.reader(f , delimiter=";")
    matricule = input("Input your ID for you get your note in th SGBD : ")
    for row in reader :
        if row[0] == matricule :
            print(f"Your name is : {row[1]}")
            print(f"your note of DS is : {row[2]}")
            print(f"your note of Examen pratique is : {row[3]}")
            print(f"your note of Tp is : {row[4]}")
            print(f"your note of Cp is : {row[2]}")
            sys.exit(0)
    print("Your ID is not found")
    sys.exit(1)
    