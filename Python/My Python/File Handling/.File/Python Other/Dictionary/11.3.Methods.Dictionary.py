# #1
# science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
# print(science)
# print(science['two'])
# print(list(science.keys()).index('four'))#final indexorkey is set as four 
# print('\n')

# #2
# #method => .key()

# science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
# print(science)
# print(science.keys())

#The keys() method returns a view object. 
#The view object contains the keys of the dictionary, as a list.
#The view object will reflect any changes done to the dictionary

# #3
# science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
# print(science.keys())
# for key in science.keys() :
#     print(key)

# #4
# science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
# for key in science :
#     print(key)
# #note that :wheather u mention method => .key() or not its default in dictonary 

# #5
# science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
# for key in science :
#     print(key,'has value of ',science[key])
# print('\n')


#6
# science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
# for key in science.keys() :
#     print(key,'has value of ',science[key])


# #7
# science = {'one':'physic','two':'biology','three':'chemistry','four':'astronomy'}
# print(list(science))




# #8
# #extra
# a = 'apple'
# i=1
# for x in a :
#     print (a[-i])
#     i=i+1


#9 values() 
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# print(PersonAge.values())
# print(list(PersonAge.values()))
# #note : .values() method takes no arguments
# #note : no garenty of order


#10 keys() method
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# print(PersonAge.keys())
# #default
# #note : no garenty of order


# # 11 items()
# #.items() method => gives the list of tuples where every tuples is a key-value paired
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# print(PersonAge.items())
# #note : no garenty of order


# # 12 in operator => boolean type output
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# print('Radha' in PersonAge)
# print('Undertaker' in PersonAge)
# #note : no garenty of order


#13
# # in operator => boolean type output
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# if 'Gomez' in PersonAge :
#     print(PersonAge['Gomez'])
# else:
#     print ('There is no any key called Gomez !')
# #note : no garenty of order


#14
# # in operator => boolean type output
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# if 'Undertaker' in PersonAge :
#     print('Age : ',PersonAge['Undertaker'])
# else:
#     print ('There is no any key called Undertaker !')
# #note : no garenty of order


# # 15 .get() method => get the value of the given key 
# #takes at least one argument
# #its like .values() but it takes cetain key as argument where as .values() doesnt
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# print(PersonAge.get('SimbA'))
# #note : no garenty of order


# # 16
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# print(PersonAge.get('Undertaker'))


# # 17 get also takes optional second argument
# PersonAge = {'SimbA':21, 'Radha':32, 'Gomez':15, 'Share':24}
# print(PersonAge.get('Undertaker',0))


# 18
# #extra assignment from coursera
# mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
# print(23 in mydict)#here 23 is value and in checks for key not value
# print("elephant" in mydict)

# 19
# total = 0
# mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
# print(mydict['cat'])
# for akey in mydict:
#     print(mydict[akey])
#     if len(akey) > 3:
#         total = total + mydict[akey]
# print(total)


# 20
# #Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this!

# places = {"Australia":2000, "Greece":2004, "China":2008, "England":200012}
# print(places)
# places['Brazil']= 2016
# print(places)


# 21
# # We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events. Do not hard code this.
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events.keys())
scores = list(medal_events.values())
print(events)
print(scores)