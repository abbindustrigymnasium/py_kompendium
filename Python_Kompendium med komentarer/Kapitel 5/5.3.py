print("skriv in ett land tack!") # skriver strängen i terminal fönstret
Land = str(input("> ")) # kallar det du skriver in i terminalen land

Norden = ["danmark", "finnland"] # en array med länderna i norden kallad norden
Storbritanien = ["england", "skottland"] # en array med länderna i storbrittanien kallad strobritannien

if Land.lower() in Norden: # om landet du skrev in oavsätt caps finns i arrayen norden
    print(Land, "beffiner sig i Norden") # skriver landet och en till sträng
elif Land.lower() in Storbritanien: # ananrs om landet du skrev in oavästt caps är i arrayen storbritannien
    print(Land, "befinner sig i Storbrittanien") # skriver landet och en till sträng
else: # annars om landet inte finns i någon av arrayenn
    print("ditt land ligger inte på kartan") # skriver ut strängen