# #1
# # random.randint()
# import random
# r = random .randint(3,9) #returns a random number between 3 and 9 (both included)
# print(r)


# #2
# import random
# cards = 52
# for card in range(cards):
#     r = random .randint(0,card) 
#     print('Range:0 -',card,' == ',r)

# #3
# import random
# cards = 52
# for card in range(cards,0,-1):
#     r = random .randint(0,card) 
#     print('Range:0 -',card,'   ==>   random-choice :',r)


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
        for card in range(len(self.deck_of_cards)-1, 0 , -1): #random card upto range(51,0) = i #here when pickking card at first we have 51 option/range then , in each increaing in loop decrease the option/range my 1
            r = random.randint(0,card)
            print('Range:0 -',card,'   ==>   random-choice :',r)

book = Deck()
book.shuffle()