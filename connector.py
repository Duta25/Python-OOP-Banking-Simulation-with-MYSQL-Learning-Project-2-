import mysql.connector as mysql

mydb = mysql.connect(
    host= "localhost",
    user= "root",
    passwd = "secret",
    database = "bank"
)    

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM accounts")
result = mycursor.fetchall()
for i in result:
    print(i)