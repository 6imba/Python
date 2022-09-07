
# # The slice object is used to slice a given sequence (string, bytes, tuple, list or range) or any object which supports sequence protocol (implements __getitem__() and __len__() method).

# # The slice() function returns a slice object.
# # A slice object is used to specify how to slice a sequence.
# # You can specify where to start the slicing, and where to end.
# # You can also specify the step, which allows you to e.g. slice only every other item.

# # Syntax
# # slice(start, end, step)

# # Syntax:
# # slice(stop)
# # slice(start, stop, step)

# # Parameter	Description
# # start	Optional. An integer number specifying at which index_position to start the slicing. Default is 0
# # end	An integer number specifying at which position to end the slicing
# # step	Optional. An integer number specifying the step of the slicing. Default is 1


#1
# # Create a tuple and a slice object. Start the slice object at position 3, and slice to position 5, and return the result:
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(3, 5)
# print(a)
# print(type(a))
# print(x)
# print(type(x))
# print(a[x])
# print(type(a[x]))




# # Create a tuple and a slice object. Use the step parameter to return every third item:

# a = ("abcdefgh")
# x = slice(0, 8, 3)
# print(x)
# print(type(x))
# print(a)
# print(type(a))
# print(a[x])
# print(type(a[x]))




# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# print(x)
# print(type(x))
# print(a)
# print(type(a))
# print(type(a[x]))
# x = slice(2, 9, 3)
# x = slice(9, 12)
# x = slice(9, 12, 4)
# print(a[x])



# # Example 1: Create a slice object for slicing
# # contains indices (0, 1, 2)
# result1 = slice(3) # Syntax : slice(stop)
# print(result1)

# # contains indices (1, 3)
# result2 = slice(1, 5, 2)
# print(slice(1, 5, 2))


# # Example 2: Get substring using slice object
# # Program to get a substring from the given string 

# py_string = 'Python'

# # stop = 3
# # contains 0, 1 and 2 indices
# slice_object = slice(3) 
# print(py_string[slice_object])  # Pyt

# # start = 1, stop = 6, step = 2
# # contains 1, 3 and 5 indices
# slice_object = slice(1, 6, 2)
# print(py_string[slice_object])   # yhn


# # Example 3: Get substring using negative index
# py_string = 'Python'

# # start = -1, stop = -4, step = -1
# # contains indices -1, -2 and -3
# slice_object = slice(-1, -4, -1)

# print(py_string[slice_object])   # noh



# # Example 4: Get sublist and sub-tuple
# py_list = ['P', 'y', 't', 'h', 'o', 'n']
# py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# # contains indices 0, 1 and 2
# slice_object = slice(3)
# print(py_list[slice_object]) # ['P', 'y', 't']

# # contains indices 1 and 3
# slice_object = slice(1, 5, 2)
# print(py_tuple[slice_object]) # ('y', 'h')  


# # Example 5: Get sublist and sub-tuple using negative index
# py_list = ['P', 'y', 't', 'h', 'o', 'n']
# py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# # contains indices -1, -2 and -3
# slice_object = slice(-1, -4, -1) 
# print(py_list[slice_object])  # ['n', 'o', 'h']

# # contains indices -1 and -3
# slice_object = slice(-1, -5, -2)
# print(py_tuple[slice_object]) # ('n', 'h')



# # Example 6: Using Indexing Syntax for Slicing
# The slice object can be substituted with the indexing syntax in Python.

# You can alternately use the following syntax for slicing:

# obj[start:stop:step]
# For example,

# py_string = 'Python'

# # contains indices 0, 1 and 2
# print(py_string[0:3])  # Pyt

# # contains indices 1 and 3
# print(py_string[1:5:2]) # yh



# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# print(a[:])
# print(a[0:7])
# print(a[0:8])
# print(a[0:9])
# print(a[0:10])
# print(a[2:5])
# print(a[::2])