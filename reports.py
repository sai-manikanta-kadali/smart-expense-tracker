# this is for total income and expenses and currnt balance and ransaction history 
#proper summary of an transactions 
class Reports:
    def __init__(self,wallet):
        self.wallet=wallet
    def display_summary(self):
        print("\n====== EXPENSE REPORT ======")

        print("Total Income:", self.wallet.total_income())

        print("Total Expenses:", self.wallet.total_expenses())

        print("Current Balance:", self.wallet.calculate_balance())

        print("============================")