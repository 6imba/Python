
# 1
# sent = "    Hello world    "
# print(sent)
# print(sent.upper())
# print(sent.lower())
# print(sent.count('l'))
# print(sent.strip())#remove space at begining and end
# print(sent.replace('o','X'))
# print(sent)


# 2
# s = "python rocks"
# print(s[1]*s.index("n"))


# # 3
# scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello " + name + ". Your score is " + str(score))


# x = 2
# y = 6
# print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))



# scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello {}. Your score is {}.".format(name, score))


# person = input('Your name: ')
# greeting = 'Hello {}!'.format(person)
# print(greeting)


# v = 2.34567
# print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))


# origPrice = float(input('Enter the original price: $'))
# discount = float(input('Enter discount percentage: '))
# newPrice = (1 - discount/100)*origPrice
# calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
# print(calculation)
# # #error



# origPrice = float(input('Enter the original price: $'))
# discount = float(input('Enter discount percentage: '))
# newPrice = (1 - discount/100)*origPrice
# calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
# print(calculation)


# name = "Sally"
# greeting = "Nice to meet you"
# s = "Hello, {}. {}."

# print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.

# print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.

# print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.




