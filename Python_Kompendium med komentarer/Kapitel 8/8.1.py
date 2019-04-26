print("Ange distans") # skriver strängen
yourdistance = int(input("> ")) # kallar det du skriver in i terminalen för yourdistance
print("Ange metric") # skriver strängen
metric = str(input("> ")) # kallar det du skriver in för metric

def km_to_miles(dist): # gör en funktion
    miles = yourdistance * 0.621371192 # sätter miles till yourdistance * 0.621371192
    print(miles) # och skriver ut miles

def miles_to_km(dist): # gör en funktion
    km = yourdistance * 1.609344 # sätter km till yoursidstance * 1.609344
    print(km) # skriver ut km

if metric == "km": # om din metric är km
    km_to_miles(yourdistance) # anropar funktionen som förvandlar km till mil
else: # annars
    miles_to_km(yourdistance) # anropar funktionen som förvandlar mil till km