# 🏦 ACME Bank System Command Line Interface (CLI) project

## Description

A simple, file-based banking system application built in Python to simulate core bank operations, including account management, transactions, and overdraft protection.

## ✨ Features

* **Secure Login:** Users can log in with a unique account ID and a password hidden via the `getpass` module.
* **Account Creation:** Create both Checking and Savings accounts.
* **Transactions:** Perform Deposits, Withdrawals, and Transfers between accounts.
* **Overdraft Protection:**  Applies a $35 fee and increments an overdraft counter upon insufficient funds.
* **Account Deactivation:** Automatically deactivates accounts after two overdraft incidents.
* **Persistent Data:** All account and transaction data is stored securely in a local `bank.csv` file.

## 🚀 Getting Started

### Dependencies

* You need Python 3.9 and above installed on your system.
* You need stdiomask module installed, if you don't have it use the following command:
    ```
    pip install stdiomask
    ```

### Installing & Executing program

1.  **Clone the repository:**
    ```
    git clone https://github.com/alkhalafaqilah-prog/banking-project
    cd banking-project
    code .
    ```

2.  **Run the application:**
    
    In your terminal run the code using:

    ```
    python ACME_Bank/bank.py
    ```

## 📝 Usage Examples

**1. Create a New Account (Option 2 or 3)**
* A unique 5-digit Account ID will be generated and displayed.

**2. Transfer Funds (Option 3 in Operations Menu)**
* You will be prompted for the source account type (`checking`/`savings`), the destination Account ID, the destination account type, and the amount.

**3. Account Deactivation**
* If a Checking account attempts a withdrawal with insufficient funds twice, it will be automatically deactivated.

## 👨‍💻 Author

Aqilah Alkhalaf: https://github.com/alkhalafaqilah-prog


## Acknowledgments

* [Michael - Coding Instructor](https://www.youtube.com/watch?v=MGhgq-hVlAU)
* [CodeBricks](https://codebricks.co.nz/python-oop-example-01)
* [Corey Schafer](https://www.youtube.com/watch?v=q5uM4VKywbA)
* [NeuralNine](https://www.youtube.com/watch?v=nqkkW0fZRWM)
