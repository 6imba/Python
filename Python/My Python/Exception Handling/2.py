# 1:
import sys
# print(sys) #<module 'sys' (built-in)>
# print(sys.exc_info) #<built-in function exc_info>
# print(sys.exc_info()) #(None, None, None)
# print(sys.exc_info()[0]) #None
# print(type(sys.exc_info())) #<class 'tuple'>
# print(type(sys.exc_info()[0])) #<class 'NoneType'>

# # 2:
# 1/0

# # 3:
# try:
#     1/0
# except:
#     print("Exception detected:")
#     print(sys.exc_info()[0])
#     print(sys.exc_info())
#     print(sys.exc_info()[1])
#     print(sys.exc_info()[2])


# # 4:TypeError
# try:
#     'x'+1
# except:
#     print("Exception detected:")
#     print(sys.exc_info())


# # 5: NameError
# try:
#     print(x)
# except:
#     print("Exception detected:")
#     print(sys.exc_info())



# # 6.1: get error_type using base Exception class.
# try:
#     print(x)
# except Exception as e:
#     print("Exception detected:")
#     print(e.__class__)
# # 6.2: get error_type using sys module.
# try:
#     print(x)
# except:
#     print("Exception detected:")
#     print(sys.exc_info()[0])



