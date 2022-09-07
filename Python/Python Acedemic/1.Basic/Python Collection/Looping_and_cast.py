# Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0
print(scores)
split_scores = scores.split(' ')
print(scores)

for score in split_scores:
    print(score)
    print(type(score))
    numb = int(score)
    print(type(numb))
    if numb >= 90:
        print(numb)
        a_scores = a_scores + 1
        print(a_scores)
print(a_scores)



# Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

new_org = org.split()
print(stopwords)
print(new_org)
print('\n')
for new_word in new_org:
    if new_word in stopwords:
        print("Stopwords to be removed = ",new_word)
        new_org.remove(new_word)
        print(new_org)
print('\n')

acro = ''
print(new_org)
print('\n')

for first_word_new_org in new_org:
    print(first_word_new_org)
    acro = acro + first_word_new_org[0]
    print(acro)
print('\n')

acro = acro.upper()
print(acro)


# Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

split_sent = sent.split()
print(split_sent)
print(stopwords)

for stop in stopwords:
    if stop in split_sent:
        print(stop)
        split_sent.remove(stop)
        print(split_sent)
        
acro = ''
for final_split_sent in split_sent:
    acro = acro + final_split_sent[0:2] +'.'

acro = acro[0:len(acro)-1]
print(acro)
acro = acro.upper()
print('Final = ' ,acro)


# In[8]:


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

split_sent = sent.split()
print(split_sent)
print(stopwords)

for stop in stopwords:
    if stop in split_sent:
        print(stop)
        split_sent.remove(stop)
        print(split_sent)
        
acro = ''
final_list = []
for final_split_sent in split_sent:
    final_split_sent = final_split_sent[0] + final_split_sent[1]
    final_list.append(final_split_sent)
    print(final_list)
    acro = '.'.join(final_list)
    print(acro)
acro = acro.upper()
print(acro)


# In[9]:


#A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
print(r_phrase)


# In[ ]:


#Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

i = 0

for item in inventory:
    print("The store has {} {}, each for {} USD.".format(inventory[i], inventory[i], inventory[i]))
    i += 1

