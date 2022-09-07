# #1
# #count total number of l in text
# text = "Hey low world ! I am SimbA."
# l = 0
# for char in text:
#     if char == 'l' :
#         l = l + 1
# print('Total number of l : ',l)


# # 2
# text = open('12.1Accumulstion.Dictionary.txt')
# story = text.read()
# # print(story)

# l_count = 0

# for all_char in story :
#     if all_char == 'l' :
#         l_count = l_count + 1
# print('Finally total l_count = ',l_count)


# # 3
# #count total number of l in text_file called '12.1Accumulstion.Dictionary'
# text = open('12.1Accumulstion.Dictionary.txt') #open
# content = text.read() #read and store in var
# l_count = 0
# for all_char in content :
#     if all_char == 'l' :#check if the current value/char hold by iteration_variable i.e(all_char) is 'l' or not
#         l_count = l_count + 1 #if yes add 1 to accumulator_variable i.e(l_count)
# print('Total number l in given text-file is ',l_count)
# print('Total number l in given text-file is '+ str(l_count))


# # 4
# #count total number of l and s in text_file called '12.1Accumulstion.Dictionary'
# text = open('12.1Accumulstion.Dictionary.txt') #open
# content = text.read() #read and store in var
# l_count = 0
# s_count = 0

# for all_char in content :
#     if all_char == 'l' :
#         l_count = l_count + 1
#     elif all_char == 's' :
#         s_count = s_count + 1
# print('Total number l in given text-file is ' + str(l_count))
# print('Total number s in given text-file is ' + str(s_count))


# # 5
# #introduce to dictionary 
# #use dictionary to count

# #count total number of l and s in text_file called '12.1Accumulstion.Dictionary'
# text = open('12.1Accumulstion.Dictionary.txt') #open
# content = text.read() #read and store in var
# count = {} #empty dictionary
# print(count)
# print(type(count))

# count['l'] = 0 #insert key-value paired into dictionary
# count['s'] = 0 #insert key-value paired into dictionary

# print(count) #print dictionary i.e(count) after insertion
# print(type(count))


# # 6
# #count total number of l and s in text_file called '12.1Accumulstion.Dictionary'
# text = open('12.1Accumulstion.Dictionary.txt') #open
# content = text.read() #read and store in var
# count = {} #empty dictionary
# count['l'] = 0
# count['s'] = 0

# for all_char in content : #check for each single char in text
#     if all_char == 'l' : #check if the current iteration_character is 'l' or not
#         count['l'] = count['l'] + 1 #if yes add 1 to the value of key('l') of dictionary(count)
#     elif all_char == 's' :
#         count['s'] = count['s'] + 1
# print('Total number l in given text-file is ' + str(count['l']))
# print('Total number s in given text-file is ' + str(count['s']))
# print(count)


# # 7 Accumulator variable
# text = open('12.1Accumulstion.Dictionary.txt') #open
# content = text.read() #read and store in var

# #note1
# l_count = 0 #it is accumulator variable and it is normal variable
# print(type(l_count))
# for all_char in content :
#     if all_char == 'l' :
#         l_count = l_count + 1 #if yes add 1 to accumulator_variable i.e(l_count)

# #note2
# count = {} #empty dictionary
# count['l'] = 0 #it is also accumulator variable but it is key of dictionay(count)
# print(type(count['l']))
# print(type(count))
# for all_char in content : 
#     if all_char == 'l' : #check if the current iteration_character is 'l' or not
#         count['l'] = count['l'] + 1 #if yes add 1 to the value of key('l') of dictionary(count)
   


# # 8
# #note : replace hard coded 'l' and  's' by acumulator variable i.e all_char

# text = open ('12.1Accumulstion.Dictionary.txt')
# content = text.read()

# count = {} #start empty dictionary
# count['l'] = 0
# count['s'] = 0

# for all_char in content :
#     if all_char == 'l' : #check if the current iteration_character is 'l' or not
#         count[all_char] = count[all_char] + 1 # since char == 'l' 
#     elif all_char == 's' :
#         count[all_char] = count[all_char] + 1 # since char == 's' 

# print('Total number of l in given text-file is ' + str(count['l']))
# print('Total number of s in given text-file is ' + str(count['s']))
# print(count)   


# # 9

# #so why do need to replace hard coded 'l' and 's' by the value of accumulator variable i.e all_char
# #see the below code

# text = open ('12.1Accumulstion.Dictionary.txt')
# content = text.read()

# count = {} #start empty dictionary
# count['l'] = 0
# count['s'] = 0
# count['a'] = 0
# count['b'] = 0
# count['c'] = 0
# count['d'] = 0
# count['e'] = 0
# #and so on....



