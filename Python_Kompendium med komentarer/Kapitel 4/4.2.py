mängd = range(500) # sätter mängd till en array med nummer från 0-500
summan=0 # sätter summa till int
for nummer in mängd: # för alla nummer i arrayen med alla nummer
    if nummer % 2 == 1: # kollar om nummret är jämt delbart med 2
        summan += nummer # adderar nummret till summan
print (summan) # skriver ut summan