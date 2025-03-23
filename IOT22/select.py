# insert.py, test to select record from MySQL database
# PgP 9/5/2022
# PgP 9/7/2022-this script runs fine on Windows, connecting to Raspberry Pi db

import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.15",
  user="user",
  password="user",
  database="sensor"
)

mycursor = mydb.cursor()

# Enforce UTF-8 for the connection.
#mycursor.execute('SET NAMES utf8mb4')
#mycursor.execute("SET CHARACTER SET utf8mb4")
#mycursor.execute("SET character_set_connection=utf8mb4")

mycursor.execute("SELECT * FROM dht;")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    

print(mycursor.rowcount, "records selected")

