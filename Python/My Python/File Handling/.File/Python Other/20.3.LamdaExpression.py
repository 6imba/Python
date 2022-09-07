#!/usr/bin/env python
# coding: utf-8

# In[1]:


#when to use a Lambda expression, and when to use a named function for your key parameter when sorting. 
# Basically, my rule of thumb is if the lambda expression is short and simple, so that it's pretty easy to understand what it's doing, use the lambda expression, and as soon as it gets too complex, refer to a name function instead, and give it a good name that describes the property you're trying to sort by. 
#When to use a Lambda Expression¶
#Though you can often use a lambda expression or a named function interchangeably when sorting, it’s generally best to use lambda expressions until the process is too complicated, and then a function should be used. For example, in the following examples, we’ll be sorting a dictionary’s keys by properties of its values. Each key is a state name and each value is a list of city names.
#For our first sort order, we want to sort the states in order by the length of the first city name. Here, it’s pretty easy to compute that property. states[state] is the list of cities associated with a particular state. So If state is a list of city strings, len(states[state][0]) is the length of the first city name. Thus, we can use a lambda expression:


# In[5]:


states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: len(states[state][0])))


# In[ ]:


#For our second sort order, the property we want to sort by is the number of cities that begin with the letter ‘S’. The function defining this property is harder to express, requiring a filter and count accumulation pattern. So we are better off defining a separate, named function. Here, we’ve chosen to make a lambda expression that looks up the value associated with the particular state and pass that value to the named function s_cities_count. We could have passed just the key, but then the function would have to look up the value, and it would be a little confusing, from the code, to figure out what dictionary the key is supposed to be looked up in. Here, we’ve done the lookup right in the lambda expression, which makes it a little bit clearer that we’re just sorting the keys of the states dictionary based on a property of their values. It also makes it easier to reuse the counting function on other city lists, even if they aren’t embedded in that particular states dictionary.


# In[6]:


def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))


# In[12]:



states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct
def s_cities_count_for_state(state):
    cities_list = states[state]
    return s_cities_count(cities_list)

print(sorted(states, key = s_cities_count_for_state))


# In[ ]:


# Congratulations, now you really know how to sort. Simple sorts, complex sorts, all sorts of sorts. You can sort dictionary keys based on some property of their values. You can break ties by having the key function return a tuple. You can use lambda expressions, you can use name functions, you are a pro at sorting.
# Play video starting at 29 seconds and follow transcript0:29
# Now in the intro to this week, I made a big deal out of saying, we're not going to go into details of which sorting algorithm gets used and how long it takes it to run.
# Play video starting at 38 seconds and follow transcript0:38
# So instead of a straight up joke, let me give you a little programmer's humor. A sorting algorithm that runs really slowly.
# Play video starting at 47 seconds and follow transcript0:47
# It's called bogosort, and it works by trial and error. Take the items, shuffle them, just at random into some random order, and check if they happen to be sorted. If they are, we're done. Otherwise, try again. Shuffle, see if they're sorted. Keep going until you get a lucky shuffle.
# Play video starting at 1 minute 6 seconds and follow transcript1:06
# Remarkably, the code for this in Python is short. In the random module, there's a built-in function called shuffle, and I wrote the function to check if a list is in order in five lines, and another four for the trial and error wild loop. But here's the full code.
# Play video starting at 1 minute 23 seconds and follow transcript1:23
# Of course, because you do a random shuffle every time, it takes a random amount of time to finish, but as you can imagine, this is not a fast way to do sorting. You got a bunch of items and you just shuffle them, the chances that it's going to be sorted aren't very good. I just ran it once on a list of ten items and it took 68 seconds to complete. I didn't dare to try it with 11 items.
# Play video starting at 1 minute 45 seconds and follow transcript1:45
# By contrast, Python's built-in sorted function was able to sort a million items in just over half a second.
# Play video starting at 1 minute 54 seconds and follow transcript1:54
# Now you have a party trick. Ask your friends who've taken some computer science courses some time ago to try to remember the slowest sorting algorithm they studied.
# Play video starting at 2 minutes 4 seconds and follow transcript2:04
# They'll have fun recalling bubble sort and insertion sort and trying to decide which one is slower, and then you can regale them with bogosort. You'll be the life of the party, trust me.
# Play video starting at 2 minutes 16 seconds and follow transcript2:16
# See you next time.

