import requests # importerar function request som tillåter oss att göra ett html anrop
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" # sätter url till den inskrivna apien
r = requests.get(url) # sätter r till det motagande dictionariet
response_dictionary = r.json() # sätter det motagnade objected vi fick till response_dictionary i json

def line(bol=False): # skapar en funktion
    amount = 30 # sätter amount till 30
    rad="" # sätter rad till en sträng
    if(bol==False): # om bol är falsk vilket den är automatiskt om inte annat blir sagt
        while amount >= 0: # medans amount är större eller lika med 0
            rad+="-" # lägg till ett -
            amount-=1 # och ta bort en från amount
        print(rad) # skriv ut rad när while loopen är klar
    else: # annars omm bol är sant
        while amount >= 0: # medans amount är större än 0  
            rad+="*" # lägger till ett *
            amount-=1 # sänker amount med 1
        print(rad) # skriver ut rad när while loopen är klar

def header(medelande): # skapar en funktion
    mellanrumm="" # sätter mellanrumm till string
    leangthstring=((30-len(medelande))/2)-1 # räknar ut längden mellan | och stringen medelande
    while leangthstring >= 0: # medans längden på stringen är större än eller lika med 0
        mellanrumm+=" " # sätt till ett mellanrum
        leangthstring-=1 # sänk 1 på leangthstring
    header="|"+mellanrumm+medelande+mellanrumm+"|" # sätter header till | och mellanrummet vi räknade ut och medelandet vi skriver 
    print(header) # skriver headern

def echo(medelande): # skapar en funktion
    echo="| "+medelande # sätter echo till | och medelandet
    print(echo) # skriver ut den

def promtt(medelande): # skapar en funktion
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" # sätter url till den inskrivna apien
    r = requests.get(url) # sätter r till det motagande dictionariet
    response_dictionary = r.json() # sätter det motagnade objected vi fick till response_dictionary i json
    response_dictionary=response_dictionary["artists"] # tar och kollar på endast artisterna i dictionariet
    artistt = str(input("Selection > ")) # kallar artistt det vi skriver i terminalen
    for artister in response_dictionary: # för artisterna i dictionariet
        if artister["name"] == artistt: # om artistens namn liknar den du skrev in
            url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artister["id"] # sätter url till den inskrivna men nu med artistens id
            r = requests.get(url) # sätter r till det motagande dictionariet
            response_dictionary = r.json() # sätter det motagnade objected vi fick till response_dictionary i json
            print(response_dictionary) # skriver ut allt om artisten

def promt(medelande): # skapar en funktion
    val = (input("| "+medelande)) # kalalr val det du skriver in

    if val == "a": # kollar igenom valet och utför följaktligen
        line()
        header("ARTIST DATABASE")
        line()
        for artist in response_dictionary["artists"]:
            echo(artist["name"])
        line()
        echo("A | List artists")
        echo("B | View artist profile")
        echo("C | Exit application")
        promt("Selection > ")
    elif val == "b":
        line()
        echo("What artist do you want to view")
        line()
        promtt("Selection > ")
    elif val == "c":
        line()
        echo("Exiting")
        line()
    else:
        line()
        echo("wtf is wrong with u ill ocme over there and bash ur head in u fuikng, detta är ett skämt från en meme ok dont freak out its not an treath aight im just bored rn")
        line()

line() # anropar funktionerna och väljer medelandet eller bol ens värde
header("ARTIST DATABASE")
line()
echo("Welcome to a world of Music!")
line()
echo("A | List artists")
echo("B | View artist profile")
echo("C | Exit application")
line()
promt("Selection > ")