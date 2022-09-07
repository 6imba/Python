import pandas as pd

read_file = pd.read_excel('../file_base/excel.xlsx')
read_file.to_csv('../file_base/font_url.csv', index = None, header=False)  # read csv file by skiping header&index from read spreadsheet file


