import mysql.connector

# db_connection = mysql.connector.connect(host="localhost",user="simba",passwd="1234",database='DataBase_1',auth_plugin='mysql_native_password')
# db_cursor = db_connection.cursor()
# db_cursor.execute("select * from student;")
# for record in db_cursor:
#     print(record)


# db_connection = mysql.connector.connect(host="localhost",user="simba",passwd="1234",database='DataBase_1',auth_plugin='mysql_native_password')
# if db_connection:
#     print('Connection success')
#     db_cursor = db_connection.cursor()
#     db_cursor.execute("select * from student;")
#     for record in db_cursor:
#         print(record)
# else:
#     print('Connection failed')

# try:
#     db_connection = mysql.connector.connect(host="localhost",user="simba",passwd="1234",database='DataBase_1',auth_plugin='mysql_native_password')
#     print('Connection success !!!')
#     db_cursor = db_connection.cursor()
#     db_cursor.execute("select * from student;")
#     for record in db_cursor:
#         print(record)
# except Exception as e:
#     print("Exception caught ===> ",e)

try:
    tableName = "test_1"
    db_connection = mysql.connector.connect(host="localhost",user="simba",passwd="1234",database='database_1',auth_plugin='mysql_native_password')
    db_cursor = db_connection.cursor()
    # print(dir(db_cursor))

    metadata_table_create_query = "CREATE TABLE if not exists {} (MetaDataID int, FullName varchar(255), DesignerName varchar(255));".format(tableName)
    metadata_table_insert_query = "INSERT INTO fontdetail VALUES (1,'cat','dog'),(2,'cat','dog'),(3,'cat','dog');"
    # db_cursor.execute          ("INSERT INTO  table1     values (%s,%s,%s,%s,%s)" , (name,address,gender,password,country))


    db_cursor.execute(metadata_table_create_query)
    db_cursor.execute(metadata_table_insert_query)
    print("Record inserted !!!")

    db_connection.commit() # when working with table data.
    db_connection.close()

#     # db_cursor.execute(metadata_table_insert_query)
#     db_cursor.execute("select * from apple")
    for x in db_cursor:
        print(x)
        print(1)


except Exception as e:
    print("Exception caught ==> ", e)