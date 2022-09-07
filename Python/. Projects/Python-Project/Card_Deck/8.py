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
        for i in range(len(self.deck_of_cards)-1, 0 , -1):
            r = random.randint(0,i)
            self.deck_of_cards[i], self.deck_of_cards[r] = self.deck_of_cards[r], self.deck_of_cards[i] 
    def draw(self):
        return self.deck_of_cards.pop()

book = Deck()
book.shuffle()
book.show()
print('*****************')
card = book.draw()
card.show_card()