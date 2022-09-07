
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
        
