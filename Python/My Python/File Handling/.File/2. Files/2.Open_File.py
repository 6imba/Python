# # 1
# #Read the given_file
# file_obj_var = open("2.Open_File.txt")
# print(file_obj_var.read())

# # 2.1
# # Write to an Existing File
# # write method help to write into the given file.....
# file_obj_var = open('2.Open_File.txt')
# file_obj_var.write("Hill Low Guwaes !")#write() method


# Note :
#write() method only cant write to the file as Python provides two ways to write into the given_file
#i.e. append and write
#so we can use any of the ways to write into the file by passing respectival mode....
#i.e. "a" or "w" --> mode


#To write to an existing file, you must add a parameter to the open() function:
#i.e. open('filename','mode')
#i.e. open('2.Open_File.txt','a') ==> Append - Opens a file for appending
#i.e. open('2.Open_File.txt','w') ==> Write - Opens a file for writing
#futher-other_more_of_mode:
#i.e. open('2.Open_File.txt','x') ==> Create - Creates the specified file
#i.e. open('2.Open_File.txt','x') ==> Binary - Binary mode (e.g. images)
#i.e. open('2.Open_File.txt','r') ==> Read - Default value. Opens a file for reading
#i.e. open('2.Open_File.txt','t') ==> Text - Default value. Text mode

#here mode 'r'=>Read and 't'=>Text are both default, no need to mentioned

# note: now note that the proper syntax of open() method is
# syntax:
#     open('filename','mode')
#     here, open() method takes  two parameter i.e filename and mode
# print('\n')


# Finally,
# 2.2
# Write to an Existing File
# write method help to write into the given file.....
# file_obj_var = open('2.Open_File.txt', 'w')
# file_obj_var = open('2.Open_File.txt', 'a')
# file_obj_var.write("Hill Low Guwaes !")#write() method
# file_obj_var.write("\nHill Low Guwaes !")#write() method

# Therefore:
# a-mode appends new_text to existing_text at last
# w-mode overwrite existing_text with new_text
