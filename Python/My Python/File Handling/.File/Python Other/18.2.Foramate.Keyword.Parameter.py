# # 1 
# def my_function(x,y=5,z=7):# here parameter y and z has default_value && x is required value
#     print('x,y,z => ',x,y,z)
# my_function()# error as we need to pass value reference for x


# # 2
# def my_function(x,y=5,z=7):#y&z => optional_parameter
#     print('x,y,z => ',x,y,z)
# my_function(2)# pass value reference for x as 2


# 3
# def my_function(x,y=5,z=7):
#     print('x,y,z => ',x,y,z)
# my_function(2)# pass value to reference_parameter x as 2
# my_function(3,4)# pass value to reference_parameter x as 3 and overwrite default_optional_parameter(y=5) as 4
# my_function(7,8,9)# pass value to reference_parameter x as  and overwrite default_optional_parameter(y=5 & z=7) as (8 & 9)


# #Now:-
# #simple keyword_parameter is tied up with optional parameters
# #means
# #what if we want to overwrite 3rd agument with out mutating 2nd argument
# #solution:-
# def my_function(x,y=5,z=7):
#     print('x,y,z => ',x,y,z)
# my_function(2,z=100) # use of keyword parameter # specifies the value to parameter


#4
# initialize = 99
# def my_function(x,y=5,z=initialize):
#     print('x,y,z => ',x,y,z)
# my_function(2)
# my_function(2,z=100)#keyword argument


#5
#keyword argument allow us to put our argument in any order
# def my_function(x,y=5,z=0):
#     print('x,y,z => ',x,y,z)
# my_function(2)
# my_function(2,y=111,z=100)#keyword argument
# my_function(y=222,z=333,x=111)#keyword argument #orderless while passing argument
# my_function(111,z=222,y=333)


# 6
# #just try error
# def my_function(x,y=5,z=0):
#     print('x,y,z => ',x,y,z)
# my_function(y=222,z=333,111)#error as y and z are keyword argument it should always comes after required_positional_argument
# my_function(111,x=111)#error required_argument repeated
# my_function(x=222,x=333,z=111)#error required_positional_argument repeated


# 7
# #etra:
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't" + action,)
#     print("if you put" + str(voltage) + "volts through it.")
#     print("-- Lovely plumage, the" +  type)
#     print("-- It's " + state + "!")

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# 8
#Keyword Parameters with .format
#Earlier you learned how to use the format method for strings, which allows you to structure strings like fill-in-the-blank sentences. 
# Now that you’ve learned about optional and keyword parameters, we can introduce a new way to use the format method.
#This other option is to specifically refer to keywords for interpolation values, like below.

# names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
# for name, scores in names_scores:
#     print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))#here nm,s1,s2,s3 are keyword_argument
    


# 9
#Sometimes, you may want to use the .format method to insert the same value into a string multiple times. 
# You can do this by simply passing the same string into the format method, assuming you have included {} s in the string everywhere 
# you want to interpolate them. But you can also use positional passing references to do this! The order in which you pass arguments 
# into the format method matters: the first one is argument 0, the second is argument 1, and so on.
# this works
# names = ["Jack","Jill","Mary"]
# for n in names:
#     print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# # but this also works!
# names = ["Jack","Jill","Mary"]
# for n in names:
#     print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))


# 10
# initial = 7
# def f(x, y = 3, z = initial):
#     print("x, y, z are:", x, y, z)

# f(2, 5)


# 11
# initial = 7
# def f(x, y = 3, z = initial):
#     print("x, y, z are:", x, y, z)

# f(2, z = 10)


# 12
# # gives error 
# initial = 7
# def f(x, y = 3, z = initial):
#     print("x, y, z are:", x, y, z)

# f(2, x=5)


# 13
# initial = 7
# def f(x, y = 3, z = initial):
#     print ("x, y, z are:", x, y, z)
# initial = 0
# f(2)


# # 14
# names = ["Alexey", "Catalina", "Misuki", "Pablo"]
# print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))


# 15
#. Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn’t work. Fix the code so that
#  it passes the test. This should only require changing one line of code.
# def waste(var = "Water", mar, marble = "type"):#error
#     final_string = var + " " + marble + " " + mar
#     return final_string

# #correction
# def waste(mar, var = "Water", marble = "type"):
#     final_string = var + " " + marble + " " + mar
#     return final_string