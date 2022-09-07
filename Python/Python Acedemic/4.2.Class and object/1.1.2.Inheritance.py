# # Python Inheritance:

# # Inheritance allows us to define a class that inherits all the methods and properties from another class.
# # Parent class is the class being inherited from, also called base class.
# # Child class is the class that inherits from another class, also called derived class.

# # Create a Parent Class:
# # Any class can be a parent class, so the syntax is the same as creating any other class:

# #  # 1   
# class Person():
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

#1.1
class Person():
    def __init__(self,name,age,color):
        self.Naam = name
        self.Umer = age
        self.Rang = color
        
    def info(self):
        print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

Person('SimbA',21,'Blue')
print(Person.Naam) # here Naam,Umer,Rang all are inside constructor so we cannot call it as property


# # 1.2
# class Person():
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

# print(Person('SimbA',21,'Blue').Naam) # here Naam,Umer,Rang all are inside constructor so we cannot call it as property



# #2
# class Person():
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

# #Use the Person class to create an object, and then execute the info method:
# obj1=Person('SimbA',21,'Blue')
# obj1.info()



# # Create a Child Class:
# # To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# # Create a class named Student, which will inherit the properties and methods from the Person class:
# class Student(Person):
#     pass
# # Note: Use the pass keyword when


# # 2
# class Person1(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info1(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

# class Student1(Person1): # Child Class
#     pass

# obj1=Student1('SimbA',21,'Blue')
# obj1.info1()


# # 3
# class ParentClass(): #parent_class
#     def method1(self):
#         print('I am method inside ParentClass !')
        
# class ChildClass(ParentClass): #child_class inheritance
#     def method2(self):
#         print('I am method inside ChildClass !')
        
# obj1Child = ChildClass() # object_of_child_class
# print(obj1Child)
# obj1Child.method2() # method of ChildClass #line_1
# obj1Child.method1() # Inherite method of ParentClass #line_2

# # # here we call function/methods of class in line_1 and line_2 when we create object of class
# # # But incase of __init__() function, __init__() function is called automatically every time class is used to create object


# # Add the __init__() Function

# # So far we have created a child class that inherits the properties and methods from its parent.
# # We want to add the __init__() function to the child class (instead of the pass keyword).
# # Note: The __init__() function is called automatically every time the class is being used to create a new object.
# class A:
#     def __init__(self):
#         print('hello')

#     age = 20
# obj1 = A()
# print(A.age)

# # Add the __init__() function to the Student class:

# class Student(Person):
#     def __init__(self, fname, lname):
#     #add properties etc.
    
# # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.


# # # 4
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

# class Student(Person): # Child Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info1(self):
#         self.info()
# obj1=Student('SimbA',21,'Blue') # assign property(name,age,color) to the object(obj1) of class(Student)
# obj1.info() # call method of class(Person) and passing propert(self.Naam,self.Umer,self.Rang) by the object(obj1) of class(Student)
# obj1.info1()



# # 5
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')

# class Student(Person): # Child Class
#     def __init__(self,name,age,color):
#         self.N1 = name
#         self.U1 = age
#         self.R1 = color
        
# obj1=Student('SimbA',21,'Blue') # assign property(name,age,color) to the object(obj1) of class(Student)
# obj1.info() # call method of class(Person) and passing propert(self.N1,self.U1,self.R1) by the object(obj1) of class(Student)


