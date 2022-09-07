from Project1_Card import Card

import random
class Deck(object):

    def __init__(self):
        self.suits =  ['Heart ♥️', 'Diamond ♦️', 'Clubs ♣', 'Spade ♠️']
        self.cardfaces = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.deck_of_cards = []
        self.build() 

    def build(self):
        for suit in self.suits:
            for value in self.cardfaces:
                self.deck_of_cards.append(Card(suit,value))
        # print(self.deck_of_cards) 

    def shuffle(self):
        for i in range(len(self.deck_of_cards)-1, 0 , -1): 
            r = random.randint(0,i) 
            self.deck_of_cards[i], self.deck_of_cards[r] = self.deck_of_cards[r], self.deck_of_cards[i] 

    def draw_card(self):
        return self.deck_of_cards.pop()
