import sys

str_score = input('Enter your score (0-100):')
try:
    num_score = int(str_score)
except ValueError:
    print('Invalid score')
    sys.exit(1)

grade = 'F'
if num_score > 100 or num_score < 0:
    print('Invalid score')
    sys.exit(1)
elif num_score >= 90:
    grade = 'A'
elif num_score >= 80:
    grade = 'B'
elif num_score >= 70:
    grade = 'C'
elif num_score >= 60:
    grade = 'D'
print(f"Your grade is: {grade}")

if grade == 'A':
    print('Congratulations!')
elif grade == 'B' or grade == 'C':
    sys.exit(0)
else:
    print('Condolances')
