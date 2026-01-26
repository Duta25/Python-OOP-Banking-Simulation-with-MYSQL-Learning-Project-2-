import mysql.connector as mysql
from bank import table_accounts

print(table_accounts)

mydb = mysql.connect(
    host= "localhost",
    user= "root",
    passwd = "secret",
    database = "bank"
)    

mycursor = mydb.cursor()

