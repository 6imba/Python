# #1
# old_list = ['apple', 'banana', 'coconut']
# new_list = old_list # new_list assignment
# print(new_list)

# #2
# x = ['apple', 'banana', 'coconut']
# y=[1,2,3]
# x = y #x list overwrite
# print(y)
# print(x)


# #3
# x = [3,5,7]
# x = z
# #error as x is list and z has no any defination

# #4
# old_list = ['apple', 'banana', 'coconut']
# new_list = old_list # new_list assignment
# new_list.append('graphs') # add new item at the end of new_list
# #now you may think that you have two list i.e (new_list and old_list )
# #and may think that new_list is just of copy of old_list change in new_list may not change the old_list.
# #but it change old_list also
# #With new_list = old_list, you don't actually have two lists.
# #The assignment just copies the reference address to the list, not the actual list,
# #means new_list dont copy the value hold by the old_list instead it reference address to the list of old_list
# #so both new_list and my_list refer to the same list after the assignment.
# #see the change below
# print(old_list)
# #see that adding value to new_list, adds value to old_list as both of them has reference to the same list address

# #5
# #so how can we just copy that list values rather than having reference to the list
# #solution_1
# #You can use the builtin list.copy() method (available since Python 3.3):
# #new_list = old_list.copy()
# old_list1 = ['apple', 'banana', 'coconut']
# new_list1 = old_list1.copy() # new_list assignment with .copy method
# new_list1.append('graphs') 
# print(old_list1)
# print(new_list1)

# #6
# #solution_2
# #You can use the built in list() function:
# #new_list = list(old_list)
# old_list2 = ['apple', 'banana', 'coconut']
# new_list2 = list(old_list2)# new_list assignment with the list of old_list using list function
# new_list2.append('graphs') 
# print(old_list2)
# print(new_list2)

# #7
# #solution_3
# #You can slice it:
# #new_list = old_list[:]
# #It creates a shallow copy of the whole list and is a good shorthand when you need a copy of the original list.

# old_list3 = ['apple', 'banana', 'coconut']
# new_list3 = old_list3[:]# new_list assignment with the list of old_list using slice operator
# new_list3.append('graphs') 
# print(old_list3)
# print(new_list3)

#8
#solution_4
#You can use generic copy.copy():
#import copy
#new_list = copy.copy(old_list)

# import copy
# old_list4 = ['apple', 'banana', 'coconut']
# new_list4 = copy.copy(old_list4)
# new_list4.append('graphs') 
# print(old_list4)
# print(new_list4)

#This is a little slower than list() because it has to find out the datatype of old_list first.

# #9
# #If the list contains objects and you want to copy them as well, use generic copy.deepcopy():

#solution_5
#You can use generic copy.deepcopy():
#import copy
#new_list = copy.deepcopy(old_list)

import copy
old_list5 = ['apple', 'banana', 'coconut']
new_list5 = copy.deepcopy(old_list5)
new_list5.append('graphs') 
print(old_list5)
print(new_list5)



