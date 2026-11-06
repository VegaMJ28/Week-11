import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE StudentDB")
print("Database created successfully")
mydb.close()