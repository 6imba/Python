#User input procedure method

import mysql.connector
import random

connection = mysql.connector.connect(host='localhost',user='root',password='',database='database_1')
db_cursor = connection.cursor()
db_cursor.execute('drop table if exists table_4') #see
db_cursor.execute('create table table_4 (ids int,name varchar(30))')

db_cursor.execute("insert into table_4 values(1,'Zoran')") #hard_code
db_cursor.execute("insert into table_4 values(2,'Hero')") #hard_code
db_cursor.execute("insert into table_4 values(3,'Hatim')") #hard_code

user_id = random.randrange(50)
user_name = input('Enter user-name : ')
sql_insert = 'insert into table_4 values(%s,%s)'
sql_value = user_id,user_name
db_cursor.execute(sql_insert,sql_value)

user_id = random.randrange(50)
user_name = input('Enter user-name : ')
sql_insert = 'insert into table_4 values(%s,%s)'
sql_value = user_id,user_name
db_cursor.execute(sql_insert,sql_value)

user_id = random.randrange(50)
user_name = input('Enter user-name : ')
sql_insert = 'insert into table_4 values(%s,%s)'
sql_value = user_id,user_name
db_cursor.execute(sql_insert,sql_value)

connection.commit()
