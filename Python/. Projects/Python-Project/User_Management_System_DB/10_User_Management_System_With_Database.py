# User_Management_System with Database !!!!!

import mysql.connector
import random

class User_Model:

    connection = mysql.connector.connect(host='localhost',user='root',password='',database='database_1') 
    db_cursor = connection.cursor()
    db_cursor.execute('create table if not exists table_10 (User_Id int(100), User_Name varchar(30), First_Name varchar(30), Last_Name varchar(30), Email_Id varchar(30), Password varchar(30))')
    

    def create_user_query(self, user_input_list): 
        sql_insert = 'insert into table_10 values(%s,%s,%s,%s,%s,%s)'
        sql_values = user_input_list[0],user_input_list[1],user_input_list[2],user_input_list[3],user_input_list[4],user_input_list[5]
        self.db_cursor.execute(sql_insert,sql_values)
        self.connection.commit()

    def update_user_query(self, user, update_action):

        if update_action == 1:
            new_user_name = input('Enter New user_name : ')
            sql_insert = 'UPDATE table_10 SET User_Name = %s WHERE User_Name = %s' 
            sql_value = new_user_name, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

        if update_action == 2:
            new_first_name = input('Enter New first_name : ')
            sql_insert = 'UPDATE table_10 SET First_Name = %s WHERE User_Name = %s' 
            sql_value = new_first_name, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

        if update_action == 3:
            new_last_name = input('Enter New last_name : ')
            sql_insert = 'UPDATE table_10 SET Last_Name = %s WHERE User_Name = %s' 
            sql_value = new_last_name, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

        if update_action == 4:
            new_email = input('Enter New email : ')
            sql_insert = 'UPDATE table_10 SET Email_Id = %s WHERE User_Name = %s' 
            sql_value = new_email, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

        if update_action == 5:
            new_password = input('Enter New password : ')
            sql_insert = 'UPDATE table_10 SET Password = %s WHERE User_Name = %s' 
            sql_value = new_password, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

            
    def delete_user_query(self, delete_user):
        sql_delete = 'DELETE FROM table_10 WHERE User_Name = %s'
        sql_value = delete_user,
        self.db_cursor.execute(sql_delete,sql_value)
        self.connection.commit()

    def retrieve_user_query(self, user_retrieve):
        sql_user_retrieve = 'SELECT * FROM table_10 WHERE User_Name = %s'
        sql_value = user_retrieve,
        self.db_cursor.execute(sql_user_retrieve, sql_value)
        user_detial = self.db_cursor.fetchall()
        print(user_detial)
   
    # def retrieve_user_query(self, user_retrieve):
    #     sql_user_retrieve = 'SELECT * FROM table_10 WHERE User_Name = %s'
    #     sql_value = user_retrieve,
    #     self.db_cursor.execute(sql_user_retrieve, sql_value)
    #     user_detial = self.db_cursor.fetchall()
    #     for user in user_detial :
    #         print(user)


    def view_all_users(self):
        self.db_cursor.execute('SELECT * FROM table_10')
        result = self.db_cursor.fetchall()
        print(result)
        print(type(result))

        for user_id in result:
            print(user_id)
        
        
class User_View(User_Model):

    def view_menu_for_admin(self):
        print("""
        Menus
        Enter number 1 to 6 to do the following task:
        1. Create User
        2. Update User
        3. Delete User
        4. Retrieve User
        5. View All Users
        """)

    def view_menu_for_user(self):
        print("""
        Menus
        Enter number 1 to 4 to do the following task:
        1. Create User
        2. Update User
        3. Retrieve User
        """)

    def view_create(self):
        print('Method View_Create !!!!!! ')
        user_id1 = random.randrange(1000)
        user_name = str(input("Enter your user name:"))
        first_name = str(input("Enter your first name:"))
        last_name = str(input("Enter your last name:"))
        email_id = input("Enter your email id:")
        password = input("Enter your password:")
            
        user_input_list = [user_id1,user_name,first_name,last_name,email_id,password]
        super().create_user_query(user_input_list)

    def view_update(self):
        user = input("Enter number User_Name : ")
        print("""
            Enter the following number to Update the information:
            1. Update User Name
            2. Update First Name
            3. Update Last Name
            4. Update Email Id
            5. Update Password              
            """)
        update_action = int(input("Enter action number : "))
        super().update_user_query(user,update_action)

    def view_delete(self):
            delete_user = input("Enter the User_Name that you want to delete : ")
            super().delete_user_query(delete_user)

    def view_retrieve(self):
            user_retrieve = str(input("Enter your user name to retrieve your information:"))
            super().retrieve_user_query(user_retrieve)

    def view_all_user(self):
            super().view_all_users()


class Permissions_Module(User_View):

    def admin_role(self):
        while True:

            super().view_menu_for_admin()

            choose_action = int(input("Enter Here:"))
           
            while choose_action > 6 or choose_action < 1:
                choose_action = int(input("Enter only form 1 to 4:")) 

            # while type(choose_action)== str:
            #     choose_action = int(input("Sring or Character is invalid! Please Enter number only form 1 to 4:")) 

            if choose_action == 1:

                super().view_create()  

            elif choose_action == 2:

                super().view_update()

            elif choose_action == 3:

                super().view_delete()

            elif choose_action == 4:

                super().view_retrieve()

            else:
                super().view_all_user()

            answer = str(input("Enter to continue or type c to close:"))
            if answer == "c":
                break


    def user_role(self):

        while True:
            super().view_menu_for_user()

            choose_action = int(input("Enter Here:"))
            
            while choose_action > 4 or choose_action < 1:
                choose_action = int(input("Enter only form 1 to 4:")) 
                
            # while type(choose_action)== str:
            #     choose_action = int(input("Sring or Character is invalid! Please Enter number only form 1 to 4:")) 

            if choose_action == 1:
                super().view_create()
            elif choose_action == 2:
                super().view_update()
            elif choose_action == 3:
                super().view_retrieve()

            answer = str(input("Enter to continue or type c to close:"))
            if answer == "c":
                break




class Role_Model(Permissions_Module):

    def choose_role(self):
        while True:
            print("""
            Enter number to choose the following role:
            1. Admin
            2. User
            """)
            user_role = int(input("Enter Here:"))
            if user_role == 1:
                super().admin_role()
            else:
                super().user_role()

            answer = str(input("Enter to continue or type c to close:"))
            if answer == "c":
                break

obj_for_role = Role_Model()
obj_for_role.choose_role()
