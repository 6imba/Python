import pandas as pd
read_file = pd.read_excel (r'./excel.xlsx', index_col=0) # read spreadsheet file by skipping first column
read_file.to_csv (r'./fontURL.csv', header=False)  # read csv file by skiping header&index from read spreadsheet file


