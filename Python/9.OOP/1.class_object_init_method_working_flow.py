# # 1
# class parent:
#     print("1")

#     def __init__(self):
#         print('haaaaaaaa')

#     def method2(self):
#         print('6')

# class child(parent):
#     print("2")

#     def __init__(self):
#         # super().__init__()
#         print('4')

#     def method1(self):
#         print('5')

# print('3')



# # 2
# class parent:
#     print("1")

#     def __init__(self):
#         print('haaaaaaaa')

#     def method2(self):
#         print('6')

# class child(parent):
#     print("2")

#     def __init__(self):
#         # super().__init__()
#         print('4')

#     def method1(self):
#         print('5')

# print('3')
# obj1 = child()
# obj1.method1()
# obj1.method2()




# 3
class parent:
    print("1")

    def __init__(self):
        print('5')

    def method2(self):
        print('8')

class Child(parent):
    print("2")

    def __init__(self):
        print('4')
        super().__init__()
        print('6')

    def method1(self):
        print('7')

print('3')
obj1 = Child()
obj1.method1()
obj1.method2()



# # 4 
# # class inheritance => init

# # 4 .1
# class parent:
#     def __init__(self):
#         print('p')
# obj = child()


# # 4 .2
# class parent:
#     def __init__(self):
#         print('p')

# class child(parent):
#     def __init__(self):
#         print('c')

# obj = child()



# # 4 .3
# class parent:
#     def __init__(self):
#         print('p')


# class child(parent):
#     # def __init__(self):
#     #     print('c')
#     pass

# obj = child()


# # 4 .3
# class parent:
#     def __init__(self):
#         print('p')


# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print('c')

# obj = child()