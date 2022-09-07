# # 1
# #  manual creation of instances (person1,person2,person3)

# class People:
#     pass

# person1 = People()
# person1.name = 'SimbA'
# person1.age = 21

# person2 = People()
# person2.name = 'Zaklin'
# person2.age = 20

# person3 = People()
# person3.name = 'Kalika'
# person3.age = 22

# print(person1)
# print(person2)
# print(person3)

# print(person1.name)
# print(person2.age)
# print(person3)






# # 2
# class People:
#     def __init__(self,name,age): # automatically initialize instance_variable or attributes (name,age) when we create instance # init method will run automatically when we create instance
#         self.name=name #self refereces to current instant ==> self.name => person1.name,person2.name,person3.name
#         self.age=age

# person1 = People('SimbA',21) # create instances of class(People) and pass instance_variable(name,age) values manually
# person2 = People('Zaklin',20)
# person3 = People('Kalika',22)

# print(person1)
# print(person2)
# print(person3)

# print(person1.name)
# print(person2.age)
# print(person3)

# # __init__() method will run automatically when we create instance(person1,person2,person3) of a class(Person)
# # when creating an instance(person1,person2,person3) of a class(Person) we should pass the values of  attributes(self,name,age) declare in__init__()method
# # as self refers to current instance we should not pass instance nase , python will recoznize its instance automatically.
# # person1 = People('SimbA',21) =# here self is occupied by person1 ...............(self,name,age)=>(person1,'SimbA',21)





# # after initializing the instance wee need some kind of ability to perform some klind of action
# # action may be ability to print out property of class
# # so to perform various action in class we can create methods


# # 3
# class People:
#     def __init__(self,name,age): 
#         self.name=name 
#         self.age=age
        
    

# person1 = People('SimbA',21) 
# person2 = People('Zaklin',20)
# person3 = People('Kalika',22)

# # we can perform action outside the class but its really annoying and concept of oop is useless if we write action_code for each instance manually
# print('{} is {} years old .'.format(person1.name,person1.age))
# print('{} is {} years old .'.format(person2.name,person2.age))
# print('{} is {} years old .'.format(person3.name,person3.age))
# # so instead lets define action_code_method within class, so that each instance can take reference of single_method 





# 4
class People:
    def __init__(self,name,age): 
        self.name=name 
        self.age=age
        
    # so instead lets define action_code_method within class   
    def display(self): # here self refers to current instant
        print('{} is {} years old .'.format(self.name,self.age))


person1 = People('SimbA',21) 
person2 = People('Zaklin',20)
person3 = People('Kalika',22)

# so that each_instance(person1,person2,person3) can take reference of single_method(display)
person1.display()
person2.display()
person3.display()
  
# same

People.display(person1)
People.display(person2)
People.display(person3)


