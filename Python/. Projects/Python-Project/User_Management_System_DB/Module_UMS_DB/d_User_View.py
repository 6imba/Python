from e_User_Model import User_Model
        
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
        import random
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