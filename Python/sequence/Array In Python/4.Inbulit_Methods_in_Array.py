# # Inbuilt Method In Array: 
# append(), 
# insert(), 
# pop(),  
# remove(), 
# reverse(), 
# extend()
#slice()


# # 1
# # append()
# # syntax :
# #     array_identifier.append(item/element)

# from array import array
# numbers = array('i',[1,2,3,4,5,6,7,8,9,0])
# numbers.append(666666)
# print(numbers)

# # Output : array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 666666])




# # 2
# # insert()
# # syntax :
# #     array_identifier.insert(index_number/new_element)

# from array import array
# numbers = array('i',[1,2,3,4,5,6,7,8,9,0])
# numbers.insert(5,123456789)
# print(numbers)

# # Output : array('i', [1, 2, 3, 4, 5, 123456789, 6, 7, 8, 9, 0])



# # 3.1
# # pop()
# # syntax :
# #     array_identifier.pop() ==> by default last index
# #     array_identifier.pop(index_number)

# from array import array
# numbers = array('i',[1111,2222,3333,4444,5555,6666,77777,8888,9999,0000])
# numbers.pop()
# print(numbers)

# # Output : array('i', [1111, 2222, 3333, 4444, 5555, 6666, 77777, 8888, 9999])


# # 3.2
# from array import array
# numbers = array('i',[1111,2222,3333,4444,5555,6666,77777,8888,9999,0000])
# numbers.pop(5)
# print(numbers)

# # Output : array('i', [1111, 2222, 3333, 4444, 5555, 77777, 8888, 9999, 0])



# # 4.1
# # remove() 
# # syntax : remove first appearance of the element
# #     array_identifier.remove()
# #     array_identifier.remove(element)

# from array import array
# numbers = array('i',[1111,2222,3333,4444,5555,6666,77777,8888,9999,0000])
# numbers.remove(6666)
# print(numbers)

# # Output : array('i', [1111, 2222, 3333, 4444, 5555, 77777, 8888, 9999, 0])



# # # 4.2
# # But if element doesnt exist in array it gives valueError

# from array import array
# numbers = array('i',[1111,2222,3333,4444,5555,6666,77777,8888,9999,0000])
# numbers.remove(2468)
# print(numbers)

# # Output : ValueError: array.remove(x): x not in array



# Note :
# pop()    ==> uses index_number to remove element
# remove() ==> uses element_name to remove element









# # 5
# # reverse() 

# # The reverse() method reverses the elements of the list.

# # reverse() parameter
# # The reverse() method doesn't take any arguments.

# # Return Value from reverse()
# # The reverse() method doesn't return any value. It updates the existing list.


# # syntax : reverse the order of array
# #     array_identifier.reverse()

# from array import array
# numbers = array('i',[1111,2222,3333,4444,5555,6666,77777,8888,9999,0000])
# numbers.reverse()
# print(numbers)

# # Output : array('i', [0, 9999, 8888, 77777, 6666, 5555, 4444, 3333, 2222, 1111])

# If element not found then valueError



# # 6
# # extend() 
# # syntax : extends existing array with any iterable_object(array, list, tuple)
# #     array_identifier.extend(array/iterable_object)

# # 6.1 --> extend array with array
# from array import array
# arr1 = array('i',[7,14,21,28,35])
# arr2 = array('i',[10, 20, 30, 40,50])
# arr1.extend(arr2)
# print(arr1)

# # Output : array('i', [7, 14, 21, 28, 35, 10, 20, 30, 40, 50])


# # 6.2 --> extend array with list
# from array import array
# arr1 = array('i',[7,14,21,28,35])
# arr1.extend([1,0,1,0,1,0])
# print(arr1)

# # Output : array('i', [7, 14, 21, 28, 35, 1, 0, 1, 0, 1, 0])


# # 6.3 --> extend array with tuple
# from array import array
# arr1 = array('i',[7,14,21,28,35])
# arr1.extend((1,0,1,0,1,0))
# print(arr1)

# # Output : array('i', [7, 14, 21, 28, 35, 1, 0, 1, 0, 1, 0])

# # extends existing array with any iterable_object(array, list, tuple) but not sting(str)
# arr1.extend('amir')
# TypeError: an integer is required (got type str)



# 7.1
# slice() : The slice() function returns a slice object that can use used to slice strings, lists, tuple etc.
# The syntax of slice() is:
#     slice(start, stop, step)


# # Example 1: Create a slice object for slicing
# result1 = slice(3)
# print(result1)
# # Output :
# # slice(None, 3, None)

# result2 = slice(1, 5, 2)
# print(slice(1, 5, 2))
# # Output :
# # slice(1, 5, 2)

# Here, result1 and result2 are slice objects.
# Now we know about slice objects, let's see how we can get substring, sub-list, sub-tuple, etc. from slice objects.



# # Example 2: Get substring using slice object
# main_string = 'abcdefghij'
# slice_obj = slice(3,8,2)
# sliced_sunstring = main_string[slice_obj]
# print(sliced_sunstring)
# # Output: dfh



# # Example 3: Get substring using negative index
# main_string = 'abcdefghij'
# slice_obj = slice(-2,-7,-2)
# sliced_sunstring = main_string[slice_obj]
# print(sliced_sunstring)
# # # Output: ige


# # Example 4: Get sublist and sub-tuple

# py_list = ['P', 'y', 't', 'h', 'o', 'n']
# slice_object = slice(3)
# print(py_list[slice_object]) # ['P', 'y', 't']
# # Output : ['P', 'y', 't']

# py_tuple = ('P', 'y', 't', 'h', 'o', 'n')
# slice_object = slice(1, 5, 2)
# print(py_tuple[slice_object]) # ('y', 'h')
# # Output : ('y', 'h')



# Example 5: Get sublist and sub-tuple using negative index
# py_list = ['P', 'y', 't', 'h', 'o', 'n']
# py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# # contains indices -1, -2 and -3
# slice_object = slice(-1, -4, -1) 
# print(py_list[slice_object])  # ['n', 'o', 'h']

# # contains indices -1 and -3
# slice_object = slice(-1, -5, -2)
# print(py_tuple[slice_object]) # ('n', 'h')
# Output

# ['n', 'o', 'h']
# ('n', 'h') 





# Example 6: Using Indexing Syntax for Slicing
# The slice object can be substituted with the indexing syntax in Python.

# You can alternately use the following syntax for slicing:

# obj[start:stop:step]
# For example,

# py_string = 'Python'

# # contains indices 0, 1 and 2
# print(py_string[0:3])  # Pyt

# # contains indices 1 and 3
# print(py_string[1:5:2]) # yh
# Output

# Pyt
# yh



