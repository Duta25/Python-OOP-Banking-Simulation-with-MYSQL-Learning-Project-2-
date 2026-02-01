🏦 Simple Banking System (Python OOP + MySQL)

This is my second backend learning project.
The goal of this project is to strengthen my understanding of:

Object-Oriented Programming (OOP)

Business logic implementation

Basic database integration (MySQL)

Error handling using exceptions

Project structure organization

This project is not production-ready and does not focus on security.
It is built purely to improve my backend fundamentals.

📌 Features

Create Account

Deposit

Withdraw

Transfer

Check Balance

All operations are connected directly to a MySQL database.

🧠 What I Practiced in This Project

Separating project structure into:

models

services

dbconfig

main.py

Using parameterized SQL queries (%s) to prevent SQL injection

Applying business validation:

Minimum first deposit

Minimum deposit amount

Insufficient balance check

Email existence validation

Raising exceptions (ValueError) instead of using print statements

Basic transaction logic implementation

🗂️ Project Structure
project/
│
├── models/
│   └── account.py
│
├── services/
│   └── bank.py
│
├── dbconfig.py
├── main.py
└── README.md

⚙️ Tech Stack

Python 3

MySQL

mysql-connector-python

🚀 How to Run

Make sure MySQL is installed and running.

Create a database and accounts table.

Configure database connection in dbconfig.py.

Run:

python main.py

🧱 Database Schema Example
CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    pin VARCHAR(100),
    balance INT,
    email VARCHAR(100) UNIQUE,
    status BOOLEAN
);

⚠️ Limitations

No password hashing

No transaction atomicity handling (transfer is not fully safe yet)

No REST API

No authentication system

No logging system

This project focuses only on backend logic practice.

📈 Learning Reflection

Through this project, I learned:

How to translate business rules into code

How to validate user input properly

How to separate logic into services and models

Why transaction handling is important in financial systems

I am currently focusing on strengthening my backend fundamentals before moving into REST API frameworks.

📌 Status

Learning Project #2
Focused on backend fundamentals and clean logic structure.
