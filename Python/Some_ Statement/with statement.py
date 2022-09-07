# - with statement in Python is used in exception handling to make the code cleaner and much more readable.
# - It simplifies the management of common resources like file streams.



# # 1) without using with statement
# file_object = open('with statement.txt', 'w')
# file_object.write('hello world1 !')
# file_object.close()



# # 2) without using with statement
# file_object = open('with statement.txt', 'w')
# try:
#     file_object.write('hello world2')
# finally:
#     file_object.close()



# # 3)using with statement
# with open('with statement.txt', 'w') as file_object:
#     file_object.write('hello world3 !')

# --------------------------------------------------------------------------------------------------------------------------------

# Reference:
#     - https://www.geeksforgeeks.org/with-statement-in-python/