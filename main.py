from services.bank import Bank

acc = Bank()

try:
    acc.check_balance('dutaduta@gmail.com')

except ValueError as err:
    print(f"Error: {err}")
