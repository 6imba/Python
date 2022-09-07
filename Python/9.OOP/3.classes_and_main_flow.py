class Person:
    print(1)
    def __init__(self, fname, lname):
        print(5)
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(8)
        print(self.firstname, self.lastname)

class Student(Person):
    print(2)
    def __init__(self, fname, lname):
        print(4)
        super().__init__(fname, lname)
        print(6)


print(3)
x = Student("Mike", "Olsen")
print(7)
x.printname()
print(9)
