#!/usr/bin/env python
# coding: utf-8

# In[30]:


#Create_text_list
Create_text_lists = [("Amir Shrestha",21,"Nepal"),("Resu Fhujuki",23,"Japan"),("John Cena",48,"USA"),("Mini Ebanbe",29,"Wkanda")]
#print(Create_text_lists.read())# since is list it give error ==> 'list' object has no attribute 'read'
print(Create_text_lists)


# In[35]:


#Create_text_list
Create_text_lists = [("Amir Shrestha",21,"Nepal"),("Resu Fhujuki",23,"Japan"),("John Cena",48,"USA"),("Mini Ebanbe",29,"Wkanda")]
#print(Create_text_lists.read())# since is list it give error ==> 'list' object has no attribute 'read'
print(Create_text_lists)

#add string using format() method
Blank_file = open("10.1.WriteIntoCSV_file.txt","w")#opened new blacnk text file to write
#Blank_file.write('Name','Age','Country')#this will give error => write() takes exactly one argument (3 given)
Blank_file.write('Name,Age,Country')#write into balnk text file
Blank_file.write('\n')#write line break
for single_list_detial in Create_text_lists:#calling a single line from a lines of list (Create_text_lists)
    value = '{},{},{}'.format(single_list_detial[0],single_list_detial[1],single_list_detial[2])#formating or making or adding each item of single list into value 
    Blank_file.write(value)#write the string hold by value into blanck text file (10.1.WriteIntoCSV_file)
    Blank_file.write('\n')#write line break
#for the number of time we execute this code for that numbers of time the string had to be added but only one time its added why
file_var = open("10.1.WriteIntoCSV_file.txt")
print (file_var.readlines())


# In[63]:


Create_text_lists = [("Amir ",21,"Nepal"),("Resu ",23,"Japan"),("John ",48,"USA"),("Mini Ebanbe",29,"Wkanda")]
print(Create_text_lists)

#add string using join() method
Blank_file = open("10.1.WriteIntoCSV_file.txt","w")
Blank_file.write('Name,Age,Country')
Blank_file.write('\n')
for single_list_detial in Create_text_lists:
    #value = ','.join(single_list_detial[0],single_list_detial[1],single_list_detial[2])# error => join() takes exactly one argument (3 given) 
    join_item_single_list_detial = single_list_detial[0] + ',' + str(single_list_detial[1]) + ',' + single_list_detial[2] #here single_list_detial[1] is an integer so cast it into string str(single_list_detial[1]) in order to concatenate  with string value in index 0 and 2
    value = ','.join(join_item_single_list_detial)#join each item of single list and assign in  value 
    Blank_file.write(value)
    Blank_file.write('\n')
#for the number of time we execute this code for that numbers of time the string had to be added but only one time its added why
file_var = open("10.1.WriteIntoCSV_file.txt")
print (file_var.readlines())


# In[68]:


Create_text_lists = [("Amir ",21,"Nepal"),("Resu ",23,"Japan"),("John ",48,"USA"),("Mini Ebanbe",29,"Wkanda")]

Blank_file = open("10.1.WriteIntoCSV_file.txt","w")
Blank_file.write('Name,Age,Country')
Blank_file.write('\n')
for single_list_detial in Create_text_lists:
    value = ','.join([single_list_detial[0],str(single_list_detial[1]),single_list_detial[2]])#join string inside list join take only one parameter that is list in this case []
    Blank_file.write(value)
    Blank_file.write('\n')
file_var = open("10.1.WriteIntoCSV_file.txt")
print (file_var.readlines())


# In[44]:


Create_text_lists = [("Amir Shrestha",21,"Nepal,147181Km"),("Resu Fhujuki",23,"Japan"),("John Cena",48,"USA"),("Mini Ebanbe",29,"Wkanda")]

Blank_file = open("10.1.WriteIntoCSV_file.txt","w")
Blank_file.write('Name,Age,Country')
Blank_file.write('\n')
for single_list_detial in Create_text_lists:
    value = '{},{},{}'.format(single_list_detial[0],single_list_detial[1],single_list_detial[2])
    Blank_file.write(value)
    Blank_file.write('\n')

