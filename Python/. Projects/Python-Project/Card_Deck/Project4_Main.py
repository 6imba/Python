from Project3_Players import Player
from Project2_Deck import Deck

players = Player()
players.Players_name() #initialize players

deck = Deck() # shuffle deck
deck.shuffle()

players.draw(deck) # draw for all players card

players.show_card() #card hold by all players
