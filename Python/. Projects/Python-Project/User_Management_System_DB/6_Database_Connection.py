# # insert user input oop

# import mysql.connector
# import random

# class Database:
#     connection = mysql.connector.connect(host="localhost", user="root", password="", database="database_1")
#     db_cursor = connection.cursor()
#     db_cursor.execute('drop table if exists table_6') # note:1 ==> this will drop current table at the time we call class(Database) and we call class once only and gon on running inside class # here note:1 says we call class but class runs itself as code execute from top top-button so we dont need to call it, we need to call method of class atributes/property are runs itself as code execute from top-botton

#     def create(self,user_list):
#         self.db_cursor.execute("CREATE TABLE table_6 (id int, name VARCHAR(255))") # when running into loop method, this line already creates table_6 in 1st iteartion so in 2nd iteration it shows error to create table_6 again so solution_1
#         sql_insert = 'insert into table_6 values(%s,%s)'
#         sql_values = user_list[0],user_list[1]
#         self.db_cursor.execute(sql_insert,sql_values)
#         self.connection.commit()

# class User(Database):
#     def view(self):
#         while True:
#             user_id1 = random.randrange(1000)
#             user_name = str(input("Enter your user name:")) 
#             user_list = [user_id1,user_name]
#             super().create(user_list)
#             answer = str(input("Enter to continue or type c to close:"))
#             if answer == "c":
#                 break

# obj1 = User()
# obj1.view()





# #solution_1...............................................

# import mysql.connector
# import random

# class Database:
#     connection = mysql.connector.connect(host="localhost", user="root", password="", database="database_1")
#     db_cursor = connection.cursor()
#     db_cursor.execute('drop table if exists table_6') # solution_2..... this will drop current table at the time we call class(Database) and we call class once only and gon on running inside class
#     db_cursor.execute("CREATE TABLE table_6 (id int, name VARCHAR(255))")  #solution_1

#     def create(self,user_list):
#         sql_insert = 'insert into table_6 values(%s,%s)'
#         sql_values = user_list[0],user_list[1]
#         self.db_cursor.execute(sql_insert,sql_values)
#         self.connection.commit()

# class User(Database):
#     def view(self):
#         while True:
#             user_id1 = random.randrange(1000)
#             user_name = str(input("Enter your user name:")) 
#             user_list = [user_id1,user_name]
#             super().create(user_list)
#             answer = str(input("Enter to continue or type c to close:"))
#             if answer == "c":
#                 break

# obj1 = User()
# obj1.view()
# # Note : This code works perfectly untill you are running this code but when you exit from this code and run again it will drop the table created previously and its data so solution_2






# # solution_2 ......................................................
# import mysql.connector
# import random

# class Database:
    
#     connection = mysql.connector.connect(host="localhost", user="root", password="", database="database_1")
#     db_cursor = connection.cursor()

#     db_cursor.execute("CREATE TABLE if not exists table_6 (id int, name VARCHAR(255))") #solution_2..... it will insert into table without dropping or editing already existed table.........

#     def create(self,user_list):
#         sql_insert = 'insert into table_6 values(%s,%s)'
#         sql_values = user_list[0],user_list[1]
#         self.db_cursor.execute(sql_insert,sql_values)
#         self.connection.commit()

# class User(Database):
    
#     def view(self):
#         while True:
#             user_id1 = random.randrange(1000)
#             user_name = str(input("Enter your user name:")) 
#             user_list = [user_id1,user_name]
#             super().create(user_list)
#             answer = str(input("Enter to continue or type c to close:"))
#             if answer == "c":
#                 break


# obj1 = User()
# obj1.view()