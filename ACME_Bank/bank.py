import random

# Main page for ACME bank system
class mainBankPage:
    # Function displaying main page welcome message
    def welcomeMessage():
        print()
        print("---------------------------------------------------")
        print("                Welcome to ACME Bank               ")
        print("---------------------------------------------------")
        print("  Please choose one of the following options:")
        print("    1.Login to existing account")
        print("    2.Create new checking account")
        print("    3.Create new saving account")
        print("    4.Exit")
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
            print(f"Deposited ${amount}. \n New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self,amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. \n New balance: ${self.balance}")
        else:
            print ("Insufficient balance or invalid withdrawal amount.")

    def display_details(self):
        print(f"Account ID: {self.account_id}. \n Account Holder: {self.account_holder}.\n Balance: {self.balance}")
