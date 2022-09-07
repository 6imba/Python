# #1
# name = ['Amir','Bipana','Cena','Divya','Engalo']
# print(name[0],name[4])
# name[0],name[4]=name[4],name[0]
# print(name[0],name[4])





# # #2
# import random
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
#         for i in range(len(self.deck_of_cards)-1, 0 , -1):
#             r = random.randint(0,i)
#             self.deck_of_cards[i], self.deck_of_cards[r] = self.deck_of_cards[r], self.deck_of_cards[i] # ??????

# book = Deck()
# book.shuffle()
# book.show()






# # 6
# import random
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


#     def shuffle(self): #cant we use ===> random.shuffle(deck_of_cards)
#         for i in range(len(self.deck_of_cards)-1, 0 , -1):
#             r = random.randint(0,i)
#             self.deck_of_cards[i], self.deck_of_cards[r] = self.deck_of_cards[r], self.deck_of_cards[i] # ??????
    
    
#     def check(self):
#         card_dict = {}
#         for card in self.deck_of_cards:
#             if card not in card_dict:
#                 card_dict[card]=1
#             elif card in card_dict:
#                 card_dict[card]+=1
#         print(card_dict)
#         print(len(card_dict))


# book = Deck()
# book.shuffle()
# book.show()
# book.check()





