# # 1
# a='abcdefghij'

# for i in range(len(a)):
#     print(i)
# print('******************')
# for i in range(len(a)-1):
#     print(i)
# print('******************')
# for i in range(len(a)-1,2,-1): # len =(0,1,2,3,4,5,6,7,8,9),and range ==> from {len(a)-1 = (0,1,2,3,4,5,6,7,8)} 8 to 2 , -1 decrecese range value => , doest count range last element as no 2
#     print(i)
# print('******************')
# for i in range(20,7,-3):
#     print(i)
# print('******************')
# for i in range(20,0,-2):
#     print(i)
# print('******************')
# for i in range(20,0,-1):
#     print(i)
# print('******************')
# for i in range(20-1,0,-1):
#     print(i)


# # 2
# class Card(object):
#     def __init__(self, Pics, daau):
#         self.Pics = Pics
#         self.daau = daau
#     def show_card(self):
#         print( '{} ko {}'.format(self.Pics , self.daau))

# class Deck(object):
#     def __init__(self):
#         self.deck_of_cards = []
#         self.build()
#     def build(self):
#         for Pics in ['Paan', 'Itta', 'Chidi', 'Surat', ]:
#             for daau in range(1,14):
#                 self.deck_of_cards.append(Card(Pics,daau)) 
#     def show(self):
#         for cards_object in self.deck_of_cards:
#             cards_object.show_card() 
#     def shuffle(self):
#         for i in range(len(self.deck_of_cards)-1, 0 , -1): #change ////////////////// pick cards upto range(51,0)
#             print(i)

# book = Deck()
# # book.show()
# book.shuffle() # prints from 51-1




# #3

import random
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
        for Pics in ['Paan', 'Itta', 'Chidi', 'Surat', ]:
            for daau in range(1,14):
                self.deck_of_cards.append(Card(Pics,daau)) 
    def show(self):
        for cards_object in self.deck_of_cards:
            cards_object.show_card() 
    def shuffle(self):
        for i in range(len(self.deck_of_cards)-1, 0 , -1): #random card upto range(51,0) = i #here when pickking card at first 
            r = random.randint(0,i)
            print(i,'=',r)
book = Deck()
book.shuffle()