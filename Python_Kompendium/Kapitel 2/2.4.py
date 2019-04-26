print("hur gammal är du?")
alder=int(input("> "))
if alder >= 18:
    print("du är redan myndig")
else:
    mynd=18-alder
    print("du är myndig om "+str(mynd),"år")