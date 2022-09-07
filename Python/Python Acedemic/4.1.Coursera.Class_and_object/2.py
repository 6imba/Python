1

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):# constructor

        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of class Point
q = Point()         # Instantiate another object of class Point

print("Nothing seems to have happened with the points")



# #2
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self): 

#         self.x = 0 # self.x ==> p.x or q.x
#         self.y = 0 # self.x ==> p.y or q.y

# p = Point()        
# q = Point()         

# print("Nothing seems to have happened with the points")
# print(p.x,p.y)
# print(q.x,q.y)



# #3
# class Point:
#     print('Instanciating Class !')

#     def __init__(self): 
#         print('Init instanciating objects default property !')
#         self.x = 0
#         self.y = 0

# print('Instanciating objects !')
# p = Point()        
# q = Point()         

# print('Printing instanciated objects_value')
# print(p.x,p.y)
# print(q.x,q.y)




# #4
# class Point:

#     def __init__(self): 

#         self.x = 0
#         self.y = 0

# p = Point()
# q = Point()

# print(p)
# print(q)

# print(p is q) # p and q are difference instance_object of class Point




# # A function like Point that creates a new object instance is called a constructor.
# # Every class automatically uses the name of the class as the name of the constructor function.
# # The definition of the constructor function is done when you write the __init__ function (method) inside the class definition.

# # It may be helpful to think of a class as a factory for making objects. 
# # The class itself isn’t an instance of a point, but it contains the machinery to make point instances. 
# # Every time you call the constructor, you’re asking the factory to make you a new object. 
# # As the object comes off the production line, its initialization method is executed to get the object properly set up with it’s factory default settings.
# # The combined process of “make me a new object” and “get its settings initialized to the factory default settings” is called instantiation.





# #Question:
# # Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, 
# # which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. 
# # Save this instance to a variable t.


# class NumberSet:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
      
# t = NumberSet(6,10)

# # self.num1 => t.num1 
# # self.num2 => t.num2 
# # self.num1 self.num1 ==> attribute