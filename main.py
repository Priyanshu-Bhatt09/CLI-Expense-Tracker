import json
from datetime import date

def add_expenses(expenses):
    description = input("Enter the description for expense: ")
    amount = int(input("Enter the amount of expense: "))

    expense = {
        "id": len(expenses)+1,
        "description": description,
        "amount": amount,
        "date": date.today()
    }
    expenses.append(expense)
    save_expense(expenses)
    print("Expense added ")


def save_expense(expenses):
    with open("expenses.json", "w") as file:
        json.dump({"expenses": expenses}, file, indent=4)