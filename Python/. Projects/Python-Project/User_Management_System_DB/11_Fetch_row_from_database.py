
import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='', database='database_1')
db_cursor = connection.cursor()

db_cursor.execute('drop table table_11')
db_cursor.execute('create table table_11 (User_Id int(100), User_Name varchar(30), Course varchar(30), Address varchar(30), Gender varchar(30))')
db_cursor.execute("insert into table_11 values('1','Resu','BHM','Japan','Female')")
db_cursor.execute("insert into table_11 values('2','Hemat','MBBS','India','Male')")
db_cursor.execute("insert into table_11 values('3','Kelly','CSIT','Nepal','Female')")






# # 1
# db_cursor.execute('select * from table_6')
# record_table_11 = db_cursor.fetchall()
# print(record_table_11)


# # 2

# db_cursor.execute('select * from table_11')
# record_table_11 = db_cursor.fetchall()
# print('id = ',record_table_11[0])
# print('name  = ',record_table_11[1])
# print('coyurse = ',record_table_11[2])
# print('address = ',record_table_11[3])
# print('gender = ',record_table_11[4])
# # error as record_table_11(table) it carries list of items(rows)


# # 3
# db_cursor.execute('select * from table_11')
# record_table_11 = db_cursor.fetchall()
# for row in record_table_11:
#     print('id = ',row[0])
#     print('name  = ',row[1])
#     print('coyurse = ',row[2])
#     print('address = ',row[3])
#     print('gender = ',row[4])




# # 4
# db_cursor.execute('select * from table_11')
# record_table_11 = db_cursor.fetchall()
# for row in record_table_11:
#     print(row)




# # 5
# db_cursor.execute('select * from table_11')
# record_table_11 = db_cursor.fetchall()
# for row in record_table_11:
#     print(row)
#     for colmn in row:
#         print(colmn)



# import mysql.connector

# connection = mysql.connector.connect(host='localhost', user='root', password='', database='database_1')
# db_cursor = connection.cursor()

# db_cursor.execute('select * from table_6')
# record_table_11 = db_cursor.fetchall()
# for row in record_table_11:
#     print('Id = ',row[0])
#     print('Name = ',row[1])
#     print('Course = ',row[2])
#     print('Address = ',row[3])
#     print('Gender = ',row[4])




# import mysql.connector

# connection = mysql.connector.connect(host='localhost', user='root', password='', database='database_1')
# db_cursor = connection.cursor()

# db_cursor.execute('select * from table_6')
# for row in db_cursor.fetchall():
#     print(row)


# import mysql.connector

# connection = mysql.connector.connect(host='localhost', user='root', password='', database='database_1')
# db_cursor = connection.cursor()

# db_cursor.execute('select * from table_6')
# for row in db_cursor.fetchall():
#     print(row)
#     for col in row:
#         print(col)


# import mysql.connector

# connection = mysql.connector.connect(host='localhost', user='root', password='', database='database_1')
# db_cursor = connection.cursor()

# db_cursor.execute('select * from table_6')
# for row in db_cursor.fetchall():
#     print(row)
#     for col in row:
#         print(col[0])
#         print(col[1])
# # this code shows error as col is no futher idexable !!!!



# python 11_Fetch_row_from_database.py