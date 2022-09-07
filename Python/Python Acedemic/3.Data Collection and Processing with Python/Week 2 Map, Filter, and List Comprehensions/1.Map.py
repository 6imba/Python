# 1
# # Introduction: Map, Filter, List Comprehensions, and Zip¶
# # Let’s revisit the accumulator pattern. We have frequently taken a list and produced another list from it that contains either a subset of the items or a transformed version of each item. When each item is transformed we say that the operation is a mapping, or just a map of the original list. When some items are omitted, we call it a filter.

# # Python provides built-in functions map and filter. Python also provides a new syntax, called list comprehensions, that lets you express a mapping and/or filtering operation. Just as with named functions and lambda expressions, some students seem to find it easier to think in terms of the map and filter functions, while other students find it easier to read and write list comprehensions. You’ll learn both ways; one may even help you understand the other. Most python programmers use list comprehensions, so make sure you learn to read those. In this course, you can choose to learn to write list comprehensions or to use map and filter, whichever you prefer. You should learn to read both list comprehensions and map/filter.

# # Other common accumulator patterns on lists aggregate all the values into a single value.

# # Map, and filter are commands that you would use in high-performance computing on big datasets. See MapReduce on Wikipedia.


# # 2

# def square(numbs):
#     list2 = []
#     for all_numb in numbs: # manual_accumulation
#         new_element = all_numb * all_numb
#         list2.append(new_element)
#     return list2

# list1 = [2,3,5]
# print(list1)
# new_list = square(list1)
# print(new_list)

# This manual_accumulation pattern of computation is so common that python offers a more general way to do mappings,
# the map function, that makes it more clear what the overall structure of the computation is.
# map takes two arguments, a function and a sequence. The function is the mapper that transforms items. 
# It is automatically applied to each item in the sequence. 
# You don’t have to initialize an accumulator or iterate with a for loop at all.


# # 2
# def square_function(numbs): #transformer_function
#     return numbs * numbs

# def square_mapping(list2): #mapping
#     list3 = map(square_function,list2)#inbulit map function
#     print(type(list3))
#     return list3 # mapping makes variable of type map
#     # return list(list3)
    
# list1 = [2,3,5]
# print(list1)
# list4 = square_mapping(list1)
# print(list4)


# # Technically, in a proper Python 3 interpreter, the map function produces an “iterator”, which is like a list but produces the items as they are needed. 
# # Most places in Python where you can use a list (e.g., in a for loop) you can use an “iterator” as if it was actually a list.
# # So you probably won’t ever notice the difference. If you ever really need a list, you can explicitly turn the output of map into a list: list(map(...)). 
# # In the runestone environment, map actually returns a real list, 
# # but to make this code compatible with a full python environment, we always convert it to a list.

# # As we did when passing a function as a parameter to the sorted function, we can specify a function to pass to map either by referring to a function by name, or by providing a lambda expression.


# # 3
# def trans_func(value): # transformer_function => trans_func
#     return 3*value

# def triple_mapping(org_1_list): # mapping_function
#     new_seq = map(trans_func, org_1_list) # map_method
#     return list(new_seq)

# org_list = [2, 5, 11]
# print(org_list)

# triple_map_list = triple_mapping(org_list)
# print(triple_map_list)


# #4
# def quadruple_mapping(org_2_list):# mapping_function
#     new_seq = map(lambda value: 4*value, org_2_list)# map_method    # transformer_function => lambda
#     return list(new_seq)


# org_list = [2, 5, 11]
# print(org_list)

# quadruple_map_list = quadruple_mapping(org_list)
# print(quadruple_map_list)



# # Of course, once we get used to using the map function, it’s no longer necessary to define functions like tripleStuff and quadrupleStuff.

# things = [2, 5, 9]
# things4 = map((lambda value: 4*value), things)
# print(list(things4))

# # or all on one line
# print(list(map((lambda value: 5*value), [1, 2, 3])))


# # 7
# # 1. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
# lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
# greeting_doubled = map(lambda item : item * 2 , lst)
# print(list(greeting_doubled))



# 2. Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
abbrevs_upper = list(map(lambda item:item.upper() , abbrevs))
print(abbrevs_upper)

