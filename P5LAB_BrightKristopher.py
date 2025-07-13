# Kristopher Bright
# 7/14/25
# P5LAB
# This program helps people that can't do money math in their head

import random

def disperse_change(change):
    total_cents = int(round(change * 100))

    dollars = total_cents // 100
    total_cents -= dollars * 100

    quarters = total_cents // 25
    total_cents -= quarters * 25

    dimes = total_cents // 10
    total_cents -= dimes * 10

    nickles = total_cents // 5
    total_cents -= nickles * 5

    pennies = total_cents

    if dollars + quarters + dimes + nickles + pennies == 0:
        print("No change")
        return

    if dollars > 0:
        print(f"{dollars} Dollar" + ("s" if dollars > 1 else ""))
    if quarters > 0:
        print(f"{quarters} Quarter" + ("s" if quarters > 1 else ""))
    if dimes > 0:
        print(f"{dimes} Dime" + ("s" if dimes > 1 else ""))
    if nickles > 0:
        print(f"{nickles} Nickle" + ("s" if nickles > 1 else ""))
    if pennies > 0:
        print(f"{pennies} Penn" + ("y" if pennies == 1 else "ies"))

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    while True:
        cash_paid = float(input("How much cash will you put in the self-checkout? "))
        if cash_paid < amount_owed:
            print(f"That’s not enough. You still owe ${amount_owed - cash_paid:.2f}. Please try again.\n")
        else:
            break

    change = round(cash_paid - amount_owed, 2)
    print(f"Change is: ${change:.2f}\n")
    disperse_change(change)

main()

