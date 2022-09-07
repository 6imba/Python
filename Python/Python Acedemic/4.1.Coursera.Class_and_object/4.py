# z=8
# class A:
#     x=2
#     y=4
#     def __init__(self):
#         self.x=6
    
# obj1 =A()
# print(obj1.x)
# # print(x) #error
# print(obj1.y)
# print(obj1.z)


#1
# z=1
# print(z)


#2
# class A:
#     x=2

# obj1 =A()
# print(obj1.x)


#3
# class A:
#     def __init__(self):
#         self.x=3
    
# obj1 =A()
# print(obj1.x)


# #4
# Apple = 10
# class Vegetable:
#     Banana = 20
#     def __init__(self):
#         self.Coconut = 30
    
# print(Apple)
# obj1 =Vegetable()
# print(obj1.Banana)
# print(obj1.Coconut)




#5
Apple = 10
class Vegetable:
    Banana1 = 201
    Banana2 = 202
    def __init__(self):
        self.Coconut = 30
        self.Banana2 = 40 #first ptority to constructor
    
print(Apple)
obj1 =Vegetable()
print(obj1.Banana1)
print(obj1.Banana2)
print(obj1.Coconut)

# #6
# apple = 10
# class Vegetable:
#     banana = 20
#     def __init__(self):
#         self.coconut = 30
    
# obj1 =Vegetable()
# print(obj1.apple) #apple is outside the class so object(obj1) doesnt recoznizes apple





# So when Python creates a new instance of point then what it does, is it creates an empty instance and then passes that into the constructor, which is typically going to set instance variables. The next thing that you need to understand is how Python searches for instance variables and class methods.
# The next thing that you need to understand is the search order that Python uses when searching for instance variables, class methods, and class variables. 
# So when we say something like print(point1.x), then the first thing that Python does is it asks, well, is this an instance variable? 
# So it looks at this instance .1, in this case, we're representing that instance with this object. 
# It looks at this instance and asks, does this have an instance variable called x? In this case, it does. 
# And when it finds it in the instance, Python gives us the value of that instance variable. 
# So in this case, we're going to get 10. Now, if we search for something that wasn't in the instance variable, so for instance, 
# let's suppose that we say print(point1.getx). Then Python first needs to evaluate, where is this method (point1.getx)? 
# So the first thing that it searches is point1. It asks, does point1 have an instance variable called get x? 
# But point1 doesn't. So the next place that Python searches is it recognizes that point1 is an instance variable of this class point.
#So in the next place that Python searches is inside of the class itself. In here, this is where Python actually finds this method getx. 
# So when Python evaluates any instance variable or a class variable, it first looks inside of the instance and then it looks inside of the class.
#If it doesn't find it inside of the instance or inside of the class, then it's going to throw a runtime error. 
# That's all for now, until next time.