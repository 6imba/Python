#Numpy in python is a library/package that contains classes, function, variables, and large library of mathematiacal function etc.
#Python doesnt support Multi-D array but Numpy does.
#when we install packages where does it get installed ?



# import numpy as np
# a = np.array([1,2,3])
# print(a)
# print(type(a))

# Output:
# [1 2 3]
# <class 'numpy.ndarray'> here ndarray is n-dimensional array.


# # 2-D array using python
# import array as arr #import module named as array as arr
# numbers = arr.array('array',[arr.array('i',[1,2,3,4]),arr.array('i',[5,6,7,8])])
# print(numbers)
# print(type(numbers))
# for numb in numbers:
#     print(numb)

# # 2-D list using python
# arr = [[1,2], [3,4]]
# print(arr)
# print(type(arr))

# # 2-D list using python
# arr = [[0,0], [0,0]]
# print(arr)
# print(type(arr))

# # Output :
# # [[0, 0], [0, 0]]


# # # 2-D array using numbpy
# import numpy as np
# arr = np.zeros((2,2))  #zero is method to create array with all element 0
# print(arr)
# print(type(arr))

# # Output :
# # [[0. 0.]
# #  [0. 0.]]
# # <class 'numpy.ndarray'>


# # # 1-D array using numbpy
# import numpy as np
# arr1 = np.ones(3)  #ones is method to create 1-D array
# print(arr1)
# arr2 = np.ones(5)
# print(arr2)
# arr2 = np.ones((5,2))
# print(arr2)

# print('.......................')

# arr2 = np.ones((5,2))
# for arr in arr2:
#     print(arr)


# print('.......................')

# arr3 = np.ones((3,9))
# print(arr3)
# print('****************************')
# for arr in arr3:
#     print(arr)



# # 3-D array using numbpy
# import numpy as np
# arr1 = np.array([ [1,2], [3,4,5], [6,7,8,9] ])
# print(arr1) 
# for arr in arr1:
#     print(arr)

# # 3-D array using numbpy
# import numpy as np
# arr1 = np.array([ [ [1,2], [3,4,5] ], [ [6,7,8,9] ] ])
# for arr in arr1:
#     print(arr)

# # 3-D array using numbpy
# import numpy as np
# arr1 = np.array([ [ [1,2], [3,4,5] ], [ [6,7,8,9], [1,0,1] ] ])
# for arr in arr1:
#     print(arr)

# print(arr1.shape)


# # 3-D array using numbpy
# import numpy as np
# arr1 = np.array([ [ [1,2,3], [3,4,5], [3,4,5], [3,4,5] ], [ [6,7,8], [1,0,1], [3,4,5], [3,4,5] ] ])
# for arr in arr1:
#     print(arr)
# print(arr1.shape)


# # 3-D array using numbpy
# import numpy as np
# arr1 = np.array([ [ [1,2,3], [3,4,5], [3,4,5], [3,4,5] ], [ [6,7,8], [1,0,1], [3,4,5], [3,4,5] ] ])
# print(arr1[0][0][0])
# # print(arr1[0])
# # print(arr1[0][0])
# # print(arr1[0][0][0])


# # Slicing
# # 3-D array using numbpy
# import numpy as np
# arr1 = np.array([ [1,2,3,5], [3,4,5,7], [3,4,7,5], [3,3,4,5] ])
# print(arr1[:2, :2])
# print(arr1[1:4, 1:3])

# # Output :
# # [[1 2]
# #  [3 4]]
# # [[4 5]
# #  [4 7]
# #  [3 4]]



# # Broadcasting
# import numpy as np
# a = np.array([0,1,2,3])
# b = np.array([5,5,5,5])
# print(a+b)

# # Output :
# # [5 6 7 8]





# a = [1,2,3,4]
# print(a+5)
# # Output :
# # TypeError: can only concatenate list (not "int") to list




# import numpy as np
# a = np.array([1,2,3,4])
# print(a+5)
# # Output : [6 7 8 9]





# # Broadcasting operation in nnumpy stretch out one among two variable if not of same type.

# i.e
# a = np.array([1,2,3,4])
# a+5 ===> [1,2,3,4] + [5,5,5,5]

# because of board casting we can perform binary operation on different size arrays
# but not a + [1,2] if two array has different shape we cannot apply boardcasting.
# i.e
# a = np.array([1,2,3])   ===> a.shape  ===> 3
# b = np.array([[1,2,3,4], [5,6,8,9]])   ===> b.shape  ===> (2,4)

# For boardcasting number of column in arrays must be same
# i.e
# a = np.array([1,2,3,4])   ===> a.shape  ===> 4
# b = np.array([[1,2,3,4], [5,6,8,9]])   ===> b.shape  ===> (2,4)





