#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=0
if a==1 :
    print('a=1')
elif a==0 :
    print('a=0')#break over here
elif a==0 :
    print('a=2')


# In[16]:



for i in range(8):
    if (i<3):
        print(i)
        continue
    if (i<6):
        print('a',i)

