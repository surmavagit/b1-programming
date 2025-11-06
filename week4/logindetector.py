login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("alice", "failed")
]
user_db = dict()
print('Checking login attempts...')
for attempt in login_attempts:
    name = attempt[0]
    status = attempt[1]
    if status == "success":
        continue
    elif name not in user_db:
        user_db[name] = 1
    else:
        user_db[name] += 1

for user in user_db:
    if user_db[user] >= 3:
        print(
            f"ALERT: User '{user}' has {user_db[user]} failed login attempts"
        )

print('Security check complete')
