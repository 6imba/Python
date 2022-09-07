# Read the given_file:
file_obj_var = open("4.1.WriteAppend.txt")
print('Original File :')
print(file_obj_var.read())


# Write to an Existing File:
# write method help to write into the given file.....
#file_obj_var = open('4.1.WriteAppend.txt')
#file_obj_var.write("Hill Low Guwaes !")#write() method

#write() method only cant write to the file as Python provides two ways to write into the given_file
#i.e. append and write
#so we can use any of the ways to write into the file by passing respectival mode....
#i.e. { "a"->append or "w"->overwrite } ==> write_mode

#To write to an existing file, you must add a parameter to the open() function:
#i.e. open('filename','mode')
#i.e. open('4.1.WriteAppend.txt','a')
#i.e. open('4.1.WriteAppend.txt','w')
#futher-other_more_of_mode:
#i.e. open('4.1.WriteAppend.txt','x')
#i.e. open('4.1.WriteAppend.txt','r') ==> Read - Default value. Opens a file for reading
#i.e. open('4.1.WriteAppend.txt','t') ==> Text - Default value. Text mode

#here mode 'r'=>Read and 't'=>Text are both default no need to mentioned

#     here, open() method takes  two parameter i.e filename and mode

# note: now note that the proper syntax of open() method is
# syntax:
#     open('parameter','parameter')
#     open('filename','mode')
#     open('4.1.WriteAppend','w')



# # append to given_file
# print('Append into the given_file :')
# file_obj_var = open('4.1.WriteAppend.txt','a')#add 'a' parameter
# file_obj_var.write("Hill Low Guwaes !")#append string

# file_obj_var = open('4.1.WriteAppend.txt')#its compulsary to open file again to read file after writing
# print(file_obj_var.read())#read file after append

#note:for the number of time you execute the append method for that number of the it keeps appendin/adding string to given file

#finally :
        #open(filevar,'a')
        #filevar.write('add_string')

