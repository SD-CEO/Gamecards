from Game.Card import Card
from random import *


# from random import randint


class DeckOfCards:  # make a new deck_cards sort by volume!, The volume card is the index num of the card
    def __init__(self):
        self.level_suit = ["Diamond", "Spade", "Heart", "Club"]
        self.level_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.lst_cards = []
        for i in self.level_value:
            for z in self.level_suit:
                card = Card(i, z)
                self.lst_cards += [card]

    def shuffle(self):  # shuffles the deck
        x = sample(self.lst_cards, 51)
        return x

    def deal_one(self):  # deasl one random card from the deck
        return choice(self.lst_cards)

    def show(self):  # show cards
        return self.lst_cards
