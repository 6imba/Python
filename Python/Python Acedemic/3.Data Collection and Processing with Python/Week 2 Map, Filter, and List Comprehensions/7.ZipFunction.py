# # 1
# # Python provides one more function that performs a common accumulation. It's called zip. 
# # It takes two sequences and zips them together, matching their first items together, their second items together, and so on.
# # It makes it easy to do operations where you have to make pairwise comparisons or pairwise combinations. 
# # At the end of this lesson, you should be able to read and write code using the zip function.


# # 2
# # Manual Accumulation
# L1=[2,4,6]
# L2=[5,15,25]
# L3=[]
# for i in range(len(L1)):
#     L3.append(L1[i] + L2[i])
# print(L3)


# # 3
# # You have seen this idea previously for iterating through the items in a single list. In many other programming languages that’s really the only 
# way to iterate through the items in a list. In Python, however, we have gotten used to the for loop where the iteration variable is bound successively
#  to each item in the list, rather than just to a number that’s used as a position or index into the list.

# # Can’t we do something similar with pairs of lists? It turns out we can.

# # The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like lists for most practical 
# purposes), pairing up all the first items as one tuple, all the second items as a tuple, and so on. Then we can iterate through those tuples, and
#  perform some operation on all the first items, all the second items, and so on.
# L1=[2,4,6]
# L2=[5,15,25]
# L3=list(zip(L1,L2))
# print(L3) #zip two list as tuple


# # 3
# # Here’s what happens when you loop through the tuples.
# L1=[2,4,6]
# L2=[5,15,25]
# L3=list(zip(L1,L2))
# L4=[]
# for x,y in L3:
#     L4.append(x+y)
# print(L4)


# # 4
# Zip List Comprehension
L1=[2,4,6]
L2=[5,15,25]
L3=[x+y for x,y in zip(L1,L2)]
print(L3)


# # 5
# # Or, using map and not unpacking the tuple (our online environment has trouble with unpacking the tuple in a lambda expression):
# L1 = [3, 4, 5]
# L2 = [1, 2, 3]
# L3 = map(sum, zip(L1,L2))
# print(list(L3))


# # 6
# L1 = [3, 4, 5]
# L2 = [1, 2, 3]
# L3 = map(lambda x: x[0] + x[1], zip(L1,L2))
# print(list(L3))


# # 7
# # Consider a function called possible, which determines whether a word is still possible to play in a game of hangman,
# # given the guesses that have been made and the current state of the blanked word.
# # Below we provide function that fulfills that purpose.

# def possible(word, blanked, guesses_made):
#     if len(word) != len(blanked):
#         return False
#     for i in range(len(word)):
#         bc = blanked[i]
#         wc = word[i]
#         if bc == '_' and wc in guesses_made:
#             return False
#         elif bc != '_' and bc != wc:
#             return False
#     return True

# print(possible("wonderwall", "_on__r__ll", "otnqurl"))
# print(possible("wonderwall", "_on__r__ll", "wotnqurl"))


# # 8
# # However, we can rewrite that using zip, to be a little more comprehensible.

# def possible(word, blanked, guesses_made):
#     if len(word) != len(blanked):
#         return False
#     for (bc, wc) in zip(blanked, word):
#         if bc == '_' and wc in guesses_made:
#             return False
#         elif bc != '_' and bc != wc:
#             return False
#     return True

# print(possible("wonderwall", "_on__r__ll", "otnqurl"))
# print(possible("wonderwall", "_on__r__ll", "wotnqurl"))


# # 9
# # 1. Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. This can be accomplished in one line of code.


# L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
# L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
# L3 = [x+y for x,y in zip(L1,L2) if x>10 and y<5]

# print(L3)

