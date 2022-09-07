#!/usr/bin/env python
# coding: utf-8

# In[4]:


#For example, suppose that we wanted to compute a Scrabble score for the Study in Scarlet text. Each occurrence of the letter ‘e’ earns one point, but ‘q’ earns 10. We have a second dictionary, stored in the variable letter_values. Now, to compute the total score, we start an accumulator at 0 and go through each of the letters in the counts dictionary. For each of those letters that has a letter value (no points for spaces, punctuation, capital letters, etc.), we add to the total score
f = open('12.1Accumulstion.Dictionary.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for y in x:
    if y in letter_values:
        tot = tot + letter_values[y] * x[y]

print(tot)


# In[6]:


#The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total. Do not hard code this!

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0
for continent in travel :
    total = total + travel[continent]
print('Total number of country traveled ',total)


# In[8]:


#schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits. Do not hardcode.

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits = 0
for class_name in schedule :
    total_credits = total_credits + schedule[class_name]
print('Total credit of sum of all course is ',total_credits)


# In[10]:


#Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for all_char in placement :
    if all_char not in d :
        d[all_char] = 0
    d[all_char] = d[all_char] + 1

for all_char in d :
    print(all_char , ' = ' , d[all_char])
    
min_value = placement[0]
print(min_value)

for all_char in d :
    if d[all_char] < d[min_value] :
        min_value = all_char
print('Min-value-key = ',min_value)


# In[3]:


# Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.



product = "iphone and android phones"
lett_d = {}
for all_char in product :
    if all_char not in lett_d :
        lett_d[all_char] = 0
    lett_d[all_char] = lett_d[all_char] + 1

for all_char in lett_d :
    print(all_char , ' = ' , lett_d[all_char])

max_value = product[0]

for all_char in lett_d :
    if lett_d[all_char] > lett_d[max_value] :
        max_value = all_char
print ('Max value is of key ',max_value, ' is ', lett_d[max_value])  


# In[25]:


#Now what if we want to find the key associated with the maximum value? It would be nice to just find the maximum value as above, and then look up the key associated with it, but dictionaries don’t work that way. You can look up the value associated with a key, but not the key associated with a value. (The reason for that is there may be more than one key that has the same value).
#The trick is to have the accumulator keep track of the best key so far instead of the best value so far. For simplicity, let’s assume that there are at least two keys in the dictionary. Then, similar to our first version of computing the max of a list, we can initialize the best-key-so-far to be the first key, and loop through the keys, replacing the best-so-far whenever we find a better one.
#In the exercise below, we have provided skeleton code. See if you can fill it in. An answer is provided, but you’ll learn more if you try to write it yourself first.

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}
print(d,' ==> Print dictionary d={}')

keys_of_dict = d.keys()
print(keys_of_dict,' ==> All keys in the dictionary d={} holded by variable(i.e keys_of_dict).')
print(type(ks),' ==> type of variable(i.e keys_of_dict) that hold All keys in the dictionary d={}')

list_of_key = list(keys_of_dict)
print(list_of_key,' ==> list of key in the dictionary d={} holded by variable(i.e keys_of_dict).')

best_key_so_far = list_of_key[0]  # Have to turn keys_of_dict into a real list before using [] to select an item
print(best_key_so_far)

for k in keys_of_dict:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

