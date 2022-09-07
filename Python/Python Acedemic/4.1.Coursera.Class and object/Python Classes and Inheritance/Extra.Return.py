#!/usr/bin/env python
# coding: utf-8

# In[26]:


#return doesnt take muliple operator
def add():
    a=10 
    return a += 5

print(add())

#return doesnt take muliple operator
# def add():
#     a=10 
#     return a = a+5

# print(add())

# def add():
#     a=10
#     a += 5
#     return a 

# print(add())

#Return value.If the return statement is without any expression, then the special value None is returned.
# a=2
# b=5
# def add():
#     pass   
# print(add())


#Return value.Method  with any expression but without return statement is returns special value None.
# a=2
# b=5
# def add():
#     a+b
# print(add())



# In[7]:


Current_Year = 2020

class Student:
    def __init__(self,name,year_born):
        self.name=name
        self.year_born=year_born
        self.knowledge = 0
    
    def getAge(self):
        return Current_Year - self.year_born
    
    def study(self):
        self.knowledge += 1
        return self.knowledge 
    
    def __str__(self): 
        return '{} is {} years old and has {} knowledge.'.format( self.name , self.getAge() , self.study())
    
student_1 = Student('Ram',1999)
print(student_1) 
    
    


# In[11]:


class Student:
    def __init__(self):
        self.knowledge = 0
    
    def __str__(self): 
        return 'Hello I am Object'
    
    
    def study(self):
        self.knowledge += 1 # it returns none but update instant_variable(self.knowledge)
        #print('instant_variable(self.knowledge) is updated.')
    
student_1 = Student()
print(student_1) # print object calls str method
print(student_1.study())
print(student_1.knowledge) # print instant_variable(self.knowledge) after updated

    
    

