sex = input("kön ")
hår = input("hår ")
ögon = input("ögon ")

sex1 = ["man", "kvinna"]
hår1 = ["brun"]
ögon1 = ["brun"]
person1 = ["daniel"]

person1[0] = [sex1[0], hår1[0], ögon1[0], "Daniel Redcliff"]

# seriöst vem orkar repitera, datorer inte jag

for i in person1:
    if(sex == i[0] and hår == i[1] and ögon == i[2]):
        print("du liknar", i[3])