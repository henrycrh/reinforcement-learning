from player.player import Player
from market.market import Market


class World:
    def __init__(self, num_players=2):
        self.market = Market(num_players)
        self.players = [Player()] * num_players

    def update_step(self):
        print("Hello")

        # Players choose actions

        # actions are applied

        # update game state
