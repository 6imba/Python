# function and return|pass.
# recursion.

# def fun1():
#     print('Hello world.')
# fun1()

# def fun2(a,b):
#     print(a+b)
# fun2(2,3)

# # Arbitrary Arguments, *args:
# def fun3(*params):
#     print(params[0],' is ',params[1],' years old, who live in ',params[2],'. Male:',params[3],'.')
# fun3('Amir',22,'Kapan',True)
# # tuple of argument.

# # Keyword Arguments:
# def fun4(c,a,b):
#     print(a,' ',b,' ',c)
# fun4(a="Apple",c="Coconut",b="banana")

# # Arbitrary Keyword Arguments, **kwargs:
# def fun4(**kparams):
#     print(kparams['a'],' ',kparams['b'],' ',kparams['c'])
# fun4(a="Apple",c="Coconut",b="banana")

# Default Parameter Value:
def my_function(country = "Earth"):
  print("I am from " + country)
my_function()
my_function('Nepal')
