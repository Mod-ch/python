import csv


cities = {
    "BTT" : 0 ,
    "NKTT" : 0 ,
    "NDB" : 0 ,
    "KAIDI" : 0 
}
with open("houses.csv" , "r") as file :
    reader = csv.reader(file , delimiter=";")
    next(reader)
    for row in reader :
        city = row[1]
        cities[city] +=1
    for city in cities :
        print(f"{city} : {cities[city]}")
    print(cities)  
        # print(i[0])
    # ======One other method ===
    # reader = csv.DictReader(file , delimiter= ";")
    # for row in reader :
    #     city = row["House"]
    #     cities[city] +=1
    # for city in cities :
    #     print(f"{city} : {cities[city]}")
    # print(cities)  
    