# #1
# Current_Year = 2020
# class Person:
#     def __init__(self,name,year_born):
#         self.name=name
#         self.year_born=year_born
    
#     def getAge(self):
#         return Current_Year - self.year_born
    
#     def __str__(self): 
#         return '{} is {} years old.'.format( self.name , self.getAge() )
    
# person_1 = Person('Ram',1999)
# print(person_1) 
    
    
    




# # 2
# # Now, suppose that I wanted to define a new class to represent a student, and what I want a student class to have is everything
# # that a person has, plus one more thing. So I want students to have this notion of knowledge. So what I'm going to do, is I'm 
# # going to start by just copying and pasting my person class. So I can this, and then let's suppose that I want to have another
# # instance variable, named knowledge, which I'll start out as 0.

# Current_Year = 2020

# class Student:
#     def __init__(self,name,year_born):
#         self.name=name
#         self.year_born=year_born
#         self.knowledge = 0
    
#     def getAge(self):
#         return Current_Year - self.year_born
    
#     def study(self):
#         self.knowledge += 1
#         return self.knowledge 
    
#     def __str__(self): 
#         return '{} is {} years old and has {} knowledge.'.format( self.name , self.getAge() , self.study())
    
# student_1 = Student('Ram',1999)
# print(student_1) 
# student_1.study()  
# print(student_1) 
    









# Current_Year = 2020

# class Person: # parent_class
#     def __init__(self,name,year_born):
#         self.name=name
#         self.year_born=year_born
    
#     def getAge(self):
#         return Current_Year - self.year_born
    
#     def __str__(self): 
#         return '{} is {} years old.'.format( self.name , self.getAge() )

# class Student(Person): # child_class
#     def __init__(self,naam,DOB):  # child_class(Student)'s constructor
#         Person.__init__(self,naam,DOB)  # calling parents_class(Person)'s constructor and initializing child constructor_variable(naam,DOB)
#         self.knowledge = 0
    
#     def study(self):
#         self.knowledge += 1
 
    
# student_1 = Student('Ram',1999)
# print(student_1)# Inorder to print object of child_class(Student) it inherits __str__ method of parents_class(Person)
# print(student_1.knowledge)
# student_1.study()
# print(student_1.knowledge)









# # initializing constructor in inheritance

# class Person: 
#     def __init__(self,name,year_born):
#         self.name=name
#         self.year_born=year_born

# class Student(Person):
#     def __init__(self,naam,DOB):  # initialize child_class(Student)'s constructor
#         Person.__init__(self,naam,DOB) # reference to parents_class(Person)'s constructor and initialize child_class(Student)'s constructor
        
#         # reuse of code of parent constructor

# # def __init__(self,naam,DOB): ==>  Person.__init__(self,naam,DOB) ==> class Person: def __init__(self,name,year_born):
# # Student_obj.naam ==> Person_reference.naam ==> Person_reference.name
# # Student_obj.DOB ==> Person_reference.DOB ==> Person_reference.year_born










Current_Year = 2020

class Person: # parent_class
    def __init__(self,name,year_born):
        self.name=name
        self.year_born=year_born
    
    def getAge(self):
        return Current_Year - self.year_born
    
    def __str__(self): 
        return '{} is {} years old.'.format( self.name , self.getAge() )

class Student(Person): # child_class
    def __init__(self,naam,DOB):  # child_class(Student)'s constructor
        Person.__init__(self,naam,DOB)  # calling parents_class(Person)'s constructor and initializing child constructor_variable(naam,DOB)
        self.knowledge = 0
    
    def study(self):
        self.knowledge += 1
 
    
student_1 = Student('Ram',1999)
print(student_1)# Inorder to print object of child_class(Student) it inherits __str__ method of parents_class(Person)

# print(student_1.knowledge)

# student_1.study()
# print(student_1.knowledge)

# print(student_1.getAge())

# print(student_1.name)
# # print(student_1.naam) error as child_constructor has instanciated parent_constructor instant_variable as its instant_variable
# # Student_obj.naam ==> Person_reference.naam ==> Person_reference.name









