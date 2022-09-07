# 1: Using external pasndas module.
# import pandas
# content = pandas.read_csv(".csv-file.csv"); # returns DataFrame
# print(len(content) + 1)

# # 2: Using core csv module.
# import csv
# with open('.csv-file.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     # csvreader = csv.reader(file, skipinitialspace=True)
#     print(csvreader.line_num)

# import csv
# with open(".csv-file.csv", 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)

#     # get total number of rows
#     print("Total no. of rows: %d"%(csvreader.line_num))


# # 2: Using core csv module.
# import csv
# with open('.csv-file.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         print(csvreader.line_num)

# # 2: Using core csv module.
# import csv
# with open('.csv-file.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile, skipinitialspace=True)
#     for row in csvreader:
#         print(row)

# 2: Using core csv module.
import csv
rows = 0
with open('.csv-file.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, skipinitialspace=True)
    for row in csvreader:
        rows += 1
print(rows)