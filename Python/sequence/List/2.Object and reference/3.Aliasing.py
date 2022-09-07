# # garbasge_collector
# # is check for id
# # == check for value

# # 1
# #list
# a = [2,4,6,8,10,12]
# b = [2,4,6,8,10,12]


# print(a is b)
# print(a == b)
# print(id(a))#id() in built function that identify the variable
# print(id(b))

# # 2
# a = [2,4,6,8,10,12]
# c = a
# print(c)
# print(a is c)
# print(a == c)
# print(id(a))
# print(id(c))


# # 3.1
#list
# a = [2,4,6,8,10,12]
# b = [2,4,6,8,10,12]

# print(id(a))#id() in built function that identify the variable
# print(id(b))

# a=b ##aliasing
# print('After aliasing !')
# print(id(a))#id() in built function that identify the variable
# print(id(b))
# print(a is b)
# print(a == b)

# # # 3.2
# #list
# a = [2,4,6,8,10,12]
# b = [2,4,6,8,10,12]

# # print(id(a))#id() in built function that identify the variable
# # print(id(b))

# b=a ##aliasing
# print('After aliasing !')
# print(id(a))#id() in built function that identify the variable
# print(id(b))
# print(a is b)
# print(a == b)





# 4
# b = ['q', 'u', 'i']
# z = b
# b[1] = 'i'
# print(b)
# z.remove('i')
# print(z)
# print(b)
# # here z and b represent to same id








