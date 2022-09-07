
# name = "Rodney Dangerfield"
# score = -1  # No respect!
# print("Hello " + name + ". Your score is " + score)




# name = "Rodney Dangerfield"
# score = -1  # No respect!
# print("Hello " + name + ". Your score is " + str(score))#str() function




# scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello " + name + ". Your score is " + str(score))





# scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello {}. Your score is {}.".format(name, score))





# trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
# trav_dest.insert(len(trav_dest),'Guadalajara')
# print(trav_dest)




# winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
# winners.sort()
# print(winners)
# winners.reverse()
# print(winners)






# winners = [1,5,3,2,10,6]#reverse string list
# winners.sort()
# print(winners)
# winners.reverse()
# print(winners)





# winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
# winners.sort()
# print(winners)
# z_winners = winners[::-1]
# print(z_winners)





# txt = "Hello World"[::-1]
# print(txt)

# txt1 = "Hello World"
# txt2 = txt1[::-1]
# print(id(txt1))
# print(id(txt2))





txt1 = "Hello World"
print(id(txt1))

txt1 = txt1[::-1]
print(id(txt1))
