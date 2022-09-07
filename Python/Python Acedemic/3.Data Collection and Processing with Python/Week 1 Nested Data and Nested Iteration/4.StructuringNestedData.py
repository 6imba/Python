# # 1
# listA = [1,2,3,4,5]
# for item in listA:
#     print(item)


# # 2
# stringB = '1,2,3,4,5'
# for item in stringB:
#     print(item)


# # 3
# stringB = '12345'
# for item in stringB:
#     print(item)


# # 4
# stringB = 5050
# for item in stringB:  # ==> int is not iterable
#     print(item)


# # 5
# stringB = '5050'
# for item in stringB: # ==> string is not iterable
#     print(item)


# # 6
# for item in range(5): # ==> range is iterable
#     print(item)


# # 7
# stringB = 5
# for item in range(stringB):
#     print(item)


# # 8
# mainlist = [1,2,['a','b','c'],'apple',[11,22,33]]
# for subs in mainlist:
#     print('Level1 : ',subs)


# 9
# # When constructing your own nested data, it is a good idea to keep the structure consistent across each level. 
# For example, if you have a list of dictionaries, then each dictionary should have the same structure, meaning the 
# same keys and the same type of value associated with a particular key in all the dictionaries. The reason for this 
# is because any deviation in the structure that is used will require extra code to handle those special cases.
#  The more the structure deviates, the more you will have to use special cases.
# # For example, let’s reconsider this nested iteration, but suppose not all the items in the outer list are lists.
# # Now the nested iteration fails.


# mainlist = [1,2,['a','b','c'],'apple',[11,22,33]]
# for sublist in mainlist:
#     print('Level1 : ',sublist)
#     for subs in sublist:#error as sublist+>1 int is not itereble
#         print('Level2 : ',subs)


# # We can solve this with special casing, a conditional that checks the type.

# mainlist = [1,2,['a','b','c'],'apple',[11,22,33]]
# for sublist in mainlist:
#     print('Level1 : ',sublist)
#     if type(sublist) is list:
#         for subs in sublist:# if iteration variable is list
#             print('    Level2 : ',subs)


# mainlist = [1,2,['a','b','c'],'apple',[11,22,33]]
# for sublist in mainlist:
#     print('Level1 : ',sublist)
#     if type(sublist) is int:#if iteration variable is int
#         continue
#     else:
#         for subs in sublist:
#             print('    Level2 : ',subs)

mainlist = [1,2,['a','b','c'],'apple',[11,22,33]]
for sublist in mainlist:
    print('Level1 : ',sublist)
    if type(sublist) is not int:#if iteration variable is not int
        for subs in sublist:
            print('    Level2 : ',subs)

