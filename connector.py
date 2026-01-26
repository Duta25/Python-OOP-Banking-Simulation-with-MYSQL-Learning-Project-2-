import mysql.connector as mysql

mydb = mysql.connect(
    host= "localhost",
    user= "root",
    passwd = "secret",
    database = "bank"
)    

mycursor = mydb.cursor()
mycursor.execute("SHOW COLUMNS FROM accounts")
result = mycursor.fetchall()
for i in result:
    print(i)