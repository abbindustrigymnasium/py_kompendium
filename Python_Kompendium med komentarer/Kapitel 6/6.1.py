import requests # importerar requests som tillåter oss göra ett html anrop

print("Ange ett positivt heltal") # skriver ut en sträng i terminalen
tal = int(input("> ")) # kallar det du skriver i terminalen tal

url = "http://77.238.56.27/examples/numinfo/?integer="+str(tal) # sätter url till den inskrivna apien + det talet du skrev in i terminalen
r = requests.get(url) # sätter r till det motagande dictionariet
response_dictionary = r.json() # sätter det motagnade objected vi fick till response_dictionary i json

print(tal, "is even =", response_dictionary["even"], "is a prime number =", response_dictionary["prime"]) # skriver ut talet du skrev och objectet i dictionaryt som har nyckel värdet even och prime
print("talets faktorer är", response_dictionary["factors"]) # och sist objectet i dictionaryt som har nyckel värdet factors