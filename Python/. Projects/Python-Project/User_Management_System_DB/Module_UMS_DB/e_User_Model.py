import mysql.connector

class User_Model:

    connection = mysql.connector.connect(host='localhost',user='root',password='',database='database_1') 
    db_cursor = connection.cursor()
    db_cursor.execute('create table if not exists final_table (User_Id int(100), User_Name varchar(30), First_Name varchar(30), Last_Name varchar(30), Email_Id varchar(30), Password varchar(30))')
    

    def create_user_query(self, user_input_list): 
        sql_insert = 'insert into final_table values(%s,%s,%s,%s,%s,%s)'
        sql_values = user_input_list[0],user_input_list[1],user_input_list[2],user_input_list[3],user_input_list[4],user_input_list[5]
        self.db_cursor.execute(sql_insert,sql_values)
        self.connection.commit()

    def update_user_query(self, user, update_action):

        if update_action == 1:
            new_user_name = input('Enter New user_name : ')
            sql_insert = 'UPDATE final_table SET User_Name = %s WHERE User_Name = %s' 
            sql_value = new_user_name, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

        if update_action == 2:
            new_first_name = input('Enter New first_name : ')
            sql_insert = 'UPDATE final_table SET First_Name = %s WHERE User_Name = %s' 
            sql_value = new_first_name, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

        if update_action == 3:
            new_last_name = input('Enter New last_name : ')
            sql_insert = 'UPDATE final_table SET Last_Name = %s WHERE User_Name = %s' 
            sql_value = new_last_name, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

        if update_action == 4:
            new_email = input('Enter New email : ')
            sql_insert = 'UPDATE final_table SET Email_Id = %s WHERE User_Name = %s' 
            sql_value = new_email, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

        if update_action == 5:
            new_password = input('Enter New password : ')
            sql_insert = 'UPDATE final_table SET Password = %s WHERE User_Name = %s' 
            sql_value = new_password, user
            self.db_cursor.execute(sql_insert,sql_value)
            self.connection.commit()

            
    def delete_user_query(self, delete_user):
        sql_delete = 'DELETE FROM final_table WHERE User_Name = %s'
        sql_value = delete_user,
        self.db_cursor.execute(sql_delete,sql_value)
        self.connection.commit()

    def retrieve_user_query(self, user_retrieve):
        sql_user_retrieve = 'SELECT * FROM final_table WHERE User_Name = %s'
        sql_value = user_retrieve,
        self.db_cursor.execute(sql_user_retrieve, sql_value)
        user_record_row = self.db_cursor.fetchall()
        print(user_record_row)
        for user_detials in user_record_row:
            print('\n')
            print('Id = ',user_detials[0])
            print('Username = ',user_detials[1])
            print('Firstname = ',user_detials[2])
            print('Lastname = ',user_detials[3])
            print('Email_Id = ',user_detials[4])
            print('Password = ',user_detials[5])

    # def retrieve_user_query(self, user_retrieve):
    #     sql_user_retrieve = 'SELECT * FROM table_10 WHERE User_Name = %s'
    #     sql_value = user_retrieve,
    #     self.db_cursor.execute(sql_user_retrieve, sql_value)
    #     user_record = self.db_cursor.fetchall()
    #     print('Id = ',user_record[0][0]) # user_record consist of only one row with user name user_retrieve i.e user_record[0]
    #     print('Username = ',user_record[0][1])
    #     print('Firstname = ',user_record[0][2])
    #     print('Lastname = ',user_record[0][3])
    #     print('Email = ',user_record[0][4])
    #     print('Password = ',user_record[0][5])

    def view_all_users(self):
        self.db_cursor.execute('SELECT * FROM final_table')
        users = self.db_cursor.fetchall()
        for user_record in users:
            print('\n')
            print('Id = ',user_record[0])
            print('Username = ',user_record[1])
            print('Firstname = ',user_record[2])
            print('Lastname = ',user_record[3])
            print('Email_Id = ',user_record[4])
            print('Password = ',user_record[5])
            
        