# #1 without constructor
# class Fruits:

#     fruit1 = ('Apple',120)
#     fruit2 = ('Banana',350)
#     fruit3 = ('Coconot',245)
        
#     list_of_fruits = [fruit1,fruit2,fruit3]

# for fruit in Fruits.list_of_fruits:
#     print(fruit)



# #2 with constructor(init)
# class Fruits:
#     def __init__(self,fruit_name,price): # constructor/instancating object
#         self.fruit_name=fruit_name
#         self.price=price

# fruit1 = Fruits('Apple',120)
# fruit2 = Fruits('Banana',350)
# fruit3 = Fruits('Coconot',245)
        
# list_of_fruits = [fruit1,fruit2,fruit3]
# print(list_of_fruits)

# for fruit in list_of_fruits:
#     print(fruit)





# #3
# class Fruits:
#     def __init__(self,fruit_name,price): # constructor/instancating object
#         self.fruit_name=fruit_name
#         self.price=price


# fruit1 = Fruits('Apple',120)
# fruit2 = Fruits('Banana',350)
# fruit3 = Fruits('Coconot',245)
        
# list_of_fruits = [fruit1,fruit2,fruit3]
# print(list_of_fruits)
# for fruit in list_of_fruits:
#     print(fruit.fruit_name)
    





# #4
# class Fruits:
#     def __init__(self,fruit_name,price): # constructor/instancating object
#         self.fruit_name=fruit_name
#         self.price=price

# fruit1 = Fruits('Apple',120)
# fruit2 = Fruits('Banana',350)
# fruit3 = Fruits('Coconot',245)
        
# list_of_fruits = [fruit1,fruit2,fruit3]

# for fruit in list_of_fruits:
#     print(sorted(list_of_fruits))
    
# # Welcome back. So given a list of instances it's often useful to be able to sort them by some index. So for example, suppose 
# # that we have a class to represent a fruit and every fruit has a name and a price. So we might have a list of fruits, for  I 
# # example, might have this list of fruits equals, the first item is a cherry whose price is $10. The second is an apple whose  
# # price is $5 and the third is a blueberry whose price is $20.
# # Now, suppose that I want to be able to sort this list of fruits by their price. Recall that the sorting method allows us to 
# # sort any list of items. So if I call print out the value of sorted L, so if I don't pass in any key into sorted, then sorted 
# # tells us that it doesn't know how to compare two fruit items. So we need to be able to tell sorted how to compare two fruit  
# # items bypassing in a value for key. 




# #5
# class Fruits:
    
#     def __init__(self,fruit_name,price): # constructor/instancating object
#         self.fruit_name=fruit_name
#         self.price=price
        
#     def sort_piority(self):
#         return self.price

    
# fruit1 = Fruits('Apple',120) # call class_constructor
# fruit2 = Fruits('Banana',350) # call class_constructor
# fruit3 = Fruits('Coconot',245) # call class_constructor
        
# list_of_fruits = [fruit1,fruit2,fruit3]
# sortby = Fruits.sort_piority # call method(sort_piority) of class(Fruits)
# print(type(sortby))
# print(sortby)
# for fruit in sorted(list_of_fruits,key=sortby):
#     print(fruit.fruit_name)












# # 6
# class Fruits:
    
#     def __init__(self,fruit_name,price): # constructor/instancating object
#         self.fruit_name=fruit_name
#         self.price=price
        
#     def sort_piority(self):
#         return self.price
    
# list_of_fruits = [ Fruits('Apple',120), # list of instances
#                    Fruits('Banana',350),
#                    Fruits('Coconot',245)
#                  ]
# print("-----sorted by price, referencing a class method(sort_piority)-----")
# for fruit in sorted(list_of_fruits,key=Fruits.sort_piority): # sorting and printing list of instances
#     print(fruit.fruit_name)
    
    
# # When each of the items in a list is an instance of a class, you need to provide a function that takes one instance as an input,
# # and returns a number. The instances will be sorted by their numbers.




# # 7
# class Fruits:
    
#     def __init__(self,fruit_name,price): # constructor/instancating object
#         self.fruit_name=fruit_name
#         self.price=price
        
#     def sort_piority(self):
#         return self.price
    
# list_of_fruits = [ Fruits('Apple',120), # list of instances
#                    Fruits('Banana',350),
#                    Fruits('Coconot',245)
#                  ]

# for fruit in sorted(list_of_fruits,key=lambda x :x.sort_piority()): # sorting and printing list of instances
#     print(fruit.fruit_name)











# L = ["Cherry", "Apple", "Blueberry"]

# print(sorted(L, key=len))
# #alternative form using lambda, if you find that easier to understand
# print(sorted(L, key= lambda x: len(x)))
