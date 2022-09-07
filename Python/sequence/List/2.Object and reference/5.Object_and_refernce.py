# # mutable_object vs immutable_object

# #string
# a = 'banana'
# b = 'banana'

# print(a is b)
# print(a == b)
# print(id(a))#id() in built function that identify the variable
# print(id(b))
# #string is immutable

# #list
# a = [2,4,6,8,10,12]
# b = [2,4,6,8,10,12]

# print(a is b)
# print(a == b)
# print(id(a))#id() in built function that identify the variable
# print(id(b))
# #list is mutable


# if two string_variable has same value then they both reference to same meomry_id
# but
# if two list_variable has same value then they both donot reference to same meomry_id, instead they reference to diddferent/separate memory_id



# a = [1,2,3,4]
# b=a
# a+=[5,6]
# b+=[7]
# print(a)
# print(b)
# print(id(a))
# print(id(b))



# a = [1,2,3,4]
# b=a
# a+=[5,6]
# b=b+[7]
# print(a)
# print(b)
# print(id(a))
# print(id(b))
