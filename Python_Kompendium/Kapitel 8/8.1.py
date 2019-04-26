print("Ange distans")
yourdistance = int(input("> "))
print("Ange metric")
metric = str(input("> "))

def km_to_miles(dist):
    miles = yourdistance * 0.621371192
    print(miles)

def miles_to_km(dist):
    km = yourdistance * 1.609344
    print(km)

if metric == "km":
    km_to_miles(yourdistance)
else:
    miles_to_km(yourdistance)