# # 1
# #Same_Directory
filevar = open('3s.SameDirectFile.txt')
print(filevar.read())
# #If your file and your Python program are in the same directory you can simply use the filename.


# 2
#Relative_File_Path
# filevar = open('1.1.Filesystem2.Fileysystem3.FileSystem/1.FileSystemText.txt')
# print(filevar.read())

#If your file and your Python program are in different directories, however, then you need to specify a path.
#Typically, you will specify a relative file path, which says where to find the file to open, relative to the directory where the code is running from.
#The ../ means to go up one level in the directory structure, to the containing folder (allProjects); myData/ says to descend into the myData subfolder.

#Means in which file_directory(folder), file_directory(folder) of source_code and  file_directory(folder) of sourde_file(textfile) meets?
#for this code:
#Means in 2.Fileysystem , 7.FindingFileSystem of 1.FileSytemCode and 7.FindingFileSystem of 1.FileSystemText meets.


# # 3
# #Absolute_File_Path
# filevar = open('C:/Users/User/Desktop/AbsoluteFile.txt')
# print(filevar.read())

# #There is also an option to use an absolute file path. For example, suppose the file is stored on a in any directory inside computer, Then code in any Python program running from any file folder could open that file by telling an absolute file path.
# #Absolute File Path is more easy because If you will ever move your programs and data to another computer (e.g., to share them with someone else), it will be much more convenient if your use relative file paths rather than absolute.  That way, if you preserve the folder structure when moving everything, you won’t need to change your code. If you use absolute paths, then the person you are sharing with probably not have the same home directory name, /Users/joebob01/. Note that Python pathnames follow the UNIX conventions (Mac OS is a UNIX variant), rather than the Windows file pathnames that use : and \. The Python interpreter will translate to Windows pathnames when running on a Windows machine; you should be able to share your Python program between a Windows machine and a MAC without having to rewrite the file open commands.

