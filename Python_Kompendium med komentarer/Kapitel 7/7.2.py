thenumber = 10 # sätter thenumber till 10
antalgissningar = 1 # sätter antalet gissningar till 1
yournumber = thenumber+1 # sätter dittnummer till numrett + 1
while yournumber != thenumber: # medans ditt nummer inte är nummret
    yournumber = int(input("> ")) # kalla yournumber till det du skriver in i terminalen
    if(yournumber > thenumber): # om ditt nummer är mer än nummrett
        print("Lower") # skriv lägre
        antalgissningar += 1 # lägg till på antalet gissningar
        continue # fortsätt med whileloopen
    elif(yournumber < thenumber): # om ditt nummer är mindre än nummrett
        print("Higher") # skriv högre
        antalgissningar += 1 # lägg till på antalet gissningar
        continue # fortsätt med whileloopen
    print(thenumber) # om du har rätt skriver den nummret är korrejt
    print("is correct")
    print("it took you " + str(antalgissningar) + " guesses") # och hur många gissningar du gjorde
    break # sedan avslutar den whileloopen
