#modelling bank account

class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.balance}")
    
    def withdraw (self, amount):
        if amount> self.balance:
            print("insufficient balance to proceed withdrawal")
        else:
             self.balance-=amount
             print(f"the amount withdrawn = {self.balance}")
        
        

obj = BankAccount("aryan")
obj.deposit(7000)
obj.withdraw(8000)
       
    

