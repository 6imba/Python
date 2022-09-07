# insert user hard-code

import mysql.connector

# connection with database
connection = mysql.connector.connect(host='localhost',user='root',password='',database='database_1')
if connection:
    print('Connection Successsfull !')
else:
    print('Connection Unsucessfull !')

#coursor(pointer like) of the current connection
db_cursor = connection.cursor()
if db_cursor:
    print('Database_Cursor Successsfull !')
else:
    print('Database_Cursor Unsuccesssfull !')

#Drop table if exists
db_cursor.execute("DROP TABLE table_1")

# Create table students
db_cursor.execute("CREATE TABLE table_1 (name VARCHAR(255), age int)")

#Insert into table
db_cursor.execute("INSERT INTO table_1 VALUES('Ankit', 21)")

#Commit over the action with the connection
connection.commit()

#main
db_cursor.execute("SELECT * FROM table_1")
for record in db_cursor.fetchall():
    print(record)