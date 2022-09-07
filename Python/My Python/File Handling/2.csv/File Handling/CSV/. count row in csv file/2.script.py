csv_file_obj = open("2.extra-space-csv-file.csv");

# import csv
# print(len(list(csv.reader(csv_file_obj))))

count = 0;
for x in csv_file_obj:
    print(x)
    print(len(x))
    print(x == '')
#     print(type(x))
#     if(x != ''):
#         count += 1;
# print(count)
