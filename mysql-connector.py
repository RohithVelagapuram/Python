import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Root',
    port='3306',
    database="python_mysql"
)
"""
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM users')
users = mycursor.fetchall()
for i in users:
    print(i)
"""
mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255))')
sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
val = ("Rohith", "Kavali 124")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute('SELECT * FROM Customers')
Customers = mycursor.fetchall()
for i in Customers:
    print(i)