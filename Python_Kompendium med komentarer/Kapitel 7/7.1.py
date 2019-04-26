multtabell = int(input("Ange multiplikationstabell")) # kallar det du skriver in i terminalen multtabell
num = 1 # sätter num till en int 1
c = 4 # sätter c till en int 4
d = 3 # sätter d till en int 3

while num < c: # medans num är mindre än c
    b = multtabell*num # multiplicera multtabell med nummrett
    num += 1 # höj nummret ett snepp
    print(b) # skriv ut den multiplicerade 
    if num == c: # om num når c så har den övre utförts 3 ggr
        e = input("fortsätt?") # så vi frågar om de vill fortsätta
        if e == "ja": # skriver de in ja
            c += 3 # läggs 3 på c så while loopen nu är true och if satsen är falsk
        else: # annars
            break # avslutas loopen