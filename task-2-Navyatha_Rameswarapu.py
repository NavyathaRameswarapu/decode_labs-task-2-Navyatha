# Expense Tracker Project
# Decode Labs Internship

expenses = []
total = 0

while True:
    expense = input("Enter expense (or type done): ")

    if expense.lower() == "done":
        break

    expense = int(expense)

    expenses.append(expense)
    total = total + expense

print("\nExpense List:", expenses)
print("Total Spent:", total)

average = total / len(expenses)

print("Average Expense:", average)