multtabell = int(input("Ange multiplikationstabell"))
num = 1
c = 4
d = 3

while num < c:
    b = multtabell*num
    num += 1
    print(b)
    if num == c:
        e = input("fortsätt?")
        if e == "ja":
            c += 3
        else:
            break