Åldrar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] # alla åldrar i en array
Sömnbehov = [14, 13, 12, 11.5, 11, 11, 10.5, 10, 10, 10, 9.5, 9, 9, 9, 9, 8.5] # antalet timmar i en array

print("skriv in din ålder") # skriver ut strängen
Ålder = int(input("> ")) # ålder kallas det du skriver in i terminalen

if Ålder in Åldrar: # om din ålder finns i arrayen med åldrar
    timmar = Sömnbehov[Ålder-1] # antalet timmar du behöver sova är indexen i arrayen sömnbehov - 1 för att objectens index i en array går från 0..
else: # om du är över 16
    timmar = 8 # ska du alltid såva 8 timmar
print("du bör såva", timmar, "timmar") # skriver ut hur länge du behöver sova