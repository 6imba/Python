# # 1
# nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
# for x in nested1:
#     print("level1: ")
#     for y in x:
#         print("     level2: " + y)


# # 2
# #Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains 
# every person’s last name, and save that list as last_names.

# info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
# last_names=[]

# for celebs in info:
#     last_names.append(celebs[1])
    
# print(last_names)


# # 3
# #Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.

# List = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
# b_strings = []

# for list in List:#nested_list
#     for item in list:
#         for char in item:
#             if char=='b':
#                 b_strings.append(item)     
# print(b_strings)


# List = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
# b_strings = []

# for list in List:#nested_list
#     for item in list:
#         if 'b' in item:
#             b_strings.append(item)     
# print(b_strings)


