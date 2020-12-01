from Game.DeckOfCards import DeckOfCards
# from Game.Card import Card
from random import *


class Player:
    def __init__(self, name):  # k = Defult num cards of deck
        self.name = name
        self.deck = DeckOfCards()
        self.deck_full = self.deck.lst_cards
        self.hand = []
        self.card_name = ""

    def set_hand(self, number_cards=10):  # deals a random set of hand to the player. defult 10 cards
        for i in range(number_cards):
            self.hand.append(self.deck_full.pop(randint(0, len(self.deck_full))))
        return self.hand

    def get_card(self):  # takes a random card from the player's hand
        x = self.deck.deal_one()
        self.card_name = x
        return self.deck.lst_cards.index(x)


    def add_card(self, card1):  # gets a card and adds it to the player's hand
        self.hand.append(card1)

    def show(self):  # prints the player's name and his hand
        return f"{self.name} {self.hand}"
