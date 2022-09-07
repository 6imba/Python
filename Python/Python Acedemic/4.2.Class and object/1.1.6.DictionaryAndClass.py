# #1
# class User_Model():
#     user_dict = {}
#     def prints(self):
#         print(user_dict)

# obj1=User_Model()
# obj1.prints()


# # 2
# class User_Model():
#     user_dictionary = {}    
#     def prints(self):
#         print(self.user_dictionary)

# obj1=User_Model()
# obj1.prints()


# # 3
# class User_Model():    
#     def prints(self):
#         print(user_dictionary)
    
# user_dictionary = {}
# obj1=User_Model()
# obj1.prints()


# 4
# class User_Model():
#     def __init__(self):
#         user_dictiona = {'a':1,'b':2,'c':3}  
#     def prints(self):
#         print(user_dictiona)

# obj1=User_Model()
# obj1.prints()


# # 5
# class User_Model():
#     def __init__(self):
#         self.user_diction = {'a':1,'b':2,'c':3}
            
#     def prints(self):
#         print(user_diction)

# obj1=User_Model()
# obj1.prints()


# # 6
# class User_Model():
#     def __init__(self):
#         user_diction = {'a':1,'b':2,'c':3}
            
#     def prints(self):
#         print(self.user_diction)

# obj1=User_Model()
# obj1.prints()


# # 7
# class User_Model():
#     def __init__(self):
#         self.user_diction = {'a':1,'b':2,'c':3}
            
#     def prints(self):
#         print(self.user_diction)

# obj1=User_Model()
# obj1.prints()


# # 8
# class A():
#     def __init__(self):
#         self.diction = {'name':'Amir'}
        
# class B(A): # here class A() is called so its constructor is initialized
#     def output(self):
#         print(self.diction) # as constructor of A() is initialized we can use self.diction
    
# obj1=B()
# obj1.output()


# 9
# class A():
#     def __init__(self):
#         self.diction = {'name':'Amir'}
        
# class B(A):
#     def __init__(self):
#         super().__init__()
    
#     def output(self):
#         d={'name':'mir'}
#         print(self.diction.update(d))
    
# obj1=B()
# obj1.output()

# # 9.1
# class A():
#     def __init__(self):
#         self.diction = {'name':'Amir'}
        
# class B(A):
#     def __init__(self):
#         super().__init__()
    
#     def output(self):
#         d={'name':'Rima'}
#         print(self.diction)
#         print(self.diction.update(d))
#         print(self.diction)
    
# obj1=B()
# obj1.output()



# # 10
# class A():
#     def __init__(self):
#         self.diction = {'name':'Amir'}
#         print(self.diction)
        
#     def name(self):
#         print('IamHuman!')
        
# class B(A):
#     pass
    
# obj2=B()
# obj2.name()


# # 11
class A():
    def __init__(self):
        self.diction = {'name':'Amir'}
        print(self.diction)
        
    def name(self):
        word='IamHuman!'
        print(word)
        
class B(A):
    def __init__(self):
        super().__init__()
    
    
obj2=B()
obj2.name()