# # # 6
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info1(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')
        
#     def info2(self):
#         print(self.U1,' years old ',self.N1,' has ',self.R1,' hair.')

# class Student(Person): # Child Class
#     def __init__(self,name,age,color):
#         self.N1 = name
#         self.U1 = age
#         self.R1 = color
        
# obj1=Student('SimbA',21,'Blue') # assign property(name,age,color) to the object(obj1) of class(Student)
# obj1.info2() # call methodinfo2() of class(Person) and passing propert(self.N1,self.U1,self.R1) by the object(obj1) of class(Student)


# # 7
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info1(self):
#         print(self.Naam,self.Umer,self.Rang)
        
#     def intro(self,a,b,c):
#         print(a,' years old ',b,' has ',c,' hair.')

# class Student(Person): # Child Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
# obj1=Student('SimbA',21,'Blue') # assign property(name,age,color) to the object(obj1) of class(Student)
# obj1.info1()
# obj1.intro('SimbA',21,'Blue') # ????? call method of class(Person) and passing propert(self.Naam,self.Umer,self.Rang) by the object(obj1) of class(Student)  ans => passing argument 'SimbA',21,'Blue' for a,b,c in intro method


# # In[7]:


# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
#     def info(self):
#         print(self.Naam,' years old ',self.Umer,' has ',self.Rang,' hair.')

# class Student(Person): # Child Class
#     def __init__(self,name,age,color):
#         super().__init__(name,age,color)
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color
        
# obj1=Student('SimbA',21,'Blue') # assign property(name,age,color) to the object(obj1) of class(Student)
# obj1.info() 


# # In[14]:


# class Person(): # Parent Class
#     def __init__(self,Name,Age,Color):
#         self.NAME = Name
#         self.AGE = Age
#         self.COLOR = Color
        
#     def info1(self):
#         print(self.AGE,' years old ',self.NAME,' has ',self.COLOR,' hair.')

# class Student(Person): # Child Class
#     def __init__(self,name,age,color,country,zone):
#         super().__init__(name,age,color)
#         self.desh = country
#         self.anchal = zone
    
#     def info2(self):
#         print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
    
#     def final_info(self):
#         print(self.NAME,' is ',self.AGE,' years old has ',self.COLOR,' hair color and lives in  ',self.desh,' Zone ',self.anchal)
    
# obj1=Student('Hari','27','Black','Nepal',14)
# obj1.info2()
# obj1.info1()
# obj1.final_info()




# #7.1

# class Person(): # Parent Class
#     print('2')
#     def __init__(self,Name,Age,Color):
#         print('4')
#         self.NAME = Name
#         self.AGE = Age
#         self.COLOR = Color
        
#     def info1(self):
#         print('7')
#         print(self.AGE,' years old ',self.NAME,' has ',self.COLOR,' hair.')

# class Student(Person): # Child Class
#     print('1')
#     def __init__(self,name,age,color,country,zone):
#         print('3')
#         super().__init__(name,age,color)
#         print('5')
#         self.desh = country
#         self.anchal = zone
    
#     def info2(self):
#         print('6')
#         print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
    
#     def final_info(self):
#         print('8')
#         print(self.NAME,' is ',self.AGE,' years old has ',self.COLOR,' hair color and lives in  ',self.desh,' Zone ',self.anchal)
    
# print('Main')
# obj1=Student('Hari','27','Black','Nepal',14)
# obj1.info2()
# obj1.info1()
# obj1.final_info()




# # In[8]:


# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         print('Constructor of parent class !')
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color 
#     def info1(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')   
#     def info2(self):
#         print(self.U1,' years old ',self.N1,' has ',self.R1,' hair.')

# class Student1(Person): # Child Class
#     pass  
        
# class Student2(Person): # Child Class
    
#     def __init__(self,name,age,color):
#         print('Constructor of child class !')
#         self.N1 = name
#         self.U1 = age
#         self.R1 = color
    
# class Student3(Person): # Child Class
#     def __init__(self,country,zone):
#         print('Constructor of child class !')
#         self.desh = country
#         self.anchal = zone
#     def info3(self):
#         print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
     
    
# obj1=Person('SimbA',21,'BlacK')
# obj1.info1() # obj1 is created
# obj1 = Student1('SimbA',21,'BlacK')
# obj1.info1()
# print(obj1)
# obj1 = Student2('SimbA',21,'BlacK')
# obj1.info2() # here obj1 is override
# obj1 = Student3('Nepal',14)
# obj1.info3()
# print(obj1)
# # here obj1 is override


# # In[24]:


# # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# class Person:
#     def __init__(self, fname, lname):
#         print('ParentConstructor ==>',fname, lname)
#         self.firstname = fname
#         self.lastname = lname
#         print('Parent_Constructor ==>',self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         print('Child_Constructor ==>',fn, ln)
#         Person.__init__(self, fn, ln) # add a call to the parent's __init__() function
# #         print('ParentConstructor ==>',fname, lname) # error fname is attriburte of parent class only
#         print('Parent_Constructor ==>',self.firstname, self.lastname)
#         print('Child_Constructor ==>',fn, ln)


        
# x = Student("Mike", "Olsen")


# # # Now we have successfully added the __init__() function, and kept the inheritance of the parent class, 
# # # and we are ready to add functionality in the __init__() function.


# # In[16]:


# # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     a=2
#     def printname1(self):
#         print('Parent const : ',self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         Person.__init__(self, fn, ln) # add a call to the parent's __init__() function
#         self.one = fn
#         self.two = ln
#     def printname2(self):
#         print('Child const : ',self.one, self.two)
        
#     def printname3(self):
#         print('Child const : ',self.one, self.two)
#         print('Parent const : ',self.firstname, self.lastname)
#         print('Parent const and Child const : ',self.one, self.lastname,self.a)
#         #here a is class variable and self.lastname is instant variable
# x = Student("Mike", "Olsen")
# x.printname1() # x is object of child class(Student)  and methd(printname1()) is is of parent class(Person)
# x.printname2() # x is object of child class(Student)  and methd(printname1()) is is of child class(Student)
# x.printname3()

# # Now we have successfully added the __init__() function, and kept the inheritance of the parent class, 
# # and we are ready to add functionality in the __init__() function.


# # In[17]:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     global a
#     a=2
#     def printname1(self):
#         print('Parent const : ',self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         Person.__init__(self, fn, ln) # add a call to the parent's __init__() function
#         self.one = fn
#         self.two = ln
#     def printname2(self):
#         print('Child const : ',self.one, self.two)
        
#     def printname3(self):
#         print('Child const : ',self.one, self.two)
#         print('Parent const : ',self.firstname, self.lastname)
#         print('Parent const and Child const : ',self.one, self.lastname,a)
#         #here a is class variable and self.lastname is instant variable
# x = Student("Mike", "Olsen")
# x.printname1() # x is object of child class(Student)  and methd(printname1()) is is of parent class(Person)
# x.printname2() # x is object of child class(Student)  and methd(printname2()) is is of child class(Student)
# x.printname3()

# # In[22]:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         self.apple = fn
#         self.ball = ln

# x = Student("Mike", "Olsen")
# x.printname()


# # In[24]:



# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         super().__init__(fn, ln)
#         self.apple = fn
#         self.ball = ln

# x = Student("Mike", "Olsen")
# x.printname()


# # In[25]:



# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname1(self):
#         print('Parent : ',self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         Person.__init__(self,fn, ln)
#         self.apple = fn
#         self.ball = ln

#     def printname2(self):
#         print('Child : ',self.apple, self.ball)
        
# x = Student("Mike", "Olsen")
# x.printname1()
# x.printname2()

# # here -----
# # fname, lname ==> parameter of parent_constructor
# # fn, ln ==> parameter of child_constructor
# # self.firstname, self.lastname ==> instant_object.variable of parent_constructor
# # self.apple, self.ball ==> instant_object.variable of child_constructor


# # In[44]:


# # Use the super() Function:
# # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fn, ln):
#         super().__init__(fn, ln)

# x = Student("Mike", "Olsen")
# x.printname()

# # By using the super() function, you do not have to use the name of the parent element, 
# # it will automatically inherit the methods and properties from its parent.

# # Parent.__init__(self,arg1, arg2)
# # super().__init__(arg1, arg2)


# # In[45]:


# # Add Properties:
# # Add a property called graduationyear to the Student class:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.graduationyear = 2019

# x = Student("Mike", "Olsen")
# print(x.graduationyear)

# # In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. 
# # To do so, add another parameter in the __init__() function:


# # In[50]:


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname,graduationyear):
#         super().__init__(fname, lname)
#         print(graduationyear)

