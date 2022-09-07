#1
# # now what if u wan to add all element in the list ????
# numbers = [2,5,8,4,9,3]
# print(int(map(numb for numb : ,numbers))) # for loop
# print(int(map(lambda numb : ,numbers))) # for loop in lambda
# how can u put for loop in map function or in lambda
#its impossible
# so here come the use of reduce() to perform mapping of (function_accumulating/iterating_sequence_element) and sequence

# #2
# def add_all(a,b): # iterating ever first and after element upto all sequence
#     return a+b

# list1 = [2,5,8,5,4,9]
# print(reduce(add_all,list1))

#3
# # but u can use reduce() method directly as reduce() function belongs to the modules called functools
# # so first of all you have to import reduce() function from  modules called functools

# from functools import reduce

# def add_all(a,b): # iterating ever first and after element upto all sequence i.e : [2,4,5,6] => [{(2+4) +5} +6]
#     return a+b

# list1 = [2,5,8,5,4,9]
# print(reduce(add_all,list1))


# #4
# # now using reduce() function with lambda expresion/function
from functools import reduce
list6 = [1,2,3,4,5,6]
print(lambda numb1,numb2 : numb1+numb2 , list6)
print(reduce(lambda numb1,numb2 : numb1+numb2 , list6))


# syntax : reduce(func, iterable[, initial])
# Where func is the function on which each element in the iterable gets cumulatively applied to, and initial is the optional value that gets
#  placed before the elements of the iterable in the calculation, and serves as a default when the iterable is empty. The following should be
#   noted about reduce(): 1. func requires two arguments, the first of which is the first element in iterable (if initial is not supplied) and
#    the second the second element in iterable. If initial is supplied, then it becomes the first argument to func and the first element in iterable 
#    becomes the second element. 2. reduce "reduces" (I know, forgive me) iterable into a single value.

# from functools import reduce
# list6 = [1,2,3,4,5,6]
# print(reduce(lambda numb1,numb2 : numb1+numb2 , list6,100)) # optinal_value  => 100 iteration begin with 100 => first_iteration = 100
