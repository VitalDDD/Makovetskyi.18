import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111",
    database="my_first_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = ("01", "john")
mycursor.execute(sql, val)

sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = ("01", "john", "10000")
mycursor.execute(sql, val)

mydb.commit()
