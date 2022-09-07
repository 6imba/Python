#!/usr/bin/env python
# coding: utf-8

# In[16]:


class A1:
    name1='Amir'
    age1=21
    def show1(self):
        print('Hello class A !')
    
class B1(A1):
    naam1='Zoya'
    umer1=19
    def output1(self):
        print('Hello class B !')
        
obj1=B1()
print(obj1.naam1)
print(obj1.umer1)
obj1.output1()

print(obj1.name1)
print(obj1.age1)
obj1.show1()

# here we can use same object(obj2) to inherit outside the class


# In[27]:


class A2:
    name2='Amir'
    age2=21
    def show2(self):# show2 need argument: 'self' object to be pass
        print('Hello class A !')
    
class B2(A2):
    naam2='Zoya'
    umer2=19
    def output2(self):
        print('Hello class B !')
        
obj2=B2()
print(obj2.naam2)
print(obj2.umer2)
obj2.output2()

print(A2.name2)
print(A2.age2)
A2.show2()

# here we can use same object(obj2) to inherit outside the class


# In[26]:


class A2:
    name2='Amir'
    age2=21
    def show2():
        print('Hello class A !')
    
class B2(A2):
    naam2='Zoya'
    umer2=19
    def output2(self):
        print('Hello class B !')
        
obj2=B2()
print(obj2.naam2)
print(obj2.umer2)
obj2.output2()

print(A2.name2)
print(A2.age2)
A2.show2()

# here we can use same object(obj2) to inherit outside the class


# In[36]:


class A2:
    name2='Amir'
    age2=21
    def show2(self):
        print('Hello class A !')
    
class B2(A2):
    naam2='Zoya'
    umer2=19
    def output2(self):
        print('Hello class B !')
        A2.show2()
        
obj2=B2()
print(obj2.naam2)
print(obj2.umer2)
obj2.output2()


# here we can use same object(obj2) to inherit outside the class


# In[41]:


class A2:
    name2='Amir'
    age2=21
    def show2(self):
        print('Hello class A !')
    
class B2(A2):
    naam2='Zoya'
    umer2=19
    def output2(self):
        print('Hello class B !')
        self.show2()
        
obj2=B2()
print(obj2.naam2)
print(obj2.umer2)
obj2.output2()


# here we can use same object(obj2) to inherit outside the class


# In[47]:


class A2:
    name2='Amir'
    age2=21
    def show2(self):
        print('Hello class A !')
    
class B2(A2):
    naam2='Zoya'
    umer2=19
    def output2(self):
        print('Hello class B !')
        obj2.show2()
        
obj2=B2()
print(obj2.naam2)
print(obj2.umer2)
obj2.output2()


# here we can use same object(obj2) to inherit outside the class


# In[49]:


class A2:
    name2='Amir'
    age2=21
    def show2(self):
        print('Hello class A !')
    
class B2(A2):
    naam2='Zoya'
    umer2=19
    def output2(self):
        print('Hello class B !')
        super().show2()
        
obj2=B2()
print(obj2.naam2)
print(obj2.umer2)
obj2.output2()


# here we can use same object(obj2) to inherit outside the class


# In[50]:


class A2:
    name2='Amir'
    age2=21
    def show2(self):
        print('Hello class A !')
    
class B2(A2):
    naam2='Zoya'
    umer2=19
    def output2(self):
        print('Hello class B !')
        super().show2()
        obj2.show2()
        self.show2()
        
obj2=B2()
print(obj2.naam2)
print(obj2.umer2)
obj2.output2()


# here we can use same object(obj2) to inherit outside the class

