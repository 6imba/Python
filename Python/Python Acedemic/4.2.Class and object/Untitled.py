#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Table:
    dictionary = {}
    Id = []
    Name = []
    Email = []


# In[32]:


class Insert(Table):
    
    def __init__(self):
        User_Id=input('Enter your User_Id : ')
        User_Name=input('Enter your User_Name : ')
        User_Email=input('Enter your User_Email : ')
        
        print('User_Id : ',User_Id)
        print('UserName: ',User_Name)
        print('UserEmail : ',User_Email)
        
        self.Id.append(User_Id)
        self.Name.append(User_Name)
        self.Email.append(User_Email)
        
        
        print(self.Id)
        print(self.Name)
        print(self.Email)


# In[33]:


obj1=Insert()


# In[ ]:


user_dictionary = {}

class User_Model():
            
    def __init__(self):
        
        self.User_Id=input('Enter your User_Id : ')
        self.User_Name=input('Enter your User_Name : ')
        self.User_Email=input('Enter your User_Email : ')
        self.User_Password=input('Enter your User_Password : ')
        
        print('User_Id : ',self.User_Id)
        print('UserName: ',self.User_Name)
        print('UserEmail : ',self.User_Email)
        print('Password: ',self.User_Password)
        
        
    def database_fake(self):

        print(user_dictionary)
        user_dictionary['UserId']=self.User_Id
        user_dictionary['UserName']=self.User_Name
        user_dictionary['UserMail']=self.User_Email
        user_dictionary['UserPassword']=self.User_Password
        print('Dictionary loaded : ',user_dictionary)

