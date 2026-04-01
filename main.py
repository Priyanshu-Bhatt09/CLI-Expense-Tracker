import json
from datetime import date

def load_expenses():
    with open("expenses.json", "r") as file:
        data = json.load(file)
        return data["expenses"]

def add_expenses(expenses):
    description = input("Enter the description for expense: ")
    amount = int(input("Enter the amount of expense: "))

    expense = {
        "id": len(expenses)+1,
        "description": description,
        "amount": amount,
        "date": date.today().isoformat()
    }
    expenses.append(expense)
    save_expense(expenses)
    print("Expense added ")


def save_expense(expenses):
    with open("expenses.json", "w") as file:
        json.dump({"expenses": expenses}, file, indent=4)

def view_expense(expenses):
    if not expenses:
        print("Expenses not found: ")
        return
    for expense in expenses:
        print(f'{expense["id"]}. {expense["date"]} {expense["description"]} Rs.{expense["amount"]}')

def update_expense(expenses):
    expense_id = int(input("Enter the expense id: "))

    for expense in expenses:
        if expense["id"] == expense_id:
            new_des = input("Enter new description: ")
            new_amount = int(input("Enter new amount: "))
            expense["description"] = new_des
            expense["amount"] = new_amount
            print("Expense Updated ")
    print("Expense not found")

def delete_expense(expenses):
    expense_id = int(input("Enter the expense id: "))

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expense(expenses)
            print("Expense deleted ")
            return
        
    print("Expense not found")

def main():
    expenses = load_expenses()

    while True:
        print("\nCLI Expense Tracker\n")
        print("1. Add expense")
        print("2. View expense")
        print("3. Update expense")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expense(expenses)
        elif choice == "3":
            update_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()