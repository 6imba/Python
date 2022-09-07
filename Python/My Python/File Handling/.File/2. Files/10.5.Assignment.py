#!/usr/bin/env python
# coding: utf-8

# In[5]:


#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

file_var = open('10.5.emotion_words.txt')
num = len(file_var.read())
print(num)


# In[8]:


#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

file_var = open('10.5.emotion_words.txt')
lines = file_var.readlines()
number_of_lines = 0
num_words = 0
for line in lines:
    number_of_lines = number_of_lines + 1
    print('Line number : ',number_of_lines)
    print('Line : ',line)
    print('List of word in line : ',line.split())
    numbofwordofsingleline = len(line.split())
    print('Numbers of word in line : ',numbofwordofsingleline)
    num_words = num_words + numbofwordofsingleline
    print('Total Numbers of words in line : ',num_words)

    


# In[11]:


#print first 30 character in 10.5.emotion_words
file_var = open('10.5.emotion_words.txt')
beginning_chars = file_var.read()[:30]
print(beginning_chars)


# In[15]:


#Using the file school_prompt.txt, assign the third word of every line to a list called three.

file_var = open('10.5.emotion_words.txt')
three = []
lines = file_var.readlines()
print(lines)
for line in lines:
    print(line)
    line_split = line.split(' ')
    print(line_split)
    print('Third word = ',line_split[2])
    three = three + [line_split[2]]
    print(three)


# In[ ]:





# In[14]:


#Create a list called emotions that contains the first word of every line in emotion_words.txt.

file_var = open('10.5.emotion_words.txt')
emotions = []
lines = file_var.readlines()
print(lines)
for line in lines:
    print(line)
    line_split = line.split(' ')
    print(line_split)
    print('First word = ',line_split[0])
    emotions = emotions + [line_split[0]]
    print(emotions)


# In[16]:


#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

file_var = open('10.5.emotion_words.txt')
first_chars = file_var.read()[:33]
print(first_chars)


# In[17]:


file_var = open('10.6.emotion_words.txt')
p_words = []
print(p_words)
lines = file_var.readlines()
for line in lines:
    line_list = line.strip().split(' ')
    print(line_list)
    print(line_list[0])
    for word in line_list:
        print(word)
        print(word[0])
        for char in word:
            if char == 'p':
                p_words = p_words + [word]
                print(p_words)
                break # it comes to use when word papers has two p in it
print('Word with p char = ',p_words)

