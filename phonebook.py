# phonebook = {

# }
# print( type(phonebook))
people ={
    "Brahim" : "34567574" ,
    "Baba" : "43168528" ,
    "Hdeid" : "31444022" ,
    "Salek" : "38686836" ,
    "Mohamed" : "34864440"
}
name = input("Input the name with the first letter uppercase which you wnet to search it number : ").capitalize()
if name in people :
    print (f"Numeber for {name} is : { people[name] }")