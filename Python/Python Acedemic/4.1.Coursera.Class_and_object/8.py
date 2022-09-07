# #1
# class Point:

#     def __init__(self, initX, initY): # initialized object
#         self.x = initX
#         self.y = initY

#     def __str__(self): 
#         return "Point({},{})".format(self.x, self.y)
        
#     def getX(self):
#         return self.x # Instances(self.x) as Return Values

#     def getY(self):
#         return self.y # Instances(self.y) as Return Values

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5


# p1 = Point(7,6) # p1 is object
# print(p1) # p1 is object
# print(p1.getX())
# print(p1.getY())
# print(p1.distanceFromOrigin())






# #2
# class Point:

#     def __init__(self, initX, initY): # initialized object
#         self.x = initX
#         self.y = initY
        
#     def mid_point(p1,p2):
#         return (p1.x+p2.x)/2,(p1.y+p2.y)/2

# p1 = Point(7,6) 
# p2 = Point(13,17) 
# mid_answer = p1.mid_point(p2)
# print(mid_answer)
# # better understand




# #3
# class Point:

#     def __init__(self, initX, initY): # initialized object
#         self.x = initX
#         self.y = initY

#     def __str__(self): 
#         return "Point({},{})".format(self.x, self.y)
        
#     def mid_point(p1,p2):
#         mid_x = (p1.x+p2.x)/2
#         mid_y = (p1.y+p2.y)/2
#         return Point(mid_x,mid_y)

# p1 = Point(7,6) 
# p2 = Point(13,17) 
# mid_answer = p1.mid_point(p2)
# print(mid_answer)




# #4
# # better understand
# class A:
#     def __init__(self,numb): #numb is attribute
#         self.numb=numb
    
#     def add(obj_num1,obj_num2):
#         return obj_num1.numb + obj_num2.numb
    
# number1=A(2)
# number2=A(7)
# number1.add(number2)



# #5
# # better understand
# class A:
#     def __init__(self,numb): #numb is attribute
#         self.numb=numb
    
#     def add(self,another_object): #(number1,number2)
#         return self.numb + another_object.numb
    
# number1=A(2)
# number2=A(7)
# number1.add(number2)





# #6
# # better understand
# class A:
#     def __init__(self,numb): #numb is attribute
#         self.numb=numb
    
#     def add(self,another_object): #(number1,number2)
#         return A(self.numb + another_object.numb)
    
# number1=A(2)
# number2=A(7)
# number1.add(number2)




# #7
# # better understand
# class A:
#     def __init__(self,numb): #numb is attribute
#         self.numb=numb
    
#     def add(self,another_object): #(number1,number2)
#         return A(self.numb + another_object.numb)
    
# number1=A(2)
# number2=A(7)
# mid=number1.add(number2)
# print(mid)




# #8
# # better understand
# class A:
#     def __init__(self,numb): #numb is attribute
#         print('__init__ ........................')
#         self.numb=numb
    
#     def __str__(self):
#         print('__str__ ............................')
#         return 'Mid-Point ==> {}'.format(self.numb) #(self.class_attribute)
    
#     def add(self,another_object): #(number1,number2)
#         print('add ..................................')
#         return A(self.numb + another_object.numb)
    
# number1=A(2)
# number2=A(7)
# mid=number1.add(number2)
# print(mid)





# #9
# class Points:
    
#     def __init__(self,x_cordinate,y_cordinate):
#         self.x=x_cordinate
#         self.y=y_cordinate
        
#     def mid(first_point,second_point):
#         mid_x=(first_point.x+second_point.x)/2
#         mid_y=(first_point.y+second_point.y)/2
#         return (mid_x,mid_y)   # return tuples     
        
# point_1 = Points(3,7)
# point_2 = Points(5,19)
# mid_point = point_1.mid(point_2)
# print(type(mid_point))
# print(mid_point)




# #10
# class Points:
    
#     def __init__(self,x_cordinate,y_cordinate):
#         self.x=x_cordinate
#         self.y=y_cordinate
        
#     def mid(first_point,second_point):
#         mid_x=(first_point.x+second_point.x)/2
#         mid_y=(first_point.y+second_point.y)/2
#         return Points(mid_x,mid_y) #Instanciate new object and Instances as Return Values 
        
# point_1 = Points(3,7)
# point_2 = Points(5,19)
# mid_point = point_1.mid(point_2)
# print(type(mid_point))
# print(mid_point)



# #11
# class Points:
    
#     def __init__(self,x_cordinate,y_cordinate):
#         self.x=x_cordinate
#         self.y=y_cordinate
        
#     def mid(first_point,second_point):
#         mid_x=(first_point.x+second_point.x)/2
#         mid_y=(first_point.y+second_point.y)/2
#         return Points(mid_x,mid_y) #Instanciate new object and Instances as Return Values 
        
