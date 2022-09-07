#!/usr/bin/env python
# coding: utf-8

# In[5]:


#we have seen before that python has dot_reverse{.reverse()} method to reverse the list 
#The .reverse() method reverses the elements of the list.

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

systems.reverse()# List Reverse
print('Updated List:', systems)# updated list

#The reverse() method doesn't 1.(return any value), 2.(take any arguments). 
#It updates the existing list.


# In[9]:


#we can reverse list even  more easily as we can specify an optional parameter for the sorted funtion called reverse
systems = ['Windows', 'macOS', 'Linux']
print(sorted(systems,reverse=True))


# In[12]:


# False is the default value for the reverse parameter.Means
#If we leave it out it will print same
systems = ['Windows', 'macOS', 'Linux']
print(sorted(systems))
print(sorted(systems,reverse=False))


# In[14]:


#1. Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.


lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst,reverse=True)
print(lst_sorted)

