from Game.Card import Card
from Game.DeckOfCards import DeckOfCards
from Game.Player import Player
from Game.CardGame import CardGame

print("starting game")
game = CardGame()
print(game.player_1.show())
print(game.player_2.show())

for i in range(1):
    print(f"{game.player_1.name}: {game.player_1.get_card()} -- {game.player_2.get_card()} :{game.player_2.name}")
    card_1 = game.player_1.get_card()
    card_2 = game.player_2.get_card()
    if game.game_deck.index(card_1) > game.game_deck.index(card_2):
        game.player_2.add_card(card_1)
        game.player_2.add_card(card_2)
        print(f"{game.player_2.name} was won that round")

    if game.game_deck.index(card_1) < game.game_deck.index(card_2):
        game.player_1.add_card(card_1)
        game.player_1.add_card(card_2)
        print(f"{game.player_1.name} was won that round")
