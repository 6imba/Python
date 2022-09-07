# return value in methods
# #It is important to remember that methods like append, sort, and reverse all return None. 


#You’ve seen some methods already, like the count and index methods. Methods are either mutating or non-mutating. Mutating methods are ones that change the object after the method has been used. Non-mutating methods do not change the object after the method has been used.
#The count and index methods are both non-mutating. 
#The dot operator can also be used to access built-in methods of list objects. append

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop() #pop returns value but remove doesnt
print(lastitem)
print(mylist)

#pop delete last item returns value but remove doesnt
#remove remove item regarding index but not return any value

# #It is important to remember that methods like append, sort, and reverse all return None. 

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist = mylist.sort()   #probably an error
print(mylist)

