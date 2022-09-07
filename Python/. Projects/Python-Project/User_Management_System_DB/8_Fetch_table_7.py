import mysql.connector
con = mysql.connector.connect(host='localhost',port='3306',user='root',password='',database='database_1')
cursor=con.cursor()
sql='select * from table_7'
cursor.execute(sql)
records=cursor.fetchall()
print(records)

# for individual in records:
#     print(individual)

# print(type(records))

# for individual in records:
#     print(type(individual))

