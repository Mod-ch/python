import csv

with open("finale.csv" , "r") as finale:
    f = csv.reader(finale , delimiter= ";")
    for i in range(6):
        next(f)
    r = 0
    for i in f :
        r +=1
        print(i[74])