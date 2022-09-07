class Card(object):
    def __init__(self, Pics, daau):#3
        self.Pics = Pics
        self.daau = daau
    
    def show_card(self): # line(4.1) ///////////////// #6
        print( '{} ko {}'.format(self.Pics , self.daau))

class Deck(object):
    def __init__(self): #1
        self.deck_of_cards = [] #4
        self.build()
    
    def build(self): #2
        for Pics in ['Paan', 'Itta', 'Chidi', 'Surat', ]:
            for daau in range(1,14):
                self.deck_of_cards.append(Card(Pics,daau)) 
    
    def show_deck(self): #5
        for cards_object in self.deck_of_cards:
            cards_object.show_card() # as deck_of_cards in line<3.1> stores list of objects of class Card(), when we print item of list it prints in object format
                                     # so, this code(cards_object.show_card()) prints objects at deck_of_cards into given format in show_card() method in calss Card() 
                                     # So this gives output of list_of_object in deck_of_cards through show_card() in line(4.1) in parent_Class 

book = Deck()
book.show_deck()