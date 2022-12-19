from item import Good, Investment, Preference
from market import Market, Listing
from inventory import Inventory

class Player:
    def __init__(self):
        self.qol = 0
        self.wallet = 0
        self.inventory = Inventory()
        self.preferences = [Preference()] * 10

    def as_state(self):
        pass







