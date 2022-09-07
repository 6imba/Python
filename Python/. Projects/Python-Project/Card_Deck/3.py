# # 1
# class Card(object):
#     def __init__(self, Pics, daau):
#         print("Parent Constructor !!! ...............")
#         self.Pics = Pics
#         self.daau = daau

# print(Card('Itta','A')) # change       ......................... //////////////// ..............


# # 2
# class Card(object):
#     def __init__(self, Pics, daau):
#         print("Parent Constructor !!! ...............")
#         self.Pics = Pics
#         self.daau = daau
#     def __str__(self): #__str__ is the string representation of an object
#         return '{} ko {}'.format(self.Pics, self.daau)

# print(Card('Itta','A')) # change       ......................... //////////////// ..............



# # 3
# class Card(object):
#     def __init__(self, Pics, daau): #line<1.1>////////////////
#         print("Parent Constructor !!! ...............")
#         self.Pics = Pics
#         self.daau = daau
    
#     def show_card(self): 
#         print("Parent show_card method !!! ...............")
#         print( '{} ko {}'.format(self.Pics , self.daau))

# class Deck(object):
#     def __init__(self):
#         print('1 . Deck class constructor !!! ................')
#         self.deck_of_cards = []  #line<1.2> ////////////
#         self.build()
#         print('5 . complete Deck class ....')
    
#     def build(self):
#         print('2 . Deck class build method !!! ................')
#         for Pics in ['Paan', 'Itta', 'Chidi', 'Surat']:
#             print('3 .  Pics .....')
#             for daau in range(1,14):
#                 print('4 . daau .....')
#                 self.deck_of_cards.append(Card(Pics,daau)) #append new object of class Cards in line<1.1> into deck_of_cards in in line<1.2>
    
#     def show(self):
#         print('6. Deck class show method !!! ................')
#         i=1
#         for cards_object in self.deck_of_cards:
#             print(i, cards_object)
#             i=i+1

# book = Deck()
# book.show()


# #4
# class Card(object):
#     def __init__(self, Pics, daau):
#         print("Parent Constructor !!! ...............")
#         self.Pics = Pics
#         self.daau = daau
    
#     def show_card(self):
#         print("Parent show_card method !!! ...............")
#         print( '{} ko {}'.format(self.Pics , self.daau))

# class Deck(object):
#     def __init__(self):
#         print('1 . Deck class constructor !!! ................')
#         self.deck_of_cards = []
#         self.build()
#         print('5 . complete Deck class ....')
    
#     def build(self):
#         print('2 . Deck class build method !!! ................')
#         for Pics in ['Paan', 'Itta', 'Chidi', 'Surat']:
#             print('3 .  Pics .....')
#             for daau in range(1,14):
#                 print('4 . daau .....')
#                 self.deck_of_cards.append(Card(Pics,daau)) 
#                 print(self.deck_of_cards) # change       ......................... //////////////// ..............
    
#     def show(self):
#         print('6. Deck class show method !!! ................')
#         i=1
#         for cards_object in self.deck_of_cards:
#             print(i, cards_object)
#             i=i+1

# book = Deck()
# book.show()
# print(book.deck_of_cards) #chnage.......................//////////..............



# # 5
# class Card(object):
#     def __init__(self, Pics, daau):
#         print("Parent Constructor !!! ...............")
#         self.Pics = Pics
#         self.daau = daau
#     def __str__(self): #__str__ is the string representation of an object
#         return '{} ko {}'.format(self.Pics, self.daau)

# object_string = Card('Itta','A')
# print(object_string)






# # 6
# class Card(object):
#     def __init__(self, Pics, daau):
#         print("Parent Constructor !!! ...............")
#         self.Pics = Pics
#         self.daau = daau

#     def __str__(self): # #line<2.1> ///////////////////
#         return '{} ko {}'.format(self.Pics, self.daau)

#     def show_card(self):
#         print("Parent show_card method !!! ...............")
#         print( '{} ko {}'.format(self.Pics , self.daau))

# class Deck(object):
#     def __init__(self):
#         print('1 . Deck class constructor !!! ................')
#         self.deck_of_cards = []   #v #line<2.2> /////////////
#         self.build()
#         print('5 . complete Deck class ....')
    
#     def build(self):
#         print('2 . Deck class build method !!! ................')
#         for Pics in ['Paan', 'Itta', 'Chidi', 'Surat']:
#             print('3 .  Pics .....')
#             for daau in range(1,14):
#                 print('4 . daau .....')
#                 self.deck_of_cards.append(Card(Pics,daau)) #append string representation of new object of class Cards in line<2.1> into deck_of_cards in in line<2.2>
    
#     def show(self):
#         print('6. Deck class show method !!! ................')
#         i=1
#         for cards_object in self.deck_of_cards:
#             print( 'card number ', i , '==>', cards_object)
#             i=i+1

# book = Deck()
# book.show()




# # conclution
class Card(object):
    def __init__(self, Pics, daau):
        self.Pics = Pics
        self.daau = daau
    def show_card(self):
        print( '{} ko {}'.format(self.Pics , self.daau))

class Deck(object):
    def __init__(self):
        self.deck_of_cards = []   
        self.build()
    def build(self):
        for Pics in ['Paan', 'Itta', 'Chidi', 'Surat']:
            for daau in range(1,14):
                self.deck_of_cards.append(Card(Pics,daau)) 
    def show(self):
        for cards_object in self.deck_of_cards:
            print( cards_object)

book = Deck()
book.show()

