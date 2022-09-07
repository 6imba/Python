class new_class():
    def __init__(self, number):
        self.multi = int(number) * 2
        self.str = str(number)

a = new_class(2)
print(a.__dict__)
# {'multi': 4, 'str': '2'}
print(a.__dict__.keys())
# dict_keys(['multi', 'str'])
print(a.__dict__.values())
# dict_values([4, '2'])
