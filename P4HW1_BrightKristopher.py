# Kristopher Bright
# 7/7/2025
# P4HW1
# A grading calculator using loops

# ask the user how many scores they want to enter.
# collect scores, warning when poor input data
# drop lowest and calculate average
# print results and grades

numScores = int(input("How many scores do you want to enter? "))
scoreList = []

for i in range(numScores):
	while True:
		score = float(input(f"Enter score #{i+1}: "))
		if 0 <= score <= 100:
			scoreList.append(score)
			break
		else:
			print("\nINVALID Score entered!!!!")
			print("Score should be between 0 and 100")
			print(f"Enter score #{i+1} again: ", end="")

lowest = min(scoreList)
scoreList.remove(lowest)
average = sum(scoreList) / len(scoreList)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n------------Results------------")
print(f"Lowest Score   : {lowest:.1f}")
print(f"Modified List  : {scoreList}")
print(f"Scores Average : {average:.2f}")
print(f"Grade          : {grade}")
print("--------------------------------")

