# https://www.youtube.com/watch?v=2p3kwF04xcA&t=282s&ab_channel=Socratica

# Approach_1
# number = int(input('Enter any natural number :'))
# print(number)
# if number>1:
#     for numb in range(2,number):
#         if (number%numb) == 0:
#             print('Not Primer Number !')
#             break
#     else:
#         print('Primer Number !')
#     print()
# else:
#     print('Not Primer Number !')
#
# print(len(range(2,2)))


# Approach_2

#function
def check_prime(number):
    if number == 1:
        return False
    for n in range(2,number):
        if number%n==0:
            return False
    return True

# #Drive_Code_1 To test code
# for n in range(1,21):
#     print(n, ' is ', check_prime(n))


#Drive_Code_2 To test code
import time
t0 = time.time()
for n in range(1,12000):
    print(n, ' is ', check_prime(n))
t1 = time.time()
print('Total time taken : ', t1+t0)


# #Drive_Code
# number = int(input('Enter any natural number :'))
# result = check_prime(number)
# print(result)