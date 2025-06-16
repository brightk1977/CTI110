# Kristopher Bright	
# 6/16/2025
# P1HW2
# Simple imput calculator based on estimated travel costs

print("This program calculates and displys travel expenses""\n")
# Ask for budget
budget = int(input("Enter Budget: "))
print()

# Ask for destination
destination = input("Enter your travel destination: ")
print()

# Ask for est gas cost
gas = int(input("How much do you think you will spend on gas? "))
print()

# Ask for est hotel cost
hotel = int(input("Approximately how much will you need for accomodations/hotel? "))
print()

# Ask for est food cost
food = int(input("Last, how much do you need for food? "))
print()

# Add expenses
totalExpenses = gas + hotel + food

# Subtract from budget
remaining = budget - totalExpenses

# Show results
print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget, "\n")
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food, "\n")
print("Remaining Balance:", remaining)

