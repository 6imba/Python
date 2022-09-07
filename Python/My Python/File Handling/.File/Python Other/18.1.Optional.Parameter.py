#!/usr/bin/env python
# coding: utf-8

# In[45]:


def optiona(a,b=[]):#default value of b is set as empty list which lives somewhere in the frame and object
    b.append(a) # mutate the value of b #append the value passed in through parameter a into b
    return b

print(optiona(2))#passing value(2) reference by parameter (a) to be append into the default empty list(k)
print(optiona('xxx'))#passing value(xxx) reference by parameter (a) to be append into the default list(k)
    


# In[46]:


print(optiona(4))
print(optiona(6))
print(optiona('Hello'))
print(optiona('Zimba'))
#note:after all this code the default list(b) => [2, 'xxx', 4, 6, 'Hello', 'Zimba']
#and if you again run this code it will start to appden value again to the final default list(b) provided by above code
#note : as we keeps on calling optiona function it keeps on mutating default function (b)
#try it by running this code again and again


# In[58]:


# The second tricky thing is that if the default value is set to a mutable object, such as a list or a dictionary, that object will be shared in all invocations of the function. This can get very confusing, so I suggest that you never set a default value that is a mutable object. For example, follow the exceution of this one carefully.

def optiona(x,y=[]):#here a takes value and b is set to default empty list
    y.append(x)
    return y

print(optiona(2))#passing value to first parameter reference (a)
print(optiona('apple'))#again calling and passing value to first parameter reference (a)
print(optiona(1010101,['Amir','Samair','Hari-bahadur']))
# here in 3rd function call:-
# a,b=[] ==> 1010101,['Amir','Samair','Hari-bahadur']
# this 3rd function call overwrites the optional_default_value of 2nd reference parameter
# (i.e overwrites empty_list which is mutated into y=[2,'apple'] by 1st and 2nd function call)
# so 3rd function call pass(1010101) to reference_to_required_value_parameter(i.e x)  and overwite the optional_default_value with(['Amir','Samair','Hari-bahadur'])
# every time we run this code it initialize optional_default_value(y) as empty_list


# In[60]:


#In the treatment of functions so far, each function definition specifies zero or more formal parameters and each function invocation provides exactly that many values. Sometimes it is convenient to have optional parameters that can be specified or omitted. When an optional parameter is omitted from a function invocation, the formal parameter is bound to a default value. When the optional parameter is included, then the formal parameter is bound to the value provided. Optional parameters are convenient when a function is almost always used in a simple way, but it’s nice to allow it to be used in a more complex way, with non-default values specified for the optional parameters.
# Consider, for example, the int function, which you have used previously. Its first parameter, which is required, specifies the object that you wish to convert to an integer. For example, if you call in on a string, int("100"), the return value will be the integer 100.
# That’s the most common way programmers want to convert strings to integers. Sometimes, however, they are working with numbers in some other “base” rather than base 10. For example, in base 8, the rightmost digit is ones, the next digit to the left is 8s, and the one to the left of that is the 64s place (8**2).
# The int function provides an optional parameter for the base. When it is not specified, the number is converted to an integer assuming the original number was in base 10. We say that 10 is the default value. So int("100") is the same as invoking int("100", 10). We can override the default of 10 by supplying a different value.

print(int("100"))
print(int("100", 10))   # same thing, 10 is the default value for the base
print(int("100", 8))     # now the base is 8, so the result is 1*64 = 64


# In[62]:


# Python int()
# The int() method returns an integer object from any number or string.
# The syntax of int() method is:
# int(x=0, base=10)
# The int() method takes two arguments: 
# print(int()) # cheack it it will return default argument 0
# x - Number or string to be converted to integer object. Default argument is zero. 
# base - Base of the number in x. Can be 0 (code literal) or 2-36.
# programariz.com


# In[63]:


#Note
# Tom Lehrer’s New Math
# Some math educators believe that elementary school students will get a much deeper understanding of the place-value system, and set a foundation for learning algebra later, if they learn to do arithmetic not only in base-10 but also in base-8 and other bases. This was part of a movement called “The New Math”, though it’s not so new now (I had it when I was in elementary school!) Tom Lehrer made a really funny song about it, and it’s set with visuals in several YouTube renditions now. Try this very nice lip-synched version.
#https://www.youtube.com/watch?v=DfCJgC2zezw

# When defining a function, you can specify a default value for a parameter. That parameter then becomes an optional parameter when the function is called. The way to specify a default value is with an assignment statement inside the parameter list. 


# In[65]:


initial = 7
def f(x, y =3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

f(2)
f(2, 5)
f(2, 5, 8)


# In[66]:


# Notice the different bindings of x, y, and z on the three invocations of f. The first time, y and z have their default values, 3 and 7. The second time, y gets the value 5 that is passed in, but z still gets the default value of 7. The last time, z gets the value 8 that is passed in.
# If you want to provide a non-default value for the third parameter (z), you also need to provide a value for the second item (y). We will see in the next section a mechanism called keyword parameters that lets you specify a value for z without specifying a value for y.
# Note
# This is a second, related but slightly different use of = than we have seen previously. In a stand-alone assignment statement, not part of a function definition, x=3 assigns 3 to the variable x. As part of specifying the parameters in a function definition, x=3 says that 3 is the default value for x, used only when no value is provided during the function invocation.
# There are two tricky things that can confuse you with default values. The first is that the default value is determined at the time that the function is defined, not at the time that it is invoked. So in the example above, if we wanted to invoke the function f with a value of 10 for z, we cannot simply set initial = 10 right before invoking f. See what happens in the code below, where z still gets the value 7 when f is invoked without specifying a value for z.


# In[68]:


initial = 7
def f(x, y =3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

initial = 10 #no effect
f(2)


# In[69]:


def f(x = 0, y = 1):
    return x * y

print(f())


# In[70]:


def f(x = 0, y = 1):
    return x * y

print(f(1))


# In[76]:


#Write a function called str_mult that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter.

def str_mult(req_string,optional_int = 3): # optional_int has defualt value so optional_int is optional integer parameter 
        return req_string * optional_int
print(str_mult('Simba_'))

