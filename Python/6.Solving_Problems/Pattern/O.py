# # Extra
# for col in range(6):
#     if col!=0 and col!=5:
#         print(True)
#     else:
#         print(False)

# for col in range(6):
#     print('Column ==> ', col)
#     if col!=0 or col!=5:
#         print(True)
#     else:
#         print(False)




# # Extra
# print(2>1)
# print(3>5)
# print(2>1 or 3>5)
# print(2>1 and 3>5)
# print(0!=0)
# print(0!=5)
# print(0!=0 or 0!=5)
# print(0!=0 and 0!=5)
# print(2>1 and 3>5 or 0!=0 or 0!=5)
# print(2>1 and 3>5 or (0!=0 or 0!=5))
# print(2>1 and 3>5 and (0!=0 or 0!=5))
# print(2>1 and 3>5 and 0!=0 or 0!=5)
# print(2>1 and 3>5 and 0!=0 and 0!=5)





# # 1
# for row in range(6):
#     for col in range(6):
#         if ((row==0 or row==5) and (col!=0 and col!=5)) or ((row>0 and row<5) and (col==0 or col==5)):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print(row)




# # 2
# for row in range(6):
#     for col in range(6):
#         if ((row==0 or row==5) and (col!=0 and col!=5)) or ((row>0 and row<5) and (col==0 or col==5)):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()


# # 3
# size = int(input('Enter the size of O :'))
# for row in range(size):
#     for col in range(size):
#         if ((row==0 or row==size-1) and (col!=0 and col!=size-1)) or ((row>0 and row<size-1) and (col==0 or col==size-1)):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()



