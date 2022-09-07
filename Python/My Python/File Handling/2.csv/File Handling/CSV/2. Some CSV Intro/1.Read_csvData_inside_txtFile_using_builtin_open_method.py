# # 1:
# txt_file = open('./1.Text_file_with_CSV_data.txt')
# # print(txt_file) #<_io.TextIOWrapper name='./1.Text_file_with_CSV_data.txt' mode='r' encoding='cp1252'>
# # print(type(txt_file)) #<class '_io.TextIOWrapper'> 
# for line in txt_file:
#     print(line)
#     print(type(line)) # str

# # 2:
# txt_file = open('./1.Text_file_with_CSV_data.txt')
# for line in txt_file:
#     print(line)

# # 3:
# txt_file = open('./1.Text_file_with_CSV_data.txt')
# lines = [line for line in txt_file] #list_comprehensive
# print(lines) #list
# print(lines[0]) #str with line_break:'\n'
# print(lines[0].strip()) #str with no line_break:'\n'
# print(lines[0].strip().split()) #lists
