

#It is also important to realize that with append, the original list is simply modified. On the other hand, with concatenation, an entirely new list is created. 



# fruits = ['apple','banana','coconut','papaya']
# print(fruits)
# print(id(fruits))
# fruits.append('orange')#append
# print(fruits)
# print(id(fruits))
# fruits = fruits + ['pine']#concatenate
# print(fruits)
# print(id(fruits))




# #This might be difficult to understand since these two lists appear to be the same. In Python, every object has a unique identification tag. Likewise, there is a built-in function that can be called on any object to return its unique id. The function is appropriately called id and takes a single parameter, the object that you are interested in knowing about. You can see in the example below that a real id is usually a very large integer value (corresponding to an address in memory). In the textbook though the number will likely be smaller.
# #This can be seen in the following codelens example where``newlist`` refers to a list which is a copy of the original list, origlist, with the new item “cat” added to the end. origlist still contains the three values it did before the concatenation. This is why the assignment operation is necessary as part of the accumulator pattern.
# origlist = [45,32,88]
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list before changes
# newlist = origlist + ['cat']
# print("newlist:", newlist)
# print("the identifier:", id(newlist))              #id of the list after concatentation
# a= origlist.append('cat')
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list after append is used

# #It is also important to realize that with append, the original list is simply modified. On the other hand, with concatenation, an entirely new list is created.




# origlist = [45,32,88]
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list before changes
# origlist = origlist + ['cat']
# print("origlist:", origlist)
# print("the identifier:", id(origlist))              #id of the list after concatentation
# origlist.append('cat')
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list after append is used




# original = 55
# print("original:", original)
# print("the identifier:", id(original))             #id of the list before changes
# original = original + 6
# print("original:", original)
# print("the identifier:", id(original))              #id of the list after concatentation
# origlist.append(8)
# print("original:", original)#appends for list only
# print("the identifier:", id(original))             #id of the list after append is used





# #We have previously described x += 1 as a shorthand for x = x + 1. With lists, += is actually a little different. In particular, origlist += [“cat”] appends “cat” to the end of the original list object. If there is another alias for `origlist, this can make a difference, as in the code below. See if you can follow (or, better yet, predict, changes in the reference diagram).

# firstlist = [23,65,87]
# print(firstlist)
# newlist = firstlist
# print(newlist)

# print('+= Operator :')
# firstlist += ['cat']
# print(firstlist)
# print(newlist)

# print('Concatenate :')
# firstlist = firstlist + ['cow']
# print(firstlist)
# print(newlist)





# st = "Warmth"
# a = []
# b = a + [st[0]]
# c = b + [st[1]]
# d = c + [st[2]]
# e = d + [st[3]]
# f = e + [st[4]]
# g = f + [st[5]]
# print(g)





# alist = [4,2,8,6,5]
# alist = alist + 999
# print(alist)
# # int with list error

# alist = [4,2,8,6,5]
# alist = alist + '999'
# print(alist)
# # str with list error

# alist = [4,2,8,6,5]
# alist = alist + [999]#int
# print(alist)

# alist = [4,2,8,6,5]
# alist = alist + ['999']#str
# print(alist)

