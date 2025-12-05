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
stats['average'] = round(sum(scores)/len(scores), 2)

unique_scores = set(scores)

grade_distribution = {}
for uniscore in unique_scores:
    grade_distribution[uniscore] = scores.count(uniscore)

print("=== STUDENT RECORDS ===")
for i in range(len(student_records)):
    name, grade = student_records[i]
    print(f"{i + 1}. {name}: {grade}")

print("=== CLASS STATISTICS ===")
print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']}")

print("=== UNIQUE SCORES ===")
print(sorted(unique_scores))
print(f"Total unique scores:", len(unique_scores))

print("=== GRADE DISTRIBUTION ===")
for grade in sorted(grade_distribution, key=grade_distribution.get, reverse=True):
    print(f"Score {grade}: {grade_distribution[grade]} students")
