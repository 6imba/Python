#User input procedure method

import mysql.connector
connection = mysql.connector.connect(
     host="localhost"
    ,user="root"
    ,password=""
    ,database="database_1"
)
db_cursor = connection.cursor()
db_cursor.execute('drop table table_3')
db_cursor.execute("CREATE TABLE table_3 (id int, name VARCHAR(255))")
connection.commit()

import random
user_id1 = random.randrange(1000)
user_name = str(input("Enter your user name:")) 
sql_insert = 'insert into table_3 values(%s,%s)'
sql_values = user_id1,user_name
db_cursor.execute(sql_insert,sql_values)
connection.commit()

