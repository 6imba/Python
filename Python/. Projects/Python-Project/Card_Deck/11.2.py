import random

class Card(object):
    def __init__(self, suits, value): 
        self.suits = suits
        self.value = value

    def show_card(self): 
        print( '{} of {}'.format(self.value, self.suits))



class Deck(object):

    def __init__(self):
        self.deck_of_cards = []
        self.build() 

    def build(self):
        for suits in ['Heart', 'Diamond', 'Clubs', 'Spade', ]:
            for value in range(1,14):
                self.deck_of_cards.append(Card(suits,value)) 

    def show(self):
        for cards_object in self.deck_of_cards: 
            cards_object.show_card()

    def shuffle(self):
        for i in range(len(self.deck_of_cards)-1, 0 , -1): 
            r = random.randint(0,i) 
            self.deck_of_cards[i], self.deck_of_cards[r] = self.deck_of_cards[r], self.deck_of_cards[i] 

    def draw_card(self):
        return self.deck_of_cards.pop()



class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck): 
        self.hand.append(deck.draw_card())
        return self 

    def showhand(self):
        for card in self.hand:
            card.show_card()

    def discard(self):
        print('discard a card !!!!')
        return self.hand.pop()




deck = Deck()
deck.shuffle()

amir = Player("Amir")
amir.draw(deck).draw(deck).draw(deck) 
amir.showhand()
amir.discard()
amir.showhand()


