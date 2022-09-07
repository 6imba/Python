# class A:
#      value1=20 #class_variable
# print(A.value1) #calling class_variable










# class B:
    
#     def value2(self): # regular_class_instant_method #  # instant_method # to use this method firstly u have to create instant
#         return 30
    
# B.value2() #calling regular_class_instant_method

# # SOLUTION

# # class B:
    
# #     def value2(self): # regular_class_instant_method
# #         return 30

# # obj1 = B()
# # obj1.value2() #calling regular_class_instant_method















# class C:
    
#     @classmethod #DEFINE class_method
#     def method3(cls): #class_method
#         return 30

# C.method3() #calling class_method














# class D:
#     value1=10 #class_variable
    
# #     def method2(self): # regular_class_instant_method
# #         return 20
    
#     @classmethod #DEFINE class_method
#     def method3(cls): # class_method
#         return 30
    
# print(D.value1) #calling class_variable

# # D.method2() #calling regular_class_instant_method

# D.method3() #calling class_method



# # # regular_class_instant_method
# # def method2(self): #self needed
    
# # # class_method
# # @classmethod
# # def method3(cls): #self not needed














# class D:
#     value1=10 #class_variable
    
#     def method2(self): # regular_class_instant_method # to use this method firstly u have to create instant 
#         print(20)
    
#     @classmethod #DEFINE class_method
#     def method3(cls): # class_method
#          return 30
    
# print(D.value1) #calling class_variable

# objD = D()
# objD.method2() #calling regular_class_instant_method

# D.method3() #calling class_method



# # # regular_class_instant_method
# # def method2(self): #self needed
    
# # # class_method
# # @classmethod
# # def method3(cls): #self not needed














# class Office:
#     salary=45000
    
# print('Class_Variable = ',Office.salary)

# staff_1 = Office()
# print('Instant_Variable = ',staff_1.salary)
# staff_1.salary = 55000 # change instant_variable(staff_1.salary) but class_variable(salary) remain same
# print('Instant_Variable = ',staff_2.salary)

# print('Class_Variable = ',Office.salary)













# class Office1:
    
#     raise_amount = 7000
    
#     def final_salary_1(self,amount_1):
#         self.salary = amount_1 + Office1.raise_amount
#         print(self.salary)
        
#     def final_salary_2(self,amount_2):
#         Office1.raise_amount = 5000
#         self.salary = amount_2 + Office1.raise_amount
#         print(self.salary)
        
    
# staff_1 = Office1()    
# staff_1.final_salary_1(25000)

# staff_2 = Office1()    
# staff_2.final_salary_2(25000)

# print(Office1.raise_amount)














# class Office_7:
#     raise_sal =7000
    
# staf_1 = Office_7()    
# print(staf_1.raise_sal)
    


















# class Office_7:
#     raise_sal =7000
    
#     def regular_raise_sal(self,amount):
#         self.raise_sal=amount
#         print()
    
#     @classmethod
#     def increase(cls,amount):
#         cls.raise_sal=amount
    
# print(Office_7.raise_sal)
    
# staf_1 = Office_7()    
# print(staf_1.raise_sal)

# staf_1.regular_raise_sal(14000)
# print(staf_1.raise_sal)
# print(Office_7.raise_sal)

# Office_7.increase(21000)
# print(Office_7.raise_sal)














# # regular_method in class automatically takes instances as its first argument i.e { def regular_method(self) }
# # so if regular_method in class automatically takes instances as its first argument , how can we change so that it takes class 
# # as its first argument , so now to do that we use class method { @classmethod  def class_method(cls) } cls represent current class
# # { @classmethod  def class_method(cls) } cls represent current class so now we are working with class instead of instance

