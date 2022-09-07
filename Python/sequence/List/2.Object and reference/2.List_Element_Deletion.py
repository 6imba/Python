

a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)


B = ['a','three','c']
print(B.index('three'))


A = ['one', 'two', 'three']
B = ['a','three','c']
for a in A:
    for b in B:
        if a == b:
            del B[B.index(b)]
print(B)

