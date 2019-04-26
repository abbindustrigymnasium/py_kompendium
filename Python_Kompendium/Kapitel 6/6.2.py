import requests

print("skriv namnet på staden som du vill ha en prognos på")
stad = str(input("> "))

url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"+str(stad)
r = requests.get(url)
response_dictionary = r.json()

for forecast in response_dictionary["forecasts"]:
    print(forecast["date"], forecast["forecast"])