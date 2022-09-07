# Passing the function as an argument/ assign function in variable
# Passing the function as an argument
# Returning functions from another functions.
# inner function or nested function are used along with decoretor





# 1
# def fun1():
#     print('hi')

# print(fun1)
# fun1()



# # 2
# def fun1():
#     print('hi')

# print(fun1)
# fun1()
# print(fun1())


# # 3
# def fun1():
#     print('hi')
#     return 0

# print(fun1)
# fun1()
# print(fun1())



# # 4
# def fun1():
#     print('hi')

# fun2 = fun1
# fun2


# # 5
# def fun1():
#     print('hi')

# fun2 = fun1
# fun2()


# # 6
# def fun1():
#     print('hi')

# fun2 = fun1
# print(fun2)


# # 7
# def fun1():
#     print('hi')

# fun2 = fun1
# print(fun2())

# # 7.1
# def fun1():
#     print('hi')

# fun2 = fun1
# fun2()




# # 8
# def fun1():
#     print('hi')

# fun2 = fun1()
# fun2
# x = fun1()
# x()




# # 9
# def fun1():
#     print('hi')

# fun2 = fun1()
# fun2()
# # TypeError: 'NoneType' object is not callable


# # 10
# def fun1():
#     print('hi')

# fun2 = fun1()
# print(fun2)


# # 11
# def fun1():
#     print('hi')

# fun2 = fun1()
# print(fun2())
# # TypeError: 'NoneType' object is not callable


# # 12
# def fun1():
#     print('hi')
#     return 0

# fun2 = fun1()
# print(fun2())
# # TypeError: 'NoneType' object is not callable


# # 13
# def fun1():
#     print('hi')

# fun2 = fun1
# print(id(fun1))
# print(id(fun2))
# del fun1
# fun2()

# # 14
# def fun1():
#     print('hi')

# fun2 = fun1
# del fun1
# fun1()




# Built-in functions : int, print, sum etc
# function can take fuction as paramter, pass function as argument, function can return function,
# nested function 



# # Python program
# # functions being be treated as objects
# def comp_name(text):
#    return text.isupper()
# print(comp_name)
# print(type(comp_name))
# print(comp_name("TUTORIALSPOINT"))

# new_name = comp_name #referencing a function with the object
# print(new_name)
# print(type(new_name))
# print(new_name("TUTORIALSPOINT"))
# # Output
# # True
# True





# def f():
#     return 'f'

# print( type(f) ) # result: <class 'function'>
# print( type(f()) ) # result: <class 'str'>






# def hello():
#     return 'hi'

# print(id(hello))   # here it returns the id of the function name

# print(id(hello())) # here it returns the id 
#                    # of the object returned by the function itself




# def hello():
#     print('hi')

# print(id(hello))   # here it returns the id of the function name

# print(id(hello())) # here it returns the id 
#                    # of the object returned by the function itself





# # Inner function
# def outer_func():
#     def inner_func():
#         print("Hello, World!")
#     inner_func()

# outer_func()



# #factorial
# def factorial(number):
# ...     # Validate input
# ...     if not isinstance(number, int):
# ...         raise TypeError("Sorry. 'number' must be an integer.")
# ...     if number < 0:
# ...         raise ValueError("Sorry. 'number' must be zero or positive.")
# ...     # Calculate the factorial of number
# ...     def inner_factorial(number):
# ...         if number <= 1:
# ...             return 1
# ...         return number * inner_factorial(number - 1)
# ...     return inner_factorial(number)
# ...

# >>> factorial(4)