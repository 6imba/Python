#1
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = zip(ids,name,email)
# print(person_info)
# # print(list(person_info))
# print(tuple(person_info))

# # The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# # zip(iterator1, iterator2, iterator3 ...)
# # Iterator objects that will be joined together


# #2
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# for person_tuple in person_info:
#     print(person_tuple)



# #3
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# for person_tuple in person_info:
#     ID,Name,Email = person_tuple
#     print(ID,Name,Email)



# #4
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# class Person:
#     def __init__(self,id1,name1,email1):
#         self.id2 = id1
#         self.name1 = name1
#         self.email1 = email1
#         return (self.id2,',', self.name1,',', self.email1) # concstructor never return any value

# for person_tuple in person_info:
#     ID,Name,Email = person_tuple
#     person1obj = Person(ID,Name,Email)



# #5
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# class Person:
#     def __init__(self,id1,name1,email1):
#         self.id2 = id1
#         self.name1 = name1
#         self.email1 = email1
       
#     def __str__(self):
#         return (self.id2,',', self.name1,',', self.email1) # __str__ only returns string

# for person_tuple in person_info:
#     ID,Name,Email = person_tuple
#     person1obj = Person(ID,Name,Email)
#     print(person1obj)





# #6
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# class Person:
#     def __init__(self,id1,name1,email1):
#         self.id2 = id1
#         self.name1 = name1
#         self.email1 = email1
       
#     def __str__(self):
#         return '{}  {}  email:{}'.format(self.id2, self.name1, self.email1)

# for person_tuple in person_info:
#     ID,Name,Email = person_tuple
#     person1obj = Person(ID,Name,Email)
#     print(person1obj)




# #7
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# class Person:
#     def __init__(self,id1,name1,email1):
#         self.id2 = id1
#         self.name1 = name1
#         self.email1 = email1
       
#     def __str__(self):
#         return '{} , {} , email:{}'.format(self.id2, self.name1, self.email1)
# Manxe = []
# for person_tuple in person_info:
#     ID,Name,Email = person_tuple
#     person1obj = Person(ID,Name,Email)
#     Manxe.append(person1obj)
# print(Manxe)



# #7
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# class Person:
#     def __init__(self,id1,name1,email1):
#         self.id2 = id1
#         self.name1 = name1
#         self.email1 = email1
       
#     def __str__(self):
#         return '{} , {} , email:{}'.format(self.id2, self.name1, self.email1)
# Manxe = []
# for person_tuple in person_info:
#     ID,Name,Email = person_tuple
#     person1obj = Person(ID,Name,Email)
#     Manxe.append(person1obj)
# print(Manxe)





# #8
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# class Person:
#     def __init__(self,id1,name1,email1):
#         self.id2 = id1
#         self.name1 = name1
#         self.email1 = email1
       
#     def __str__(self):
#         return '{} , {} , email:{}'.format(self.id2, self.name1, self.email1)
    
# Manxe = [Person(ID,Name,Email) for (ID,Name,Email) in  person_info] # List Comprehensive
# print(Manxe)



# #9
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# class Person:
#     def __init__(self,id1,name1,email1):
#         self.id2 = id1
#         self.name1 = name1
#         self.email1 = email1
       
#     def __str__(self):
#         return '{} , {} , email:{}'.format(self.id2, self.name1, self.email1)
    
# Manxe = [Person(*t) for t in  person_info] # List Comprehensive with tuple
# print(Manxe)


# # 9
# ids = [172,201,387,114]
# name = ['Amir','Ram','Bipin','Suraj']
# email = ['a.com','r.com','b.com','s.com']
# person_info = list(zip(ids,name,email))
# print(person_info)

# class Person:
#     def __init__(self,id1,name1,email1):
#         self.id2 = id1
#         self.name1 = name1
#         self.email1 = email1
       
#     def __str__(self):
#         return '{} , {} , email:{}'.format(self.id2, self.name1, self.email1)
    
# Manxe = [Person(*t) for t in  person_info] # List Comprehensive with tuple
# print(Manxe)

# z = [print(Person(*t)) for t in  person_info]



ids = [172,201,387,114]
name = ['Amir','Ram','Bipin','Suraj']
email = ['a.com','r.com','b.com','s.com']
person_info = list(zip(ids,name,email))
print(person_info)

class Person:
    def __init__(self,id1,name1,email1):
        self.id2 = id1
        self.name1 = name1
        self.email1 = email1
       
    def __str__(self):
        return '{} , {} , email:{}'.format(self.id2, self.name1, self.email1)
Manxe = []
for person_tuple in person_info:
    ID,Name,Email = person_tuple
    person1obj = Person(ID,Name,Email)
    Manxe.append(str(person1obj))
print(Manxe)