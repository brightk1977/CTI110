# Kristopher Bright 
# 7/7/2025
# multiplications times table for positive intigers

runAgain = "yes"  

while runAgain.lower() == "yes":
    num = int(input("Enter an integer: "))

    if num < 0:
        print("\nThis program does not handle negative numbers.\n")
    else:
        for i in range(1, 13):  
            print(f"{num} * {i} = {num * i}")
        print()

    runAgain = input("Would you like to run the program again? ")

print("\nExiting program...")

