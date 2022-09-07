# #!/usr/bin/env python
# # coding: utf-8

# # In[11]:


# # Python Classes/Objects

# # Python is an object oriented programming language.
# # Almost everything in Python is an object, with its properties and methods.
# # A Class is like an object constructor, or a "blueprint" for creating objects.


# # In[7]:


# # Create a Class
# # To create a class, use the keyword class:

# class ClassName : 
#     property1 = 'red'
# print(ClassName)

# # Create a class named ClassName, with a property named property1:


# # In[9]:


# class FirstClass: #create class named as FirstClass
#     age = 21 # property of class
# print(FirstClass)


# # In[1]:


# # Create Object
# # Now we can use the class named FirstClass to create objects:
# class FirstClass:
#         age =21
# object1 = FirstClass.age # Create Object(object1) and assign value of property(age) present inside class(FirstClass) to it(object1)
# print(object1)


# # In[3]:


# class FirstClass:
#         age =21
# object1 = FirstClass 
# print(object1)
# print(object1.age)


# # In[18]:


# # The __init__() Function

# # The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# # To understand the meaning of classes we have to understand the built-in __init__() function.
# # All classes have a function called __init__(), which is always executed when the class is being initiated.
# # Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
    
# class FirstClass:
#     def __init__(self,age,color):
#         self.umer = age
#         self.rang = color
    
# obj1 = FirstClass(21,'Red')
# print(obj1)
# print(obj1.umer)
# print(obj1.rang)

# # Note: The __init__() function is called automatically every time the class is being used to create a new object.
# # so you can suppose or it is the constructor


# # In[24]:


# # Object Methods
# # Objects can also contain methods. Methods in objects are functions that belong to the object.

# class FirstClass:
#     def __init__(self,age,color): # property
#         self.umer=age
#         self.rang=color
#     def MethodClass (self): # method
#         print('Person with age ',self.umer,' is ',self.rang,' in color.')
        
# obj1=FirstClass(21,'Blue') #object class to constructor
# obj1.MethodClass() # object call method


# # In[27]:


# # Let us create a method,property in the Person class and object:

# class Person():
#     def __init__(self,name,age,color): # Constructor
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

# obj1=Person('SimbA',21,'Blue')
# obj1.info()


# # In[1]:


# # Extra
# class Person():
#     def __init__(self,name,age,color): # Constructor
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

# obj1=Person('SimbA',21,'Blue')
# obj2.info() # error obj1 is defined but obj2 is not


# # In[5]:


# # The self Parameter:
# # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# class Aaaa:
#     def __init__(apple,name):
#         apple.naam=name
# obj1=Aaaa('Ram')
# print(obj1.naam)


# # In[39]:


# # Modify Object Properties
# # You can modify properties on objects like this:

# class Aaaa:
#     def __init__(apple,name):
#         apple.naam=name
# obj1=Aaaa('Ram')
# print(obj1.naam)

# obj1.naam='Shyam' # Modify Object Properties
# print(obj1.naam)


# # In[6]:


# # Delete Objects
# # You can delete objects by using the del keyword:

# class Aaaa:
#     def __init__(apple,name):
#         apple.naam=name
# obj1=Aaaa('Ram')
# print(obj1.naam)

# del obj1 # Delete Object
# print(obj1.naam)


# # In[48]:


# # The pass Statement
# # class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# class Person:

# obj1 = Person
# print(obj1)
# # having an empty class definition like this, would raise an error without the pass statement


# # In[1]:


# # The pass Statement
# # class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# class Person:
#     pass

# obj1 = Person
# print(obj1)


# # In[3]:


# class User_Model():
#     def __init__(self,ids):
#         self.user_id = ids
#     print(self.user_id) # self.user_id is a local variable inside method
        
# User_Id=input('Enter your User_Id : ')
# obj1=User_Model(User_Id)


# # In[6]:


# class User_Model():
#     ii = 0
#     def __init__(self,ids):
#         self.user_id = ids
#         ii = self.user_id
#     print(ii) # self.user_id is a local variable inside method
        
# User_Id=input('Enter your User_Id : ')
# obj1=User_Model(User_Id)


# # In[8]:


# User_Id=input('Enter your User_Id : ')

# class User_Model():
#     ii = 0
#     def __init__(self,ids):
#         self.user_id = ids
#         ii = self.user_id
#     print(ii) # self.user_id is a local variable inside method
        
# obj1=User_Model(User_Id)


# # In[10]:


# User_Id=input('Enter your User_Id : ')
# obj1=User_Model(User_Id)

# class User_Model():
#     ii = 0
#     def __init__(self,ids):
#         self.user_id = ids
#         ii = self.user_id
#     print(ii) # self.user_id is a local variable inside method


# # In[13]:


# User_Id=input('Enter your User_Id : ')
# obj1=User_Model(User_Id)

# class User_Model():
#     ii = 0
#     def __init__(self,ids):
#         self.user_id = ids
#         ii = ids
#     print(ii) # self.user_id is a local variable inside method


# # In[14]:


class User_Model():
    def __init__(self,ids):
        self.user_id = ids
        print(self.user_id)
        
User_Id=input('Enter your User_Id : ')
obj1=User_Model(User_Id)

