import requests

print("Ange ett positivt heltal")
tal = int(input("> "))

url = "http://77.238.56.27/examples/numinfo/?integer="+str(tal)
r = requests.get(url)
response_dictionary = r.json()

print(tal, "is even =", response_dictionary["even"], "is a prime number =", response_dictionary["prime"])
print("talets faktorer är", response_dictionary["factors"])