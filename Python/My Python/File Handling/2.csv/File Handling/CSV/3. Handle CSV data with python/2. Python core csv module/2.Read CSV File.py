# # 1:
# import csv
# with open('2.Wite_CSV.csv', 'r') as file:
#     print(file) # <_io.TextIOWrapper name='2.Wite_CSV.csv' mode='r' encoding='cp1252'>

# # 2:
# import csv
# with open('2.Wite_CSV.csv', 'r') as file:
#     reader = csv.reader(file)
#     print(reader) # <_csv.reader object at 0x0000027967812820>

# # 3:
# import csv
# with open('2.Wite_CSV.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#         # print(type(row)) # list

# # 123
# import csv
# with open('2.Wite_CSV.csv', 'r') as file:
#     reader = csv.reader(file)
#     # reader = csv.reader(file, skipinitialspace=True)
#     # reader = csv.reader(file, skipinitialspace=True, quoting=csv.QUOTE_ALL)
#     for row in reader:
#         print(row)