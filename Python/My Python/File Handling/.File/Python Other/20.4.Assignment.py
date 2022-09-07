#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters,reverse=True)


# In[2]:


#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)


# In[5]:


#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)
alphabetical = sorted(medals.keys())


# In[6]:


#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def g(k,d):
    return d[k]
top_three = sorted(medals.keys(),key=lambda x : g(x,medals),reverse = True)[:3]


# In[7]:


#We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.


groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

def values(items,dictionary):
    return(dictionary[items])

most_needed = sorted(groceries.keys(), key = lambda x:values(x,groceries), reverse=True)


# In[14]:


# # extra sort from highest key value

# #1
# groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
# most_needed = sorted(groceries)#sort by dictionary keys aphbetically

# #2
# most_needed = sorted(groceries,value)#sort the keys by its value

# #3 going into value extraction 
# most_needed = sorted(groceries, key=value)#sort the key_method & value_property

#4
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

def values(item,dictionary):
    return dictionary[item]

most_needed = sorted(groceries,key=lambda x: values(x,groceries))#lambda expression provides the key of the dictionary and values funtion provide value of the provided key
most_needed = sorted(groceries,key=lambda x: values(x,groceries), reverse=True)#decendening order
print(most_needed)


# In[22]:


#extra
x='aasasdasd'
print( x[-4:2])


# In[28]:


#Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

def last_four(x):
    return str(x)[-4:]

sorted_ids = sorted(ids, key=last_four)
print(sorted_ids)


# In[30]:


#Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id=sorted(ids, key=lambda x: str(x)[-4:])
print(sorted_id)


# In[ ]:


# Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

