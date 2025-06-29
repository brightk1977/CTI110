# Kristopher Bright
# 6/23/2025
# P2HW2
# a grading calculator and organizer

# 1) Prompt to enter a grade for each module
# 2) Convert each grade to a float and store in a list
# 3) Use functions to find the lowest highest and sum of the grades
# 4) Calculate the average 
# 5) Display results 

grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

grades = [grade1, grade2, grade3, grade4, grade5, grade6]

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\n------------Results------------")
print("Lowest Grade:     ", lowest)
print("Highest Grade:    ", highest)
print("Sum of Grades:    ", total)
print(f"Average:           {average:.2f}")
print("--------------------------------")

