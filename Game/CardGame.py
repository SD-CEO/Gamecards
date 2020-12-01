from Game.DeckOfCards import DeckOfCards
from Game.Card import Card
from Game.Player import Player
from random import *


class CardGame:
    def __init__(self, number_cards=10):  # creates a new deck
        game_deck = DeckOfCards()
        self.player_1 = Player("Dolev")
        self.player_2 = Player("Shay")
        self.game_deck = game_deck.lst_cards
        self.number_cards = number_cards
        self.new_game()

    def new_game(self):  # shuffels the deck and deals each player the number of decided cards
        self.player_1.set_hand()
        self.player_2.set_hand()


    def get_winner(self):  # prints the player with the least card. if equal,gives None
        if len(self.player_1.hand) > len(self.player_2.hand):
            return f"{self.player_2.name} won!"
        if len(self.player_2.hand) > len(self.player_1.hand):
            return f'{self.player_1.name} won!'
        else:
            return None
