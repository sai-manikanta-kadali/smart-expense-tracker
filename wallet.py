#it is a composition class and we are storing the income and expense classes in it 
from transaction import Income,Expense
class Wallet:
    def __init__(self):
     self.transactions=[]
    def add_transaction(self,transaction):
       self.transactions.append(transaction)
    def display(self):
        for transaction in self.transactions:
           transaction.display()
    def __len__(self):
       return len(self.transactions)
    def __getitem__(self, index):
       return self.transactions[index]
    #adding wrong transactions to replace it we use __setitem__()
    def __setitem__(self, index,transaction):
       if isinstance(transaction,(Income,Expense)):
         self.transactions[index]=transaction
       else:
          raise TypeError("Only Income and Expense are allowed")
    #check that particular class 
    def __contains__(self,transaction):
       return transaction in self.transactions
    def __str__(self):
       return f"Wallet had {len(self.transactions)} transactions"
    def calculate_balance(self):
       balance = 0 
       for transaction in self.transactions:
         if isinstance(transaction,Income):
          balance+=transaction.amount
         elif isinstance(transaction,Expense):
          balance-=transaction.amount
       return balance
    def total_income(self):
       total=0
       for transaction in self.transactions:
        if isinstance(transaction,Income):
          total+=transaction.amount
       return total
    def total_expenses(self):
       total=0
       for transaction in self.transactions:
        if isinstance(transaction,Expense):
         total+=transaction.amount
       return total
    def add_transaction(self, transaction):
     if isinstance(transaction, (Income, Expense)):
        self.transactions.append(transaction)
     else:
        raise TypeError("Only Income and Expense transactions are allowed")
       