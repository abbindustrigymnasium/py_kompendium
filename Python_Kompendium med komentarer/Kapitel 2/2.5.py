print("fråga inte varför jag gjorde dethär") # skriver ut strängen 

print("hur många vill äta 2 korvar") # skriver ut strängen
tvåkorv=int(input("> ")) # kallar det du skriver in i terminalen tvåkorv
print("hur många vill äta 3 korvar") # skriver ut strängen
trekorv=int(input("> ")) # kallar det du skriver in i terminalen trekorv
print("hur många vill äta 2 veganska korvar") # skriver ut strängen
tvåvkorv=int(input("> ")) # kallar det du skriver in i terminalen tvåvkorv
print("hur många vill äta 3 veganska korvar") # skriver ut strängen
trevkorv=int(input("> ")) # kallar det du skriver in i terminalen trevkorv
antalpackkorv=tvåkorv*2+trekorv*3 # räknar ut antalet korvar
apk=int(antalpackkorv/8) # räknar ut antalet packet
# print("du behöver köpa", str(apk), "förpackningar korvar")
antalpackVkorv=tvåvkorv*2+trevkorv*3 # räknar ut antalet veg korvar
apVk=int(antalpackVkorv/4) # räknar ut antalet packet
# print("du behöver köpa", str(apVk), "förpackningar vego korvar")
dryck=tvåkorv+trekorv+tvåvkorv+trevkorv # räknar ut antalet drickor
# print("du behöver köpa in", str(dryck), ("drickor"))
betala=int(apk*20.95+apVk*34.95+dryck*13.95) # räknar ut kostnaden
# print("kostnaden blir", str(betala), "kr")
print(".:KORVKOLLEN:.") # skriver ut strängen
print("----------------------------") # skriver ut strängen
print("Hur många elever vill ha...") # skriver ut strängen
print("2 vanliga korvar -",str(tvåkorv)) # skriver ut strängen och antalet 2 st korvar
print("3 vanliga korvar -",str(trekorv)) # skriver ut strängen och antalet 3 st korvar
print("2 veganska korvar -",str(tvåvkorv)) # skriver ut strängen och antalet 2 st v korvar
print("4 veganska korvar -",str(trevkorv)) # skriver ut strängen och antalet 3 st v korvar
print("----------------------------") # skriver ut strängen
print("-INKÖPSLISTA-") # skriver ut strängen
print("----------------------------") # skriver ut strängen
print("Vanlig korv:",str(apk),"förpackningar") # skriver ut strängen och antalet pakc
print("Vegansk korv:",str(apVk),"förpackningar") # skriver ut strängen och antalet pack
print("Dryck:",str(dryck),"drickor") # skriver ut strängen och antalet dryck
print("----------------------------") # skriver ut strängen
print(str(betala), "SEK") # skriver ut strängen och antalet kr
print("----------------------------") # skriver ut strängen