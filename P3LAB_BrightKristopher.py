# Kristopher Bright
# 6/29/2025
# P3LAB Assignment
# This script converts a dollar amount in to cash and coins

amount = float(input("Enter the amount of money as a float: $"))
cents = int(amount * 100)

dollars = cents // 100
cents = cents - (dollars * 100)

quarters = cents // 25
cents = cents - (quarters * 25)

dimes = cents // 10
cents = cents - (dimes * 10)

nickels = cents // 5
cents = cents - (nickels * 5)

pennies = cents

print("" if amount > 0 else "No change")

print(str(dollars) + " Dollar" * (dollars == 1) + " Dollars" * (dollars > 1))
print(str(quarters) + " Quarter" * (quarters == 1) + " Quarters" * (quarters > 1))
print(str(dimes) + " Dime" * (dimes == 1) + " Dimes" * (dimes > 1))
print(str(nickels) + " Nickel" * (nickels == 1) + " Nickels" * (nickels > 1))
print(str(pennies) + " Penny" * (pennies == 1) + " Pennies" * (pennies > 1))

