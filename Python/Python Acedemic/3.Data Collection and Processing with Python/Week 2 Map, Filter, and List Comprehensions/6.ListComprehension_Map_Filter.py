# # 1
# # Write a function called longlengths that returns the lengths of those strings that has atleast 4 character .
# #Manual_Dictionary_Accumulation

# def longlengths(list2):
#     dict3={}
#     for element in list2:
#         if len(element)>=4:
#             dict3[element]=len(element)
#     return(dict3)

# list1 = ['axe','apple','banana','dog','cucumber','amir']
# print(longlengths(list1))


# # 2
# #Manual_List_Accumulation
# def longlengths(list2):
#     list3=[]
#     for element in list2:
#         if len(element)>=4:
#             list3.append(len(element))
#     return(list3)

# list1 = ['axe','apple','banana','dog','cucumber','amir']
# print(longlengths(list1))


# 3.1
# only List_Mapping
# def longlengths(list2):
#     list3 = map(lambda element : len(element)>=4 , list2)
#     return list(list3)
    
# list1 = ['axe','apple','banana','dog','cucumber','amir']
# print(longlengths(list1))

# 3.1.1
# list1 = ['axe','apple','banana','dog','cucumber','amir']
# print(list(map( lambda element : element if len(element)>=4 , list1)))


# # 3.2
# # only List_Filtering
# def longlengths(list2):
#     list3 = filter(lambda element : len(element)>=4 , list2)
#     return list(list3)
    
# list1 = ['axe','apple','banana','dog','cucumber','amir']
# longlengths(list1)

# # 3.2.1
# list1 = ['axe','apple','banana','dog','cucumber','amir']
# print(list(filter( lambda element : len(element) >=4 , list1)))


# # 4.1
# #Both List_Mapping_And_Filtering
# def longlengths(list2):
#     list3 = filter(lambda element : len(element)>=4 , list2) # filter elements
#     #return map(len,list3)
#     return map(lambda s:len(s),list3)
# list1 = ['axe','apple','banana','dog','cucumber','amir'] # map length of filtered items
# list4 = longlengths(list1)
# print(list4)
# print(list(list4))



# 4.2
# list1 = ['axe','apple','banana','dog','cucumber','amir']
# print(filter( lambda elements : len(elements) >=4 , list1))
# print( list ( filter( lambda elements : len(elements) >=4 , list1)))

# list1 = ['axe','apple','banana','dog','cucumber','amir']
# items = filter( lambda elements : len(elements) >=4 , list1)
# len_item = map( lambda item : len(item),items)
# print(list(len_item))


# # 4.3 Map and filter
# list1 = ['axe','apple','banana','dog','cucumber','amir']
# len_list = map( lambda item : len(item), filter( lambda elements : len(elements) >=4 , list1))
# print(len_list)


# # # List_Comprehension

# list1 = ['axe','apple','banana','dog','cucumber','amir']
# len_list = [len(element) for element in list1 if len(element)>=4 ]
# print(len_list)

# list1 = ['axe','apple','banana','dog','cucumber','amir']
# [print(len(element)) for element in list1 if len(element)>=4 ]


# # 5
# List_Comprehenssion ==> [ expression for item in list if conditional ]


# # final Map and filter
# list1 = ['axe','apple','banana','dog','cucumber','amir']
# len_list = map( lambda item : len(item), filter( lambda elements : len(elements) >=4 , list1))
# print(len_list)

# # final List_Comprehenssion
list1 = ['axe','apple','banana','dog','cucumber','amir']
len_list = [len(element) for element in list1 if len(element) >= 4]
print(len_list)
print(type(len_list))

#reduce
from functools import reduce
print(reduce( lambda len1,len2 : len1+len2 , len_list))
print(reduce( lambda len1,len2 : len1+len2 , list(len_list)))


