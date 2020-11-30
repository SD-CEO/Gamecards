from Game.DeckOfCards import DeckOfCards
# from Game.Card import Card
from random import *


class Player:
    def __init__(self, name):  # k = Defult num cards of deck
        self.name = name
        deck = DeckOfCards()
        self.deck = deck.lst_cards

    def set_hand(self, number_cards=10):  # deals a random set of hand to the player. defult 10 cards
        shuffle(self.deck)
        self.hand = sample(self.deck, number_cards)
        return self.hand

    def get_card(self):  # takes a random card from the player's hand
        [x] = sample(self.hand, 1)
        self.hand.remove(x)
        return x

    def add_card(self, card1):  # gets a card and adds it to the player's hand
        self.hand.append(card1)

    def show(self):  # prints the player's name and his hand
        return f"{self.name} {self.set_hand()}"
