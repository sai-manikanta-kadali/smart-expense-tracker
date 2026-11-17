#Transaction - we are managing the common things 
#abstraction - for future child classes we define a common rule 
from abc import ABC,abstractmethod 
class Transaction(ABC):
    def __init__(self,amount,category,description):
        self.amount=amount
        Transaction.validate_text(category)
        Transaction.validate_text(description)
        self.category=category
        self.description=description
        #if user leaves empty string in category or description we raise the error 
    @staticmethod
    def validate_text(value):
        if value.strip()!="":
           return True
        else:
            raise ValueError("Text Cannot be Empty")
#Encapsulation - user give -ve amount value prblm so 
    @property #Getter and setter amount we are managing to not giving the -ve values 
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,value):
        if value>0:
            self._amount = value
        else:
            raise ValueError("Amount must be greater than zero")
    @abstractmethod
    def display(self):
        print(f"Amount : {self.amount}")
        print(f"Category : {self.category}")
        print(f"Description : {self.description}")
#Inheritance - creating child classes Income and Expense
class Income(Transaction):
#creating a method overriding class to money receive and spent for both the classess
    def display(self):
        super().display()
        print("Money Received!")
#creating an expense class 
class Expense(Transaction):
    def display(self):
        super().display()
        print("Money Spent!")
#class method - user entering the transactions in dict format
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["amount"],
            data["category"],
            data["description"]
        )
#creating a polymorphism for both the classes 
# This is called an Run-time Polymorphism
