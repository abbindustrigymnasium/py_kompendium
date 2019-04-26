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

def promt(medelande):
    val = (input("| "+medelande))

    if val == "a":
        print("visar lista")
    elif val == "b":
        print("vilken vara vill du lägga in")
    elif val == "c":
        print("vilken vara vill du ta bort")
    elif val == "x":
        print("stänger programmet")
    else:
        print("wtf is wrong with u ill ocme over there and bash ur head in u fuikng, detta är ett skämt från en meme ok dont freak out its not an treath aight im just bored rn")

line()
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