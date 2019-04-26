male=["11","12","13","14","15"] # gör en array med 5 object som kallas male
female=["21","22","23","24","25"] # gör en array med 5 object som kallas female
others=["lol", "fattar", "du?!?!?!?!", "detta", "är", "ett", "skämt"] # gör en array som inte ska ta seriöst

print (male[0]) # skriver ut objectet i arrayen male med index 0
print (female[2]) #skriver ut objectet i arrayen female med index 2
print (female[4]) # skriver ut objectet i arrayen female med index 4
print (male[1]) # skriver ut objectet i arrayen male med index 1

print(others[0]) # skriver ut objectet i arrayen others med index 0

del male[2] # tar bort objectet i arrayen male med index 2
del female[0] # tar bort objectet i arrayen female med index 0
del others[1] # tar bort objectet i arrayen others med index 1

male.append("simon") # sätter it ett object (string simon) i arrayen male

male.sort() # sorterar arrayen male
female.sort() # sorterar arrayen female

print("män:", male) # skriver ut arrayen male
print("kvinnor:", female) # skriver ut arrayen male
print("vem vill du ta bort?") # skriver ut strängen
simsalabim = str(input("> ")) # det du skriver i terminalen blir simsalabim
people=male+female # lägger samman arrayen male och female
people.remove(simsalabim) # tar bort den i arrayen som liknar simsalabim 
print(people) # skriver ut arrayen