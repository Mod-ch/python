import csv
import sys
with open("finale.csv" , "r") as fi :
    reader = csv.reader(fi , delimiter= ";")
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    list = {}
    rang = input("input your Id for you show your result : ")
    li = []
    n = 0
    for row in reader :
        if row[1] == rang :
            n = 1
            break
    if n == 0 :
        print("You're not in the major DSI")
    else :    
        
        for row in reader :
            ls = [] 
            if row[1] == "" :
                break
            s = row[74].replace("," , ".")
            ls.append(row[1])
            ls.append(row[2])
            ls.append(float(s))
            # list[row[1]] = row[74]
            li.append(ls)
            p = []
        for i in li :
            k =1
            for j in li :
                if i[2] <  j[2] and j[0] not in list:
                    i = j
                    
            # if len(list) == rang :
            #     rang = rang + 1
                
            # p.append(rang)
            list[i[0]] = [i[1] ,i[2] ]#, len(list)]
            # print(len(list))
            
        print(list[rang] )
    # print(p[0])
##    ## matricule = input("input your ID for you get your moyene and the decision about you : ")
####3###     for row in reader :
####3###         if row[1] == matricule :
####3###             print(f"Hello {row[2]} {row[3]} ")
####3###             print(f"your moyene is {row[74]}")
####3###             print(f"your credit is : {row[75]}")
####3###             print(f"the decision about you is : {row[76]}")
####3###             sys.exit(0)
    # print("Your aren't in the filiere DSI")
    # sys.exit(1)
####3    # lists = []
####3    # i = 7;
####3    # lis=[]
####3    # for rj in reader:
####3    #      if(i==197):
####3    #                  break;
####3    #      lis.append(rj)
####3    #      i+=1
####3    # for ro in lis :
####3        
####3        
####3    #     ls = ro
####3    #     x_moyen = ls[74].replace(",",".");
####3    #     for r in lis :
####3    #         if len(r[74]) >1:
####3    #             moyen =r[74].replace(",",".");
####3    #             if float(x_moyen) < float(moyen)  and  
####3    #                 x_moyen = moyen;
####3    #                 ls = r
####3        
####3    #     lists.append(ls)
####3       
####3    # print(lists)
####3    # print(i)
            
        # if row[1] == matricule :
        #     print(f"Hello {row[2]} {row[3]} ")
        #     print(f"your moyene is {row[74]}")
        #     print(f"your credit is : {row[75]}")
        #     print(f"the decision about you is : {row[76]}")
        #     sys.exit(0)
    # print("Your aren't in the filiere DSI")
    # sys.exit(1)