# #1
# # A method behaves like a function but it is invoked on a specific instance.

# class Point:

#     def __init__(self, initX, initY): # pass argument to constructor
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

# point1 = Point(3,7)
# print(point1.getX())
# print(point1.getY())



# #2
# class Point:

#     def __init__(self, initX, initY):
#         self.x = initX
#         self.y = initY

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5


# p1 = Point(7,6)
# print(p1.distanceFromOrigin())

# p2 = Point(2,3)
# print(p2.distanceFromOrigin())




#3
# Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. 
# Create an instance method called limbs that, when called, returns the total number of limbs the animal has. 
# To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. 
# Call the limbs method on the spider instance and save the result to the variable name spidlimbs.

class Animal :
    def __init__(self,arms,legs):
        self.arms=arms
        self.legs=legs
        
    def limbs (self):
        return self.arms + self.legs
        
spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)