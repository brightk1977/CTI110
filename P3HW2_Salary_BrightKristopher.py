# Kristopher Bright
# 6/30/25
# P3HW2 - Salary Calculator
# A hourly pay generator w/ nice spacing 

# Get employee name: emp
# get number of hours worked: hours
# get pay rate: rate
# determin if regular or overtime pay
# determin payrate
# print outputs


emp= input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))

if hours > 40:
    overtimeHours = hours - 40
    regularHours = 40
else:
    overtimeHours = 0
    regularHours = hours

overtimePay = overtimeHours * pay * 1.5
regularPay = regularHours * pay
grossPay = regularPay + overtimePay

print('-------------------------------------------')
print(f'Employee name:  {emp}')
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<10}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<10}')
print('-' * 75)
print(f'{hours:<15.1f}{pay:<12.1f}{overtimeHours:<10.1f}{overtimePay:<15.2f}${regularPay:<14.2f}${grossPay:<10.2f}')

