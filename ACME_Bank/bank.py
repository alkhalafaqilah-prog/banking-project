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

