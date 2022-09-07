# # 1:
# print(open('../.csv-data.csv')) # The open() function opens the file as file object(returns a file object).

# ------------------------------------------------------------------------------------------------------------------------

# # 2: Read Files.
# print(open('../.csv-data.csv', 'r')) # open file for read mode
# print(open('../.csv-data.csv', 'r').read()) # read the file using read() method. Reading the content of the file.
# print(open('../.csv-data.csv', 'r').read(50)) # read() method returns the whole text, but you can also specify how many characters you want to return.
# print(open('../.csv-data.csv', 'r').readline()) # return one line by using the readline() method.

# print(open('../.csv-data.csv', 'r').readline()) # return one line by using the readline() method.
# print(open('../.csv-data.csv', 'r').readline()) # By calling readline() two times, you can read the two first lines.

# content = open('../.csv-data.csv')
# for line in content:
#     print(line)
# # By looping through the file-object, you can read the whole file, line by line:

# ------------------------------------------------------------------------------------------------------------------------

# # 3: File Write.

# # - "a" - Append - will append to the end of the file
# print(open('../.csv-data.csv', 'a')) # open file for append mode
# print(open('../.csv-data.csv', 'a').write('7,Sahasa,GK,7777777,Sundhara')) # write() method with mode:'a' append content to the end of the file.

# # - "w" - Write - will overwrite any existing content
# print(open('../.csv-data.csv', 'w')) # open file for write mode
# print(open('../.csv-data.csv', 'a').write('8,Temb,Tourism,888888,Khumbu')) # write() method with mode:'a' append content to the end of the file.

# .write() methods returns the length of added content.

# ------------------------------------------------------------------------------------------------------------------------

# # 4: Delete a File.

# - To delete a file, you must import the OS module, and run its os.remove() function:

# import os
# print(os.remove("del-test.txt")) # returns None

# import os
# if os.path.exists("del-test.txt.txt"):
#     os.remove("del-test.txt.txt")
# else:
#     print("The file does not exist!")

# ------------------------------------------------------------------------------------------------------------------------

# # 5: Delete a Folder.

# # - To delete an entire folder, use the os.rmdir() method:

# import os
# print(os.rmdir("testDelMyfolder")) # returns None

# # - You can only remove empty folders.

# ------------------------------------------------------------------------------------------------------------------------

# # 6: Close Files.
# print(open('../.csv-data.csv').close())

# ------------------------------------------------------------------------------------------------------------------------