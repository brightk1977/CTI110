# Kristopher Bright
# 07/07/25
# P4HW2 
# payment and overtime calculator for multiple employees

# set up totals
# calculate hours
# calculate pay
# print output of payment
# set totals again
# print final output


numEmployees = 0
totalOvertimePay = 0
totalRegularPay = 0
totalGrossPay = 0

while True:
    emp = input('Enter employee\'s name or "Done" to terminate: ')
    if emp.lower() == "done":
        break

    hours = float(input(f"How many hours did {emp} work? "))
    rate = float(input(f"What is {emp}'s pay rate? "))

    if hours > 40:
        overtimeHours = hours - 40
        regularHours = 40
    else:
        overtimeHours = 0
        regularHours = hours

    overtimePay = overtimeHours * rate * 1.5
    regularPay = regularHours * rate
    grossPay = regularPay + overtimePay

    print()
    print(f'Employee name:  {emp}')
    print()
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<10}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<10}')
    print('-' * 75)
    print(f'{hours:<15.1f}{rate:<12.2f}{overtimeHours:<10.1f}{overtimePay:<15.2f}${regularPay:<14.2f}${grossPay:<10.2f}')
    print()

    numEmployees += 1
    totalOvertimePay += overtimePay
    totalRegularPay += regularPay
    totalGrossPay += grossPay

print()
print(f'Total number of employees entered: {numEmployees}')
print(f'Total amount paid for overtime: ${totalOvertimePay:.2f}')
print(f'Total amount paid for regular hours: ${totalRegularPay:.2f}')
print(f'Total amount paid in gross: ${totalGrossPay:.2f}')

