import random


class User_Model:

    users_database = []

    def create_user_query(self, user_input_dictionary): 
        print('create_user_query ==> append into database')
        self.users_database.append(user_input_dictionary)
            
    def update_user_query(self, update_info):
        
        if update_info == 1:
            user_name = str(input("Enter your User Name:"))
            for dictionaries in self.users_database:
                for key, value in dictionaries.items():
                    if key == "User Name" and value == user_name:
                        updated_user_name = str(input("Enter new user name to update:"))
                        updated_dictionary = {"User Name": updated_user_name}
                        dictionaries.update(updated_dictionary)
                        print("Successful Updated")
                        
        elif update_info == 2:
            user_name = str(input("Enter your User Name:"))
            for dictionaries in self.users_database:
                for key, value in dictionaries.items():
                    if key == "User Name" and value == user_name:
                        updated_first_name = str(input("Enter new first name to update:"))
                        updated_dictionary = {"First Name": updated_first_name}
                        dictionaries.update(updated_dictionary)
                        print("Successful Updated")
                        
        elif update_info == 3:
            user_name = str(input("Enter your User Name:"))
            for dictionaries in self.users_database:
                for key, value in dictionaries.items():
                    if key == "User Name" and value == user_name:
                        updated_last_name = str(input("Enter new last name to update:"))
                        updated_dictionary = {"Last Name": updated_last_name}
                        dictionaries.update(updated_dictionary)
                        print("Successful Updated")
                        
        elif update_info == 4:
            user_name = str(input("Enter your User Name:"))
            for dictionaries in self.users_database:
                for key, value in dictionaries.items():
                    if key == "User Name" and value == user_name:
                        updated_email = str(input("Enter new email to update:"))
                        updated_dictionary = {"Email Id": updated_email}
                        dictionaries.update(updated_dictionary)
                        print("Successful Updated")
                        
        elif update_info == 5:
            user_name = str(input("Enter your User Name:"))
            for dictionaries in self.users_database:
                for key, value in dictionaries.items():
                    if key == "User Name" and value == user_name:
                        updated_password = str(input("Enter new password to update:"))
                        updated_dictionary = {"Password": updated_password}
                        dictionaries.update(updated_dictionary)
                        print("Successful Updated")
                        
        else:
            print("Enter number from 1 to 4")

            
    def delete_user_query(self, delete_user):
        for dictionary in self.users_database:
            if dictionary["User Name"] == delete_user:
                print(dictionary) # print dictionary which consist the given user_name
                dict_index = self.users_database.index(dictionary) # identify the index of the current dictionary in list (users_database)
                del self.users_database[dict_index] # delete the value(dictionary) in the given index(dict_index) of list(users_database)
                print("Successful User Deleted")
                break
             
    def retrieve_user_query(self, show_your_info):
        for dictionaries in self.users_database:
            for key, value in dictionaries.items():
                if key == "User Name" and value == show_your_info:
                    print(dictionaries)
   

    def view_all_users(self):
        print(self.users_database)
        
        
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
            
        user_input_dictionary = {
        "User Id": user_id1,
        "User Name": user_name,
        "First Name": first_name,
        "Last Name": last_name,
        "Email Id": email_id,
        "Password": password}
        super().create_user_query(user_input_dictionary)

    def view_update(self):
            print("""
             Enter the following number to Update the information:
             1. Update User Name
             2. Update First Name
             3. Update Last Name
             4. Update Email Id
             5. Update Password              
             """)
            update_info = int(input("Enter number here:"))
            super().update_user_query(update_info)

    def view_delete(self):
            delete_user = input("Enter the User_Name that you want to delete : ")
            super().delete_user_query(delete_user)

    def view_retrieve(self):
            show_your_info = str(input("Enter your user name to retrieve your information:"))
            super().retrieve_user_query(show_your_info)

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
