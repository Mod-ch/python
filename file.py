import csv
import sys
# file = open("phonebook.txt" , "r")
### form clean
     ##       # with open("phonebook.csv" , "r") as file :
       
       ##     #     lines = file.readlines()
        ##   #     clean_lines = [line for line in lines if line.strip()]
    ##  # with open("phonebook.csv" , "w") as file :
      ##      #     file.writelines(clean_lines)
        ##    # print(f"Lignes supperiers : {len(lines) - len(clean_lines)}")

# data = file.read()

# print(data)
# file.close()
# with open("phonebook.csv" , "a") as file :

list = []
file = open("phonebook.csv" , "r" , newline='')
reader = csv.reader(file , delimiter=";")
for raw in reader :
    if raw  == []:
       break
    list.append(raw)
file.close()
with open("phonebook.csv" , "a" , newline='') as file :
  name = input("write the name : ").lower()
  number = input("input the number of last name : ")
  for raw in list :
    # print(raw)
    if raw[0] == name :
      print("this name  is alerdy saving")
      sys(exit(1))
  
    elif raw[1] == number :
      print("this number is alerdy saving")
      sys(exit(1))
  writer = csv.writer(file , delimiter=";")
  writer.writerow([name,number])
  sys(exit(0))
# with open("phonebook.csv" , "r") as f :
#     data = f.read()
# print(data)