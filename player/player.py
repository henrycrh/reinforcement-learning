import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from item import Good, Investment, Preference
from market import Market, Listing
from player.inventory import Inventory

class Player:
    def __init__(self, idx, world, items):
        self.idx = idx
        self.qol = 0
        self.wallet = 0
        self.inventory = Inventory(self, world, items)

    def __repr__(self):
        return "Player(idx={}, qol={}, wallet={}, item_count={})".format(self.idx, self.qol, self.wallet, sum([x.quantity for x in self.inventory.items]))

    def as_state(self):
        pass







