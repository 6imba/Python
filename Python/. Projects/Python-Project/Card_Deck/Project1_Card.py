import random

class Card(object):
    def __init__(self, suits, value): 
        self.suits = suits
        self.value = value

    def show(self): 
        return '{} of {}'.format(self.value, self.suits)

