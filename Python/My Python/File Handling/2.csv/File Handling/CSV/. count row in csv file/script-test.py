csv_file = open("1.simple-csv-file.csv");
# csv_file = open("csv-sample.csv");
# csv_file = open("csv-sample.txt");
# csv_file = open("csv-sample-test.csv");

# 1:
count = 0;
for x in csv_file:
    count += 1
    print(x)
    print(type(x))
print(count)

# # 2:
# print(csv_file.readlines());
# print(type(csv_file.readlines())); #<class 'list'>
# print(len(csv_file.readlines()));

# # # list1 = [1,2,3,4,5,6,7]
# # list1 = ['1','2','3','4','5','6','7']
# list1 = ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n']
# print(list1)
# print(type(list1))
# print(len(list1))