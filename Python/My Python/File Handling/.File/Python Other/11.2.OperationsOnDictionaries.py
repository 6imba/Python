#!/usr/bin/env python
# coding: utf-8

# In[5]:


inventory = {'apple':430,'banana':312,'orange':525,'pears':217}#created four key-value
print(inventory)
del inventory['orange']#del => deletes the paired key-value from the dictionary
print(inventory)


# In[8]:


inventory = {'apple':430,'banana':312,'orange':525,'pears':217}
print(inventory)
inventory['apple'] = 12.12 # update the value associated with key_paired
print(inventory)


# In[13]:


inventory = {'apple':430,'banana':312,'orange':525,'pears':217}
print(inventory)
print(inventory['pears'])
inventory['pears'] = inventory['pears'] + 10000 #add integer(1000) to the value associated with key_paired(inventory['pears'])
print(inventory['pears'])
print(inventory)


# In[17]:


inventory = {'apple':430,'banana':312,'orange':525,'pears':217}
print(inventory)
numItems = len(inventory)#gives the number of key value paired in the given dictionary
print(numItems)

