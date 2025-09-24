import csv
import random
import datetime

# Main page for ACME bank system
class MainBankPage:
    # Function displaying main page welcome message
    def welcomeMessage():
        while True:
            print()
            print("-" * 50)
            print("                Welcome to ACME Bank               ")
            print("-" * 50)
            print("  Please choose one of the following options:")
            print("    1. Login to existing account.")
            print("    2. Create new checking account.")
            print("    3. Create new saving account.")
            print("    4. Exit.")
            print()
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid input. Please try again.")
    
    def accountOperations():
        while True:
            print()
            print("-" * 50)
            print("                Account Operations               ")
            print("-" * 50)
            print("  Please choose one of the following options:")
            print("    1. Deposit.")
            print("    2. Withdraw.")
            print("    3. Transfer.")
            print("    4. Check Balance.")
            print("    5. View transaction history.")
            print("    6. Exit.")
            print()
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid input. Please try again.")
            

# Source Michael - Coding Instructor YT
class Transaction:
    def __init__(self,amount, transaction_type):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date} - {self.transaction_type} - ${self.amount}"


# function for generating random and unique account_id
def generate_account_id():
    return random.randint (10000,99999)

class BankAccount:
    def __init__(self, bankData="bank.csv"):
        self.bankData= bankData
        self.accounts = self.get_accounts()
        self.transactions = []
        
    def get_accounts(self):
        accounts = {}
        with open(self.bankData, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                accounts[row['account_id']] = {
                    'frst_name': row['frst_name'],
                    'last_name': row['last_name'],
                    'password': row['password'],
                    'balance_checking': float(row['balance_checking']),
                    'balance_savings': float(row['balance_savings']),
                    'overdraft_count': int(row.get('overdraft_count', 0)),
                    'is_active': row.get('is_active', 'True').lower() == 'true'
                    }
        return accounts
    
    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f"Deposited ${amount}\nNew balance: ${self.balance}")
            self.transactions.append(Transaction(amount, "Deposit"))
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}\nNew balance: ${self.balance}")
            self.transactions.append(Transaction(amount, "Withdrawal"))
        else:
            print ("Insufficient balance or invalid withdrawal amount.")

    def display_details(self):
        print(f"Account ID: {self.account_id}, Account Holder: {self.account_holder}, Balance: {self.balance}")
    
    def print_transaction_history(self):
        print("Transaction History: ")
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, minimum_balance):
        super().__init__(account_holder)
        self.minimum_balance  = minimum_balance
    
    def withdraw(self,amount):
        if self.balance - amount < self.minimum_balance:
            print ("Cannot withdraw, minimum balance requirement not met.")
        else:
            super().withdraw(amount)
        


class CheckingAccount(BankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.checkbook_issued = False

    def issue_checkbook(self):
        if not self.checkbook_issued:
            self.checkbook_issued = True
            print ("Checkbook issued")
        else:
            print("Checkbook already issued.")


