# N pattern

# *     *
# **    *
# * *   *
# *  *  *
# *   * *
# *    **
# *     *


# # 1...............
# g=5
# for row in range(0,7):
#     if row==0 or row==1:
#         print('*'*(row+1)+' '*g+'*')
#         g-=1
#     if row>1 and row<6:
#         print('*'+' '*(row-1)+'*'+' '*g+'*')
#         g-=1
#     if row==6:
#         print('*'+' '*(row-1)+'*')




# # # 2...............
# size = int(input('Enter the size of N :'))
# gap_last_col = size-2

# for row in range(0,size):
#     if row==0 or row==1:
#         print('*'*(row+1)+' '*gap_last_col+'*')
#         gap_last_col-=1
#     if row>1 and row<size-1:
#         print('*'+' '*(row-1)+'*'+' '*gap_last_col+'*')
#         gap_last_col-=1
#     if row==size-1:
#         print('*'+' '*(row-1)+'*')






# # 3...............
# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or (col==row and col>0 and col<5):
#             print('*',end='')
#         else:
#             print(end=' ')
#         if col==5:
#             print()



# # # 4...............
# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or (col==row and col>0 and col<5):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()


# # 5...............
# size = int(input('Enter the size of N :'))
# for row in range(size):
#     for col in range(size):
#         if col==0 or col==size-1 or (col==row and col>0 and col<size-1):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()