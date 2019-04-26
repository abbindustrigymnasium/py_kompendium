import requests
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests.get(url)
response_dictionary = r.json()

for artist in response_dictionary["artists"]:
    print(artist["name"])

response_dictionary=response_dictionary["artists"]

print("jag vill ha artisten")
artistt = str(input("> "))

for artister in response_dictionary:
    if artister["name"] == artistt:
        url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artister["id"]
        r = requests.get(url)
        response_dictionary = r.json()
        print(response_dictionary)