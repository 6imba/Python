from c_Permission import Permissions_Module

class Role_Model(Permissions_Module):

    def choose_role(self): # self == obj_for_role
        while True:
            print("""
            Enter number to choose the following role:
            1. Admin
            2. User
            """)
            user_role = int(input("Enter Here:"))
            if user_role == 1:
                super().admin_role() # super() = self == obj_for_role
            else:
                super().user_role()

            answer = str(input("Type c to close Enter to continue :"))
            if answer == "c":
                break
