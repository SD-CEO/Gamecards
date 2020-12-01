from Game.Card import Card
from Game.DeckOfCards import DeckOfCards
from Game.Player import Player
from Game.CardGame import CardGame

print("starting game")
game = CardGame()
print(game.player_1.show())
print(game.player_2.show())
for i in game.player_1.hand:
    while i in game.player_2.hand:
        game.player_2.hand.remove(i)
        game.player_2.hand.append(game.player_2.set_hand(1))


card_1 = game.player_1.get_card()
card_2 = game.player_2.get_card()
print(card_1)
print(card_2)
# print(game.game_deck.index(card_1))
# # print(game.game_deck.index(card_2))
