

# #Read the given_file
# file_obj_var = open("4.2.WriteOverwrite.txt")
# print('Original File :')
# print(file_obj_var.read())

# #over_write to given_file
# print('\n')
# print('Over write the original file :')
# file_obj_var = open('4.2.WriteOverwrite.txt','w')#add 'w' parameter
# file_obj_var.write('I have overwrite the original text-file')#overwrite
# file_obj_var = open('4.2.WriteOverwrite.txt')
# print(file_obj_var.read())
# #finally :
#         #open(filevar,'w')
#         #filevar.write('add_string')





# print('Over write the original empty file :')
# file_obj_var = open('4.3.WriteOverwrite.txt','w')
# print('As text_file is blank_empty if we try to read it it will show wrror not readable !!')
# print('\n')
# for number in range(13):
#     square = number * number
#     print(square)
#     file_obj_var.write(str(square))#inorder to write into the file we need to cast any datatype into str at first
#     print('Wrote',square,'Into The given blank_text_file !!!')
# file_obj_var.close()

# print('\n')

# # read the black file
# file_obj_var = open('4.3.WriteOverwrite.txt')
# print('Read Empty File :',file_obj_var.read())





# file_obj_var = open('4.3.WriteOverwrite.txt','w')
# for number in range(13):
#     square = number * number
#     file_obj_var.write(str(square) + '\n')#also write a line break
# # read the black file
# file_obj_var = open('4.3.WriteOverwrite.txt')
# print('Read Empty File :',file_obj_var.read())
# file_obj_var.close()





file_obj_var = open('4.3.WriteOverwrite.txt','w')
for number in range(13):
    square = number * number
    file_obj_var.write(str(square) + '\n')
file_obj_var = open('4.3.WriteOverwrite.txt')
print('Print First 10 chars :',file_obj_var.read()[:10])#observe there is a space after every intchar # it also count line break \n
file_obj_var.close()

