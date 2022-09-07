#!/usr/bin/env python
# coding: utf-8

# In[64]:


var1 = 99
print(var1)


# In[65]:


var1 = 99
def output():
    print(var1)
output()
output


# In[63]:


var1 = 99
print(var1)
var1=var1+10000
print(var1)


# In[76]:


var1 = 99
def output():
    print(var1)
def update():
    print(var1)
    var1=var1+100
    print(var1)
output()
update()


# In[83]:


x= "awesome" # global_variable

def myfunc():
  x = "fantastic" #local_variable
  print("Python is " + x) #call local_variable
myfunc()

print("Python is " + x) # call global_variable


# In[91]:


var1 = 99

def update():
    global var1
    print(var1)
    var1=var1+100
    print(var1)
    
update()
print(var1)


# In[96]:


var1 = 99

def update():
    print(var1)
    
update()
print(var1)


# In[102]:


var1 = 99
print(var1)

def update():
    print(var1)
    global var1
    
print(var1)
update()


# In[82]:


print('1==>')
var1 = 99

def output():
    print('2==>')
    print(var1)
    
def update():
    print('3==>')
    print(var1)
    global var1
    var1=var1+100
    print(var1)
    
print('4==>')
output()
print('5==>')
update()


# In[42]:


class A:
    asas=123
    def pri(self):
         print(asas)
#         print(self.asas)
obj1=A()
obj1.pri()


# In[38]:


class A:
    global xxx
    xxx=123
    def pri(self):
         print(xxx)
#         print(self.xxx)
obj1=A()
obj1.pri()


# In[3]:


class A:
    numb1=123
    def output(self):
        numb2=999
        print(self.numb1)
        print(numb2)
obj1=A()
obj1.output()


# In[9]:


print('1')

class User_Model():
    print('3')
    ii = 0
    jj = 0
    print('4',ii,jj)
    
    def __init__(self,ids):
        self.user_id = ids
        ii = ids
        jj = jj + ids
        
    print(ii) # self.user_id is a local variable inside method
    print(jj)
    
    print('5')
    
print('2')
User_Id=input('Enter your User_Id : ')
obj1=User_Model(User_Id)


# In[14]:


print('1')

class User_Model():
    print('3')
    ii = 0
    jj = 0
    print('4',ii,jj)
    
    def __init__(self,ids):
        self.user_id = ids
        ii = ids
        self.jj = self.jj + int(ids)
        
    print(ii) 
    print(jj)
    
    print('5')
    
print('2')
User_Id=input('Enter your User_Id : ')
obj1=User_Model(User_Id)


# In[20]:


print('1')

class User_Model():
    print('3')
    ii = 0
    jj = 0
    print('4',ii,jj)
    
    def __init__(self,ids):
        self.user_id = ids
        ii = ids
        self.jj = self.jj + int(ids)
    
    print('5')
    
    def output(self):
        print(ii) 
        print(jj)
    
print('2')
User_Id=input('Enter your User_Id : ')
obj1=User_Model(User_Id)
obj1.output()


# In[25]:


print('1')

class User_Model():
    print('3')
    ii = 0
    jj = 0
    print('4',ii,jj)
    
    def __init__(self,ids):
        self.user_id = ids
        ii = ids
        self.jj = self.jj + int(ids)
    
    print('5')
    
    def output(self):
        print(self.ii) 
        print(self.jj)
    
print('2')
User_Id=input('Enter your User_Id : ')
obj1=User_Model(User_Id)
obj1.output()


# In[26]:


print('1')

class User_Model():
    print('3')
    ii = 0
    jj = 0
    print('4',ii,jj)
    
    def __init__(self,ids):
        self.user_id = ids
        self.ii = ids
        self.jj = self.jj + int(ids)
    
    print('5')
    
    def output(self):
        print(self.ii) 
        print(self.jj)
    
print('2')
User_Id=input('Enter your User_Id : ')
obj1=User_Model(User_Id)
obj1.output()


# In[29]:


a=11
def change(self): # self only for classs instant
    a=22
change()
print(a)


# In[6]:


a=11
def change():
    a=22
change()
print(a)


# In[32]:


a=11
def change():
    a=a+22
change()
print(a)


# In[33]:


a=11
def change():
    global a 
    a=a+22
change()
print(a)


# In[8]:


def f(): 
    global s 
    print (s) 
    s = "Look for Geeksforgeeks Python Section"
    print(s)

# Global Scope 
s = "Python is great!" 
f() 
print(s) 

