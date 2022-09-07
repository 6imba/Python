#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

# Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.

# Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

# Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.

# Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.

# Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


lista = [1,4,6,7,9,5,0,3]
sublist = []
def sublist(x):
    for alll in x:
        a

X = (1,4,6,7,9,5,0,3)
print(sublist(X))


# def sublist(lst):
#     counter = 0
#     new =[]
#     while counter<len(lst):
#         if lst[counter] == 5:
#            return new
#         else:
#             new.append(lst[counter])
#         counter+=1
#     return new
# print(sublist(list(map(int, input().strip().split(',')))))
# 
# 

# In[14]:


def sublist(x):
    sub = []
    x = (num for num in x)  # create a generator
    num = next(x, 5)  
    while num != 5:
        sub.append(num)
        num = next(x, 5)  # iterate
    return sub

x = [1, 3, 4, 5, 1, 2, 3]
sublist(x)

>>> [1, 3, 4]


# In[11]:


def sublist(x):
    accum = 0
    sub = []
    while accum < len(x):
        if x[accum]== 5:
            return sub
        else:
            sub.append(x[accum])
        accum = accum +1
    return sub

x = [1, 3, 4, 5,6,7,8]
print(sublist(x))


# In[17]:


num = [1, 2, 3, 17, 1, 3, 5, 4, 3, 7, 5, 6, 9]
new = []
def check_nums(x):
    idx = 0
    while idx < len(x) and x[idx] != 7:
        print(idx)
        new.append(x[idx])
        idx += 1
    print(idx)
    return new
print(check_nums(num))


# In[22]:


def check(x):
    sub=[]
    n=0
    while()


# In[35]:


def check_nums(x):
    sub_list = []
    i=0
    while i<len(x) and x[i] != 7:
        sub_list.append(x[i])
        i=i+1
    return sub_list     

lista = [1,6,2,3,9] 
print(check_nums(lista))


# In[36]:


def sublist(string_lst):
    sub = []
    i=0
    while(i<len(string_lst) and string_lst[i] != 'STOP'):
        sub.append(string_lst[i])
        i=i+1
    return sub
main_list = ['a b c d','go','ready','stop','STOP']    
print(sublist(main_list))


# In[37]:



def stop_at_z(aaa):
    sub = []
    i=0
    while(i<len(aaa) and aaa[i] != 'z'):
        sub.append(aaa[i])
        i=i+1
    return sub
listss = ['a','d','Z','ffbfb','z','t']
print(stop_at_z(listss))    


# In[38]:



sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2=0 #accumulator variable
i=0 # iteration variable
while(i<len(lst)):
    sum2 = sum2 + lst[i]
    i=i+1


# In[39]:


def beginning(x):
    i=0
    acum_sub_list = []
    while(i<len(x) and x[i] !='bye'):
        acum_sub_list.append(x[i])
        i=i+1
    if(len(x)>10):
        return acum_sub_list[:10]
    elif(len(x)<10):
        return acum_sub_list
        
        
main_list = [1,2,3,4,5,6,7,8,9,0,12,'bye']
main_list = [1,2,0,12,'bye']


# In[43]:


def beginning(x):
    i=0
    acum_sub_list = []
    while(i<len(x) and x[i] !='bye'):
        acum_sub_list.append(x[i])
        i=i+1
    if(len(x)>10):
        z=[]
        i=0
        while i<10:
            z.append(acum_sub_list[i])
            i=i+1
        return z
    elif(len(x)<10):
        return acum_sub_list
        
        
main_list = [1,2,3,4,5,6,7,8,9,0,12,'bye']
#main_list = [1,2,0,12,'bye']
print(beginning(main_list))

