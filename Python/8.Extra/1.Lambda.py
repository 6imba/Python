#lambda function =-==> inline funtion


# # normal_function
# def square (a):
#     return a*a
# print(square(2))


# #lambda_function
# square = lambda a: a*a
# print(square(2))


# # normal_function
# def add (a,b):
#     return a+b
# print(add(2,3))


# #lambda_function
# add = lambda a,b: a+b
# print(add(1,2))


# list1 = [[4,2],[4,0],[11,6],[1,5],[20,1]]
# # print(id(list1))
# list1.sort()
# print(list1)
# # print(id(list1))


# # # sort list4 according to index[0] of list item
# def clause_func (list4):
#     return list4[0]

# list4 = [[4,2],[11,6],[1,5],[20,1]]
# list4.sort(key = clause_func)
# print(list4)


# # sort list3 according to index[1] of list item
# def clause_func (list2):
#     return list2[1]

# list2 = [[4,2],[11,6],[1,5],[20,1]]
# list2.sort(key = clause_func)
# print(list2)

# # sort list3 according to index[2] of list item
# def clause_func (a_list):
#     return a_list[2]

# list3 = [[4,2,8],[11,6,3],[1,5,44],[20,1,13]]
# list3.sort(key = clause_func)
# print(list3)

# list5 = [[4,2,8],[11,6,3],[1,5,44],[20,1,13]]
# list5.sort(key = lambda list5:list5[1] )
# print(list5)

# list5 = [[4,2,8],[11,6,3],[1,5,44],[20,1,13]]
# list5.sort(key = lambda x:x[1] )
# print(list5)

# list5 = [[4,2,8],[11,6,3],[1,5,44],[20,1,13]]
# print(sorted(list5,key = lambda x:x[1] ))






# # 2.1
# # Manual_Accumulation
# def quard(numb_list1):
#     numb_list2 = []
#     for numb in numb_list1:
#         numb_list2.append(numb*4)
#     return numb_list2

# numb_list = [3, 4, 6, 7, 0, 1]
# print(quard(numb_list))



# # 2.3
# # Mapping
numb_list = [3, 4, 6, 7, 0, 1]
quard = map((lambda numb: 4*numb), numb_list)
print(quard)#map_object
print(list(quard))


# here
# for numb in numbs:   ............   2.2
#         numb_list2.append(numb*4)
#     return numb_list2

# euqivalent to ==>

# lambda numb:4*numb .............   2.3

# Therefore, You don’t have to initialize an accumulator or iterate with a for loop at all.