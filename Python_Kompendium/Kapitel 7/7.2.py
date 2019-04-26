thenumber = 10
antalgissningar = 1
yournumber = thenumber+1
while yournumber != thenumber:
    yournumber = int(input("> "))
    if(yournumber > thenumber):
        print("Lower")
        antalgissningar += 1
        continue
    elif(yournumber < thenumber):
        print("Higher")
        antalgissningar += 1
        continue
    print(thenumber)
    print("is correct")
    print("it took you " + str(antalgissningar) + " guesses")
    break