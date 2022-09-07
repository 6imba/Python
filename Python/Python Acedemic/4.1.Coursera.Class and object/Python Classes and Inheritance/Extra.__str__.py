#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Person:
    def __init__(self,name,year_born):
        self.name=name
        self.year_born=year_born
    
    def __str__(self): 
        return '{} is {} years old.'.format( self.name , self.year_born )
    
person_1 = Person('Ram',22)
print(person_1) # when ever we print object it automatically calls str method


# In[10]:


Current_Year = 2020
class Person:
    def __init__(self,name,year_born):
        self.name=name
        self.year_born=year_born
    
    def getAge(self):
        return Current_Year - self.year_born
    
    def __str__(self): 
        return '{} is {} years old.'.format( self.name , self.getAge() )
    
person_1 = Person('Ram',1999)
print(person_1) # when ever we print object it calls str method 
    
    
    


# In[13]:


# class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
# class Child:
    
# # Child(Parent) => inherit methods and property of Parent only
# # Parent.__init__(self,a,b) => inherit constructor of Parent only
# # super().__init__(a,b) => inherit both methods_property and constructor of Parent 


# In[46]:


class Person(): # Parent Class
    def __init__(self,Name,Age,Color):
        self.NAME = Name
        self.AGE = Age
        self.COLOR = Color
        
    def info1(self):
        print(self.AGE,' years old ',self.NAME,' has ',self.COLOR,' hair.')

class Student(Person): # Child Class
    def __init__(self,name,age,color,country,zone):
        super().__init__(name,age,color)
        self.desh = country
        self.anchal = zone
    
    def info2(self):
        print('Country ==> ',self.desh,' Zone ==> ',self.anchal)
    
    def final_info(self):
        print('Name ==> ',self.NAME,' is ',self.AGE,' years old has ',self.COLOR,' hair color and lives in  ',self.desh,' Zone ',self.anchal)
    
obj1=Student('Hari','27','Black','Nepal',14)
obj1.info2()
obj1.info1()
obj1.final_info()

