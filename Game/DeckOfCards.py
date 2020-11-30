from Game.Card import Card
from random import *


# from random import randint


class DeckOfCards:  # make a new deck_cards
    def __init__(self):
        self.level_suit = ["Diamond", "Spade", "Heart", "Club"]
        self.level_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.lst_cards = []
        for i in self.level_value:
            for z in self.level_suit:
                card = Card(i, z)
                self.lst_cards += [card]

    def shuffle(self): #shuffles the deck
        shuffle(self.lst_cards)
        return self.lst_cards

    def deal_one(self, k=1): #deasl one random card from the deck
        return sample(self.lst_cards, k)

    def show(self): #show cards
        return self.lst_cards
