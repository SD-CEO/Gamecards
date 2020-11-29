from Game.DeckOfCards import DeckOfCards
# from Game.Card import Card
from random import *


class Player:
    def __init__(self, name):  # k = Defult num cards of deck
        self.name = name
        deck = DeckOfCards()
        self.deck = deck.lst_cards

    def set_hand(self, k=10):
        shuffle(self.deck)
        return sample(self.deck, k)

    def get_card(self):
        return sample(self.deck, 1)

    def add_card(self):
        Main = DeckOfCards()
        for i in range(len(Main.lst_cards)):
            if i not in self.deck:
                self.deck.append(i)

    def show(self):
        print(f"{self.name} {self.set_hand()}")
