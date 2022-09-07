# # 1
# class A:
#     age=4
# print(A.age)


# # 2
# #error
# class A:
# print(A)


# # 3
# class A:
#     pass
# print(A)


# # 4
# class A:
#     age=4
# print(A.age)
# obj1 = A()
# print(obj1.age)

#4.1
# class A:
#     age=4
# print(A.age)
# obj1 = A()
# obj1.age = 5
# print(obj1.age)

# #4.2
# class A:
#     age=4
# print(A.age) #......
# obj1 = A()
# obj1.age = 5
# A.age = 6
# print(A.age) #......
# print(obj1.age) #......


# #4.3
# class Nepal: # create class
#     identity = 'nepali' # property of class

# print(Nepal.identity) #1.... print property of class

# newar = Nepal() #create object
# newar.identity = 'shrestha'  # set new property of object instead of assumming default property of  class # note :this doesnt chage the property of class
# print(newar.identity)

# # note :this doesnt chage the property of class
# print(Nepal.identity)



# # 5
# class A:
#     age=4
# obj1 = A()
# obj2 = A()
# print(obj1.age == obj2.age)


# # 6
# class A:
#     pass
# obj1=A()


# # constructor
# # 7
# class A:
#     def __init__(self):#constructor  #self points to the current object or current instant of object
#         print('Hi')
# obj1=A()



# # 8
# class A:
#     def __init__(self):
#         print('Hi ',self)
# obj1=A()
# print(obj1)


# 9
class A:
    pass
obj1=A()
print(obj1)
print(A)
print(A())

