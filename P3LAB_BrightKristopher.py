# Kristopher Bright 
# 6/30/25
# P3LAB 
# This program takes a dollar amount and converts it to change


amount = float(input("Enter the amount of money as a float: $"))
total_cents = int(amount * 100)

dollars = total_cents // 100
total_cents = total_cents - dollars * 100

quarters = total_cents // 25
total_cents = total_cents - quarters * 25

dimes = total_cents // 10
total_cents = total_cents - dimes * 10

nickels = total_cents // 5
total_cents = total_cents - nickels * 5

pennies = total_cents


print("No change" * (dollars + quarters + dimes + nickels + pennies == 0))

print(str(dollars) + " Dollar" * (dollars == 1) + " Dollars" * (dollars > 1))
print(str(quarters) + " Quarter" * (quarters == 1) + " Quarters" * (quarters > 1))
print(str(dimes) + " Dime" * (dimes == 1) + " Dimes" * (dimes > 1))
print(str(nickels) + " Nickel" * (nickels == 1) + " Nickels" * (nickels > 1))
print(str(pennies) + " Penny" * (pennies == 1) + " Pennies" * (pennies > 1))

