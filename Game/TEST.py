from random import *
from Game.DeckOfCards import DeckOfCards

full = DeckOfCards()
print(full.shuffle())
print(full.deal_one())
print(full.show())

