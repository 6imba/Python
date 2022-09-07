# # 1
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


# # 2.1
# def fun1():
#     return "hi"

# print(fun1)
# fun1()
# print(fun1(),  "**************")


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
# print(fun2, "**************")


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

# print("1")
# fun2 = fun1()
# print("2")
# fun2
# print("3")
# print(fun2)
# print("4")
# fun2()




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


# # 1
# print(print)



# # 1.1
# def executor (func):
#     print(type(func))
#     return func
# print(executor(print))



# # 2
# def executor (func):
#     return func
# x = executor(print)
# print(x)


# # 3
# def executor (func):
#     return func
# x = executor(print)
# x('hi')


# # 4
# def executor (func):
#     func('Hi')
# executor(print)


# # 5
# print(sum)
# def executor (func):
#     return func([1,2,3,4,5], 100)
# print(executor(sum))



# # 6.1
# def inbuilt():
#     print('Hi i am in-bulit function !')
# inbuilt()


# # 6.2
# def inbuilt():
#     print('Hi i am in-bulit function !')

# def change_inbuilt(in_fuc):
#     print('Lets start changing !')
#     in_fuc()
#     print('Change made ! !')

# modified_in_fuc = change_inbuilt(inbuilt)



# # 6.3
# def inbuilt():
#     print('Hi i am in-bulit function !')

# def decorate(in_fuc):
#     print('Lets start changing !')
#     in_fuc()
#     print('Change made ! !')

# modified = decorate(inbuilt)






# # 6.4
# # Nested function
# def finction1():
#     def nestedfunction() :
#         print('I am Nested function ! !')
#     print('I am Main function ! !')
#     nestedfunction()

# finction1()




# # 6.4
# # Nested function with function as parameter
# def extrafunction():
#     print('I am Extrafunction')
# def finction1(para1):
#     def nestedfunction() :
#         print('I am Nested function ! !')
#     print('I am Main function ! !')
#     nestedfunction()
#     para1()
#     extrafunction()

# finction1(extrafunction)




# # 6.4
# def extrafunction():
#     print('I am Extrafunction')
# def finction1(para1):
#     def nestedfunction() :
#         print('I am Nested function ! !')
#         extrafunction()
#         para1()
#     print('I am Main function ! !')
#     return nestedfunction

# ok = finction1(extrafunction)
# ok()





# # 6.4
# def extrafunction():
#     print('I am Extrafunction')
# def finction1(para1):
#     def nestedfunction() :
#         print('I am Nested function ! !')
#         extrafunction()
#     print('I am Main function ! !')

# finction1(extrafunction)
# nestedfunction() # nestedfunction  is in a local scope of finction1





# # 6.4.1
# def inbuilt():
#     print('Hi i am in-bulit function !')

# def decorate(in_fuc):
#     def extra() :
#         print('Lets start changing !')
#         in_fuc()
#         print('Change made ! !')
#         print(id(extra), "*********************")
#     return extra
# modified = decorate(inbuilt)
# modified()
# print(id(modified), "*********************")





# # 6.4.2
# def inbuilt():
#     print('3')

# def decorate(in_fuc):
#     def extra() :
#         print('2')
#         in_fuc()
#         print('4')
#     print('1')
#     return extra

# modified = decorate(inbuilt)
# modified()







# # 6.5
# def inbuilt():
#     print('7')

# def decorate(in_fuc):
#     print('1')
#     def extra() :
#         print('6')
#         in_fuc()
#         print(id(in_fuc))
#         print('8')
#     print('2')
#     return extra
#     print('3')

# print('main')
# modified = decorate(inbuilt)
# print('4')
# print(modified) #function inside function
# print('5')
# modified() #function call
# print('9')
# print(id(inbuilt))








# # 6.6
# def decorate(in_fuc):
#     def extra() :
#         print('before')
#         in_fuc()
#         print('after')
#     return extra

# @decorate
# def inbuilt():
#     print('inbuit')

# inbuilt()







# when we need to perform same chnage in different function we use decorator
# when we need to extend the functionality if an existing function without any actually hard-coding change in  that function we use decorator


# # 7.1
# def div(a,b):
#     print(a/b)
# div(4,2)



# # 7.2
# def div(a,b):
#     if b==0:
#         a,b = b,a
#     print(a/b)
# div(4,0)
# # note : we changed the function


# Now using decorator
# decoration_function takes function_to_be_changed as a parameter

# # 7.3
# def div(a,b):
#     print(a/b)

# def check(func):
#     def inner(a,b):
#         if b == 0:
#             a,b = b,a
#             print(a)
#             print(b)
#         func(a,b)
#     return inner
# div = check(div) #holds inner_function of decoration_function
# print(div(4,0))







# def div(a,b): #old_function_defination
#     print('4............')
#     print(a/b)

# def check(func): #decorator
#     print('1............')
#     def inner(a,b): #function with additional feature before calling original function
#         print('3............')
#         if b == 0:
#             a,b = b,a
#         func(a,b) #old_function_call
#     return inner

# div = check(div) #call decorator and return function with additional feature/innerfunction #holds inner_function of decoration_function
# print('2............')
# print(div(4,0)) # call function with additional feature/innerfunction








# # 7.4 short syntax for decorator in python

# def check(func):
#     print('1.......')
#     def inner(a,b):
#         print('2.......')
#         if b == 0:
#             a,b = b,a
#         func(a,b)
#     return inner

# @check
# def div(a,b):
#     print('3.......')
#     print(a/b)

# print(div(4,0))

#jun fucntion ko behaviour extend garne ho tyo function ma hard code nagari tyo function lai chai arko external helper function ma waraped argument jasari pathaune.











# # extra
# def apple():
#     def ball():
#         return "I am Ball"
#     return ball()+" I am Apple"
# print(apple())


# # extra
# def apple(arg):
#     def ball(): 
#         return "I am Ball"
#     return ball()+" I am Apple" + arg
# print(apple("Argument"))










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
# # True





# # Python program
# # functions being passed as arguments to other functions
# def new_inp(text):
#     print('2................')
#     return text.upper()
# def old_inp(text):
#    return text.lower()
# def display(func):
#    print('1................')
#    # storing the function in a normal variable
#    code = func("Love Coding, Learn everything on Tutorials Point")
#    print('3................')
#    print (code)
# display(new_inp) #directly referenced by passing functions as arguments.
# display(old_inp)