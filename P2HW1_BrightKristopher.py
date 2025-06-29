# Kristopher Bright	
# 6/23/2025
# P2HW1
# Simple imput calculator based on estimated travel costs

print("This program calculates and displays travel expenses\n")

# Ask for budget
budget = float(input("Enter Budget: "))
print()

# Ask for destination
destination = input("Enter your travel destination: ")
print()

# Ask for est gas cost
gas = float(input("How much do you think you will spend on gas? "))
print()

# Ask for est hotel cost
hotel = float(input("Approximately how much will you need for accomodations/hotel? "))
print()

# Ask for est food cost
food = float(input("Last, how much do you need for food? "))
print()

# Add expenses
totalExpenses = gas + hotel + food

# Subtract from budget
remaining = budget - totalExpenses

# Show results
print("------------Travel Expenses------------")
print(f"{'Location:':20s}{destination}")
print(f"{'Initial Budget:':20s}${budget:.2f}")
print(f"{'Fuel:':20s}${gas:.2f}")
print(f"{'Accomodation:':20s}${hotel:.2f}")
print(f"{'Food:':20s}${food:.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':20s}${remaining:.2f}")
