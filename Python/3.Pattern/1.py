# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')


# for i in range(6):
#     print(i)
# for i in range(4,8):
#     print(i)
# for i in range(-6,4):
#     print(i)






# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *

# for row in range(1,6):
#     for col in range(1,6):
#         print('*  ',end='')
#     print()



# # *
# # *  *
# # *  *  *
# # *  *  *  *
# # *  *  *  *  *
#
# for row in range(1,6):
#     for col in range(1,row+1):
#         print('*  ',end='')
#     print()


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




#             *
#          *  *
#       *  *  *
#    *  *  *  *
# *  *  *  *  *


# print('a'*5)
#
# height = int(input('Enter height : '))
# gap='   ' # three space
# print(gap*(height-1),end='')
# print('*')



# height = int(input('Enter height : '))
# gap='   ' # three space
# star='*  ' #star with two space after
# for row in range(1,height+1):
#     ok =star*row #star according to rage iteration
#     print(gap*(height-row)+ok,end='') #row contain star according to range row or row number and remaining place is occupied by space(gap)
#     print()




# height = int(input('Enter height : '))
# gap='abc' # three space
# star='*12' #star with two space after
# for i in range(1,height+1):
#     ok =star*i
#     print(gap*(height-i)+ok,end='')
#     print()


# col = int(input('Enter a height/column : '))
# for i in range(1,col+1):
#     print('   ' * (col - i) + '*  ' * i)

#
# # *  *  *  *  *
# # *  *  *  *
# # *  *  *
# # *  *
# # *
# for row in range(5,0,-1):
#     for col in range(1,row+1):
#         print('*  ',end='')
#     print()

# for i in range(5,0,-1):
#     print('*  '*i)


#check it
# gap='   '
# for row in range(5,0,-1):
#     for col in range(1,row+1):
#         if row==5:
#             print('*  ',end='')
#         if row!=5:
#             okgap = gap*col
#             print(okgap,end='')
#             for col in range(1, row + 1):
#                 print('*  ', end='')
#     print()

# col = int(input('Enter a height/column : '))
# for i in range(1,col+1):
#     print('   ' * (col - i) + '*  ' * i)
#     # print('123'*(col-i)+'*45'*i)



# s=1
# for i in range(5,0,-1):
#     print('   '*(i-1)+'*  '*s)
#     s+=1




#soln
# *  *  *  *  *
#    *  *  *  *
#       *  *  *
#          *  *
#             *
#
# gap='   ' # three space
# star='*  ' #star with two space after
# for i in range(5,0,-1):
#     ok =star*i
#     print(gap*(5-i)+ok,end='')
#     print()

# col = int(input('Enter a height/column : '))
# for i in range(0,col):
#     print('   '*i+'*  '*(col-i))




#             *
#          *  *  *
#       *  *  *  *  *
#    *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *

# height = int(input('Enter height : '))
# gap='   ' # three space
# star='*  ' #star with two space after
# for row in range(1,height+1):
#     if row==1:
#         ok =star*row #star according to rage iteration
#     else:
#         ok = star * row+star*(row-1)
#     print(gap*(height-row)+ok,end='') #row contain star according to range row or row number and remaining place is occupied by space(gap)
#     print()

# col = int(input('Enter a number of row : '))
# star='*  '
# for i in range(1,col+1):
#     print('   '*(col-i)+star)
#     star=star+'*  *  '





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
#
# row = int(input('Enter a number of row : '))
# first_half_row = int((row/2)+1)
# star='*  '
# for i in range(1,first_half_row+1):
#     print('   '*(first_half_row-i)+star)
#     if i==first_half_row:
#         break
#     star=star+'*  *  '
#
# second_half_row = first_half_row - 1
# gap=1
# for i in range(second_half_row):
#     star=star[0:-6]
#     print('   '*gap+star)
#     gap+=1
#









# #             *
# #          *     *
# #       *     *     *
# #    *     *     *     *
# # *     *     *     *     *
#
# height = int(input('Enter height : '))
# gap='   ' # three space
# star='*     ' #star with five space after
# for row in range(1,height+1):
#     ok =star*row #star according to rage iteration
#
#     print(gap*(height-row)+ok,end='') #row contain star according to range row or row number and remaining place is occupied by space(gap)
#     print()


# col = int(input('Enter a number of row : '))
# star='*  '
# for i in range(1,col+1):
#     print('   '*(col-i)+star)
#     star=star+'   *  '




#             *
#          *     *
#       *     *     *
#    *     *     *     *
# *     *     *     *     *
#    *     *     *     *
#       *     *     *
#          *     *
#             *



# for i in range(4,1):
#     print(i) #this doesnt execute
# for i in range(4,1,-1):
#     print(i)
# for i in range(4, 0, -1):
#     print(i)




# height = int(input('Enter height : '))
# gap='   ' # three space
# star='*     ' #star with five space after
# for row in range(1,height+1):
#     ok =star*row #star according to rage iteration

#     print(gap*(height-row)+ok,end='') #row contain star according to range row or row number and remaining place is occupied by space(gap)
#     print()
# for row in range(height+1,1): #this doesnt execute
#     ok =star*row #star according to rage iteration

#     print(gap*(height-row)+ok,end='') #row contain star according to range row or row number and remaining place is occupied by space(gap)
#     print()


#
# height = int(input('Enter height : '))
# gap='   '
# star='*     '
# for row in range(1,height+1):
#     ok =star*row
#
#     print(gap*(height-row)+ok,end='')
#     print()
# for row in range(height+1,1,-1): # see difference 6 row
#     ok =star*row
#
#     print(gap*(height-row)+ok,end='')
#     print()


# height = int(input('Enter height : '))
# gap='   '
# star='*     '
# for row in range(1,height+1):
#     ok =star*row
#
#     print(gap*(height-row)+ok,end='')
#     print()
# for row in range(height,1,-1): # see difference two row 5
#     ok =star*row
#
#     print(gap*(height-row)+ok,end='')
#     print()


# height = int(input('Enter height : '))
# gap='   '
# star='*     '
# for row in range(1,height+1):
#     ok =star*row
#
#     print(gap*(height-row)+ok,end='')
#     print()
# for row in range(height-1,1,-1): # see difference while reversing range start from row 4 i.e height-1 but end excluding 1 so gap at end
#     ok =star*row
#
#     print(gap*(height-row)+ok,end='')
#     print()


# height = int(input('Enter height : '))
# gap='   '
# star='*     '
# for row in range(1,height+1):
#     ok =star*row
#
#     print(gap*(height-row)+ok,end='')
#     print()
# for row in range(height-1,0,-1): # stop at 0
#     ok =star*row
#
#     print(gap*(height-row)+ok,end='')
#     print()

