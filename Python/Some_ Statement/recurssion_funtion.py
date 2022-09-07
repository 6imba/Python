

# def factorial(numb):
#     if numb <= 1:
#         return 1
#     else:
#         return factorial(numb - 1)

# answer = factorial(4)
# print(answer)
# # here logic for recurtion is wrong









# def factorial(numb):
#     if numb <= 1:
#         return 1
#     else:
#         return numb * factorial(numb - 1)

# answer = factorial(4)
# print(answer)








# def factorial(numb):
#     if numb <= 1:
#         return 1
#     return numb * factorial(numb - 1)

# answer = factorial(4)
# print(answer)







# def factorial(numb):
#     if numb <= 1:
#         return 1
#     return numb * factorial(numb - 1)

# numb = int(input("Enter a number"))
# answer = factorial(numb)
# print(answer)






# print(int(3.3))
# print(int("3"))
# print(int("3.3"))
# # we cannot directly cast string in float form int integer
# # x = float("3.3")
# # print(int(x))





# def factorial(numb):
#     if not isinstance(numb, int):
#         return "Provided number must be an integer type !"
#     if numb < 0:
#         return "Provided number must be a positive integer !"
#     if numb <= 1:
#         return 1
#     return numb * factorial(numb - 1)

# numb = int(input("Enter a number: "))
# answer = factorial(numb)
# print(answer)




# def factorial(numb):
#     if not isinstance(numb, int):
#         return "Provided number must be an integer type !"
#     if numb < 0:
#         return "Provided number must be a positive integer !"
#     if numb <= 1:
#         return 1
#     return numb * factorial(numb - 1)

# numb = int(float(input("Enter a number: ")))
# answer = factorial(numb)
# print(answer)





# def factorial(numb):
#     if not isinstance(numb, int):
#         return "Provided number must be an integer type !"
#     if numb < 0:
#         return "Provided number must be a positive integer !"
#     if numb <= 1:
#         return 1
#     return numb * factorial(numb - 1)

# answer = factorial(2.2)
# print(answer)




# def factorial(numb):
#     if not isinstance(numb, int):
#         return TypeError("Provided number must be an integer type !")
#     if numb < 0:
#         return ValueError("Provided number must be a positive integer !")
#     if numb <= 1:
#         return 1
#     return numb * factorial(numb - 1)

# answer = factorial(2.2)
# print(answer)





# def factorial(numb):
#     if not isinstance(numb, int):
#         return TypeError("Provided number must be an integer type !")
#     if numb < 0:
#         return ValueError("Provided number must be a positive integer !")
#     if numb <= 1:
#         return 1
#     return numb * factorial(numb - 1)

# numb = int(input("Enter a number: "))
# answer = factorial(numb)
# print(answer)






# def factorial(numb):
#     if not isinstance(numb, int):
#         raise TypeError("Provided number must be an integer type !")
#     if numb < 0:
#         raise ValueError("Provided number must be a positive integer !")
#     if numb <= 1:
#         return 1
#     return numb * factorial(numb - 1)

# numb = int(input("Enter a number: "))
# answer = factorial(numb)
# print(answer)







# def factorial(number):
#      # Validate input
#      if not isinstance(number, int):
#          raise TypeError("Sorry. 'number' must be an integer.")
#      if number < 0:
#          raise ValueError("Sorry. 'number' must be zero or positive.")
#      # Calculate the factorial of number
#      def inner_factorial(number):
#          if number <= 1:
#              return 1
#          return number * inner_factorial(number - 1)
#      return inner_factorial(number)
# print(factorial(4))