# for all_char in content : #check for each single char in text
#     if all_char == 'l' : #check if the current value/char hold by iteration_variable i.e(all_char) is 'l' or not
#         count['l'] = count['l'] + 1 #if yes add 1 to the value of key('l') of dictionary(count)
#     elif all_char == 's' :
#         count['s'] = count['s'] + 1
#     elif all_char == 'a' :
#         count['a'] = count['a'] + 1
#     elif all_char == 'b' :
#         count['b'] = count['b'] + 1
#     elif all_char == 'c' :
#         count['c'] = count['c'] + 1
#     elif all_char == 'd' :
#         count['d'] = count['d'] + 1
#     #and so on....


# print('Total number of l in given text-file is ' + str(count['l']))
# print('Total number of s in given text-file is ' + str(count['s']))
# print('Total number of s in given text-file is ' + str(count['a']))
# print('Total number of s in given text-file is ' + str(count['b']))
# print('Total number of s in given text-file is ' + str(count['c']))
# print('Total number of s in given text-file is ' + str(count['d']))
# print('Total number of s in given text-file is ' + str(count['e']))


# print(count)   


# #so let suppose rather than counting just 'l' and 's' we needed to count number of every char in text 
# #then it will take long time as we need to initialize separate accumulator variable for every single char in text
# #and check each char and just keep on incrementing each number
# #SO therefoe insted of hard coding char, we are doing it by dictionary accumulation pattern


# # 10
# #Finally Dictionary Accumulation Pattern
# text = open ('12.1Accumulstion.Dictionary.txt')
# content = text.read()

# char_dict = {} #start empty dictionary for updating key-value paired or char-cumber paired

# for all_char in content :
#     if all_char not in char_dict : # if the given char hold by iteration_variable(all_char) is not added to the dictionary(char_dict) 
#         char_dict[all_char] = 0# then add it to dictionary and initialize its value as 0
#     char_dict[all_char] = char_dict[all_char] + 1 # if it is already or just after it is added and initialize add 1 to its value number

# print(char_dict)  #print all char and its weight in dictionary(char_dict)

# for item_tup in char_dict.items() : # print key-value_paired / tuples /item  of dictionary(char_dict)
#     print (item_tup)

# for item_key in char_dict:  # print key(item_key) and value(char_dict[item_key]) from dictionary(char_dict)
#     print ('The total number of ',item_key,' is ',char_dict[item_key])
    
# #note it also take space and other character


# # 11

# text = 'Hello world, I am SimbA !'
# dict_char = {}
# for all_char in text :
#     if all_char not in dict_char :
#         dict_char[all_char] = 0
#     dict_char[all_char] = dict_char[all_char] + 1
        
# for all_char in text :  #taking char in text not in dictionary
#     print('Char(',all_char,') = ',dict_char[all_char])
    
# #note it also take space and other character
# #improvise it ......


# # 12
# text = 'Hello world, I am SimbA !'

# dict_char = {}

# for all_char in text :
#     if all_char == ' ' or all_char == ',' or all_char == '!' : # remove space comma and exclametory (' ' , !)
#         continue #if all_char is space then skip for this all_char and continue from another iteration variable all_char
#     if all_char not in dict_char :
#         dict_char[all_char] = 0
#     dict_char[all_char] = dict_char[all_char] + 1
#     print(all_char,' = ',dict_char[all_char])#it print every char in iteration and char may repeat again
    
# for all_char in dict_char : #print each char final value store in dictionary
#     print ('Total Number of ',all_char,' = ',dict_char[all_char])


# # 13

# #extra
# #Which of the following will print out True if there are more occurrences of e than t in the text of A Study in Scarlet, and False if t occurred more frequently (assumming that the previous code, from dict_accum_5, has already run.)
# A. print(txt['e'] > txt['t'])
# B. print(x['e'] > x['t'])#answer
# C. print(x[e] > x[t])
# D. print(x[c] > txt[c])
# E. print(e[x] > t[x])


# # 14
# #Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.
# sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
# split_sent_list = sentence.split()
# print(split_sent_list)
# print(type(split_sent_list))
# word_counts = {}
# for all_word in split_sent_list :
#     if all_word not in word_counts :
#         word_counts[all_word] = 0
#     word_counts[all_word] = word_counts[all_word] + 1
    
# for all_word in word_counts :
#     print(all_word , ' = ' , word_counts[all_word])

   
    


# 15
# Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = 'what can I do'
char_d = {}
for all_char in stri :
    if all_char not in char_d : #i made mistake here not in stri instead of  not in char_d be sure u store key_value to dictionary not in text variable
        char_d[all_char] = 0
    char_d[all_char] = char_d[all_char] + 1
    
for all_char in char_d :
    print(all_char , ' = ',char_d[all_char])

