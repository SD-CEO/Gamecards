from Game.Card import Card
from Game.DeckOfCards import DeckOfCards
from Game.Player import Player
from random import *
from Game.CardGame import CardGame

print("starting game")
game = CardGame()  # start a game with default 10 cards per player
print(game.player_1.show())
print(game.player_2.show())
for i in game.player_1.hand:
    if i in game.player_2.hand:
        game.player_1.hand.remove(i)
        game.player_1.add_card(choice(game.player_1.deck_full))
for i in range(10):
    card_1 = game.player_1.get_card()
    card_2 = game.player_2.get_card()
    # print(game.game_deck)
    print(f"{game.player_1.name}----{game.player_1.card_name}\n{game.player_2.name}----{game.player_2.card_name} ")
    if card_1 > card_2:
        print(f"{game.player_1.name} won this round!")
        game.player_1.add_card(game.player_2.card_name)
        game.player_1.add_card(game.player_1.card_name)
        continue
    if card_2 > card_1:
        print(f"{game.player_2.name} won this round!")
        game.player_2.add_card(game.player_1.card_name)
        game.player_2.add_card(game.player_2.card_name)
        continue


