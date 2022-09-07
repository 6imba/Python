# # 1
# def return_odd_ints(i):
#     x = 1
#     while x <= i:
#         print(x)
#         return x #as returns gets executed it just gets out of function at the time returing the value
#         x += 2

# output = return_odd_ints(10)
# print(output)
# print(type(output))
# for out in output:
#     print(out)







# # 2
# def return_odd_ints(i):
#     x = 1
#     while x <= i:
#         print(x)
#         print(type(x))
#         yield x #as returns gets executed it just gets out of function at the time returing the value
#         x += 2

# output = return_odd_ints(10)
# print(output, "**********************")
# print(type(output))
# for out in output:
#     print(out)









# # 3
# def p():
#     print('hi')
# p()
# print(p()) # as no return keyword so output: None







# # 3.1
# def p():
#     print('hi')
#     return 1
# p()

# # 3.2
# def p():
#     print('hi')
#     return 1
# print(p())

# # 3.2
# def p():
#     print('hi')
#     return 1
# x=p()
# print(x)

# # 3.3
# def p():
#     for i in range(5):
#         print('hilo')
# p()


# # 3.4
# def p(x):
#     for i in range(x):
#         print('hilo')
# p(5)



# # 3.5
# def return_odd_ints(i):
#     x = 1
#     while x <= i:
#         print(x)
#         print(type(x))
#         x += 2
# output = return_odd_ints(10)



# # 3.6
# def return_odd_ints(i):
#     x = 1
#     while x <= i:
#         print(x)
#         print(type(x))
#         yield x #as returns gets executed it just gets out of function at the time returing the value
#         x += 2
# output = return_odd_ints(10)

# # 3.7
# def return_odd_ints(i):
#     x = 1
#     while x <= i:
#         print(x)
#         print(type(x))
#         yield x #as returns gets executed it just gets out of function at the time returing the value
#         x += 2

# output = return_odd_ints(10)
# print(output)
# print(type(output))