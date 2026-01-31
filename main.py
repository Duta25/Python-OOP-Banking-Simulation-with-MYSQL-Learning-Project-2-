from services.bank import Bank

acc = Bank()

try:
    acc.check_balance("dutaduta@gmail.com")

except RuntimeError:
    print(f"error {RuntimeError}")