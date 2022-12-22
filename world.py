from player.player import Player
from item import Good, Investment, Preference
from market import Market

class World:
    def __init__(self, num_players = 3, items = []):
        self.market = Market(num_players, items)
        self.players = [Player(i, self, items) for i in range(num_players)]

    
    def update_step(self):
        for player in self.players:
            print(player.inventory.items)
            for item in player.inventory.items:
                item.tick()
    