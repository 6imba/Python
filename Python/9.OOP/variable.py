var = 1
class Apple:
    var = 2

    def fruits(self):
        self.var = 3
        return self.var

print(var)
print(Apple.var)
print(Apple.fruits)
print(Apple.fruits())