#     def __str__(self):
#         return 'Mid-Point = ({},{})'.format(self.x,self.y) #change and return Returned_Instances object  into String in given below formate # called automatically
        
# point_1 = Points(3,7)
# point_2 = Points(5,19)
# mid_point = point_1.mid(point_2)
# print(type(mid_point))
# print(mid_point)




# #12
# class Points:
    
#     def __init__(self,x_cordinate,y_cordinate):
#         self.x=x_cordinate
#         self.y=y_cordinate
        
#     def mid(first_point,second_point):
#         mid_x=(first_point.x+second_point.x)/2
#         mid_y=(first_point.y+second_point.y)/2
#         return Points(mid_x,mid_y) #Instanciate new object and Instances as Return Values 
        
#     def __str__(self):
#         return 'Mid-Point = ({},{})'.format(self.x,self.y) #change and return Returned_Instances object  into String in given below formate # called automatically
        
#     def getX(self):
#         return self.x # Instances(self.x) as Return Values

#     def getY(self):
#         return self.y # Instances(self.y) as Return Values
    
# point_1 = Points(3,7) #instance_object of class(Points)
# point_2 = Points(5,19) #instance_object of class(Points)
# mid_point = point_1.mid(point_2) # mid_point is new instance_object of class(Points)
# print(type(mid_point))
# print(mid_point)
# print(mid_point.getX()) # print x_cordinate of new_instance_object (mid_point)
# print(mid_point.getY()) # print y_cordinate of new_instance_object (mid_point)



# # Functions and methods can return objects. This is actually nothing new since everything in Python is an object 
# # and we have been returning values for quite some time. (You can also have lists or tuples of object instances, etc.) 
# # The difference here is that we want to have the method create an object using the constructor and 
# # then return it as the value of the method.

# # Suppose you have a point object and wish to find the midpoint halfway between it and some other target point.
# # We would like to write a method, let’s call it halfway, which takes another Point as a parameter and 
# # returns the Point that is halfway between the point and the target point it accepts as input.





# #13
# class Points:
    
#     def __init__(self,x_cordinate,y_cordinate):
#         self.x=x_cordinate
#         self.y=y_cordinate
        
#     def mid(first_point,second_point):
#         mid_x=(first_point.x+second_point.x)/2
#         mid_y=(first_point.y+second_point.y)/2
#         return mid_x,mid_y #Instanciate new object and Instances as Return Values 
        
#     def __str__(self):
#         return 'Mid-Point = ({},{})'.format(self.x,self.y) #change and return Returned_Instances object  into String in given below formate # called automatically
        
#     def getX(self):
#         return self.x # Instances(self.x) as Return Values

#     def getY(self):
#         return self.y # Instances(self.y) as Return Values
    
# point_1 = Points(3,7) #instance_object of class(Points)
# point_2 = Points(5,19) #instance_object of class(Points)
# mid_point = point_1.mid(point_2) # mid_point is new instance_object of class(Points)
# print(type(mid_point))
# print(mid_point)
# print(mid_point.getX()) # print x_cordinate of new_instance_object (mid_point)
# print(mid_point.getY()) # print y_cordinate of new_instance_object (mid_point)
# print(getX()) 
# print(getY()) 
# print(point_1.getX()) 
# print(point_2.getY())






#13
class Points:
    
    def __init__(self,x_cordinate,y_cordinate):
        self.x=x_cordinate
        self.y=y_cordinate
        
    def mid(first_point,second_point):
        mid_x=(first_point.x+second_point.x)/2
        mid_y=(first_point.y+second_point.y)/2
        return Points(mid_x,mid_y) #Instanciate new object and Instances as Return Values 
        
    def __str__(self):
        return 'Mid-Point = ({},{})'.format(self.x,self.y) #change and return Returned_Instances object  into String in given below formate # called automatically
        
    def getX(self):
        return self.x # Instances(self.x) as Return Values

    def getY(self):
        return self.y # Instances(self.y) as Return Values
    
point_1 = Points(3,7) #instance_object of class(Points)
point_2 = Points(5,19) #instance_object of class(Points)
mid_point = point_1.mid(point_2) # mid_point is new instance_object of class(Points)
print(type(mid_point))
print(mid_point) #use __str__
print(mid_point.getX()) # print x_cordinate of new_instance_object (mid_point)
print(mid_point.getY()) # print y_cordinate of new_instance_object (mid_point)
print(point_1.getX()) 
print(point_2.getY())

# __str__ helps to print object
# 1. if you print obj1 without __str__ it will gives output as ===> <class '__main__.Points'>
# 2. if you print obj1 with __str__ it will gives output as ===>Mid-Point = (4.0,13.0)
# hence __str__ helps to print object
# obj1 = Points(1,2)