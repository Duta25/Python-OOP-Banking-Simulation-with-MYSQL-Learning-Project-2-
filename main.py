from services.bank import Bank

try:
    acc = Bank.create_account(Bank, "duta", "123123", 100000, "dutaduta@gmail.com")
    print("account was created!")
except RuntimeError:
    print(f"error {RuntimeError}")