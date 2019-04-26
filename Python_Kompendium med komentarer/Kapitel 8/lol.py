import requests # importerar requests som tillåter oss göra ett html anrop
def lamao(url): # skapar en funktion
    r = requests.get(url) # sätter r till det motagande dictionariet från den inskrivna apien
    response_dictionary = r.json()  # sätter det motagnade objected vi fick till response_dictionary i json
    print(response_dictionary) # skriver ut dictionariet