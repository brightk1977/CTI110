# Kristopher Bright 
# 6/23/2025
# P2LAB2
# A MPG calculator

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()
print(keys)

vehicle = input("Enter a vehicle to see it's mpg: ")

mpg = vehicles[vehicle]
print("The", vehicle, "gets", mpg, "mpg.")

miles = float(input("How many miles will you drive the " + vehicle + "? "))

gallons = miles / mpg

print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")

