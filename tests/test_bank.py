import unittest
import os 
import sys
# Source : Stack overflow , python main page
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ACME_Bank.bank import BankAccount, MainBankPage, Transaction

class TestBank (unittest.TestCase):
    def setUp(self):
        self.test_csv_bank = 'test_bank.csv'
        self.bank = BankAccount(bankData=self.test_csv_bank)
        
        self.mock_csv_bank = (
            "account_id,frst_name,last_name,password,balance_checking,balance_savings,minimum_savings,overdraft_count,is_active\n"
            "10001,suresh,sigera,juagw362,1100.0,10000.0,0.0,0,True\n"
            "10002,james,taylor,idh36%@#FGd,10000.0,10000.0,0.0,0,True\n"
            "10003,melvin,gordon,uYWE732g4ga1,2000.0,20000.0,0.0,0,True\n"
            "10004,stacey,abrams,DEU8_qw3y72$,2000.0,20000.0,0.0,0,True\n"
            "10005,jake,paul,d^dg23g)@,100000.0,100000.0,0.0,0,True\n"
            "64481,Aqilah,Alkhalaf,pppp,780.0,250.0,0.0,0,True\n"
            "61879,Osama,Ahmed,oooo,-5.0,0.0,0.0,3,False\n"
            "79129,Mohammed,Rada,Okiuy,0.0,700.0,100.0,0,True\n"
        )
        
        with open(self.test_csv_bank,'w',newline='') as file:
            file.write(self.mock_csv_bank)
        
        self.bank = BankAccount(bankData=self.test_csv_bank)
        
    # def tearDown(self):
    #     if os.path.exists(self.test_csv_bank):
    #         os.remove(self.test_csv_bank)
    
    def test_bank_accounts(self):
        self.assertIsInstance(self.bank,BankAccount)
        self.assertEqual(len(self.bank.accounts),8)
        self.assertIn('10003',self.bank.accounts)
        self.assertIn('61879',self.bank.accounts)
        self.assertIn('79129',self.bank.accounts)
    
    def test_main_bank_page(self):
        main_page = MainBankPage()
        self.assertIsInstance(main_page,MainBankPage)
    
    def test_login_confirmation(self):
        account = self.bank.login('10001','juagw362')
        
        #Test if login is successful
        self.assertIsNotNone(account)
        self.assertEqual(account['frst_name'], 'suresh')
        
        #Test incorrect password
        self.assertIsNotNone (self.bank.login('10001','apdcvb'))
        
        #Test not exited account id
        self.assertIsNone (self.bank.login('10007','apdcvb'))
    
    def test_add_new_customer(self):
        new_cust = self.bank.add_new_customer("Norah","Khaled","PASSWORD")
        self.assertIn(new_cust, self.bank.accounts)
        self.assertEqual(self.bank.accounts[new_cust]['frst_name'], "Norah")
        self.assertEqual(self.bank.accounts[new_cust]['balance_checking'], 0.0)
        self.assertEqual(self.bank.accounts[new_cust]['balance_savings'], 0.0)
    
    def test_deposit(self):
        current_balance = self.bank.accounts['10003']['balance_checking']
        self.bank.deposit('10003','checking',100)
        self.assertEqual(self.bank.accounts['10003']['balance_checking'], current_balance + 100)
        self.assertEqual(len(self.bank.transactions), 1)
    
    def test_withdraw(self):
        #Test successful withdraw
        current_balance = self.bank.accounts['10002']['balance_checking']
        self.bank.withdraw('10002', 'checking', 50)
        self.assertEqual(self.bank.accounts['10002']['balance_checking'], current_balance - 50)
        
        #Test of insufficient amount withdraw
        initial_balance = self.bank.accounts['64481']['balance_checking']
        self.bank.withdraw('64481', 'checking', 900)
        self.assertEqual(self.bank.accounts['64481']['balance_checking'], initial_balance)
        
        #Test withdrawing an amount more than minimum balance in savings
        minimum_balance = self.bank.accounts['79129']['balance_savings']
        self.bank.withdraw('79129', 'savings', 650)
        self.assertEqual(self.bank.accounts['79129']['balance_savings'], minimum_balance)

    def test_overdraft_protection(self):
        self.bank.accounts['10005']['balance_checking'] = -20
        self.bank.accounts['10005']['overdraft_count'] = 1
        self.bank.withdraw('10005', 'checking', 50)
        self.assertEqual(self.bank.accounts['10005']['balance_checking'], -20 - 35)
        self.assertFalse(self.bank.accounts['10005']['is_active'])
    
    def test_transfer_success(self):
        #Test successful transfer
        sent_initial_balance = self.bank.accounts['10001']['balance_checking']
        received_initial_balance = self.bank.accounts['10002']['balance_checking']
        
        self.bank.transfer('10001', '10002', 'checking', 'checking', 100)
        
        self.assertEqual(self.bank.accounts['10001']['balance_checking'], sent_initial_balance - 100)
        self.assertEqual(self.bank.accounts['10002']['balance_checking'], received_initial_balance + 100)
        #Test transferring insufficient amount
        sent_balance = self.bank.accounts['10001']['balance_checking']
        received_balance = self.bank.accounts['10002']['balance_checking']
        
        self.bank.transfer('10001', '10002', 'checking', 'checking', 20000)
        
        self.assertEqual(self.bank.accounts['10001']['balance_checking'], sent_balance)
        self.assertNotEqual(self.bank.accounts['10002']['balance_checking'], received_balance)
    
    if __name__ == '__main__':
            unittest.main()