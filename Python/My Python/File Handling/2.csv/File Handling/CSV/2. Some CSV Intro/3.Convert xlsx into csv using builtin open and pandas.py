# # 1:
# excel_file = open('./3.Excel-Tabular-Data.xlsx')
# print(excel_file) #<_io.TextIOWrapper name='./3.Excel-Tabular-Data.xlsx' mode='r' encoding='cp1252'>

# # 2:
# excel_file = open('./3.Excel-Tabular-Data.xlsx')
# lines1= [line for line in excel_file]
# # UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 22: character maps to <undefined>

# If I have a excel_worksheet and i want to work with data in that excel_worksheet.
# Directly working with excel_worksheet's data is not possible because none of the software, except MS_Excel, doesn't accepts excel_file.
# So, we use csv formate.
# So first we need to convert excel_file(.xlsx) into CSV_file(.csv) & then work with this CSV_file(.csv).

# # 2: pip install pandas, openpyxl
import pandas as pd
read_file = pd.read_excel (r'./3.Excel-Tabular-Data.xlsx')
print(read_file)
# read_file.to_csv (r'C:\PythonDjango\Python\Data_Storing_File_Formate\3.CSV\Code\2. Handle CSV file\.csv-data.csv', index = None, header=True)
