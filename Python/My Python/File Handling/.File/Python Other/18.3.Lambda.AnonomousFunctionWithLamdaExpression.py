# # 1
# def sub(x):
#     return x-1
# print(sub(5))
# print(sub)
# print(type(sub))


# # 2
# # Anonomous Function With Lamda Expression
# # To further drive home the idea that we are passing a function object as a parameter to the sorted object, let’s see an alternative notation 
# # for creating a function, a lambda expression. The syntax of a lambda expression is the word “lambda” followed by parameter names, separated by
# #  commas but not inside (parentheses), followed by a colon and then an expression. lambda arguments: expression yields a function object. This 
# # unnamed object behaves just like the function object constructed below.
# def fname(arguments):
#     return expression
# def func(agrs):
#     return rel_var
# equivalent to :
# func = lambda agrs:rel_var

# sub = lambda x:x-1
# print(sub(5))
# print(sub)
# print(type(sub))

# #return is implicit in lambda


# # 3
# stringing = 'Rima'

# def last_char(s):
#     return s[-1]
# print(last_char(stringing))

# last_char = lambda s:s[-1]
# print(last_char(stringing))

# def absolute(x):
#     if x>=0:
#         return x
#     else:
#         return -x


# #absolute = lambda x: if x>=0:return x else:return -x wrong syntax
# absolute = lambda x:  x if x>=0 else  -x
# print(absolute(2))

# 4
# If the input to this lambda function is a number, what is returned?
# (lambda x: -x)
#  A number of the opposite sign (positive number becomes negative, negative becomes positive).

