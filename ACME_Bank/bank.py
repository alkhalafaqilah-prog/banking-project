import csv
import random
import datetime

# Source Michael - Coding Instructor YT & codeBricks
class BankAccount:
    def __init__(self, bankData="bank.csv"):
        self.bankData= bankData
        self.accounts = self.get_accounts()
        self.transactions = []
        
    def get_accounts(self):
        accounts = {}
        with open(self.bankData, 'r', newline='') as file:
            reader = csv.DictReader(file)
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
    
    def upload_accounts(self):
        fieldnames = ['account_id', 'frst_name', 'last_name', 'password', 'balance_checking', 'balance_savings', 'overdraft_count', 'is_active']
        with open(self.bankData, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = fieldnames )
            writer.writeheader()
            for account_id, data in self.accounts.items():
                row = {'account_id': account_id, **data}
                writer.writerow(row)
            
    # function for generating random and unique account_id
    def generate_account_id(self):
        while True:
            new_account_id  = str(random.randint (10000,99999))
            if new_account_id not in self.accounts:
                return new_account_id
    
    def add_new_customer(self, frst_name, last_name, password, checking_balance =0.0, savings_balance =0.0):
        account_id = self.generate_account_id()
        self.accounts[account_id] = {
            'frst_name': frst_name,
            'last_name': last_name,
            'password' : password,
            'balance_checking' : checking_balance,
            'balance_savings': savings_balance,
            'overdraft_count': 0,
            'is_active': True
        }
        self.upload_accounts()
        return account_id
    
    def login(self, account_id, password):
        if account_id not in self.accounts:
            print("Entered account does not exist!")
        if not self.accounts[account_id]['is_active']:
            print("Your account is deactivated.")
        if self.accounts[account_id]['password'] != password:
            print("Incorrect password.")
        print("\n   <<<     Login Confirmed!     >>>")
        return self.accounts[account_id]
    
    def deposit(self, account_id, account_type, amount):
        if amount >0:
            self.accounts[account_id][f'balance_{account_type}'] += amount
            print(f"Deposited {amount} SAR\nNew balance: {self.accounts[account_id][f'balance_{account_type}']} SAR")
            self.transactions.append(Transaction(amount, "Deposit"))
            self.upload_accounts()
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, account_id, account_type, amount):
        if 0 <= amount <= self.accounts[account_id][f'balance_{account_type}']:
            self.accounts[account_id][f'balance_{account_type}'] -= amount
            print(f"Withdrew {amount} SAR\nNew balance: {self.accounts[account_id][f'balance_{account_type}']} SAR")
            self.transactions.append(Transaction(amount, "Withdrawal"))
            self.upload_accounts()
        else:
            print ("Insufficient balance or invalid withdrawal amount.")

    def transfer(self, from_id, to_id, from_account_type,to_account_type, amount):
        if amount <= 0:
            print("Please enter a positive amount.")
        if from_id not in self.accounts or not self.accounts[from_id]['is_active']:
            print("Your account dose not exist or is not active!")
        if to_id not in self.accounts or not self.accounts[to_id]['is_active']:
            print("The account you trying to transfer money dose not exist or is not active!")
        
        self.withdraw(from_id, from_account_type, amount)
        self.deposit(to_id, to_account_type, amount)
        
        self.transactions.append(Transaction(amount, "Transfer"))
        self.upload_accounts()

    def display_details(self, account_id):
        account_info = self.accounts[account_id]
        full_name = f"{account_info['frst_name']} {account_info['last_name']}"
        print(f"Account ID: {account_id}, Account Holder: {full_name}, \nBalance_checking: {account_info['balance_checking']} SAR , Balance_savings: {account_info['balance_savings']} SAR.")
    
    def print_transaction_history(self):
        print("Transaction History: ")
        for transaction in self.transactions:
            print(transaction)

class Transaction (BankAccount):
    def __init__(self,amount, transaction_type):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date} - {self.transaction_type} - {self.amount} SAR"


class SavingsAccount(BankAccount):
    def __init__(self, account_id, minimum_balance):
        super().__init__(account_id)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, account_id, amount):
        if self.accounts[account_id]['balance_savings'] - amount < self.minimum_balance:
            print ("Cannot withdraw, minimum balance requirement not met.")
        else:
            super().withdraw(amount)
        

class CheckingAccount(BankAccount):
    def __init__(self, account_id):
        super().__init__(account_id)
        self.checkbook_issued = False

    def issue_checkbook(self):
        if not self.checkbook_issued:
            self.checkbook_issued = True
            print ("Checkbook issued")
        else:
            print("Checkbook already issued.")

# Main page for ACME bank system
class MainBankPage (BankAccount):
    def __init__(self):
        super().__init__()
    # Function displaying main page welcome message
    def welcomeMessage(self):
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
                account_id = input("Enter your account ID: ")
                password = input("Enter your account password: ")
                self.login(account_id,password)
                self.accountOperations(account_id)
                
            elif choice == "2":
                print("\n    <<<    New Customer Registration    >>>")
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                password = input("Create a password: ")
                account_id = self.add_new_customer(first_name, last_name, password, checking_balance=0.0, savings_balance=0.0)
                print(f"\nSuccessfully created a new checking account! Your Account ID is: {account_id}")
                
            elif choice == "3":
                print("\n    <<<    New Customer Registration    >>>")
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                password = input("Create a password: ")
                account_id = self.add_new_customer(first_name, last_name, password, checking_balance=0.0, savings_balance=0.0)
                print(f"\nSuccessfully created a new savings account! Your Account ID is: {account_id}")
                
            elif choice == "4":
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid input. Please try again.")
    
    def accountOperations(self, account_id):
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
                account_type = input("Which account to deposit to?(checking/savings): ")
                amount = float(input("Enter deposit amount: "))
                self.deposit(account_id, account_type, amount)
                
            elif choice == "2":
                account_type = input("Which account to withdraw from?(checking/savings): ")
                amount = float(input("Enter withdraw amount: "))
                self.withdraw(account_id, account_type, amount)
                
            elif choice == "3":
                from_account_type = input("Which account would you transfer from?(checking,savings): ")
                to_id = input("Enter the user ID or your personal ID to transfer to: ")
                to_account_type = input("Transfer to Account Type(checking/savings): ")
                amount = float(input("Enter the amount to transfer: "))
                self.transfer(account_id, to_id, from_account_type, to_account_type, amount)
                print (f"{amount} SAR transferred successfully!")
                
            elif choice == "4":
                self.display_details(account_id)
            elif choice == "5":
                self.print_transaction_history()
            elif choice == "6":
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid input. Please try again.")
            

if __name__ == "__main__":
    bank = MainBankPage()
    bank.welcomeMessage()

