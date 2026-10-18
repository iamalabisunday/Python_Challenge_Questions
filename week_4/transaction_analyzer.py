transactions = [
    {"name": "Laptop", "amount": 250000, "type": "expense"},
    {"name": "Salary", "amount": 500000, "type": "income"},
    {"name": "Internet", "amount": 30000, "type": "expense"},
    {"name": "Freelance", "amount": 150000, "type": "income"},
    {"name": "Food", "amount": 45000, "type": "expense"}
]


def filter_transactions(condition, transactions):
    return list(filter(condition, transactions))


def balance(income, expense):
    return income - expense


# Income List
incomes = filter_transactions(
    lambda transaction: transaction["type"] == "income", transactions)

# Expense List
expenses = filter_transactions(
    lambda transaction: transaction["type"] == "expense", transactions)


def total_income(incomes):
    total = 0
    for income in incomes:
        total += income["amount"]
    return total


def total_expense(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def largest_expense(expenses):
    largest_amount = float('-inf')
    largest_item = ""

    for expense in expenses:
        if expense["amount"] > largest_amount:
            largest_item = expense["name"]
            largest_amount = expense["amount"]

    return f"{largest_item} ({largest_amount})"


def number_expenses(expenses):
    count = 0
    for _ in expenses:
        count += 1
    return count


def status():
    bal = balance(total_income(incomes), total_expense(expenses))
    if bal >= 0:
        return "Positive balance"
    else:
        return "Negative balance"


print("Total income:", total_income(incomes))
print("Total expense:", total_expense(expenses))
print("Balance:", balance(total_income(incomes), total_expense(expenses)))
print("Largest expense:", largest_expense(expenses))
print("Number of expenses:", number_expenses(expenses))
print("Status:", status())
