
addition_str = "2+5+10+20"
numbs = addition_str.split("+")
SUM=0
for numb in numbs:
    print(numb)
    x=int(numb)
    print(type(SUM))
    print(type(x))
    SUM =SUM+x
print(SUM)


