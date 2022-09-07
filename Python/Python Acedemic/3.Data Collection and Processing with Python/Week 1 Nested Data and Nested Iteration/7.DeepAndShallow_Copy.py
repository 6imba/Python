# # 1
# list1 = [2,4,6,8,10]
# list2 = list1#shallow copy # both list1 and list2 reference to same object
# print(list1)
# print(list2)


# # 2
# list1 = [2,4,6,8,10]
# list2 = list1#shallow copy
# list1.append(666666)
# print(list1)
# print(list2)


# # 3
# list1 = [2,4,6,8,10]
# list2 = []#deeper copy to new object
# for item in list1:
#     list2.append(item)#deeper copy
# print(list1)
# print(list2)


# 4
# list1 = [2,4,6,8,10]
# list2 = list1[:]#deeper copy
# print(list1)
# print(list2)


# # 5
# list1 = [2,4,6,8,10]
# list2 = list1[:]#deeper copy slice to new object
# list1.append(666666)
# print(list1)
# print(list2)


# # 6
# #Shallow and deep copy

# list1 = [2,4,6,8,10]
# list2 = list1 # shallow copy
# list3 = list1[:]# deeper copy slice to new object
# list1.append(666666)
# print(list1)# orginal
# print(list2)# shallow copy
# print(list3)# deeper copy


# # 7
# # #Shallow and deep copy
# list1 = [[2,4],['a','b']]
# list2 = list1 # shallow copy
# list3 = list1[:]# deeper copy slice to new object
# list1.append(666666)
# print(list1)# orginal
# print(list2)# shallow copy
# print(list3)# deeper copy


# # 8
# #Shallow and deep copy
# import copy
# list1 = [[2,4],['a','b']]
# list2 = list1[:] # shallow copy
# list3 = copy.deepcopy(list1)# deeper copy slice to new object
# list1.append(666666)

# print(list1)# orginal
# print(list2)# shallow copy
# print(list3)# deeper copy


# 9
#Shallow and deep copy
import copy
list1 = [[2,4],['a','b']]
list2 = list1 #assignment operator
list3 = list1[:] # shallow copy or deep copy ?
list4 = copy.deepcopy(list1)# deeper copy slice to new object
list1.append(666666)
list1[0].append(6)

print('List_1 ( orginal) : ',list1)# orginal
print('Id_1 : ',id(list1))
print('List_2  (assignment) : ',list2)#assignment 
print('Id_2 : ',id(list2))
print('List_3 (shallow_copy) : ',list3)# shallow copy
print('Id_3 : ',id(list3))
print('List_4 (deeper_copy) : ',list4)# deeper copy
print('Id_4 : ',id(list4))


# # 10
# import copy
# original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]

# shallow_copy_version = original[:] 
# # the original and the shallow copy diverge, because the original gets Hi there at the end. So we appended to the top level list, and there the original is different than the shallow copy. So Hi there got appended to original, did not get appended to shallow copy.

# deeply_copied_version = copy.deepcopy(original)

# original.append("Hi there")
# original[0].append(["marsupials"])
# print("-------- Original -----------")
# print(original)
# print("-------- deep copy -----------")
# print(deeply_copied_version)
# print("-------- shallow copy -----------")

# print(shallow_copy_version)
# # the original and the shallow copy diverge, because the original gets Hi there at the end. So we appended to the top level list, and there the original is different than the shallow copy. So Hi there got appended to original, did not get appended to shallow copy.


# # 11
# numb1 = [1,2,3,4,5,6,7]
# print(id(numb1))
# numb2 = numb1
# print(numb2)
# print(type(numb2))
# print(id(numb2))

# numb3=numb1[:]
# print(numb3)
# print(type(numb3))
# print(id(numb3))

# print(numb2 is numb3 )
# print(numb2 == numb3 )


# # 12
# # #Shallow and deep copy
# import copy
# list1 = [[2,4],['a','b']]
# print(list1)# orginal

# list2 = list1 # shallow copy
# list3 = list1[:] # deep copy 
# list4 = copy.deepcopy(list1)# deep copy  with deepcopy() method of copy module
# list1.append(666666)
# list1[0].append(6)

# print(list1)# orginal
# print(list2)# shallow copy
# print(list3)# deeper copy
# print(list4)# deeper copy

