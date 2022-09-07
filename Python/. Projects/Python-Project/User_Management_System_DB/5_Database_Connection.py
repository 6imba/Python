# insert user input oop

import mysql.connector
import random 

class Database:
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="database_1")
    db_cursor = connection.cursor()
    def create(self,user_list):
        self.db_cursor.execute('drop table if exists table_5') # this will drop current table every time this method(create) is call
        self.db_cursor.execute("CREATE TABLE table_5 (id int, name VARCHAR(255))")
        sql_insert = 'insert into table_5 values(%s,%s)'
        sql_values = user_list[0],user_list[1]
        self.db_cursor.execute(sql_insert,sql_values)
        self.connection.commit()

class User(Database):
    def view(self):
        while True:
            user_id1 = random.randrange(1000)
            user_name = str(input("Enter your user name:")) 
            user_list = [user_id1,user_name]
            super().create(user_list)
            answer = str(input("Enter to continue or type c to close:"))
            if answer == "c":
                break

obj1 = User()
obj1.view()




# #Two.........................................

# import mysql.connector
# import random

# class Database:
    
#     print('I am Parent class_database !')
#     connection = mysql.connector.connect(host="localhost", user="root", password="", database="database_1")
#     print('I am Parent Connection')

#     db_cursor = connection.cursor()
#     print('I am Parent Cursor')

#     def create(self,user_list):
#         print('I am method of parent class_user !')
#         self.db_cursor.execute('drop table table_1')
#         self.db_cursor.execute("CREATE TABLE table_1 (id int, name VARCHAR(255))")
#         sql_insert = 'insert into table_1 values(%s,%s)'
#         sql_values = user_list[0],user_list[1]
#         self.db_cursor.execute(sql_insert,sql_values)
#         self.connection.commit()

# class User(Database):
    
#     print('I am child class_user !')
#     def view(self):
#         print('I am method_view of child class !')
#         while True:
#             user_id1 = random.randrange(1000)
#             print('I am variable_id of child class !')
#             user_name = str(input("Enter your user name:")) 
#             print('I am variable_name of child class !')
#             user_list = [user_id1,user_name]
#             print('pass var id and name as list to parent_class create method !')
#             super().create(user_list)
#             answer = str(input("Enter to continue or type c to close:"))
#             if answer == "c":
#                 break

# obj1 = User()
# print('*****************************')
# obj1.view()



