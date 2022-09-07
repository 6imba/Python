import mysql.connector

connection = mysql.connector.connect(host='localhost',user='root',password='',database='database_1')
if connection:
    print('Connection Successful !!!')
else:
    print('Connection UnSuccessful !!!')

db_cursor = connection.cursor()
if db_cursor:
    print('Database_Cursor Successful !!!')
else:
    print('Database_Cursor UnSuccessful !!!')

# #Drop table if exists
# a1 = db_cursor.execute("DROP TABLE table_2")
# if a1:
#     print('Drop table')

# # Create table students
# a2 = db_cursor.execute("CREATE TABLE table_2 (name VARCHAR(255), age int)")
# if a2:
#     print('Create table')

# #Insert into table
# a3 = db_cursor.execute("INSERT INTO table_2 VALUES('Ankit', 21)")
# if a3:
#     print('Insert into table')

# connection.commit()












