class A:
    x=4
    def __init__(self, name):
        print(1)
        self.name=name

print(A)
print(A.x)
# print(A.name)
a=A('amir')
print(a.name)