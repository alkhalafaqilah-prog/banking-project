import random
import datetime

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

class transaction:
    def __init__(self,amount, transaction_type):
        self.date = datetime.now()
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date} - {self.transaction_type} - {self.amount}"


# function for generating random and unique account_id
def generate_account_id():
    return random.randint (10000,99999)

class bankAccount:
    def __init__(self, account_holder):
        self.account_id = generate_account_id()
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []
        
    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f"Deposited ${amount}\nNew balance: ${self.balance}")
            self.transactions.append(transaction(amount, "Deposit"))
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}\nNew balance: ${self.balance}")
            self.transactions.append(transaction(amount, "Withdrawal"))
        else:
            print ("Insufficient balance or invalid withdrawal amount.")

    def display_details(self):
        print(f"Account ID: {self.account_id}, Account Holder: {self.account_holder}, Balance: {self.balance}")
    
    


class savingsAccount(bankAccount):
    def __init__(self, account_holder, minimum_balance):
        super().__init__(account_holder)
        self.minimum_balance  = minimum_balance
    
    def withdraw(self,amount):
        if self.balance - amount < self.minimum_balance:
            print ("Cannot withdraw, minimum balance requirement not met.")
        else:
            super().withdraw(amount)
        


class checkingAccount(bankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.checkbook_issued = False

    def issue_checkbook(self):
        if not self.checkbook_issued:
            self.checkbook_issued = True
            print ("Checkbook issued")
        else:
            print("Checkbook already issued.")


# frodo_savings = savingsAccount("Frodo Baggins", 500)
# frodo_savings.deposit(1000)
# frodo_savings.withdraw(600)
# frodo_savings.display_details()

# print("-" * 50)

# voldi_checking = checkingAccount("Lord Voldemort")
# voldi_checking.deposit(2000)
# voldi_checking.issue_checkbook()
# voldi_checking.withdraw(1500)
# voldi_checking.display_details()


#bank_account1 = bankAccount("Michael")
#bank_account1.deposit(100)
#bank_account1.deposit(100)
#bank_account1.withdraw(50)

#print("-" * 50)

#bank_account2 = bankAccount("Kalen")
#bank_account2.deposit(500)
#bank_account2.deposit(-30)
#bank_account2.withdraw(780)

#print("-" * 50)

#bank_account1.display_details()
#bank_account2.display_details()

