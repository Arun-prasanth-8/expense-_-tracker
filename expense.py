import csv
import datetime
import os

# File to store expenses
FILE_NAME = 'expenses.csv'

# Ensure the file exists with headers
if not os.path.isfile(FILE_NAME):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])

def add_expense():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    category = input("Enter the category (e.g., food, transportation, entertainment): ").strip().lower()
    description = input("Enter a brief description: ").strip()

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    
    print("Expense added successfully.")

def view_expenses():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        for expense in expenses:
            print(f"Date: {expense[0]}, Amount: {expense[1]}, Category: {expense[2]}, Description: {expense[3]}")
    except Exception as e:
        print(f"An error occurred while reading expenses: {e}")

def summary_by_month():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        monthly_summary = {}
        for expense in expenses:
            month = expense[0][:7]  # Extracting 'YYYY-MM' format
            amount = float(expense[1])
            if month in monthly_summary:
                monthly_summary[month] += amount
            else:
                monthly_summary[month] = amount

        for month, total in monthly_summary.items():
            print(f"Month: {month}, Total Spent: {total:.2f}")
    except Exception as e:
        print(f"An error occurred while summarizing expenses: {e}")

def summary_by_category():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        category_summary = {}
        for expense in expenses:
            category = expense[2]
            amount = float(expense[1])
            if category in category_summary:
                category_summary[category] += amount
            else:
                category_summary[category] = amount

        for category, total in category_summary.items():
            print(f"Category: {category}, Total Spent: {total:.2f}")
    except Exception as e:
        print(f"An error occurred while summarizing expenses: {e}")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Expense Summary")
        print("4. Category-wise Expense Summary")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_by_month()
        elif choice == '4':
            summary_by_category()
        elif choice == '5':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
