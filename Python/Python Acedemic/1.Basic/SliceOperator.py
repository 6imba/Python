
# # String Slice 
# # A substring of a string is called a slice. Selecting a slice is similar to selecting a character:

singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])



# fruit = "banana"
# print(fruit[:3])
# print(fruit[3:])



# # List Slices
# # The slice operation we saw with strings also work on lists. Remember that the first index is the starting point for the slice and the second number is one index past the end of the slice (up to but not including that element). Recall also that if you omit the first index (before the colon), the slice starts at the beginning of the sequence. If you omit the second index, the slice goes to the end of the sequence.

# a_list = ['a', 'b', 'c', 'd', 'e', 'f']
# print(a_list[1:3])
# print(a_list[:4])
# print(a_list[3:])
# print(a_list[:])



# # Tuple Slices
# # We can’t modify the elements of a tuple, but we can make a variable reference a new tuple holding different information. Thankfully we can also use the slice operation on tuples as well as strings and lists. To construct the new tuple, we can slice parts of the old tuple and join up the bits to make the new tuple. So julia has a new recent film, and we might want to change her tuple. We can easily slice off the parts we want and concatenate them with the new tuple.

# julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# print(julia[2])
# print(julia[2:6])

# print(len(julia))

# julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
# print(julia)



# # What is printed by the following statements?

# L = [0.34, '6', 'SI106', 'Python', -2]
# print(len(L[1:-1]))



# lisA = [1,2,3,4,5,6,7,8,9,10]
# print(lisA[2:5])
# print(lisA[:5])
# print(lisA[0:5])
# print(lisA[5:])
# print(lisA[5:10])
# print(lisA[5:11])
# print(lisA[1:-1])
# print(lisA[0:10])
# print(lisA[0:-1])
# print(lisA[0:0])
# print(lisA[:])#ALL



# lisA = [1,2,3,4,5,6,7,8,9,10]
# print(lisA[2:5])#SLICE OPERATOR
# print(lisA[slice(2,5)])#SLICE FUNCTION
# print(slice(2,5))

