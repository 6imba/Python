

numbs = [1,2,3,4,5,6,7,8,9]
print(numbs)
print(numbs[3:7])#see_difference
#Using slices to delete list elements can be awkward and therefore error-prone. 
#Python provides an alternative that is more readable.
#The del statement removes an element from a list by using its position.


numbs = [1,2,3,4,5,6,7,8,9]
print(numbs)
del numbs[3:7]#see_difference
print(numbs)
del numbs[3]
print(numbs)
del numbs[3:7]#see_difference
print(numbs)
# del numbs
print(numbs) #if uncomment above del key work then error in this line






