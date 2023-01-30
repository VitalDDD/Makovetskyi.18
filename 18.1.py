import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111"

)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db")
