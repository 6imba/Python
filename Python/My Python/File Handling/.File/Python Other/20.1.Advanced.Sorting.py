#!/usr/bin/env python
# coding: utf-8

# In[21]:


List = ['A','F','D','G','D','G','B','A','S','A','Z']#list
dis = {} #create empty list

for item in List:#adding item of list into dictionary
    if item in dis:
        dis[item]=dis[item]+1 # if item is already in disctionary(dis) then plus 1 to its value
    else:
        dis[item]=1 # if item is not in disctionary(dis) then add that item to the disctionary(dis) and define its value 1

for key in dis.keys():
    print('{} has frequency of {}.'.format(key,dis[key]))  
#here output is unsorted
    
# for key in dis:
#     print('{} has frequency of {}.'.format(key,str(dis[key])))  
# for key in dis.keys():
#     print('{} has frequency of {}.'.format(key,str(dis[key])))  


# In[24]:


#Now sorting output:
List = ['A','F','D','G','D','G','B','A','S','A','Z']
dis = {} 

for item in List:
    if item in dis:
        dis[item]=dis[item]+1 
    else:
        dis[item]=1 

for key in sorted(dis.keys()):#sorting
    print('{} has frequency of {}.'.format(key,dis[key]))  


# In[30]:


#Now sorting output according to item frequency:
List = ['A','F','D','G','D','G','B','A','S','A','Z']
dis = {} 

for item in List:
    if item in dis:
        dis[item]=dis[item]+1 
    else:
        dis[item]=1 

for key in sorted(dis.keys(),key=lambda k:dis[k]):#sorting by optional_parameter according to frequency
    print('{} has frequency of {}.'.format(key,dis[key]))  
#dis.keys() refer to the key in a dictionary i.e 'A','F','D' and so on
#sorted(,key) refer to the optional_parameter name in the sorted function
#lambda k:dis[k] ==>
#def key(k):
#    return dis[k]


# In[32]:


List = ['A','F','D','G','D','G','B','A','S','A','Z']
dis = {} 

for item in List:
    if item in dis:
        dis[item]=dis[item]+1 
    else:
        dis[item]=1 

for key in sorted(dis.keys(),key=lambda k:dis[k],reverse=True):
    print('{} has frequency of {}.'.format(key,dis[key])) 


# In[34]:


List = ['A','F','D','G','D','G','B','A','S','A','Z']
dis = {} 

for item in List:
    if item in dis:
        dis[item]=dis[item]+1 
    else:
        dis[item]=1 

for key in sorted(dis,key=lambda k:dis[k],reverse=True):#automatic figure out key from dictionary
    print('{} has frequency of {}.'.format(key,dis[key])) 


# In[1]:


# Note
# When we sort the keys, passing a function with key=lambda x: d[x] does not specify to sort the keys of a dictionary. The lists of keys are passed as the first parameter value in the invocation of sort. The key parameter provides a function that says how to sort them.
# Eventually, you will be able to read code like that and immediately know what it’s doing. For now, when you come across something confusing, like line 11, try breaking it down. The function sorted is invoked. Its first parameter value is a dictionary, which really means the keys of the dictionary. The second parameter, the key function, decorates the dictionary key with a post-it note containing that key’s value in dictionary d. The last parameter, True, says to sort in reverse order.
# There is another way to sort dictionaries, by calling .items() to extract a sequence of (key, value) tuples, and then sorting that sequence of tuples. But it’s better to learn the pythonic way of doing it, sorting the dictionary keys using a key function that takes one key as input and looks up the value in the dictionary.


# In[4]:


# Which of the following will sort the keys of d in ascending order of their values (i.e., from lowest to highest)?
# A. sorted(ks, key=g)
# B. sorted(ks, key=lambda x: g(x, d))
# C. sorted(ks, key=lambda x: d[x])


L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k, d):
    return d[k]

ks = d.keys()

print(sorted(ks, key=lambda x: g(x, d)))
print(sorted(ks, key=lambda x: d[x]))


# In[5]:


#Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys.

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
sorted_keys = sorted(dictionary.keys())


# In[7]:


#3. Below, we have provided the dictionary groceries, whose keys are grocery items, and values are the number of each item that you need to buy at the store. Sort the dictionary’s keys into alphabetical order, and save them as a list called grocery_keys_sorted.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
grocery_keys_sorted = groceries.keys().sort()


# In[8]:


#3. Below, we have provided the dictionary groceries, whose keys are grocery items, and values are the number of each item that you need to buy at the store. Sort the dictionary’s keys into alphabetical order, and save them as a list called grocery_keys_sorted.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
grocery_keys_sorted = sorted(groceries.keys())


# In[22]:


#4. Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values

sorted_values=[]
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
for key in sorted(dictionary.keys(),key=lambda k:dictionary[k],reverse=True):
    sorted_values = sorted_values + [key]
print(sorted_values)


# In[19]:



dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
for key in sorted(dictionary.keys(),key=lambda k:dictionary[k],reverse=True):
    sorted_values = dictionary[key]
    print(key , '==>' , sorted_values)

