disctionary={'a':2,'z':3,'s':1,"y":9}
for key in sorted(disctionary.keys(),key = lambda k:disctionary[k]):
    print("{} = {}".format(key,disctionary[key]))
