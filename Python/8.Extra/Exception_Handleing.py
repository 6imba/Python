# We can handle exception in python using try and except :
# try block ==> contain code_part that can gives exception
# except block ==> what to return if eception occured


# Example_1
# x=5
# y=0
# div = x/y  ==> here this line may give error is y value is 0. So, keep this line in try block.
# print(div)

# Error_Handling_1
x=5
y=0
try:
    div = x/y
    print(div)
except:
    print('Infinity !')



#So what error may we get : If we know that then we can specify error messange : ZeroDivisionError
# Some of error name :
#     ZeroDivisionError <==> 5/0
#     TypeError <==> 10+'amir'
#     NameError <==> 
#     ValueError <==> 


# IfElse vs TryCatch :

#1
#IfElse:
x=5
y=0
if y!= 0:
    div = x/y #here we have to give/check condition
    print(div)
else:
    print('Infinity !')


#2
# Error_Handling_1
x=5
y=0
try:
    div = x/y #ZeroDivisionError
    print(div)
except:
    print('Infinity !')


#3 TypeError
#IfElse:
# x=5
# y='Amir'
# print(x+y)
# So how to magae this error using If_Else. Its quit not proper way to manage error

#4 TypeError
# Error_Handling_2
x=5
y='Amir'
try:
    print(x+y)
except:
    print('TypeError')



# So inorder to handle/manage/bypass various_error and complex_execepton we use Exception_Handling where as IfElse is used to check condition

#We have Three Types of error in general in  python :
# 1. Compile/Syntatic Time Error --> Syntax Error, Developing Time error.
# 2. Logical/Symentic Error --> Wrong logic/formula, Not correct Output,  Testing Time error/bug.
# 3. Run Time Error --> Wrong input from user, like one inpu is 1  and another input is 0 and result needed is 1/0, Mistake done by user, Error while implementing/Using application.

# The moment we get Run_Time_Error our application_execution gets stoped.
# So Inoder to continue execution of our program even if exception/error occured here comes use of exception handling.
# i.e :Try below program,
# a=1
# b=0
# print(1/0)
# print('Opps') #you see  this statement doesnt get executed as excetion of program stops at upper statement as exception occurs

# So, User Exception Handling

# Error_Handling_1
a=1
b=0
try:
    print(1/0)
except:
    print('Opps !')


# Error_Handling_2 --> if want show  default exception message
a=1
b=0
try:
    print(1/0)
except Exception as e:
    print(e)



# Notes
# x=5 --> Normal_Statement
# y=0 --> Normal_Statement
# div = x/y --> Critical_Statement : Statement that may cause exception

# Note : We keep Critical_Statement inside try block



# Here we have learn try and except but now what is finally ?

# Error_Handling_Finally_1
a=1
b=0
try:
    print('Open Me') #see this will get printed 
    print(1/0) #exception occurs
    print('Close Me') #so, see this will not get printed
except Exception as e:
    print(e) #see directly this will get printed

# So how to print Close Me?
# We can do this



# Error_Handling_Finally_2
a=1
b=0
try:
    print('Open Me') #see this will get printed 
    print(1/0) #exception occurs
except Exception as e:
    print(e) #see directly this will get printed
    print('Close Me') #so, see this will also get printed


# Note: when we dont know hat exception will appear then we use Exception or else we use name of exception :

# When we dont know hat exception will appear then we use Exception
# except Exception as e:
#     print(e)

# # Else we use name of exception :
# except ValueError as e:
#     print(e)

# except NameError as e:
#     print(e)

# except TypeError as e:
#     print(e)

# etc





# But what is eception doent occur then Close Me wont occurs
# So here comes use of finally

# Error_Handling_Finally_3
a=1
b=0
try:
    print('Open Me') #1. See this will get printed 
    print(1/0) #exception occurs
except Exception as e:
    print(e) #2. Then, see directly this will get printed
finally:
    print('Close Me') #3. Finally, see this will also get printed

# Finally block execute if we get error as well as if dont get exception


# Summary:
# 1. exceute, either try or except
# 2. exceute, all try and except and finally

# Try block get executed if we dont get error
# Except get executed if we get error
# Finally block get executed if we get error as well as if dont get exception







#Therefore :

# try:
#     print('Open Me') #1. See this will get printed 
#     print(1/0) #exception occurs
# except Exception as e:
#     print(e) #2. Then, see directly this will get printed
# finally:
#     print('Close Me') #3. Finally, see this will also get printed


# OR

# try:
#     print('Open Me') #1. See this will get printed 
#     print(1/0) #exception occurs
# except TypeError as e:
#     print(e) #2. Then, see directly this will get printed
# finally:
#     print('Close Me') #3. Finally, see this will also get printed



l = [1,2]
try:
    print('a')
    ans = l[3]
    print('b')
except:
    print('c')
    ans = False #just simply mean ans is out of index dont see it as logic code its just we declare it
    print('d')
print('e')



# if you can specify error and number of errors are little then use if else
# but 
# if you cannot specify the error but you dont know what error there might be and also if number of errors are more then use exception handling