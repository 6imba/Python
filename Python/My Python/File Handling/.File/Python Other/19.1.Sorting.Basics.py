#!/usr/bin/env python
# coding: utf-8

# In[7]:


#sorting sequence(list)
# Python provides two ways to sort a sequence, 
#the dot sort method and the function sorted. 


# In[10]:


#.sort() => the dot sort method
list1 = [1,7,4,-2,3,4]
list2 = ['dog','zebre','ape']

list1.sort()
print(list1)
list2.sort()
print(list2)


# In[14]:


list1 = [1,7,4,-2,3,4]
list1.sort()
print(list1)
print(list1.sort())
#.sort() methods arrage list into order but return nothing
#.sort() method mutate the origial list into given order


# In[19]:


#sorted() => function sorted.
listone = [1,7,4,-2,3,4]
listtwo = ['dog','zebre','ape']
print(sorted(listone))
duplist = sorted(listtwo)
print(duplist)
#sorted() methods sort the list in given order but doesnt mutate original list
print(listone)
print(listtwo)


# In[37]:


org = [2,-4,6,5,9,-2,7]
print(org)

print('\n')

print(sorted(org))
dupli = sorted(org)
print(dupli)
print(org)

print('\n')

print(org.sort())
org.sort()
print(org)


# In[38]:


x='ball'
print(x.sort())
#.sort() method can be done in mutable_sequences(list,dic)


# In[36]:


print(sorted('Apple'))
#sorted method can be done in both mutable_sequences(list) and immutable_sequences(string,tuples)
#Since strings and tuples are immutable, there is no sort() method that update the original object

