förnamn =[" Maria ", " Erik ", " Karl "] # en array med 3 förnamn
efternamn =[" Svensson ", " Karlsson ", " Andersson "] # en array med 3 efternamn

for namecombo in efternamn: # for  loop som går igenom alla förnamn
    for namecomboo in förnamn: # for loop som går igenom alla efternamn i förnamnet konstanterat i översta for loopen
        print(namecomboo, namecombo) # skriver ut de båda namnen