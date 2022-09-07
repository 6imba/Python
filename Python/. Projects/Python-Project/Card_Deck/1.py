class Card(object):
    def __init__(self, Pics, daau):
        self.Pics = Pics
        self.daau = daau
    
    def show_card(self):
        print( '{} ko {}'.format(self.Pics , self.daau))

Amir_ko_patta = Card('Paan','Batsa')
Amir_ko_patta.show_card()

