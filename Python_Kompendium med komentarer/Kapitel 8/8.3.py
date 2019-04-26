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

def promt(medelande): # skapar en funktion
    val = (input("| "+medelande)) # kallar det du skriver in i terminalen för val

    if val == "a": # kollar vilket val du valde och fortsätter följaktligen
        print("visar lista")
    elif val == "b":
        print("vilken vara vill du lägga in")
    elif val == "c":
        print("vilken vara vill du ta bort")
    elif val == "x":
        print("stänger programmet")
    else:
        print("wtf is wrong with u ill ocme over there and bash ur head in u fuikng, detta är ett skämt från en meme ok dont freak out its not an treath aight im just bored rn hatar att kommentera kod")

line() # anropar funktionerna och väljer medelandet eller bol ens värde
header("EXEMPEL")
line(True)
echo("Detta är ett exempel på hur")
echo("ett grännsnitt kan se ut.")
line()
header("vad vill du göra?")
line()
echo("A | Visa inköpslista")
echo("B | Lägg till vara")
echo("C | Ta bort vara")
echo("X | Stäng programmet")
line()
promt("Val ")