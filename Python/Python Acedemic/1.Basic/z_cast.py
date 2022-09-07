
addition_str = "2+5+10+20"
numbs = addition_str.split("+")
print(numbs)
print(type(numbs))
SUM=0
for numb in numbs:
    print(numb)
    x=int(numb)
    print(type(SUM))
    print(type(x))
    SUM =SUM+x
print(SUM)



addition_str = "2+5+10+20"
numbs = addition_str.split("+")
sum_val = 0
for numb in numbs:
    print(numb)
    x=int(numb)
    print(type(sum_val))
    print(type(x))
    sum_val = sum_val + x
print(sum_val)



week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
splited_string = week_temps_f.split(",")
print(splited_string)
SUM = 0
for temps_f in splited_string:
    cast = float(temps_f)
    SUM = SUM + cast
avg_temp = SUM / len(splited_string)
print(avg_temp)
    





