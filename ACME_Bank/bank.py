import random

# Main page for ACME bank system
class mainBankPage:
    # Function displaying main page welcome message
    def welcomeMessage():
        print()
        print("-" * 50)
        print("                Welcome to ACME Bank               ")
        print("-" * 50)
        print("  Please choose one of the following options:")
        print("    1.Login to existing account.")
        print("    2.Create new checking account.")
        print("    3.Create new saving account.")
        print("    4.Exit.")
        print()
    welcomeMessage()

# function for generating random and unique account_id
def generate_account_id():
    return random.randint (10000,99999)

class BankAccount:
    def __init__(self, account_holder):
        self.account_id = generate_account_id()
        self.account_holder = account_holder
        self.balance = 0
        
    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f"Deposited ${amount}\nNew balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}\nNew balance: ${self.balance}")
        else:
            print ("Insufficient balance or invalid withdrawal amount.")

    def display_details(self):
        print(f"Account ID: {self.account_id}, Account Holder: {self.account_holder}, Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, minimum_balance):
        super().__init__(account_holder)
        self.minimum_balance  = minimum_balance
    
    def withdraw(self,amount):
        if self.balance - amount < self.minimum_balance:
            print ("Cannot withdraw, minimum balance requirement not met.")
        else:
            super().withdraw(amount)
        


class CheckingAccount():
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.checkbook_issued = False
        
#bank_account1 = BankAccount("Michael")
#bank_account1.deposit(100)
#bank_account1.deposit(100)
#bank_account1.withdraw(50)

#print("-" * 50)

#bank_account2 = BankAccount("Kalen")
#bank_account2.deposit(500)
#bank_account2.deposit(-30)
#bank_account2.withdraw(780)

#print("-" * 50)

#bank_account1.display_details()
#bank_account2.display_details()

