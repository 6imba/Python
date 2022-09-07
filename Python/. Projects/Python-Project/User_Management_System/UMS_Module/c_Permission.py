from d_View import User_View

class Permissions_Module(User_View):

    def admin_role(self):
        while True:

            super().view_menu_for_admin()

            choose_action = int(input("Enter Here:"))
           
            while choose_action > 6 or choose_action < 1:
                choose_action = int(input("Enter only form 1 to 5:")) 

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
            
            while choose_action > 3 or choose_action < 1:
                choose_action = int(input("Enter only form 1 to 3:")) 
                
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



