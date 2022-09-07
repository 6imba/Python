import pandas
content = pandas.read_csv("1.data.csv"); # returns DataFrame
# print(content)
# print(type(content)) # class 'pandas.core.frame.DataFrame'>
print(len(content))

# for row in content:
#     print(row)
#     print(type(row))