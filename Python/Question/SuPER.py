class A2:
    name2='Amir'
    age2=21
    def show2(self):
        print('Hello class A !')
    
class B2(A2):
    naam2='Zoya'
    umer2=19
    def output2(self):
        print('Hello class B !')
        super().show2()
        obj2.show2()
        self.show2()
        
obj2=B2()
print(obj2.naam2)
print(obj2.umer2)
obj2.output2()


# here we can use same object(obj2) to inherit outside the class