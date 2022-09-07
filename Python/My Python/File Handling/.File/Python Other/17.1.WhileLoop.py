#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('hello')


# In[8]:


for a in (a=5):
    print(a)
    a=a-1


# In[10]:


def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """

    theSum  = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))

print(sumTo(1000))

#Introduction of the while statement causes us to think about the types of iteration we have seen. The for statement will always iterate through a sequence of values like the list of names for the party or the list of numbers created by range. Since we know that it will iterate once for each value in the collection, it is often said that a for loop creates a definite iteration because we definitely know how many times we are going to iterate. On the other hand, the while statement is dependent on a condition that needs to evaluate to False in order for the loop to terminate. Since we do not necessarily know when this will happen, it creates what we call indefinite iteration. Indefinite iteration simply means that we don’t know how many times we will repeat but eventually the condition controlling the iteration will fail and the iteration will stop. (Unless we have an infinite loop which is of course a problem)


# In[12]:


moreiter-2-3: Which type of loop can be used to perform the following iteration: You choose a positive integer at random and then print the numbers from 1 up to and including the selected integer.

A. a for-loop or a while-loop
Although you do not know how many iterations you loop will run before the program starts running, once you have chosen your random integer, Python knows exactly how many iterations the loop will run, so either a for-loop or a while-loop will work.


# In[15]:


eve_nums = []
n=0
while(n<=15):
    if n%2 == 0:
        eve_nums.append(n)
    n=n+1


# In[ ]:


#Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.


list1 = [8, 3, 4, 5, 6, 7, 9]
tot = 0
for elem in list1:
    tot = tot + elem
    
accum=0
i = len(list1)
b=0
while(b<i):
    accum = accum + list1[b]
    b=b+1


# In[ ]:


#Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.

def stop_at_four():  
    list_=[3,7,4,8,3]
    accum_lst=[]
    accum_var=0
    
    while list_[accum_var] !=4:
        accum_lst.append(list_[accum_var])
    accum_var+=1
    return accum_lst
print(stop_at_four())

