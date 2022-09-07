#!/usr/bin/env python
# coding: utf-8

# In[1]:


class A:
    def show(self):
        print('Class A')
        
class B(A):
    def output(self):
        show()
        
    
objectb=B()
objectb.output()


# In[4]:


class A:
    def show(self):
        print('Class A')
        
class B(A):
    def output(self):
        A.show()
        
    
objectb=B()
objectb.output()


# In[5]:


class A:
    def show():
        print('Class A')
        
class B(A):
    def output(self):
        A.show()
        
    
objectb=B()
objectb.output()


# In[4]:


class A:
    def show(self):
        print('Class A')
        
class B(A):
    def output(self):
        super().show()
        
    
objectb=B()
objectb.output()


# In[5]:


class A:
    def show(self):
        print('Class A')
        
class B(A):
    def output(self):
        self.show()
        
    
objectb=B()
objectb.output()

