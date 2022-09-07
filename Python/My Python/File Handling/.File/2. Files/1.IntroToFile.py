# Note:
# reference_to_file_object = open("1.IntroToFile.txt",'r')
# reference_to_file_object = open_function("File_name",'action_to_file')
# open() = To open the given filename, we would call the open function that returns file_object
# 'r' -> action_to_file -> allows to read the opened_file
# reference_to_file_object = Variable that holds a reference to the file_object returned by open

# # 1:
# reference_to_file_object = open("1.IntroToFile.txt",'r')
# content = reference_to_file_object.read()#.read() -> reads whole file_content hold by file_object(reference_to_file_object)
# print(content)
# print('\n')
# print(content[:160])
# reference_to_file_object.close()#close reference to the file_object returned by open

# # Python file method close() closes the opened file. A closed file cannot be read or written any more. Any operation, which requires that the 
# # file be opened will raise a ValueError after the file has been closed. Calling close() more than once is allowed



# # The open() function opens a file, and returns it as a file object.
# print(open("1.IntroToFile.txt",'r'))
# # Output:
# # <_io.TextIOWrapper name='1.IntroToFile.txt' mode='r' encoding='cp1252'>



# # 2
# reference_to_file_object = open("1.IntroToFile.txt",'r')
# all_lines = reference_to_file_object.readlines()
# print(all_lines)#print '\n' after each paragrapgh
# #readlines() -> gives list_of_lines present in paragraph where each single paragraph is a string i.e list_of_string.Each string is ended 
# #  with '\n' means new string begin

# # Output:
# # ['Topic sentences are similar to mini thesis statements. Like a thesis statement, a topic sentence has a specific main pointapple,banana,cata,dog. \n', 'I am SimbA. I am Living Being.\n', 'I am Ryagor. I am Alien.']


# # 3
reference_to_file_object = open("1.IntroToFile.txt",'r')
all_lines = reference_to_file_object.readlines()

# # 3.1
# for line in all_lines:#here line holds each paragrapgh of all_lines of file(paragrapgh) seperately.
#     print(line)#print each paragraph seperately


# # 3.2
# for line in all_lines:
#     print(line[:20])#print first 20 char of each seperate_paragraph from index 0-19

# # 3.3
# for line in all_lines[:2]:#print first two paragraph
#     print(line)


# # 3.4
# for line in all_lines[:1]:
#     print(line)

# # #note : [:3] means [0,1,2]

# # 3.5
# for line in all_lines:
#     print(line.strip())

# # strip() method -> removes characters from both left and right based on the argument (a string specifying the set of characters to be removed).
# # string = '  xoxo love xoxo   ' --> print(string.strip()) --> Output : 'xoxo love xoxo' --> remove front and back space
# # print(line.strip) this gives some kind of output what does this mens???????
# # print(line.strip) ====> Output:<built-in method strip of str object at 0x000002C45C480670>





