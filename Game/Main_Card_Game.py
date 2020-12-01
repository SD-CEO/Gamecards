from Game.Card import Card
from Game.DeckOfCards import DeckOfCards
from Game.Player import Player
from Game.CardGame import CardGame

print("starting game")
game = CardGame()
print(game.player_1.show())
print(game.player_2.show())
#
card1 = game.player_1.get_card()
card2 = game.player_2.get_card()
print(game.player_1.card)
print("VS")
print(game.player_2.card)

if card1 > card2:
    print(True)
print(game.game_deck)









