# # 1:
# list1 = [1,2,3,4,5,6,2,4,6]
# list2 = []
# for x in list1:
#     if x not in list2:
#         list2.append(x) 
# print(list2)

# 2:
list1 = [1,2,3,4,5,6,2,4,6]
list2 = [element for element in list1 if list1.count(element)==1]
print(list2)