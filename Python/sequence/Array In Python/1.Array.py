# #1 Without array:

# student1 = 'Amir'
# student2 = 'Samir'
# student3 = 'Ram'
# student4 = 'Hari'
# student5 = 'Shyam'

# print(student1)
# print(student2)
# print(student3)
# print(student4)
# print(student5)


# ................................................................................................................................


# #2 List
# students = ['Amir', 'Samir', 'Ram', 'Hari', 'Shyam']
# print(students)
# print(type(students))
# for std in students:
#     print(std)


# ................................................................................................................................


# # 3 array:

# # 3.1
# import array #import module named as array which contain different class, object, variable etc.
# numbers = array.array('i',[1,2,3,4,5,6,7,8,9,0])
# print(numbers)
# print(type(numbers))
# for numb in numbers:
#     print(numb)


# # 3.2
# import array as arr #import module named as array as arr
# numbers = arr.array('i',[1,2,3,4,5,6,7,8,9,0])
# print(numbers)
# print(type(numbers))
# for numb in numbers:
#     print(numb)



# # 3.3
# from array import * #import all class, object, variable etc. from module named as array
# numbers = array('i',[1,2,3,4,5,6,7,8,9,0])
# print(numbers)
# print(type(numbers))
# for numb in numbers:
#     print(numb)


# # 3.4
# from array import array #import array class from module named as array
# numbers = array('i',[1,2,3,4,5,6,7,8,9,0])
# print(numbers)
# print(type(numbers))
# for numb in numbers:
#     print(numb)


# # Therefore Syntax :
# # import array as arr
# # array_identifier = arr.array('type_code', [elements])
# # OR,
# # array_identifier = arr.array('array_datatype', [list_of_elements])

# Note : There is no any type code for string or char in string in array
# So, you can either encode/convert default array module or use/install python package called as numbpy
# In python array module has less feature so we have external module/package with more feature in python which allow us to use string,int,float,char etc.

#Index ==> position number of array/lists elements. starts with 0




# # Int array
# # 3.5
# from array import array #import array class from module named as array
# numbers = array('i',[1,2,3,4,5,6,7,8,9,0])
# print(numbers)
# print(type(numbers))
# for numb in numbers:
#     print(numb)
#     print(type(numb))


# # Float array
# # 3.6
# from array import array #import array class from module named as array
# numbers = array('f',[1,2,3,4,5,6,7,8,9,0])
# print(numbers)
# print(type(numbers))
# for numb in numbers:
#     print(numb)
#     print(type(numb))




# # Create Empty Array named as arr1.
# from array import array
# arr1 = array('i',[])