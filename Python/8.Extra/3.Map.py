

# def square1 (a):
#     return a*a
# print(square1(3))
# # print(map(square,3)) mapping is for sqquence not for int

# #mapping
# def square2 (a):
#     return a*a
# print(list(map(square2,[1,2,3,4,5])))
# #mapping with lambda
# print(list(map(lambda numb : numb*numb ,[1,2,3,4,5])))

#when ever we want to change/update item in sequence we use map()

# #double item of list
# list1 = [2,5,8,4,9,3]
# print(list(map(lambda numb : numb + numb,list1)))

#sysntax:
#map( function_to_update , sequence)
# function_to_update ==> a function to which map passes each element of given iterable_sequence
# sequence ==> iterable which is to be mapped

# numbers = [2,5,8,4,9,3]
# for numb in numbers:
#     sum = sum + numb
# print(sum)
# sum =0


# numbers = [2,5,8,4,9,3]
# print(int(map(lambda numb : ,numbers)))



# # now what if u wan to add all element in the list ????
# numbers = [2,5,8,4,9,3]
# print(int(map(numb for numb : ,numbers))) # for loop
# print(int(map(lambda numb : ,numbers))) # for loop in lambda
# how can u put for loop in map function or in lambda
#its impossible
# so here come the use of reduce() to perform mapping of (function_accumulating/iterating_sequence_element) and sequence