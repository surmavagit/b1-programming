import re

passwords = ["Pass123", "SecurePassword1", "weak", "MyP@ssw0rd", "NOLOWER123"]

print('Validating passwords...')

good_passwords = 0
for word in passwords:
    broken_rules = []

    if len(word) < 8:
        broken_rules.append('Too short')

    if not re.search('[0-9]', word):
        broken_rules.append('No digits')

    if not re.search('[a-z]', word):
        broken_rules.append('No lowercase letters')

    if not re.search('[A-Z]', word):
        broken_rules.append('No uppercase letters')

    if len(broken_rules) == 0:
        print(f"PASS: '{word}' - Meets all requirements")
        good_passwords += 1
    else:
        print(f"FAIL: '{word}' -", ', '.join(broken_rules))

print(f"Summary: {good_passwords} compliant, {len(passwords) - good_passwords} non-compliant")
