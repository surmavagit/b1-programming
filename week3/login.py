import sys

correct_password = 'password'
max_attempts = 4
curr_attempts = 0

while curr_attempts < max_attempts:
    pass_try = input('Enter your password:')
    if pass_try == correct_password:
        print('Welcome!')
        sys.exit(0)
    print('Incorrect')
    curr_attempts += 1

print('Too many login attempts')
