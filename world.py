from player import Player
from item import Good, Investment, Preference
from market import Market

class World:
    def __init__(self, num_players = 3, properties = []):
        self.market = Market(num_players, properties)
    
    def update_step(self):
        print("Hello")
    