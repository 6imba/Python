#!/usr/bin/env python
# coding: utf-8

# In[8]:


#extra basics of list tuples and string
list_of_tups = [('A',3,2),('C',1,4),('B',3,1),('A',2,4),('C',1,2)]
print(list_of_tups)
print(type(list_of_tups))
for tups in list_of_tups:
    print(tups)
for tups in list_of_tups:
    print(type(tups))
for tups in list_of_tups:
    for item in tups:
        print(item)
        print(type(item))


# In[11]:


list_of_tups = [('A',3,2),('C',1,4),('B',3,1),('A',2,4),('C',1,2)]
print(list_of_tups)
print(sorted(list_of_tups))#sorted tuples inside list


# In[16]:


list_of_tups = [('A',3,2),('C',1,4),('B',3,1),('A',2,4),('C',1,2)]
for tups in list_of_tups:
    print(tups)
print('.......................................................')
for tups in sorted(list_of_tups):
    print(tups)#sorted tuples inside list


# In[22]:


#What happens when two items are “tied” in the sort order? For example, suppose we sort a list of words by their lengths. Which five letter word will appear first?
#The answer is that the python interpreter will sort the tied items in the same order they were in before the sorting.
#What if we wanted to sort them by some other property, say alphabetically, when the words were the same length? Python allows us to specify multiple conditions when we perform a sort by returning a tuple from a key function.
#First, let’s see how python sorts tuples. We’ve already seen that there’s a built-in sort order, if we don’t specify any key function. For numbers, it’s lowest to highest. For strings, it’s alphabetic order. For a sequence of tuples, the default sort order is based on the default sort order for the first elements of the tuples, with ties being broken by the second elements, and then third elements if necessary, etc.


list_of_tups = [('A',5,4),('A',5,3),('A',3,10000),('A',1,3),('A',1,55),('A',3,10000),('A',1,2)]

for tups in sorted(list_of_tups):
    print(tups)#sorted tuples inside list
# Here sorting tuples sort first item of the tuple first and the 2nd and 3rd and so on


# In[25]:


#In the code below, we are going to sort a list of fruit words first by their length, smallest to largest, and then alphabetically to break ties among words of the same length. To do that, we have the key function return a tuple whose first element is the length of the fruit’s name, and second element is the fruit name itself.

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)
    
#using tuple to create a tie breaking mechanism
#As always take one item as input and it's supposed to return a property of the item that instead of returning one property of the item, we're going to return a tuple, containing two properties of the item.
#(len(fruit_name), fruit_name)
#(5,'peach')
#(4,'kiwi')
#(4,'pear')
#when it comes along, and sees four comma pair, it's going to have a tie, when it compares four with four, and it's going to then use alphabetic ordering, as the secondary sort order to break the ties.


# In[31]:


fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name),reverse=True)#reverse our sort order
for fruit in new_order:
    print(fruit)


# In[32]:


fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:                          #reverse primary property     
    print(fruit)


# In[33]:


# sort-5-1: What will the sorted function sort by?

# weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
#            'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
#            'Cairo': {'temp': 96, 'condition': 'sunny'},
#            'Berlin': {'temp': 89, 'condition': 'sunny'},
#            'Caloocan': {'temp': 78, 'condition': 'sunny'}}

# sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
# A. first city name (alphabetically), then temperature (lowest to highest)
#✔️ Correct! First we sort alphabetically by city name, then by the temperature, from lowest to highest.
# B. first temperature (highest to lowest), then city name (alphabetically)
#✖️ The order of the tuple matters. The first item in the tuple is the first condition used to sort.
# C. first city name (alphabetically), then temperature (highest to lowest)
#✖️ Not quite, remember that by default, the sorted function will sort by alphabetical order, or lowest to highest. Is the reverse parameter set to True? Has a negative sign been used in the key parameter?
# D. first temperature (lowest to highest), then city name (alphabetically)
#✖️ The order of the tuple matters. The first item in the tuple is the first condition used to sort.


# In[34]:


# sort-5-2: What how will the following data be sorted?

# weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
#            'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
#            'Cairo': {'temp': 96, 'condition': 'sunny'},
#            'Berlin': {'temp': 89, 'condition': 'sunny'},
#            'Caloocan': {'temp': 78, 'condition': 'sunny'}}

# sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
# A. first city name (reverse alphabetically), then temperature (lowest to highest)
# ✔️ Correct! In this case, the reverse parameter will cause the city name to be sorted reverse alphabetically instead of alphabetically, and it will also negate the negative sign in front of the temperature.
# B. first temperature (highest to lowest), then city name (alphabetically)
# ✖️ The order of the tuple matters. The first item in the tuple is the first condition used to sort. Also, take note of the reverse parameter - what will it do in this instance?
# C. first city name (reverse alphabetically), then temperature (highest to lowest)
# ✖️ Not quite - is the reverse parameter set to True? Has a negative sign been used in the key parameter? What happens when those are both used?
# D. first temperature (lowest to highest), then city name (alphabetically)
# ✖️ The order of the tuple matters. The first item in the tuple is the first condition used to sort.
# E. first city name (alphabetically), then temperature (lowest to highest)
# ✖️ Not quite, remember that by default, the sorted function will sort by alphabetical order, or lowest to highest. Is the reverse parameter set to True? Has a negative sign been used in the key parameter?


# In[ ]:




