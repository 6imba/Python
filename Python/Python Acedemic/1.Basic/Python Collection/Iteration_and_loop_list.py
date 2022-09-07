
# #iteration over list
# for name in ["Jetha","Maila","Kaila","Saila","Dhaila","Kanxa"]:
#     print("K xa ho ",name,"!!! Please donate for orphanage.")



# # iteration over string
# for dialouge in "Hey Sankhar ho mero naam !!!":
#     print(dialouge)



# # iteration over list of numbers
# # here range function evqluates to iterables containing integers
# for index in range(4):#range(4)=[0,1,2,3]
#     square = index*index
#     print(square)


# iterationsentences="apple"
# for loopvar in iterationsentences:
#     print("laaa")



# iterationsentences="catdog"
# for loopvariable in iterationsentences:
#     print(++1)


# x=1
# iterationsentences="catd"
# for loopvariable in iterationsentences:
#     x+=1
#     print(x)
   



# iterationsentences="catdog"
# for loopvariable in iterationsentences[2:4]:
#     y=3
#     print(y)
#     y+=5



# print("This will execute first")

# for _ in range(3):
#     print("This line will execute three times")
#     print("This line will also execute three times")

# print("Now we are outside of the for loop!")


# import turtle            # set up alex
# wn = turtle.Screen()
# alex = turtle.Turtle()

# for i in [0, 1, 2, 3]:      # repeat four times
#     alex.forward(50)
#     alex.left(90)

# wn.exitonclick()


# import turtle            # set up alex
# wn = turtle.Screen()
# alex = turtle.Turtle()

# for aColor in ["yellow", "red", "purple", "blue"]:      # repeat four times
#     alex.forward(50)
#     alex.left(90)

# wn.exitonclick()



# import turtle            # set up alex
# wn = turtle.Screen()
# alex = turtle.Turtle()

# for aColor in ["yellow", "red", "purple", "blue"]:
#     alex.color(aColor)
#     alex.forward(50)
#     alex.left(90)

# wn.exitonclick()


# p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
# for ch in p:
#     print(ch)



# for i in range(0,53):
#     print(i)



# Ranges = range(10)
# TotalSum = 0
# print("TotalSum = ",TotalSum)
# print("***** Befor Loop *****")
# print("***** Loop Started *****")
# for Range in Ranges:
#     print("***** A New Loop ",Range,"( Iteration *****")
#     print("Range : ",Range)
#     TotalSum += Range
#     print("TotalSum : ",TotalSum,"--------------------------")
# print("***** End Of Loop *****")
# print("Final TotalSum is ",TotalSum)



# several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
# for var1 in several_things:
#     print(var1)
# for var2 in several_things:
#     print(type(var2))


# str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# # Write your code here.
# for var in str_list:
#     print(var," = length = ",len(var))



# original_str = "The quick brown rhino jumped over the extremely lazy fox."
# num_chars = 0
# for num_original_str in original_str:
#     num_chars = num_chars + 1
#     print(num_chars)
# print ("Length of original_str = ",num_chars)



# addition_str = "2+5+10+20"
# numbs_list = addition_str.split("+")
# print(numbs_list)
# print(type(numbs_list))
# SUM=0
# for numb in numbs_list:
#     print(numb)
#     print(type(SUM))
#     print(type(numb))
#     SUM =SUM+int(numb)
# print(SUM)



lett = ""
for i in range(7):
    lett += "b"
print(lett)
print(len(lett))

