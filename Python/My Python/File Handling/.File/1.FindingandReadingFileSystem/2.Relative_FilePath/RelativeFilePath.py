# 1:
filevar = open('../1.Filesystem/2.Fileysystem/3.FileSystem/1.FileSystemText.txt')
print(filevar.read())


#final conclusion:
#here folder of source code is '2.Relative_FilePath' and folder of needed_file is '1.1.Filesystem'
#here both '2.Relative_FilePath' and '1.Filesystem' is sub_directory of 1.FindingFileSystem
#so you have to give path upto the higher folder of file where folder_directory of needed_file,where directory of sourcecode and file is sub_directory of on main file

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# print(filevar) # <_io.TextIOWrapper name='../1.1.Filesystem/2.Fileysystem/3.FileSystem/1.FileSystemText.txt' mode='r' encoding='cp1252'>
# print(type(filevar)) # <class '_io.TextIOWrapper'>

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - To open the file, use the built-in open() function.

# f = open("demofile.txt")
# Or
# f = open("demofile.txt", "rt") #default
# - Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# - The open() function returns a file object, which has a read() method for reading the content of the file:
# f = open("demofile.txt", "r")
# print(f.read())


# - specify how many characters you want to read/return:
    # print(f.read(5))

# - specify how many lines you want to read/return:
    # print(f.readline())

# - By calling readline() two times, you can read the two first lines:

# - You can loop through the file-object returned by open method. where each of the line is element of itertable:file-object.

# - Close the file when you are done with it:
    # f.close()
    # -Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# - 

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Path:
    # - Current same dir path
    # - Relative path
    # - Absolute path
    # - Url path

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Read file:
# print(csv_file.read());
# print(csv_file.readline());
# print(csv_file.readlines());