# x = Student("Mike", "Olsen",2019)


# # In[17]:


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname,graduationyear):
#         super().__init__(fname, lname)
#         print(graduationyear)
#         self.GradYear = graduationyear

# x = Student("Mike", "Olsen",2019)
# print(x.GradYear)
# print(x.GradYear) 


# # In[18]:


# # Add a year parameter, and pass the correct year when creating objects:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)


# # In[55]:


# # Add Methods 1:
# # Add a method called welcome to the Student class:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()


# # If you add a method in the child class with the same name as a function in the parent class, 
# # the inheritance of the parent method will be overridden.


# # In[57]:


# # Add Methods 2:
# # Add a method called welcome to the Student class:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, f_name, l_name, year):
#         super().__init__(l_name, l_name)
#         self.fn =f_name
#         self.ln =l_name
#         self.graduationyear = year
# # note here we are again initializing first_name(self.fn) and last_name(self.ln) in child_class 
# # which is already initialized in parent_class so its waste of time memory so Add Methods 1  is better
#     def welcome(self):
#         print("Welcome", self.fn, self.ln, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()


# # In[22]:


# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color 
#     def info1(self):
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.')   
#     def info2(self):
#         print(self.U1,' years old ',self.N1,' has ',self.R1,' hair.')

# class Student1(Person): # Child Class
#     pass  
        
