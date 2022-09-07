# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

data = '123456'
# print(data[0:5])
# print(data[:5])
# print(data[1:5])
# print(data[0:])
# print(data[:])
# print(data[4:1])
# print(data[4:1:-1])
# print(data[:])
# print(data[::])
# print(data[::-1])
# print(data[:-1])
# print(data[:-2])
# print(data[:-3])
# print(data[:-4])
# print(data[:-4:-1])
# print(data[-4::-1])

total_times = []
# # 1
# #start time
# import time
# t0 = time.time()

# # Check Pallindrome using slice operator (:)
# data1 = str(input('Enter to check pallindrome : '))
# if data1 == data1[::-1]:
#     print('Pallindrome !')
# else:
#     print('Not Pallindrome !')

# # end time
# t1 = time.time()
# # time taken
# time_taken_1 = t1 - t0
# total_times.append(time_taken_1)
# print('Total time taken by 1st : ', time_taken_1)




# # 2
# #start time
# t00 = time.time()

# # Check Pallindrome using for loop :
# data2 = str(input('Enter to check pallindrome : '))
# rev_data2 = ''
# for char in data2:
#     rev_data2 = char + rev_data2
# if data2 == rev_data2 :
#     print('Pallindrome !')
# else:
#     print('Not Pallindrome !')

# # end time
# t11 = time.time()
# # time taken
# time_taken_2 = t11 - t00
# total_times.append(time_taken_2)
# print('Total time taken by 2nd : ', time_taken_2)



# # # 3
# # # Iterative Method: This method is contributed by Shariq Raza. Run a loop from starting to length/2 and check the first character
# # # to the last character of the string and second to second last one and so on …. If any character mismatches, the string wouldn’t
# # # be a palindrome.

# a='0123'
# print(a[len(a)-1])
# print(a[len(a)-2])
# print(a[len(a)-3])

# #start time
# t000 = time.time()

# #function
# def isPalindrome(str):
#     # Run loop from 0 to len/2
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True


# # main function
# s = input('Enter : ')
# ans = isPalindrome(s)
# if (ans):
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")

# # end time
# t111 = time.time()
# # time taken
# time_taken_3 = t111-t000
# total_times.append(time_taken_3)
# print('Total time taken by 3rd : ', time_taken_3)


# print('Here least time is ', min(total_times))