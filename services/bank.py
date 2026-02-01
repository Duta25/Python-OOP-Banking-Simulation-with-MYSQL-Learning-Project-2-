from dbconfig import mycursor, mydb
from models.account import Account

class Bank:
    def __init__(self) -> None:
        self.first_depo = 100000  # minimum deposit for creating account
        self.min_depo = 50000  # minimum deposit next moment

    def create_account(self, name: str, pin: str, balance: int, email: str):
        # access data and compare status
        sql = "SELECT * FROM accounts WHERE email = %s"
        val = (email,)
        mycursor.execute(sql, val)
        account = mycursor.fetchone()

        # validate account status
        if account:
            raise ValueError("Account with this email is already exist!")
        
        # validate first deposit from user
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
        
    def withdraw(self, amount, email):
        # access balance from database
        balance = "SELECT balance FROM accounts WHERE email = %s"
        val = (email,)
        mycursor.execute(balance, val)
        account = mycursor.fetchone()
        
        # validate if email not found
        if account is None:
            raise ValueError("Email Not Found!")

        # validate if balance not enough
        if account[0] < amount:
            raise ValueError("Balance not enough!")

        # update balance value from database
        sql = "UPDATE accounts SET balance = balance - %s WHERE email = %s"
        val = (amount, email)
        mycursor.execute(sql, val)
        mydb.commit()

    def check_balance(self, email):
        # access balance in database
        sql = "SELECT balance FROM accounts WHERE email = %s"
        val = (email,)
        mycursor.execute(sql, val)
        account = mycursor.fetchone()

        # validate if email not found
        if account is None:
            raise ValueError("Email not found!")

        return account[0]

    def transfer(self, amount, frm_email, to_email):
        # access account into database
        sql = "SELECT balance FROM accounts WHERE email = %s"
        val = (frm_email,)
        mycursor.execute(sql, val)
        account = mycursor.fetchone()

        # raise error if email not found
        if account is None:
            raise ValueError("email not found")

        # raise error if balance not enough
        if account[0] < amount:
            raise ValueError("Balance not enough")
        
        # access email data recipient
        sql = "SELECT * FROM accounts WHERE email = %s"
        val = (to_email,)
        mycursor.execute(sql, val)
        account = mycursor.fetchone()
        
        # raise error if email recipient not found
        if account is None:
            raise ValueError("Email which is aimed not found!")
      
        # update balance data recipient
        sql = "UPDATE accounts SET balance = balance + %s WHERE email = %s"
        val = (amount, to_email)
        mycursor.execute(sql, val)
        mydb.commit()

        # update balance data sender
        sql = "UPDATE accounts SET balance = balance - %s WHERE email = %s"
        val = (amount, frm_email)
        mycursor.execute(sql, val)
        mydb.commit()
        
    def deposit(self, amount, email):
        # access balance from database
        sql = "SELECT balance FROM accounts WHERE email = %s"
        val = (email,)
        mycursor.execute(sql, val)
        account = mycursor.fetchone()

        # validate account status
        if account is None:
            raise ValueError("Email not found!")

        # validate min deposit
        if amount < self.min_depo:
            raise ValueError(f"Min deposit: {self.min_depo}")
        
        # update balance based on deposit
        sql = "UPDATE accounts SET balance = balance + %s WHERE email = %s"
        val = (amount, email)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Deposit success!")