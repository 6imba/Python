#!/usr/bin/env python
# coding: utf-8

# In[39]:


science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
print(science)
print(science['two'])
print(index)#final indexorkey is set as four 
print('\n')


# In[42]:


#method => .key()

science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
print(science)
print(science.keys())

#The keys() method returns a view object. 
#The view object contains the keys of the dictionary, as a list.
#The view object will reflect any changes done to the dictionary


# In[4]:


science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}

for key in science.keys() :
    print(key)


# In[6]:


science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}

for key in science :
    print(key)

#note that :wheather u mention method => .key() or not its default in dictonary 


# In[22]:


science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}

for key in science :
    print(key,'has value of ',science[key])
print('\n')


# In[27]:


science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
   
for key in science.keys() :
    print(key,'has value of ',science[key])


# In[34]:


science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}

for key in science :
    key = list(science)
    print(key)


# In[36]:


science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}

for key in science :
    key = list(science.keys())
    print(key)


# In[8]:


science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}

key = list(science)
print(key)
#note that :wheather u mention method => .key() or not its default in dictonary 


# In[9]:


#extra
a = 'apple'
i=1
for x in a :
    print (a[-i])
    i=i+1


# In[29]:


#.values() method
PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
print(PersonAge.values())
#note : .values() method takes no arguments
#note : no garenty of order


# In[14]:


#.keys() method
PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
print(PersonAge.keys())
#default
#note : no garenty of order


# In[16]:


#.items() method => gives the list of tuples where every tuples is a key-value paired
PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
print(PersonAge.items())
#note : no garenty of order


# In[19]:


# in operator => boolean type output
PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
print('Radha' in PersonAge)
print('Undertaker' in PersonAge)
#note : no garenty of order


# In[23]:


# in operator => boolean type output
PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
if 'Gomez' in PersonAge :
    print(PersonAge['Gomez'])
else:
    print ('There is no any key called Gomez !')
#note : no garenty of order


# In[35]:


# in operator => boolean type output
PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
if 'Undertaker' in PersonAge :
    print('Age : ',PersonAge['Undertaker'])
else:
    print ('There is no any key called Undertaker !')
#note : no garenty of order


# In[33]:


#.get() method => get the value of the given key 
#takes at least one argument
#its like .values() but it takes cetain key as argument where as .values() doesnt
PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
print(PersonAge.get('SimbA'))
#note : no garenty of order


# In[44]:


PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
print(PersonAge.get('Undertaker'))


# In[45]:


#.get also takes optional second argument
PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
print(PersonAge.get('Undertaker',0))


# In[47]:


#extra assignment from coursera
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print(23 in mydict)#here 23 is value and in checks for key not value


# In[52]:


total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print(mydict['cat'])
for akey in mydict:
    print(mydict[akey])
    if len(akey) > 3:
        total = total + mydict[akey]
print(total)


# In[55]:


#Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this!

places = {"Australia":2000, "Greece":2004, "China":2008, "England":200012}
print(places)
places['Brazil']= 2016
print(places)


# In[ ]:


# We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events. Do not hard code this.

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events.keys())

