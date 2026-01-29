from dbconfig import mycursor, mydb
from models.account import Account

class Bank:
    def __init__(self) -> None:
        self.first_depo = 100000  # minimum deposit for creating account
        self.min_depo = 50000  # minimum deposit next moment

    def create_account(self, name: str, pin: str, balance: int, email: str):
        #access data and compare status
        sql = "SELECT * FROM accounts WHERE email = %s"
        val = (email,)
        mycursor.execute(sql, val)
        account = mycursor.fetchone()

        #validating account status
        if account:
            raise ValueError("Account with this email is already exist!")
        
        # validating first deposit from user
        if balance < self.first_depo:
            raise ValueError(f"minimum deposit is {self.first_depo}")            

        # insert data account into database
        sql = "INSERT INTO accounts (name, pin, balance, email, status) VALUES (%s, %s, %s, %s, %s)"
        val = (name, pin, balance, email, True)
        mycursor.execute(sql, val)
        mydb.commit()

        # update account status instance to be True
        account = Account(name, pin, balance, email)
        account.status = True
        account.balance = balance

        return account
        
    def withdraw(self):
        pass

    def check_balance(self):
        pass

    def transfer(self):
        pass

    def deposit(self):
        pass