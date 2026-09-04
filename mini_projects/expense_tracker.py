expenses = []


def add_expense():
    category = input("Enter expense category: ").strip()
    amount = float(input("Enter expense amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("✅ Expense added successfully.")


def view_expenses():
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\n===== EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']:.2f}")


def show_total():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\n💰 Total Expenses: ₹{total:.2f}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("👋 Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please choose 1-4.")
        