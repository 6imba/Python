import random

class Card(object):
    def __init__(self, suits, value): #initialize card object called by line<1.1>
        self.suits = suits
        self.value = value
    def show_card(self): #print the card #it cal be call from any classes to show the card
        print( '{} of {}'.format(self.value, self.suits))

class Deck(object):
    def __init__(self):
        self.deck_of_cards = []
        self.build() #method to creaate cards and append into deck_of_cards

    def build(self):
        for suits in ['Heart', 'Diamond', 'Clubs', 'Spade', ]:
            for value in range(1,14):
                self.deck_of_cards.append(Card(suits,value)) #line<1.1> ////////////
    def show(self):
        for cards_object in self.deck_of_cards: 
            cards_object.show_card() # print the card_object in string form through show_card() method in Class_Card
    def shuffle(self): #Fisher-Yates Shuffle Modern Algorithm 
        for i in range(len(self.deck_of_cards)-1, 0 , -1): #here i is index number of card_object in deck_of_card, so at firt i=52-1 =51 and 0 means loop upto 1 index, as second parameter(0) is exclusive in range(), -1 means reverse
            r = random.randint(0,i) #random number between (0,i) here 0 and i (both included):
            self.deck_of_cards[i], self.deck_of_cards[r] = self.deck_of_cards[r], self.deck_of_cards[i] 
    def draw_card(self):
        return self.deck_of_cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck): # deck(primary_object,secondary_object)
        self.hand.append(deck.draw_card())

    def showhand(self):
        for card in self.hand:
            card.show_card()

    def discard(self):
        return self.hand.pop()


deck = Deck()
deck.shuffle()

amir = Player("Amir")
amir.draw(deck)
amir.showhand()

