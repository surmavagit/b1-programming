import sys

student_records = []
stats = {}

def ask_for_input():
    total_number_of_students = 6
    student_number = 1
    while student_number <= total_number_of_students:
        student_number = student_number + 1
        name = input("Enter your name:\n")
        grade = input("Enter your grade:\n")
        valid_grade = 0
        try:
            valid_grade = int(grade)
        except ValueError:
            print("Invalid grade. Aborting")
            sys.exit(1)
        student_records.append((name, valid_grade))

ask_for_input()

scores = []
for _, score in student_records:
    scores.append(score)


stats['highest'] = max(scores)
stats['lowest'] = min(scores)
stats['average'] = sum(scores)/len(scores)

unique_scores = set(scores)

grade_distribution = {}
for uniscore in unique_scores:
    grade_distribution[uniscore] = scores.count(uniscore)

print(grade_distribution)
