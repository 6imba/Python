# # - Read CSV files with quotes
# import csv
# with open('3.1 CSV File with quotes.csv', 'r') as file:
#     # reader = csv.reader(file)
#     # reader = csv.reader(file, skipinitialspace=True)
#     for row in reader:
#         print(row)



# # Delimiters: commas (,), semicolon (;), quotes ( ", ' ), braces ({}), pipes (|), slashes ( / \ ), space(d\<space>), tabs(\t)
#     # - When a program stores sequential or tabular data, it delimits each item of data with a predefined character.
# import csv
# with open('3.1 CSV File with quotes.csv', 'r') as file:
#     reader = csv.reader(file, delimiter = 'a')
#     for row in reader:
#         print(row)



# # CSV files with initial spaces
# import csv
# with open('3.1 CSV File with quotes.csv', 'r') as file:
#     reader = csv.reader(file, skipinitialspace=True)
#     for row in reader:
#         print(row)



# # CSV files with quotes:
# import csv
# with open('3.1 CSV File with quotes.csv', 'r') as file:
#     reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
#     for row in reader:
#         print(row)



# ------------------------------------------------------------------------------------------------------------------------
