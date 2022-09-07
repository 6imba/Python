# #1
# class Point:

#     def __init__(self, initX, initY): # initialized object

#         self.x = initX
#         self.y = initY

# p1 = Point(7,6)
# print(p1) # p1 is object so print <__main__.Point object at 0x068D4F10>




# #2
# class Point:

#     def __init__(self, initX, initY): # initialized object

#         self.x = initX
#         self.y = initY

#     def __str__(self): #change and return Initialized object into String in given below formate # called automatically
#         return "x = {}, y = {}".format(self.x, self.y)

# p3 = Point(7,6)
# print(p3)


# #3
# class Point:

#     def __init__(self, initX, initY): # initialized object
#         self.x = initX
#         self.y = initY

#     def __str__(self): #change and return Initialized object into String in given below formate # called automatically
#         return "Point({},{})".format(self.x, self.y)

# p1 = Point(7,6)
# print(p1)
# p2 = Point(3,9)
# print(p2)


# #3
# class Point:

#     def __init__(self, initX, initY): # initialized object
#         print('__init__')
#         self.x = initX
#         self.y = initY

#     def __str__(self): #change and return Initialized object into String in given below formate # called automatically
#         print('__str__')
#         return "Point({},{})".format(self.x, self.y)

# p1 = Point(7,6)
# print(p1)
# p2 = Point(3,9)
# print(p2)



# #4
# class Point:

#     def __init__(self, initX, initY): # initialized object
#         self.x = initX
#         self.y = initY

#     def __str__(self): #change and return Initialized object into String in given below formate # called automatically
#         return 'Hello World!'


# p1 = Point(7,6)
# print(p1) # p1 is object




# #5
# class Point:

#     def __init__(self, initX, initY): # initialized object
#         self.x = initX
#         self.y = initY
        
#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5


# p1 = Point(7,6) # p1 is object
# print(p1) # p1 is object
# print(p1.getX())
# print(p1.getY())
# print(p1.distanceFromOrigin())


# #6
# class Point:

#     def __init__(self, initX, initY): # initialized object
#         self.x = initX
#         self.y = initY

#     def __str__(self): #change and return Initialized object into String in given below formate # called automatically
#         return "Point({},{})".format(self.x, self.y)
        
#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5


# p1 = Point(7,6) # p1 is object
# print(p1) # p1 is object
# print(p1.getX())
# print(p1.getY())
# print(p1.distanceFromOrigin())


# #7
# # Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and 
# # assigns them to 3 instance variables in the constructor: name, brand, and fiber. 
# # When an instance of Cereal is printed, the user should see the following: 
# # “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!” 
# # To the variable name c1, assign an instance of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2. 
# # To the variable name c2, assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3.
# # Practice printing both!



# class Cereal:
#     def __init__(self,name,brand,fiber): # Initialized object
#         self.n=name
#         self.b=brand
#         self.f=fiber

# c1 = Cereal("Corn Flakes","Kellogg's",2)
# print(c1)
# c2 = Cereal("Honey Nut Cheerios","General Mills",3)
# print(c2)


# #8
# class Cereal:
#     def __init__(self,name,brand,fiber): # Initialized object
#         self.n=name
#         self.b=brand
#         self.f=fiber
#     def __str__(self): #change and return Initialized object into String
#         return '{} cereal is produced by {} and has {} grams of fiber in every serving!'.format(self.n,self.b,self.f)
       
# c1 = Cereal("Corn Flakes","Kellogg's",2)
# print(c1)
# c2 = Cereal("Honey Nut Cheerios","General Mills",3)
# print(c2)


# #9
# class Point_A:
#     def __init__(self,cordinate_x,cordinate_y):
#         self.x = cordinate_x
#         self.y = cordinate_y
        
    
#     def __add__(self,point_2): # return object # this method is called when + operator is used with class_object (point_1 + point_2)
#         return Point_A(self.x + point_2.x,
#                        self.y + point_2.y
#                         )
        
# point_1 = Point_A(3,5)
# point_2 = Point_A(7,13)
# print(point_1 + point_2) 




# #10
# class Point_A:
#     def __init__(self,cordinate_x,cordinate_y):
#         print('__init__')
#         self.x = cordinate_x
#         self.y = cordinate_y
        
