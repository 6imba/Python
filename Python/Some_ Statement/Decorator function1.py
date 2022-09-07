# # 1.1 Assigning Function_returned_value to a Variables
# def plus_one(number):
#     return number + 1
# add_one = plus_one(1)
# print(add_one)


# # 1.2 Assigning Functions_itself to Variables
# def plus_one(number):
#     return number + 1
# add_one = plus_one #function_assign_to_variable
# add_one(5) #function_call




# # 2.1 Defining Functions Inside other Functions
# def plus_one(number):
#     def add_one(number):
#         return number + 1
#     result = add_one(number)
#     return result

# plus_one(4)





# # 2.2 Passing Functions as Arguments to other Functions
# def plus_one(number):
#     return number + 1

# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)

# function_call(plus_one)


# # 2.2.1 Passing Functions as Arguments to other Functions
# def plus_one(number):
#     return number + 1

# def function_call(function, x):
#     number_to_add = 5
#     return function(number_to_add) + x

# z = function_call(plus_one, 1000)
# print(z)



# # 2.3 Functions Returning other Functions
# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi

# hello = hello_function()
# hello()



# # 2.3 Nested Functions have access to the Enclosing Function's Variable Scope
# def print_message(message1): #Enclosong Function #message1:Enclosing Function's Variable Scope
#     def message_sender(): #Nested Function/ Closure
#         print(message1)  #message1:Enclosing Function's Variable Scope
#     message_sender()

# print_message("Some random message")





# # 3.1 Creating Decorators
# def uppercase_decorator(function): #decoretor_function/enclosed_function, that convert a sentence to uppercase
#     def wrapper(): # nested_inline_function
#         func = function() # call function to be decorated
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# # Our decorator function takes a function as an argument
# # we shall, therefore, define a function to be decorated and pass it to our decorator.

# def say_hi(): #define a function to be decorated
#     return 'hello there'

# decorate = uppercase_decorator(say_hi) #pass function to be decorated to our decorator and assign a return_value by decorator_function to a variable(decorate). Here decorator returns a inlne_function(wrapper) inside decoretor_function
# decorate() # call inlne_function






# 3.2
# def uppercase_decorator(function): #2 #decoretor_function
#     def wrapper(): #6 # nested_inline_function
#         func = function() #7 #10 # call function to be decorated_______3
#         make_uppercase = func.upper()
#         return make_uppercase #11
#     return wrapper #3

# def say_hi(): #8 #define a function to be decorated
#     return 'hello there' #9

# decorate = uppercase_decorator(say_hi) #1 #4 call decorator_function_______1
# answer = decorate() #5 #12 # call inlne_function_________2
# print(answer) #13



# # 3.3
# # Python provides a much easier way for us to apply decorators.
# # We simply use the @ symbol along with decorator_function before the function we'd like to decorate.

# def uppercase_decorator(function): #decoretor_function/enclosed_function, that convert a sentence to uppercase
#     def wrapper(): # nested_inline_function
#         func = function() # call function to be decorated
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# @uppercase_decorator #call_decorator_function
# def say_hi(): #define a function to be decorated
#     return 'hello there'

# answer = say_hi()# call inlne_function returned by decorator
# print(answer)







# @decorator_function
# def function_to_be_decorated:
# adding @decorator_function (symbol + decorator_function_name) before function_to_be_decorated means, we are passing the function_to_be_decorated into decorator_function and re-assigning the function_to_be_decorated to returned_funtion_by_decorator_function/inline_function/wrapper_function


# As we can see that adding the @ symbol is a sweeter way than creating a new variable to do same thing( to store returned_value from decorator function).
# It makes our code much cleaner as we dont need to assign decorator function into new variable






# # 4.1
# # Applying Multiple Decorators to a Single Function
# # We can use multiple decorators to a single function. However, the decorators will be applied in the order that we've called them.

# def uppercase_decorator(function): #decoretor_function/enclosed_function
#     def wrapper(): # nested_inline_function
#         func = function() # call function to be decorated
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# def split_string(function): #decoretor_function/enclosed_function
#     def wrapper(): # nested_inline_function
#         func = function() # call function to be decorated
#         splitted_string = func.split()
#         return splitted_string
#     return wrapper

# @uppercase_decorator #AttributeError: 'list' object has no attribute 'upper'
# @split_string
# def say_hi():
#     return 'hello there'

# print(say_hi())



# # 4.2
# # Applying Multiple Decorators to a Single Function
# # We can use multiple decorators to a single function. However, the decorators will be applied in the order that we've called them.

# def uppercase_decorator(function): #decoretor_function/enclosed_function
#     def wrapper(): # nested_inline_function
#         func = function() # call function to be decorated
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# def split_string(function): #decoretor_function/enclosed_function
#     def wrapper(): # nested_inline_function
#         func = function() # call function to be decorated
#         splitted_string = func.split()
#         return splitted_string
#     return wrapper

# @split_string
# @uppercase_decorator #an error since lists don't have an upper attribute. The sentence has first been converted to uppercase and then split into a list.
# def say_hi():
#     return 'hello there'

# print(say_hi())





# # 5.1
# # Accepting Arguments in Decorator Functions
# # Sometimes we might need to define a decorator that accepts arguments. We achieve this by passing the arguments to the wrapper function. The arguments will then be passed to the function that is being decorated at call time.

# def decorator_with_arguments(function):
#     def wrapper_accepting_arguments(arg1, arg2):
#         print("My arguments are: {0}, {1}".format(arg1,arg2))
#         function(arg1, arg2)
#     return wrapper_accepting_arguments

# @decorator_with_arguments
# def cities(city_one, city_two):
#     print("Cities I love are {0} and {1}".format(city_one, city_two))

# cities("Nairobi", "Accra")


