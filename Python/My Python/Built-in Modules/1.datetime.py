import datetime

print(datetime)
print(datetime.datetime)
print(datetime.datetime.now())
print(type(datetime.datetime.now()))

# methods of datetime module:
print(datetime.datetime.now())
print(datetime.datetime.year)
print(datetime.datetime.now().year)
print(datetime.datetime.now().strftime("%A"))

# create date object:
x = datetime.datetime(2020, 5, 17)
print(x)

