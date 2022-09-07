from c_Permission_Model import Permissions_Module

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
