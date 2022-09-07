Current_Year = 2020
print('1')
class Person: # parent_class
    print('2')
    def __init__(self,name,year_born):
        print('3')
        self.name=name
        self.year_born=year_born
    
    def getAge(self):
        print('4')
        return Current_Year - self.year_born
    
    def __str__(self): 
        print('5')
        return '{} is {} years old.'.format( self.name , self.getAge() )
    print('22')


print('6')
class Student(Person): # child_class
    print('7')
    def __init__(self,naam,DOB):  # child_class(Student)'s constructor
        print('8')
        Person.__init__(self,naam,DOB)  # calling parents_class(Person)'s constructor and initializing child constructor_variable(naam,DOB)
        self.knowledge = 0
    
    def study(self):
        print('9')
        self.knowledge += 1
    print('77')
 

print('10')  
student_1 = Student('Ram',1999)
print('12')
print(student_1)# Inorder to print object of child_class(Student) it inherits __str__ method of parents_class(Person)
print('13')
student_1.study()
print(Current_Year)




# class Person:
#     print(1)
#     def __init__(self, fname, lname):
#         print(4)
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(7)
#         print(self.firstname, self.lastname)

# class Student(Person):
#     print(2)
#     def __init__(self, fname, lname):
#         # self.firstname = fname
#         # self.lastname = lname
#         print(3) # error
#         super().__init__(fname, lname)
#         print(5)

# x = Student("Mike", "Olsen")
# print(6)
# x.printname()
# print(8)







# class Person:
#     print(1)
#     def __init__(self, fname, lname):
#         print(4)
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(7)
#         print(self.firstname, self.lastname)

# class Student(Person):
#     print(2)
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#         print(3)
#         super().__init__(fname, lname)
#         print(5)

# x = Student("Mike", "Olsen")
# print(6)
# x.printname()
# print(8)