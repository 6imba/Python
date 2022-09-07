# import pandas;
# # ModuleNotFoundError: No module named 'pandas'
# # pip install pandas

# print(pandas) # NameError: name 'pandas' is not defined. So first import pandas library.
#  # <module 'pandas' from 'C:\\Python3.9.4\\lib\\site-packages\\pandas\\__init__.py'>

# # --------------------------------------------------------------------------------------------------------

# import pandas;
# print(pandas) # <module 'pandas' from 'C:\\Python3.9.4\\lib\\site-packages\\pandas\\__init__.py'>
# print(type(pandas)) # <class 'module'>
# help(pandas)
# print(dir(pandas)) # shows directory of csv module
# print(pandas.__dict__)
# print(type(pandas.__dict__))
# print(pandas.__dict__.keys())
# print(pandas.read_csv) #<function read_csv at 0x000001F71553E4C0>

# # --------------------------------------------------------------------------------------------------------

# import pandas as pd;
# x = pd.read_csv("1.data.csv")
# print(x)
# print(type(x)) # <class 'pandas.core.frame.DataFrame'>
# print(x.to_string())
# print(x)
# print(type(x))

# # --------------------------------------------------------------------------------------------------------

import pandas
# content = pandas.read_csv(".csv-file.csv"); # returns DataFrame
content = pandas.read_csv("1.simple-csv-file.csv"); # returns DataFrame
# print(content)
# print(type(content)) # class 'pandas.core.frame.DataFrame'>
print(len(content))

for row in content:
    print(row)
    print(type(row))

# print(reader)
# print(row_count)

# print(len(content))
# print(len("Amir"))
# print(len(""))
# print(list(content))
# print(len(list(content)))
# print(pandas)
# print(pandas.core)
# print(pandas.core.frame)
# print(pandas.core.frame.DataFrame)
# print(len(content.to_string()))

# print(pandas.options.display.max_rows)