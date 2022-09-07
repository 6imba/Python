

# #CSV stands for Comma Separated Values
# #If you print out tabular data in CSV format, it can be easily imported into other programs like Excel, Google spreadsheets, or a statistics package (R, stata, SPSS, etc.).
# file_var = open("9.CSV_File.txt") #9.CSV_File.txt is the csv file.
# print(file_var)


# file_var = open("9.CSV_File.txt")
# lines = file_var.read()
# print(lines)



# file_var = open("9.CSV_File.txt")
# print(file_var.readlines())



# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()
# for line in lines:
#     print(line)



# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()
# for line in lines:
#     print(line[:6])



# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()
# for line in lines[:6]:
#     print(line)




# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()
# for line in lines[:6]:
#     print(line.strip())#??? strip() method to get rid of the trailing n.




# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()
# header = lines[0]
# print(header)




# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()
# header = lines[0]
# header_feild_item = header.split(',')
# print(header_feild_item)



# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()
# header = lines[0]
# header_feild_item = header.strip().split(',')#strip() funtion removes '\n'->line_breaker
# print('Header Items List : ',header_feild_item)
# #split() method splits a string into a list where each word is a list item
# #here header hold the string of header_detial and split() method split it into list hold by header_feild_item




# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()

# header = lines[0]
# header_feild_item = header.strip().split(',')#strip() funtion removes '\n'->line_breaker
# print('Header Items List : ',header_feild_item)

# for rows in lines[1:6]:
#     print(rows)




# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()

# header = lines[0]
# header_feild_item = header.strip().split(',')#strip() funtion removes '\n'->line_breaker
# print('Header Items List : ',header_feild_item)

# for rows in lines[1:6]:
#     rows_values = rows.strip().split(',')
#     print(rows_values)






# file_var = open("9.CSV_File.txt")
# lines = file_var.readlines()

# header = lines[0]
# header_feild_item = header.strip().split(',')#strip() funtion removes '\n'->line_breaker
# print('Header Items List : ',header_feild_item)

# for rows in lines:
#     rows_values = rows.strip().split(',')
#     if rows_values[5] != 'NA': #only if index 5 of rows_values has medal
#         print(rows_values)#print the list of olompians with medals only.






# #formate method
# #The format() method formats the specified value(s) and insert them inside the string's placeholder{}.
# #string.format(value1, value2...)
# #e.g => "My name is {}".format("Amir Shrestha")
# print("My name is {}".format("Amir Shrestha"))
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))




# #named indexes:
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# #numbered indexes:
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# #empty placeholders:
# txt3 = "My name is {}, I'm {}".format("John",36)

# print(txt1)
# print(txt2)
# print(txt3)



# #print players with medal using format method
# file_var = open("9.CSV_File.txt")#open file
# players_detial_lines = file_var.readlines()#all players of file
# for single_player in players_detial_lines:#single player of file
#     player_detial = single_player.strip().split(",")#listitem of single player of file
#     if player_detial[5] != "NA":#check if player has medal or not 
#             print("Name:{} Event:{} Medal:{}".format(player_detial[0],player_detial[4],player_detial[5]))#print detial in format method

