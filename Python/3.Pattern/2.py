# # p
# # p  y
# # p  y  t
# # p  y  t  h
# # p  y  t  h  o
# # p  y  t  h  o  n
#
#
# word = input('Enter a word : ')
# length = len(word)
# ok=''
# for char in word:
#     ok=ok+char+'  '
#     print(ok)



# # *
# # *  *
# # *  *  *
# # *  *  *  *
# # *  *  *  *  *
# col = int(input('Enter a height/column : '))
# ok=''
# for i in range(col):
#     ok=ok+'*'+'  '
#     print(ok)

# for i in range(1,6):
#     print(i)

# #             *
# #          *  *
# #       *  *  *
# #    *  *  *  *
# # *  *  *  *  *
#
# col = int(input('Enter a height/column : '))
# for i in range(1,col+1):
#     print('   ' * (col - i) + '*  ' * i)
#     # print('123'*(col-i)+'*45'*i)



# # *  *  *  *  *
# # *  *  *  *
# # *  *  *
# # *  *
# # *
# col = int(input('Enter a height/column : '))
# for i in range(0,col):
#     print('*  '*(col-i))


# *  *  *  *  *
#    *  *  *  *
#       *  *  *
#          *  *
#             *
# col = int(input('Enter a height/column : '))
# for i in range(0,col):
#     print('   '*i+'*  '*(col-i))


# #             *
# #          *  *  *
# #       *  *  *  *  *
# #    *  *  *  *  *  *  *
# # *  *  *  *  *  *  *  *  *

# row = int(input('Enter a number of row : '))
# star='*  '
# for i in range(1,row+1):
#     print('   '*(row-i)+star)
#     star=star+'*  *  '



# #             *
# #          *     *
# #       *     *     *
# #    *     *     *     *
# # *     *     *     *     *
#
# col = int(input('Enter a number of row : '))
# star='*  '
# for i in range(1,col+1):
#     print('   '*(col-i)+star)
#     star=star+'   *  '
#


#
# #             *
# #          *  *  *
# #       *  *  *  *  *
# #    *  *  *  *  *  *  *
# # *  *  *  *  *  *  *  *  *
# #    *  *  *  *  *  *  *
# #       *  *  *  *  *
# #          *  *  *
# #             *

# row = int(input('Enter a number of row : '))
# first_half_row = int((row/2)+1)
# star='*  '
# for i in range(1,first_half_row+1):
#     print('   '*(first_half_row-i)+star)
#     if i==first_half_row:
#         break
#     star=star+'*  *  '
# second_half_row = first_half_row - 1
# gap=1
# for i in range(second_half_row):
#     star=star[0:-6]
#     print('   '*gap+star)
#     gap+=1


# a='123456789'
# print(a[0:-3])




# #          *
# #       *     *
# #    *           *
# # *                 *
# #    *           *
# #       *     *
# #          *
# #
#
height = int(input('Enter odd number height of pattern : '))
first_half = int(height/2)+1
star='*  '
f_middle_gap=1
for i in range(1, first_half+1):
    if i==1:
        print('   '*(first_half-i)+star)
    else:
        print('   '*(first_half-i)+star+'   '*f_middle_gap+star)
        f_middle_gap += 2

second_half = first_half-1
front_gap=1
s_middle_gap=f_middle_gap-4
for i in range(second_half,0,-1):
    if i==1:
        print('   '*front_gap+'*')
    else:
        print('   '*front_gap+'*  '+s_middle_gap*'   '+'*')
    front_gap+=1
    s_middle_gap=s_middle_gap-2
