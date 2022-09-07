# # 1
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author=author
        
#     def __str__(self):
#         return '{} by {}.'.format(self.title,self.author)
        
# mybook = Book('Jiban Katha','Sakhyamuni')
# print(mybook)





# # 2
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author=author
        
#     def __str__(self):
#         return '{} by {}.'.format(self.title,self.author)
        
# class PersonnelBook(Book): 
#     def __init__(self,title,author,page):
#         super().__init__(title,author)
#         self.page = page
              
# mybook = PersonnelBook('Jiban Katha','Sakhyamuni',3099)
# print(mybook)
# print(mybook.title)
# print(mybook.page)




# # 3
# class Book:
#     def __init__(self,title,author):
#         print('Hi i am Parent Constructor !')
#         self.title = title
#         self.author=author
        
#     def __str__(self):
#         return '{} by {}.'.format(self.title,self.author)
        
# class PersonnelBook(Book): 
#     def __init__(self,title,author,content):
#         super().__init__(title,author)
#         self.content = content
        
# class PublicBook(Book): 
#     def __init__(self,title,author,page):
#         super().__init__(title,author)
#         self.page = page
    
# my_personnel_book = PersonnelBook('Jiban Katha','Sakhyamuni','1 Million')
# print(my_personnel_book)
# print(my_personnel_book.title)
# print(my_personnel_book.content)

# my_public_book = PublicBook('Number_Book','Mr. Khan',37)
# print(my_public_book)
# print(my_public_book.title)
# print(my_public_book.page)

# parent_obj = Book(1,2)
# print(parent_obj)





# # 4
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author=author
        
#     def __str__(self):
#         return '{} by {}.'.format(self.title,self.author)
        
# class PersonnelBook(Book): 
#     def __init__(self,title,author,content):
#         super().__init__(title,author)
#         self.content = content
        
# class PublicBook(Book): 
#     def __init__(self,title,author,page):
#         super().__init__(title,author)
#         self.page = page
    
# class Libaries:
#     def __init__(self):
#         self.book = []
#     def add_book(self,book):
#         self.book.append(book)
#     def output_books(self):
#         return len(self.book)

# my_personnel_book = PersonnelBook('Jiban Katha','Sakhyamuni','1 Million')
# my_public_book = PublicBook('Number_Book','Mr. Khan',37)

# obj_books = Libaries()
# obj_books.add_book(my_personnel_book)
# obj_books.add_book(my_public_book)
# print(obj_books.output_books())




# # 5
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author=author
        
#     def __str__(self): # object
#         return '{} by {}.'.format(self.title,self.author)
        
# class PersonnelBook(Book): 
#     def __init__(self,title,author,content):
#         super().__init__(title,author)
#         self.content = content
        
# class PublicBook(Book): 
#     def __init__(self,title,author,page):
#         super().__init__(title,author)
#         self.page = page
    
# class Libaries:
#     def __init__(self):
#         self.book = [] # list of object
#     def add_book(self,book):
#         self.book.append(book) # append object
#     def output_books(self):
#         print('Total books ',len(self.book),' => ',self.book)

# my_personnel_book = PersonnelBook('Jiban Katha','Sakhyamuni','1 Million')
# my_public_book = PublicBook('Number_Book','Mr. Khan',37)

# obj_books = Libaries()
# obj_books.add_book(my_personnel_book) # append object
# obj_books.add_book(my_public_book)
# obj_books.output_books()






# # 6
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author=author
        
#     def __repr__(self): # soln
#         return '{} by {}.'.format(self.title,self.author)
        
# class PersonnelBook(Book): 
#     def __init__(self,title,author,content):
#         super().__init__(title,author)
#         self.content = content
        
# class PublicBook(Book): 
#     def __init__(self,title,author,page):
#         super().__init__(title,author)
#         self.page = page
    
# class Libaries:
#     def __init__(self):
#         self.book = [] 
#     def add_book(self,book):
#         self.book.append(book) 
#     def output_books(self):
#         print('Total books ',len(self.book),' => ',self.book)

# my_personnel_book = PersonnelBook('Jiban Katha','Sakhyamuni','1 Million')
# my_public_book = PublicBook('Number_Book','Mr. Khan',37)
# print(my_personnel_book)
# obj_books = Libaries()
# obj_books.add_book(my_personnel_book) 
# obj_books.add_book(my_public_book)
# obj_books.output_books()




# # 6
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author=author
        
#     def __str__(self): # soln
#         return '{} by {}.'.format(self.title,self.author)
        
#     def __repr__(self): # soln
#         return '{} by {}.'.format(self.title,self.author)
        
# class PersonnelBook(Book): 
#     def __init__(self,title,author,content):
#         super().__init__(title,author)
#         self.content = content
        

    
# my_personnel_book = PersonnelBook('Jiban Katha','Sakhyamuni','1 Million')
# print(my_personnel_book)
# print(my_personnel_book.__str__())
# print(my_personnel_book.__repr__())


# what is difference betweeen __str__ and __repr__