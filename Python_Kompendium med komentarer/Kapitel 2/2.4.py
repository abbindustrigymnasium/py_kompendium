print("hur gammal är du?") # skriver ut stringen
alder=int(input("> ")) # input som tillåter dig att 
if alder >= 18: # kollar om alder är större än eller lika med 18
    print("du är redan myndig") # skriver ut strängen
else: # om den förra if satsen inte är true
    mynd=18-alder # sätter mynd till 18 - din ålder
    print("du är myndig om "+str(mynd),"år") # och skriver ut stringen