# # 1. csv module:
# import csv
# print(csv) #module ==> type:<class 'module'>, identity:<module 'csv' from 'C:\\Python3.9.4\\lib\\csv.py'>.
# # print(dir(csv)) #list ==> type:<class 'list'>, shows directory of csv module
# # print(type(csv.__dict__)) # type: <class 'dict'>
# # print(csv.__dict__.keys()) # type: <class 'dict_keys'>
# # help(csv)

# # ------------------------------------------------------------------------------------------------------------------------

# 2. Read CSV File:
import csv
csv_file1 = open('1.CSV_Formate.csv') # returns file_object for mode:'r' ==> <_io.TextIOWrapper name='2.Wite_CSV.csv' mode='r' encoding='cp1252'>
reader_object = csv.reader(csv_file1) # returns a reader_object ==> <_csv.reader object at 0x000001EA04892580>

# print(reader_object) #<_csv.reader object at 0x0000029489DE28E0>



for row in reader_object:
    print(row) #list
    print(type(row)) #list

# data = [row for row in reader_object] #read remaining data
# print(data) # lists of list
# print(data[0])
# print(data[0][0])
# print(type(data[0][0]))
# print(data[0][1], ' ==> Type:' ,type(data[0][1]))

# header = next(reader_object)
# print(header) #list: ['Id', 'Name', 'Faculty', 'Contact', 'Address'] ==> The first line is header
# print(type(header)) #<class 'list'>
# - An iterator is an object with a next() method that will return the next value available or raise StopIteration if no value is available.


