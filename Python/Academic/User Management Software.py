import random


class User_Model:
    # User Model
    """ Where every logic is written and database is maintained."""

    # This is a list a.k.a a main database where dictionary in added. In each dictionary, there is the information of user.
    users_database = []

    def create_user_query(self, user_input):

        # creating a method so that user can create their id.
        self.user_id1 = random.randrange(1000)
        self.user_id1 = self.user_id1
        self.user_name = user_input[0]
        self.firstname = user_input[1]
        self.lastname = user_input[2]
        self.email = user_input[3]
        self.password = user_input[4]

        # Database
        creat_dictionary = {
            "User Id": self.user_id1,
            "User Name": self.user_name,
            "First Name": self.firstname,
            "Last Name": self.lastname,
            "Email Id": self.email,
            "Password": self.password
        }

        # Adding to the list.
        self.users_database.append(creat_dictionary)

    def add_user_query(self, add_info):
        # Creating a method where user can add.
        if add_info == 1:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.add_first_name = str(input("Enter first name to add:"))
                        add_dictionary = {"First Name": self.add_first_name}
                        self.dictionaries.update(add_dictionary)
                        print("Successful Added")
        elif add_info == 2:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.add_last_name = str(input("Enter last name to add:"))
                        add_dictionary = {"Last Name": self.add_last_name}
                        self.dictionaries.update(add_dictionary)
                        print("Successful Added")
        elif add_info == 3:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.add_email = str(input("Enter email id to add:"))
                        add_dictionary = {"Email Id": self.add_email}
                        self.dictionaries.update(add_dictionary)
                        print("Successful Added")
        elif add_info == 4:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.add_password = str(input("Enter password to add:"))
                        add_dictionary = {"First Name": self.add_password}
                        self.dictionaries.update(add_dictionary)
                        print("Successful Added")
        else:
            print("Enter number from 1 to 4")

    def update_user_query(self, update_info):
        # Creating a method where user can update their information.
        if update_info == 1:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.updated_user_name = str(input("Enter new user name to update:"))
                        updated_dictionary = {"User Name": self.updated_user_name}
                        self.dictionaries.update(updated_dictionary)
                        print("Successful Updated")
        elif update_info == 2:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.updated_first_name = str(input("Enter new first name to update:"))
                        updated_dictionary = {"First Name": self.updated_first_name}
                        self.dictionaries.update(updated_dictionary)
                        print("Successful Updated")
        elif update_info == 3:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.updated_last_name = str(input("Enter new last name to update:"))
                        updated_dictionary = {"Last Name": self.updated_last_name}
                        self.dictionaries.update(updated_dictionary)
                        print("Successful Updated")
        elif update_info == 4:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.updated_email = str(input("Enter new email to update:"))
                        updated_dictionary = {"Email Id": self.updated_email}
                        self.dictionaries.update(updated_dictionary)
                        print("Successful Updated")
        elif update_info == 5:
            self.user_name = str(input("Enter your User Name:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "User Name" and self.value == self.user_name:
                        self.updated_password = str(input("Enter new password to update:"))
                        updated_dictionary = {"Password": self.updated_password}
                        self.dictionaries.update(updated_dictionary)
                        print("Successful Updated")
        else:
            print("Enter number from 1 to 4")

    def delete_user_query(self, delete_info):
        # creating a delete method so that users can delete their information.
        if delete_info == 1:
            self.first_name = str(input("Enter your First Name to delete:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "First Name" and self.value == self.first_name:
                        del self.dictionaries["First Name"]
                        print("Successful Deleted")
                        break
        elif delete_info == 2:
            self.lastname = str(input("Enter your Last Name to delete:"))
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "Last Name" and self.value == self.lastname:
                        del self.dictionaries["Last Name"]
                        print("Successful Deleted")
                        break
        elif delete_info == 3:
            self.email = input("Enter your Email to delete:")
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "Email Id" and self.value == self.email:
                        del self.dictionaries["Email Id"]
                        print("Successful Deleted")
                        break
        elif delete_info == 4:
            self.password = input("Enter your password to delete:")
            for self.dictionaries in self.users_database:
                for self.key, self.value in self.dictionaries.items():
                    if self.key == "Password" and self.value == self.password:
                        del self.dictionaries["Password"]
                        print("Successful Deleted")
                        break
        else:
            print("Enter number from 1 to 4")

    def retrieve_user_query(self, show_your_info):
        # creating a method so that users can retrieve their information and see.
        for self.dictionaries in self.users_database:
            for self.key, self.value in self.dictionaries.items():
                if self.key == "User Name" and self.value == show_your_info:
                    print(self.dictionaries)

    def view_all_users(self):
        print(self.users_database)


class User_View(User_Model):

    # creating a class user view to show the function to the users so that they can take action on it.

    def view_menu_for_admin(self):
        print("""
        Menus
        Enter number 1 to 6 to do the following task:
        1. Create User
        2. Add User
        3. Update User
        4. Delete User 
        5. Retrieve User
        6. View All Users
        """)

    def view_menu_for_user(self):
        print("""
        Menus
        Enter number 1 to 5 to do the following task:
        1. Create User
        2. Add User
        3. Update User
        4. Retrieve User
        """)

    def view_create(self):
            user_name = str(input("Enter your user name:"))
            first_name = str(input("Enter your first name:"))
            last_name = str(input("Enter your last name:"))
            email_id = input("Enter your email id:")
            password = input("Enter your password:")
            user_input = [user_name, first_name, last_name, email_id, password]
            super().create_user_query(user_input)

    def view_add(self):
            print("""
            Enter the following number to add the information:            
            1. Add First Name
            2. Add Last Name
            3. Add Email Id
            4. Add Password
            """)
            add_info = int(input("Enter number here:"))
            super().add_user_query(add_info)

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
            print("""
                Enter the following number to delete the  information:
                1. Delete First Name
                2. Delete Last Name
                3. Delete Email Id
                4. Delete Password
                """)
            delete_info = int(input("Enter number here:"))
            super().delete_user_query(delete_info)

    def view_retrieve(self):
            # RetrieveUser from database
            show_your_info = str(input("Enter your user name to retrieve your information:"))
            super().retrieve_user_query(show_your_info)

    def view_all_user(self):
            # view all data
            super().view_all_users()


class User_Controller(User_View):
    # User Controller

    def menu_admin_controller(self):
        super().view_menu_for_admin()

    def menu_user_controller(self):
        super().view_menu_for_user()

    def create_user_controller(self):
        super().view_create()

    def add_user_controller(self):
        super().view_add()

    def update_user_controller(self):
        super().view_update()

    def delete_user_controller(self):
        super().view_delete()

    def retrieve_userv(self):
        super().view_retrieve()

    def view_all_controller(self):
        super().view_all_user()




class Permissions_Module(User_Controller):

    # creating a class permission module so that we can give access to the users
    def admin_role(self):
        while True:

            super().menu_admin_controller()

            choose_action = int(input("Enter Here:"))
            while True:
                if choose_action > 6 and choose_action < 1:
                    choose_action = int(input("Enter only form 1 to 6:"))
                break

            if choose_action == 1:

                super().create_user_controller()

            elif choose_action == 2:

                super().add_user_controller()

            elif choose_action == 3:

                super().update_user_controller()

            elif choose_action == 4:

                super().delete_user_controller()

            elif choose_action == 5:

                super().retrieve_userv()

            else:
                super().view_all_controller()

            answer = str(input("Enter to continue or type c to close:"))
            if answer == "c":
                break


    def user_role(self):

        while True:
            super().menu_user_controller()

            choose_action = int(input("Enter Here:"))
            while True:
                if choose_action > 4 and choose_action < 1:
                    choose_action = int(input("Enter only form 1 to 4:"))
                break
            if choose_action == 1:
                super().create_user_controller()
            elif choose_action == 2:
                super().add_user_controller()
            elif choose_action == 3:
                super().update_user_controller()
            else:
                super().retrieve_userv()

            answer = str(input("Enter to continue or type c to close:"))
            if answer == "c":
                break




class Role_Model(Permissions_Module):

    # creating a class so that we can assign roll for the users.

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

