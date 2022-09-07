cardfaces = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['Heart', 'Spade', 'Clubs', 'Diamond']
deck = []

for suit in suits: #maky deck of cards
    for cardface in cardfaces:
        deck.append(str(cardface) +' of ' +suit) # cardfaces consist of int so needed to cast into str inorder to use +(addition) operator

print(deck) # print deck before shuffle

import random
random.shuffle(deck)
print(deck) # print deck after shuffle

draw = deck.pop()
print(draw)

hand = []
hand.append(draw)
print(hand)


draw = deck.pop()
print(draw)

hand.append(draw)
print(hand)

draw = deck.pop()
print(draw)

hand.append(draw)
print(hand)



# so use oop
