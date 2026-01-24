class Account:
    def __init__(self, pin, balance) -> None:
        self.pin = pin
        self.balance = balance
        self.status = False

    def create_account(self, pin, deposit):
        pass 

class User:
    def __init__(self, name, birthdate) -> None:
        self.name = name
        self.birthdate = birthdate

class Bank:
    def __init__(self, ) -> None:
        pass

    def withdraw(self): 
        pass

    def check_balance(self):
        pass

    def transfer(self):
        pass
    
    def deposit(self):
        pass