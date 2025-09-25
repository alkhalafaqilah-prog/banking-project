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