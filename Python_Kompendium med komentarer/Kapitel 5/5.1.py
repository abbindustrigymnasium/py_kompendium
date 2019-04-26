sex = input("kön ") # det du skriver in i terminalen kallas hår
hår = input("hår ") # det du skriver in i terminalen kallas hår
ögon = input("ögon ") # det du skriver in i terminalen kallas hår

sex1 = ["man", "kvinna"] # det kändisarna kan vara
hår1 = ["brun"] # hårfägen känsisar kan ha
ögon1 = ["brun"] # ögonfärg kändisarna kan ha
person1 = ["daniel"] # antalet kändisar

person1[0] = [sex1[0], hår1[0], ögon1[0], "Daniel Redcliff"] # daniel redcliff får könet man, hårfärgen brun och ögonfärgen brun

# seriöst vem orkar repitera, datorer inte jag, du förstår nog vad jag utgår på

for i in person1: # går igenom alla object i arrayen person1
    if(sex == i[0] and hår == i[1] and ögon == i[2]): # om ditt sex, hår, ögon, liknar kändisen
        print("du liknar", i[3]) # skriv vem du liknar