import requests # importerar function request som tillåter oss att göra ett html anrop

print("skriv namnet på staden som du vill ha en prognos på") # skriver ut strängen i terminalen
stad = str(input("> ")) # sätter stad till det du skriver in i terminalen

url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"+str(stad) # sätter url till den inskrivna apien + den staden du skrev in i terminalen
r = requests.get(url) # sätter r till det motagande dictionariet 
response_dictionary = r.json() # sätter det motagnade objected vi fick till response_dictionary i json

for forecast in response_dictionary["forecasts"]: # för alla komponenter i dictionaryt
    print(forecast["date"], forecast["forecast"]) # skriver ut objectet med datanyckeln date och forecast