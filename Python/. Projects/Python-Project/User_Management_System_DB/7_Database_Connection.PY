import random
import mysql.connector

class User_Model:
    
    connection = mysql.connector.connect(host='localhost',user='root',password='',database='database_1')
    db_cursor = connection.cursor()

    db_cursor.execute('create table if not exists table_7 (id int,user_name varchar(30))')


    def create_user_query(self, user_input_list): 
        sql_insert = 'insert into table_7 values(%s,%s)'
        sql_values = user_input_list[0],user_input_list[1]
        self.db_cursor.execute(sql_insert,sql_values)
        self.connection.commit()
        
       
class User_View(User_Model):

    def view_create(self):
        user_id1 = random.randrange(1000)
        user_name = str(input("Enter your user name:"))         
        user_input_list = [user_id1,user_name]        
        super().create_user_query(user_input_list) 


class Permissions_Module(User_View):
    def user_role(self):
        while True:
            super().view_create()
            answer = str(input("Enter to continue or type c to close:"))
            if answer == "c":
                break

obj_for_role = Permissions_Module()
obj_for_role.user_role()
