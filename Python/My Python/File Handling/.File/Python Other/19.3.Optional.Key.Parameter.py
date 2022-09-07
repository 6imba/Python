#!/usr/bin/env python
# coding: utf-8

# In[3]:


#absolute value means value regardless of sign
def absolute(x):#this function return absolute value
    if x>=0:
        return x
    else:
        return -x
print(absolute(-3))
print(absolute(45))
print(absolute(-66))


# In[6]:


#here we can sort this list by its elements absolute value
#means absolute value of list is [1,7,4,2,3] regardless of sign

L1 = [1,-7,4,-2,3]
def absolute(x):
    if x>=0:
        return x
    else:
        return -x
    
for y in L1:
    print(absolute(y))#print absolute value of the given list element


# In[19]:


#by now you may get known that sorted() method takes two parameter 1.sequence_variable and 2.Way_to_sort_or_order_function
#like sort by reverse,absolute_value,

L1 = [1,-7,4,-2,3]
def absolute(x):
    if x>=0:
        return x
    else:
        return -x
sorted(L1,key = absolute)#sort list(L1) by absolute value
#here key is one of the optional_parameter or funtion for sorted() method that hold item of the list
#and absolute is the property of optional_parameter


# In[14]:


#sorted(L1,key = absolute_value)
#sorted(L1,reverse = True)
# here we know that
# sorted() method takes two parameter
# 1.sequence_variable ==> L1
# 2.Way_to_sort_or_order_function ==> key,reverse ==> optional_Key
#and True,absolute_value are the parameter or property of optional_Key


# In[16]:


L1 = [1,-7,4,-2,3]
def absolute(x):
    if x>=0:
        return x
    else:
        return -x
sorted(L1, reverse=True, key=absolute)
#now see her any method can have any number of optional parameter
#so finally sorted() method only donot take two parameter it can take one required_parameter and numbers of optional_parameter


# In[21]:


L1 = [1, 7, 4, -2, 3]

def absolute(x):
    print("--- figuring out what to write on the post-it note for " + str(x))
    if x >= 0:
        return x
    else:
        return -x

print("About to call sorted")
L2 = sorted(L1, key=absolute)
print("Finished execution of sorted")
print(L2)


# In[23]:


L1 = [1,-7,4,-2,3]
def absolute(x):
    if x>=0:
        return x
    else:
        return -x
sorted(L1, reverse=True, key=lambda x:absolute(x))#use of lambda

