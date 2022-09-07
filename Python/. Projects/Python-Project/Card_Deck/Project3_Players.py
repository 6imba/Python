from Project2_Deck import Deck

class Player(object):

    def __init__(self):
        self.names = []
        self.dict1 = {}

    def Players_name(self):
        numb = int(input('Enter number of players : '))
        for i in range(0,numb):
            self.names.append(input('Enter name :'))
        print(self.names)

    def draw(self, deck1): 
        for i in range(0,3):
            if i == 0:
                for name in self.names:
                    self.dict1[name] = [deck1.draw_card()]
            else :
                for name in self.names:
                    self.dict1[name].append(deck1.draw_card())
        print(self.dict1)

    def show_card(self):
        for player in self.dict1: 
            print('{} : \n    {}\n    {}\n    {}'.format(player, self.dict1[player][0].show(), self.dict1[player][1].show(), self.dict1[player][2].show()))

  