# class Student2(Person): # Child Class
#     def __init__(self,name,age,color):
#         self.N1 = name
#         self.U1 = age
#         self.R1 = color
    
# class Student3(Person): # Child Class
#     def __init__(self,country,zone):
#         self.desh = country
#         self.anchal = zone
#     def info3(self):
#         print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
    
# class Student4(Person): # Child Class
#     def __init__(self,country,zone):
#         self.desh = country
#         self.anchal = zone
#     def info4(self):
#         print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.') 
#     #here crontructor of parent is not inheritaed
    
# # class Student4(Person): # Child Class
# #     def __init__(self,name,age,color,country,zone):
# #         super().__init__(name,age,color)
# #         self.desh = country
# #         self.anchal = zone
# #     def info4(self):
# #         print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
# #         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.') 
# # try this
    
    
# obj1=Person('SimbA',21,'BlacK')
# obj1.info1()
# obj1 = Student1('SimbA',21,'BlacK')
# obj1.info1()
# obj1 = Student2('SimbA',21,'BlacK')
# obj1.info2()
# obj1 = Student3('Nepal',14)
# obj1.info3()
# obj1 = Student4('Japan',33)
# # obj1 = Student4('SimbA',21,'BlacK','Japan',33)  # try
# obj1.info4()


# # In[69]:


# #solution 
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color 

# class Student4(Person): # Child Class
#     def __init__(self,country,zone,name,age,color):
#         super().__init__(name,age,color)
#         self.desh = country
#         self.anchal = zone
#     def info4(self):
#         print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.') 
        
    
    

# obj1 = Student4('Japan',33,'zingPing',100,'Brown')
# obj1.info4()


# # In[72]:


# #also
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color 

# class Student4(Person): # Child Class
#     def __init__(self,country,zone,name,age,color):
#         super().__init__(name,age,color)
#         self.desh = country
#         self.anchal = zone
#     def info4(self):
#         print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.') 
        
    
    

# obj1 = Student4(country='Japan',zone=33,name='zingPing',age=100,color='Brown')
# obj1.info4()

# #initializeing both parent constructor and child constrictor


# # In[75]:


# #also
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color 

# class Student4(Person): # Child Class
#     def __init__(self,country,name,age,color):
#         super().__init__(name,age,color)
#         self.desh = country
#     def info4(self):
#         print('Country ==> ',self.desh)
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.') 
        
    
    

# obj1 = Student4(country='Japan',name='zingPing',age=100,color='Brown')
# obj1.info4()

# #initializeing both parent constructor and child constrictor


# # In[77]:


# #also
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color 

# class Student4(Person): # Child Class
#     def __init__(self,country,age,name,color):
#         super().__init__(name,age,color)
#         self.desh = country
#     def info4(self):
#         print('Country ==> ',self.desh)
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.') 
        
    
    

# obj1 = Student4(country='Japan',name='zingPing',age=100,color='Brown')
# obj1.info4()

# #initializeing both parent constructor and child constrictor


# # In[79]:


# #also
# class Person(): # Parent Class
#     def __init__(self,name,age,color):
#         self.Naam = name
#         self.Umer = age
#         self.Rang = color 

# class Student4(Person): # Child Class
#     def __init__(self,country,age,name,color):
#         super().__init__(name,age,color)
#         self.desh = country
#     def info4(self):
#         print('Country ==> ',self.desh)
#         print(self.Umer,' years old ',self.Naam,' has ',self.Rang,' hair.') 
        
    
    

# obj1 = Student4('Japan','zingPing',100,'Brown') # its not good
# obj1.info4()

# #initializeing both parent constructor and child constrictor