#     def __str__(self): # change returned object into String
#         print('__str__')
#         return 'Point({},{})'.format(self.x,self.y)
    
#     def __add__(self,point_2): # return object
#         print('__add__')
#         return Point_A(self.x + point_2.x,
#                        self.y + point_2.y
#                         )
        
# point_1 = Point_A(3,5)
# point_2 = Point_A(7,13)
# print(point_1 + point_2)




# #11
# # Finally 1

# class Points:
#     def __init__(self,cordinate_x,cordinate_y):
#         self.x=cordinate_x
#         self.y=cordinate_y
        
# point_1=Points(2,5)
# point_2=Points(7,11)

# print(point_1)
# print(point_2)



# #12
# # Finally 2

# class Points:
#     def __init__(self,cordinate_x,cordinate_y): # initialized object
#         self.x=cordinate_x
#         self.y=cordinate_y
        
#     def __str__(self):
#         return 'Point = ({},{})'.format(self.x,self.y)
        
# point_1=Points(2,5)  # p1 is object
# point_2=Points(7,11) # p2 is object

# print(point_1)
# print(point_2)


# #13
# #Finally 2
# class Points:
#     def __init__(self,cordinate_x,cordinate_y):
#         print('__init__')
#         self.x=cordinate_x
#         self.y=cordinate_y
        
#     def __str__(self): #change and return Initialized object into String in given below formate # called automatically
#         print('__str__')
#         return 'Point = ({},{})'.format(self.x,self.y)
        
# point_1=Points(2,5)
# point_2=Points(7,11)

# print(point_1) 
# print(point_2)


# #14
# # Finally 3

# class Points:
#     def __init__(self,cordinate_x,cordinate_y):
#         self.x=cordinate_x
#         self.y=cordinate_y
        
# #     def __str__(self):
# #         return 'Point = ({},{})'.format(self.x,self.y)
    
#     def __add__(point_1,point_2): # this method is called when + operator is used with class_objects (point_1 + point_2) # return object 
#         return Points( point_1.x + point_2.x,
#                        point_1.y + point_2.y
#                         )
        
# point_1=Points(2,5)
# point_2=Points(7,11)

# # print(point_1) 
# # print(point_2)
# print( point_1 + point_2 )



# #15
# # Finally 4

# class Points:
#     def __init__(self,cordinate_x,cordinate_y):
#         self.x=cordinate_x
#         self.y=cordinate_y
        
#     def __str__(self):
#         return 'Point = ({},{})'.format(self.x,self.y)
    
#     def __add__(point_1,point_2): # this method is called when + operator is used with class_objects (point_1 + point_2) # return object 
#         return Points( point_1.x + point_2.x,
#                        point_1.y + point_2.y
#                         )
        
# point_1=Points(2,5)
# point_2=Points(7,11)

# print(point_1) 
# print(point_2)
# print( point_1 + point_2 )




# #16
# # Full_Finall

# class Points:
#     def __init__(self,cordinate_x,cordinate_y):
#         self.x=cordinate_x
#         self.y=cordinate_y
        
#     def __str__(self): # Converting an Object to a String
#         return 'Point = ({},{})'.format(self.x,self.y)
    
#     def __add__(point_1,point_2): # this method is called when + operator is used with class_objects (point_1 + point_2) # return object 
#         return Points( point_1.x + point_2.x,
#                        point_1.y + point_2.y
#                         )
#     def __sub__(one_object,another_object): # this method is called when - operator is used with class_objects (one_object,another_object)
#         return Points(one_object.x - another_object.x,
#                       one_object.y - another_object.y
#                         )
# #     def __mult__(first_object,second_object): # this method is called when * operator is used with class_objects (first_object,second_object)
# #         return Points(first_object.x * second_object.x,
# #                       first_object.y * second_object.y
# #                         )    
    
# point_1=Points(2,5)
# point_2=Points(7,11)

# print(point_1) 
# print(point_2)
# print( point_1 + point_2 )
# print( point_1 - point_2 )
# # print( point_1 * point_2 ) # __mult is not defined in python
# # dir(__mult__)




