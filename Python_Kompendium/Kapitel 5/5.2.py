Åldrar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Sömnbehov = [14, 13, 12, 11.5, 11, 11, 10.5, 10, 10, 10, 9.5, 9, 9, 9, 9, 8.5]

print("skriv in din ålder")
Ålder = int(input("> "))

if Ålder in Åldrar:
    timmar = Sömnbehov[Ålder-1]
else:
    timmar = 8
print("du bör såva", timmar, "timmar")