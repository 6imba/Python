# #!/usr/bin/env python
# # coding: utf-8

# # In[1]:


# # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         Person.__init__(self, fn, ln) # add a call to the parent's __init__() function

# x = Student("Mike", "Olsen")
# x.printname()

# # Now we have successfully added the __init__() function, and kept the inheritance of the parent class, 
# # and we are ready to add functionality in the __init__() function.


# # In[2]:


# class Person:

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         self.firstname = fn
#         self.lastname = ln

# x = Student("Mike", "Olsen")
# x.printname()


# # In[7]:


# class A:
#     def __init__(self):
#         print('I am Parent Constructor !')
# class B(A):
#     def __init__(self):
#         print('I am Child Constructor !')
        
# obj2=B()


# # In[11]:


# class A:
#     def __init__(self):
#         print('I am Parent Constructor !')
# class B(A):
#     def __init__(self):
#         A.__init__(self) #  what is puropse of calling constructor of bothg parentclass and child class
#         print('I am Child Constructor !')
        
# obj2=B()


# # In[18]:


# class A:
#     def __init__(self):
#         print('I am Parent Constructor !')
# class B(A):
#     def __init__(self):
#         super().__init__() #calling parent class constructor  # no_self
#         print('I am Child Constructor !')
        
# obj2=B()


# # In[22]:


# class A:
#     def __init__(self):
#         self.parentvar=1000
#         print('I am Parent Constructor !')
# class B(A):
#     def __init__(self):
#         super().__init__() #calling parent class constructor  # no_self
#         print('I am Child Constructor !')
        
#     def output(self):
#         print('Calling parent property from child : ',self.parentvar)
        
# obj2=B()
# obj2.output()


# # In[29]:


# class A:
#     def __init__(self,xxx):
#         self.parentvar=xxx
#         print('I am Parent Constructor !')
# class B(A):
#     def __init__(self,ooo):
#         super().__init__(ooo) #calling parent class constructor  # no_self
#         print('I am Child Constructor !')
        
#     def output(self):
#         print('Calling parent property from child : ',self.parentvar)
        
# obj2=B(1000)
# obj2.output()


# # In[31]:


# class A:
#     def __init__(self,xxx):
#         self.parentvar=xxx
#         print('I am Parent Constructor !')
# class B(A):
#     def __init__(self,xxx,ttt):
#         super().__init__(xxx) #calling parent class constructor  # no_self
#         self.childvar=ttt
#         print('I am Child Constructor !')
        
#     def output(self):
#         print('Calling parent property from child : ',self.parentvar,self.childvar)
        
# obj2=B(1000,500000)
# obj2.output()

