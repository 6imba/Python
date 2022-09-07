# # 1. Write CSV File:
# import csv
# file_object = open('3.Wite_CSV.csv', 'w') # returns file_object for write mode.
# writer_object = csv.writer(file_object) # Return a writer_object. ==> <_csv.writer object at 0x00000160BA40BA40>
# x = writer_object.writerow([3,'John','CSIT',33333,'Boudha']) # returns character length. # overwrite file_content with new_row + two linw_break(/n)
# # writer_object.writerow("3,John,CSIT,33333,Boudha")



# # Steps for writing a CSV file:
# #     - First, open the CSV file for writing (w mode) by using the open() function.
# #     - Second, create a CSV writer object by calling the writer() function of the csv module.
# #     - Third, write data to CSV file by calling the writerow() or writerows() method of the CSV writer object.
# #     - Finally, close the file once you complete writing data to it.



# # The following code illustrates the above steps:
# import csv
# # open the file in the write mode
# f = open('path/to/csv_file', 'w')
# # create the csv writer
# writer = csv.writer(f)
# # write a row to the csv file
# writer.writerow(row)
# # close the file
# f.close()



# # It’ll be shorter if you use the with statement so that you don’t need to call the close() method to explicitly close the file:
# import csv
# # open the file in the write mode
# with open('path/to/csv_file', 'w') as f:
#     # create the csv writer
#     writer = csv.writer(f)
#     # write a row to the csv file
#     writer.writerow(row)



# # - Writing to CSV files example
# # - The following example shows how to write data to the CSV file:
# import csv
# header = ['name', 'area', 'country_code2', 'country_code3']
# data = ['Afghanistan', 652090, 'AF', 'AFG']
# with open('countries.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     # write the header
#     writer.writerow(header)
#     # write the data
#     writer.writerow(data)



# - To remove the blank line, you pass the keyword argument newline='' to the open() function as follows:
    # open('countries.csv', 'w',  newline='')


# # Writing multiple rows to CSV files at once:
# import csv
# header = ['name', 'area', 'country_code']
# data = [
#     ['Albania', 28748, 'AL'],
#     ['Algeria', 2381741, 'DZ'],
#     ['American Samoa', 199, 'AS'],
#     ['Andorra', 468, 'AD'],
#     ['Angola', 1246700, 'AO']
# ]
# # with open('3.Wite_CSV.csv', 'w') as f:
# with open('3.Wite_CSV.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     # write the header
#     writer.writerow(header)
#     # write multiple rows
#     writer.writerows(data)

# ------------------------------------------------------------------------------------------------------------------------

# - If each row of the CSV file is a dictionary, you can use the DictWriter class of the csv module to write the dictionary to the CSV file:
import csv
# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code3']
# csv data
rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]
with open('3.Wite_CSV.csv', 'w', newline='') as f:
# with open('3.Wite_CSV.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# ------------------------------------------------------------------------------------------------------------------------
