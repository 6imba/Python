# #1
# print(len(range(2,2)))
#
# # range(2, 2) is an empty sequence. Ranges are half-open, so range(2, 2) means "all integers >=2 but <2", of which there are none:
# # https://stackoverflow.com/questions/51940104/python-for-i-in-range2-2-printi-what-does-i-variable-contain-it-doesnt-co
# # >>> len(range(2, 2))
# # 0
#
# # >>> list(range(2, 2))
# # []
#
# # >>> it = iter(range(2, 2))
# # >>> next(it)
# # StopIteration:


## 2
# i = 'this is a string'
# for i in range(2, 2):
#     pass
# print(i)
#
# for i in range(2, 6):
#     pass
# print(i)



# #3
#
# def func1(number):
#     if number == 1 or 0:
#     # if number == 0 or 1:
#         return False
#
# number = 0
# print(func1(number))
#
# number = 1
# print(func1(number))



# 4
# print('2'+'2')
# print('2','2')


# #5 slice operator
# a='0123456789'
# print(a[:])
# print(a[0:10])
# print(a[0:10:1])
# print(a[::-1])
# print(a[::-2])
# # all same