print("skriv in ett land tack!")
Land = str(input("> "))

Norden = ["danmark", "finnland"]
Storbritanien = ["england", "skottland"]

if Land.lower() in Norden:
    print(Land, "beffiner sig i Norden")
elif Land.lower() in Storbritanien:
    print(Land, "befinner sig i Storbrittanien")
else:
    print("ditt land ligger inte på kartan")