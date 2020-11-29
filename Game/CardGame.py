from Game.DeckOfCards import DeckOfCards
# from Game.Card import Card
from Game.Player import Player
from random import *


class CardGame:
    def __init__(self, k=10):
        game_deck = DeckOfCards()
        self.game_deck = game_deck.lst_cards
        self.k = k
        self.new_game()

    def new_game(self):
        shuffle(self.game_deck)
        player_1 = Player('player1')
        player_2 = Player('player2')
        player_1.set_hand()
        player_2.set_hand()
        return f"{player_1.set_hand()}"

    def get_winner(self):
        if

