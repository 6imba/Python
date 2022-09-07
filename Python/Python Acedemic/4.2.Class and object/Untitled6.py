#!/usr/bin/env python
# coding: utf-8

# In[20]:


class A:
    def show1(self): # this class_variable i.e show1 takes instance
        print('A class')
class B(A):
    def show2(self):
        A.show1()
        
obj=B()   
obj.show2()


# In[22]:


class One:
    showw1=10 # this class_variable 
class Two(One):
    def showw2(self):
        print(One.showw1)
        
obj=Two()   
obj.showw2()

