
import json
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    """Load saved expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)
            if isinstance(expenses, list):
                return expenses
            print("Warning: Invalid data format. Starting with an empty list.")
            return []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read expense data.")
        return []


def save_expenses(expenses):
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def get_amount():
    """Ask for a valid positive expense amount."""
    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid amount. Enter a number, such as 150 or 99.50.")


def get_category():
    """Ask for a non-empty expense category."""
    while True:
        category = input("Enter category (e.g. Food, Travel): ").strip()
        if category:
            return category.title()
        print("Category cannot be empty.")


def get_date():
    """Ask for a date in YYYY-MM-DD format."""
    while True:
        expense_date = input(
            f"Enter date (YYYY-MM-DD) or press Enter for today "
            f"[{date.today()}]: "
        ).strip()

        if not expense_date:
            return date.today().isoformat()

        try:
            return date.fromisoformat(expense_date).isoformat()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, e.g. 2026-10-26.")


def add_expense(expenses):
    """Collect expense details and save the new expense."""
    expense = {
        "amount": get_amount(),
        "category": get_category(),
        "date": get_date()
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added and saved successfully!")


def view_expenses(expenses):
    """Display all saved expenses."""
    if not expenses:
        print("No expenses found. Add an expense first.")
        return

    print("\n--- All Expenses ---")
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. Date: {expense['date']} | "
            f"Category: {expense['category']} | "
            f"Amount: ₹{expense['amount']:.2f}"
        )


def total_by_category(expenses):
    """Calculate and display totals for each category."""
    if not expenses:
        print("No expenses available to calculate totals.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        totals[category] = totals.get(category, 0) + amount

    print("\n--- Total by Category ---")
    for category, total in sorted(totals.items()):
        print(f"{category}: ₹{total:.2f}")

    grand_total = sum(totals.values())
    print(f"Grand Total: ₹{grand_total:.2f}")


def main():
    """Run the menu-driven expense tracker."""
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_by_category(expenses)
        elif choice == "4":
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
