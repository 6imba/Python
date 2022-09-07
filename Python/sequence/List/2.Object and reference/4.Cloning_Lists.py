

a = [23,65,76]
b = a[:] #make a clone using slice
print(a==b)
print(a is b)

b[0] = 5
print(a)
print(b)

