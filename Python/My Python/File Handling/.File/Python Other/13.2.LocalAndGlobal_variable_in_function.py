
# Note that in jupyter all code box act as same as we have declare add funtion in this box we can access it from another box
def add(x) :
    y=2#local variable
    return x+y

print(add(5))


def add(x) :
    y=2#local variable
    return x+y

def minus(x) :
    return x-j # j is not define as we cannot access local variable of another function

print(minus(12))



def add(x) : #x is parameter
    z=2 #local variable
    return x+y

def minus(x) : #x is parameter
    return x-z #z is not define as we cannot access local variable of another function

def multi(x) : #x is parameter
    return x*y # here x is given parameter and y is not given. So at first function search for local variable y. If there is no any local variable called y then it search for the global variable outside the function and if there exist gobal_variable then function uses it...

y=10 # gobal_varible
print(multi(5))
print(add(5))

# note : x as a parameter in different function is different
# here x is given parameter and y is not given in minus() function. So at first function search for local variable y. If there is no any local variable called y then it search for the global variable outside the function and if there exist gobal_variable then function uses it...and if there exist no gobal_variable then it gives error 



def add(x) :# pass x as 5
    x = 7 # overwite x as 7
    y = 2
    return x+y # 7 + 2

print(add(5))




# What is a variable’s scope?
# The range of statements in the code where a variable can be accessed.

# What is a local variable?
# A temporary variable that is only used inside a function

# Can you use the same name for a local variable as a global variable?
# Yes, but it is considered bad form.

