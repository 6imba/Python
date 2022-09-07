
#There are only two boolean values. They are True and False. 
#Capitalization is important, since true and false are not boolean values 
#(remember Python is case sensitive).
print(True)
print(type(True))
print(type(False))


#Boolean values are not strings!
#It is extremely important to realize that True and False are not strings.
#They are not surrounded by quotes. They are the only two values in the data type bool. 
#Take a close look at the types shown below.print("True")
print("True")
print(type("True"))
print(type(True))



#boolean_expression
print(5==5)
print(5==6)
print(type(5==6))
#here == is comparism operator
#A boolean expression is an expression that evaluates to a boolean value.
#The equality operator, ==, compares two values and produces a boolean value
#related to whether the two values are equal to one another.


#boolean logical operators
print(3>2)
print(3<2)
print(7>=4)
print(8<=1)
print(2!=3)
print( 3 + 4 == 7)



x = 5
print('xcvsdv',x>0 and x<10)
print(x>0 and x<4)

y = 25
print(y%5 == 0 or y%3 ==0)
print(y%5 == 0 or y%35 ==0)
print(y%2 == 0 or y%3 ==0)



# What is the correct Python expression for checking to see if a number stored in a variable x is between 0 and 5.
x=4
print(x > 0 and x < 5)

y=7
print(y > 0 and y < 5)



#Boolean in operator 
print('a' in 'apple')
#Note that a string is a substring of itself,
#and the empty string is a substring of any other string.
print('a' in 'a')
print('p' in 'apple')
print('app' in 'apple')
print('pa' in 'apple')
print('p' not in 'apple')
print('t' not in 'apple')
print('a' in ['apple','axe','amazone','ape'])#list
print('ape' in ['apple','axe','amazone','ape'])#list
print('' in 'x')#empty_string
print(' ' in 'x')#empty_string
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])








