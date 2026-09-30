expenses = []

def add_expense(category, amount):
    expenses.append({
        "category": category,
        "amount": amount
    })

def display_expenses():
    for expense in expenses:
        print(expense)

add_expense("Food", 500)
add_expense("Travel", 300)

display_expenses()
