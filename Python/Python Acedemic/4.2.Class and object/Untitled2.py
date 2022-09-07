#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random


# In[55]:


Database class

database = {}

def view_database():
  print(databse)

def save_to_database(id, name, age):
  database = {
      'id': list_of_id
      ,'name': list_of_name
      ,'age': list_of_age
  }

def update_database(name, id):
  """Update dictionary with new name if id matches to the value existing in database"""

  Loop in the database:
    if(id exists in the database):
        Update name
        save to database
    else:
      print("Id doesn't exist")


# In[57]:


class People:
  """Class for people"""
  def __init__(self):
    self.id = random.randrange(1000)
    self.name = "Not Assigned"
    self.age = 1
  
  def show_details(self):
    print("The identifier of person is", self.id)
    print("Name is ",self.name)
    print("Age is ",self.age)
  
  def put_name(self, name):
    self.name = name
  
  def save_people(self):
    save_to_database(self.id, self.name, self.age)
  
  def update_people(self, name):
    self.name = name
    update_database(self.name, self.id)

  def show_id(self):
    print(self.id)


# In[58]:


people_1 = People()
people_1.put_name(name="Smriti")
people_1.show_details()


# In[48]:


people_1.save_to_database()


# In[49]:


people_1.view_database()


# In[50]:


people_1.update_database(name="Suman")
people_1.view_database()


# In[51]:


class Student(People):
  """Class for Student"""
  def __init__(self):
    super().__init__()


# In[53]:


std1 = Student()
std1.show_details()


# In[60]:


people_1.show_id()


# In[61]:


people_2 = People()
people_2.show_details()


# In[62]:


people_2.show_id()


# In[ ]:


oldname exist in database => fetch index of the name
id fetch = id[index]
fetch id from the row where oldname matches


# In[ ]:





# In[19]:


people_2 = People()
people_2.show_details()


# In[20]:


people_3 = People()
people_3.show_details()


# In[34]:





# In[35]:


class User_Model(abc):
    
    user_dictionary={}
    
    def __init__(self):
        pass
        
    def __call__(self, name):
        self.name = name
        
        super().abc_function(self.name)
        
    
    def dictionary_fake(self):
        self.user_dictionary['name']=self.username # here it override the previous key:vale of dictionary of list
            # needed ==> [{'name': '1'}, {'name': '2'}, {'name': '3'}]
            # output ==> [{'name': '3'}, {'name': '3'}, {'name': '3'}]
            #this self.user_dictionary should be instance of person_2 when calling from person_2.dictionary_fake() but why is it updating person_1 's list 
    def database_fake(self):
        user_list.append(self.user_dictionary)
    
    def dict_show(self):
        print(self.user_dictionary)
    
    def list_show(self):
        print(user_list)
        
um = User_Model()
um.user_dictionary
um()

 


am = User_model()
am()

