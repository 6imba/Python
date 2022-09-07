# #1
# class A:
#     lista=['1','2']
#     def output(self):
#         print(self.lista) #print list of same_class inside_function in same_class using self__current_instance
#         print(A.lista) #print list inside function of same_class using class_name(A)
#     print(lista) #print list of inside_current_class
    
# print(A.lista) #print list FROM outside_class

# a=A()
# a.output()



# 2

class A:
    lista=['a','b','c']
    print('2....',lista) #inside_class
    
print('1...',A.lista)#outside_class

class B(A):
    def output(self):
        print(self.lista)
        self.lista.append('z')
        print(A.lista)

objB=B()
objB.output()

