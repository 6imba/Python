#7.1

class Person(): # Parent Class
    print('2')
    def __init__(self,Name,Age,Color):
        print('4')
        self.NAME = Name
        self.AGE = Age
        self.COLOR = Color

    def info1(self):
        print('7')
        print(self.AGE,' years old ',self.NAME,' has ',self.COLOR,' hair.')

class Student(Person): # Child Class
    print('1')
    def __init__(self,name,age,color,country,zone):
        print('3')
        super().__init__(name,age,color)
        print('5')
        self.desh = country
        self.anchal = zone

    def info2(self):
        print('6')
        print('Country ==> ',self.desh,' Zone ==> ',self.anchal)

    def final_info(self):
        print('8')
        print(self.NAME,' is ',self.AGE,' years old has ',self.COLOR,' hair color and lives in  ',self.desh,' Zone ',self.anchal)

print('Main')
obj1=Student('Hari','27','Black','Nepal',14)
obj1.info2()
obj1.info1()
obj1.final_info()