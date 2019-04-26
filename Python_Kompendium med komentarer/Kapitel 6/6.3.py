import requests # importerar function request som tillåter oss att göra ett html anrop
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" # sätter url till den inskrivna apien
r = requests.get(url) # sätter r till det motagande dictionariet
response_dictionary = r.json() # sätter det motagnade objected vi fick till response_dictionary i json

for artist in response_dictionary["artists"]: # för alla artister i trädet med datanyckeln artists
    print(artist["name"]) # skriver ut deras namn

response_dictionary=response_dictionary["artists"] # tar och kollar på endast artisterna i dictionariet

print("jag vill ha artisten") # skriver ut strängen i terminalen
artistt = str(input("> ")) # kalalr det du skriver in i terminalen för artistt

for artister in response_dictionary: # kollar igenom alla artister i dictionariet
    if artister["name"] == artistt: # om artistens namn liknar den inskrivna
        url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artister["id"] # sätter url till den inskrivna men nu med artistens id
        r = requests.get(url) # sätter r till det motagande dictionariet
        response_dictionary = r.json() # sätter det motagnade objected vi fick till response_dictionary i json
        print(response_dictionary) # skriver ut allt om artisten