
import mysql.connector
connection = mysql.connector.connect(host='localhost', user='root', password='', database='database_1')
db_cursor = connection.cursor()

db_cursor.execute('select * from table_6')
record_table_6 = db_cursor.fetchall()
print('id = ',record_table_6[0])
print('name  = ',record_table_6[1])
print('coyurse = ',record_table_6[2])
print('address = ',record_table_6[3])
print('gender = ',record_table_6[4])
# error as record_table_6(table) it carries list of items(rows)
