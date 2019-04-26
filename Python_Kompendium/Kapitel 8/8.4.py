import requests
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests.get(url)
response_dictionary = r.json()

def line(bol=False):
    amount = 30
    rad=""
    if(bol==False):
        while amount >= 0:
            rad+="-"
            amount-=1
        print(rad)
    else:
        while amount >= 0:
            rad+="*"
            amount-=1
        print(rad)

def header(medelande):
    mellanrumm=""
    leangthstring=((30-len(medelande))/2)-1
    while leangthstring >= 0:
        mellanrumm+=" "
        leangthstring-=1
    header="|"+mellanrumm+medelande+mellanrumm+"|"
    print(header)

def echo(medelande):
    echo="| "+medelande
    print(echo)

def promtt(medelande):
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    r = requests.get(url)
    response_dictionary = r.json()
    response_dictionary=response_dictionary["artists"]
    artistt = str(input("Selection > "))
    for artister in response_dictionary:
        if artister["name"] == artistt:
            url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artister["id"]
            r = requests.get(url)
            response_dictionary = r.json()
            print(response_dictionary)

def promt(medelande):
    val = (input("| "+medelande))

    if val == "a":
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

line()
header("ARTIST DATABASE")
line()
echo("Welcome to a world of Music!")
line()
echo("A | List artists")
echo("B | View artist profile")
echo("C | Exit application")
line()
promt("Selection > ")