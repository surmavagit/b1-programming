import sys

expense_records = []
category_totals = {}
unique_categories = set()

def ask_for_input(input_number):
    category = input(f"Enter expence {input_number + 1} category: \n")
    amount = input(f"Enter expence {input_number + 1} amount: \n")
    valid_amount = 0
    try:
        valid_amount = float(amount)
    except ValueError:
        print("Invalid amount. Aborting")
        sys.exit(1)

    date = input(f"Enter expence {input_number + 1} date: \n")
    return (category, valid_amount, date)

for i in range(5):
    expense_records.append(ask_for_input(i))

print(expense_records)


