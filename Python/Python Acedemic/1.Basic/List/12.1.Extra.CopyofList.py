#!/usr/bin/env python
# coding: utf-8

# In[14]:


old_list = ['apple', 'banana', 'coconut']
new_list = old_list # new_list assignment
print(old_list)


# In[8]:


x = ['apple', 'banana', 'coconut']
y=[1,2,3]
x = y #x list overwrite
print(y)


# In[15]:


x = [3,5,7]
x = z
#error as x is list and z has no any defination


# In[16]:


old_list = ['apple', 'banana', 'coconut']
new_list = old_list # new_list assignment
new_list.append('graphs') # add new key_value at the end of new_list
#now you may think that you have two list i.e (new_list and old_list )
#and may think that new_list is just of copy of old_list change in new_list may not change the old_list.
#but it change old_list also
#With new_list = old_list, you don't actually have two lists.
#The assignment just copies the reference to the list, not the actual list,
#means new_list dont copy the value hold by the old_list instead it reference to the list of old_list
#so both new_list and my_list refer to the same list after the assignment.
#see the change below
print(old_list)
#see that adding value to new_list, adds value to old_list as both of them has reference to the same list

