# mode : r
# methdo : read(), readline(), readlines(), read(6)

# #Once you have a file “object”, the thing returned by the open function, Python provides three methods to read data from that object.
# #read(),realine(),readlines()

# file_obj_var = open('3.ReadToFile.txt')#reference to file object in filevariable(file_obj_var)
# print(file_obj_var.read())#read() method

# #The read() method returns the entire contents of the file as a single string (or just some characters if you provide a number as an input parameter. 
# #note : never forget the file extention as (.txt) for this givn file

# #finally :
#         #open('filevar')
#         #filevar.read()








# file_obj_var = open('3.ReadToFile.txt','r') # 'r' mode is optional its default
# print(file_obj_var.readline())#readline() method
# #The readline method reads one line from the file and returns it as a string. 

# # finally : 
# #         open('filevar')
# #         filevar.readline()





# file_obj_var = open('3.ReadToFile.txt')
# print(file_obj_var.readlines())#readlines() method

# #The readlines method returns the entire contents of the entire file as a list of strings, where each item in the list is one line of the file. 

# #finally :
#         #open('filevar')
#         #filevar.readlines()






#read file with n number of char

# file_obj_var = open('3.ReadToFile.txt')
# print(file_obj_var.read(2))

# print('\n')

# file_obj_var = open('3.ReadToFile.txt')
# print(file_obj_var.readline(6))

# print('\n')

# file_obj_var = open('3.ReadToFile.txt')
# print(file_obj_var.readlines(12))#readlines() method

# #note:  If n is provided then n characters are read 





# file_obj_var = open('3.ReadToFile.txt')
# print(file_obj_var.readlines())#readlines() method

# #note : A common error that novice programmers make is not realizing that all these ways of reading the file contents, use up the file. After you call readlines(), if you call it again you’ll get an empty list.

# #note if you try to read a file which is blank or empty then it will show error not readable

