from connector import mycursor


class User:
    def __init__(self, name, birthdate, email) -> str:
        self.name = name
        self.birthdate = birthdate
        self.email = email


class Account:
    def __init__(self, pin) -> str:
        self.pin = pin
        self.balance = 0
        self.status = False


class Bank:
    def __init__(self) -> None:
        self.first_depo = 100000  # minimum deposit for creating account
        self.min_depo = 50000  # minimum deposit next moment

    def create_account(self, name: str, pin: str, first_deposit: int):
        #access data and compare status
        table_accounts = mycursor.execute("SELECT * FROM accounts")
        sql = "SELECT * FROM accounts WHERE name = '%s'"
        val = name
        account = mycursor.execute(sql, val)

        #validating account status
        if account in table_accounts:
            print("this account is already exist!")
            return
        
        # validating first deposit from user
        if first_deposit <= self.first_depo:
            print(f"min deposit = {self.first_depo}")
            return

        # update account status to be True
        account = Account(pin)
        account.status = True
        account.balance = first_deposit

        # insert data account into database
        sql = "INSERT INTO accounts (pin, balance) VALUES (%s, %i)"
        val = (pin, first_deposit)
        mycursor.execute(sql, val)
        print("Create account success!")

    def withdraw(self):
        pass

    def check_balance(self):
        pass

    def transfer(self):
        pass

    def deposit(self):
        pass

b = Bank()
b.create_account("ucup kurucup", "123123", 25000)
