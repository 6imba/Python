# # 1:
# csv_file1 = open('./CSV_file_with_CSV_data.csv')
# lines1= [line for line in csv_file1] #list_comprehensive
# print(lines1) #list of string(record)
# print(len(lines1))
# print(lines1[0]) #str with line_break:'\n'
# print(lines1[0].strip()) #str with no line_break:'\n'
# print(lines1[0].strip().split()) #lists of field
# print(len(lines1[0].strip().split()))
# print(lines1[0].strip().split(",")) #lists of field
# print(len(lines1[0].strip().split(",")))
# # - strip(): The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
# # - The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.

# # 2:
# csv_file2 = open('./CSV_file_with_CSV_data.csv')
# lines2 = [line.strip().split(",") for line in csv_file2] # list of list using list_comprehensive,strip,split.
# print(lines2) #list of list
# print(lines2[0]) #nested list
# print(lines2[1]) #nested list
# print(lines2[2]) #nested list

