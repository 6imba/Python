# #1
# class Points:

#     def __init__(self, x_cord, y_cord):
#         print('............ __init__ .............')
#         self.x = x_cord
#         self.y = y_cord

# print('Instance_Object ..........')
# p1 = Points(2,7)
# print('Printing Instance_Object ..........')
# print(p1)





# #2
# class Points:

#     def __init__(self, x_cord, y_cord):
#         print('............ __init__ .............')
#         self.x = x_cord
#         self.y = y_cord

#     def __str__(self):
#         print('............ __str__ .............')
#         return '{} {}'.format(self.x,self.y)

# print('Instance_Object ..........')
# p1 = Points(2,7)
# print('Printing Instance_Object ..........')
# print(p1)




#3
class Points:

    def __init__(self, x_cord, y_cord):
        print('............ __init__ .............')
        self.x = x_cord
        self.y = y_cord

    def __str__(self):
        print('............ __str__ .............')
        return '{} {}'.format(self.x,self.y)


    def add(p1):
        print('............ add .............')
        return p1.x+p1.y


p1 =Points(9,23)
print(p1)
print(p1.add())