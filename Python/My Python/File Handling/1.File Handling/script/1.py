# open file and mode:r,w,a,x|t,b
# open,read,readline,write,close,
# os.remove()



# file_obj = open("nofile.txt")
# print(file_obj)

# file_obj = open("../file base/demo.txt")
# print(file_obj)
# # <_io.TextIOWrapper name='../file base/demo.txt' mode='r' encoding='cp1252'>

# file_obj = open("../file base/demo.txt")
# print(file_obj)
# # <_io.TextIOWrapper name='../file base/demo.txt' mode='r' encoding='cp1252'>

# file_obj = open("../file base/demo.txt")
# data = file_obj.read()
# print(data)
# data_piece = file_obj.read(5)
# print(data_piece)
# # once file is read, its closed automatically.
# # So open it again.

# file_obj1 = open("../file base/demo.txt")
# data = file_obj1.read()
# print(data)
# file_obj2 = open("../file base/demo.txt")
# data_piece = file_obj2.read(5)
# print(data_piece)

# file_obj = open("../file base/demo.txt")
# data_line = file_obj.readline()
# print(data_line)


file_obj = open("../file base/demo.txt")
for line in file_obj:
    print(line)
file_obj.close()
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.