from transaction import Income, Expense
from wallet import Wallet
from reports import Reports

wallet = Wallet()

try:
    i1 = Income(5000, "Scholarship", "College scholarship")
    e1 = Expense(500, "Food", "Lunch")
    e2 = Expense(400, "Biryani", "Rajma")

    wallet.add_transaction(i1)
    wallet.add_transaction(e1)
    wallet.add_transaction(e2)

    # Transaction history
    print("\n===== TRANSACTION HISTORY =====")
    wallet.display()

    # Dunder methods
    print("\nTotal Transactions:", len(wallet))
    wallet[2].display()
    print(i1 in wallet)
    print(wallet)

    # Replace transaction
    new_expense = Expense(300, "Travel", "Bus ticket")
    new_expense = Expense(900, "Travel", "Train Ticket")
    wallet.add_transaction(new_expense)

    print("\n===== AFTER UPDATING =====")
    wallet.display()

    # Financial calculations
    print("\nTotal Income:", wallet.total_income())
    print("Total Expenses:", wallet.total_expenses())
    print("Balance:", wallet.calculate_balance())

    # Reports
    report = Reports(wallet)
    report.display_summary()

except (ValueError, TypeError) as e:
    print("Error:", e)