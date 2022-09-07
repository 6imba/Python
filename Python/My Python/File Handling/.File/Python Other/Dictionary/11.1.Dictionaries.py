# #1
# #A dictionary is an unordered collection of key-value pairs.
# # {key:value}

# science = {} #created empty dictionaries
# print(science) # print dictionaries
# print(type(science)) #print type of dictionary
# science['one'] = 'Physic' #asigned a paired key&value into empty dictionary {} hold by global_frame->science where 'one' is key and 'physic' is value
# print(science) #print global_frame->science after assignment of key&value
# science['two'] = 'Biology' # again asigned another paired key&value to the dictionary {} hold by global_frame->science
# print(science) # and again print it 
# science['three'] = 'Astronomy'
# print(science)

# # note : here key is of string data type
# # key&value are unorder   





# #2
# student = {}
# print('Created empty dictionary assign as variable student =>',student)
# print('Print type of dictionary => ',type(student))
# student[1] = 'Aaraz Sharma' # inserted key&value into dictionary
# print('Print dictionary student after assignning one paired key&value => ',student)
# print('{key : value} => ',student)
# student[2] = 'Bipana Tamang'
# print('{key : value} => ',student)





# #3
# science = {'one':'Physic','two':'Biology','three':'Astronomy'} #created dictionary
# print(science)
# print(type(science))

# #4
# animal = {}
# animal[1] = 'Ape'
# animal[2] = 'Bat'
# animal[3] = 'Cat'
# animal['four'] = 'Dog'

# print(animal)#1
# print(animal[2])#2
# print(animal['four'])#3

# value = animal[3]#assign key to var value
# print(value)#4

# animal[1] = 'Aaaaaaaaaaaaaa'
# print(animal[1])#5
# print(animal)#6

# print(value)#7    #first assign value as animal[3]
# value = animal[2] #then assign value as animal[2] that changes the value of value
# print(value)#8   
# print(animal[3])#9     # change in value doesnt change animal[3]

# #5
# medals = {}
# medals['gold'] = 33
# medals['silver'] = 17
# medals['bronze'] = 12
# print(medals)

