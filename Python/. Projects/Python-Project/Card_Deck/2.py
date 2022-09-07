class Deck(object):
    def __init__(self):
        self.deck_of_cards = []
        self.build() #automatically initialize build method
    
    def build(self):
        for Pics in ['Paan', 'Itta', 'Chidi', 'Surat', ]:
            print('***',Pics,'***',Pics,'***',Pics,'***',Pics,'***',Pics,'***')
            for daau in range(1,14):
                print( '{} ko {} '.format(Pics, daau))

book = Deck()

