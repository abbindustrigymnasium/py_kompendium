registrerade = [" Anna ", " Eva ", " Erik ", " Lars ", " Karl "] # en array med 5 namn
avanmälningar = [" Anna ", " Erik ", " Karl "] # en array med 3 namn

for person in avanmälningar: # för varje person i avanmälningar
    registrerade.remove(person) # tar bort personen från registerande

print ( registrerade ) # skriver ut arrayen