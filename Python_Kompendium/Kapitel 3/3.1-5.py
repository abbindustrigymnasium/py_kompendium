male=["11","12","13","14","15"]
female=["21","22","23","24","25"]
others=["lol", "fattar", "du?!?!?!?!", "detta", "är", "ett", "skämt"]

print (male[0])
print (female[2])
print (female[4])
print (male[1])

print(others[0])

del male[2]
del female[0]
del others[1]

male.append("simon")

male.sort()
female.sort()

print("män:", male)
print("kvinnor:", female)
print("vem vill du ta bort?")
simsalabim = str(input("> "))
people=male+female
people.remove(simsalabim)
print(people)