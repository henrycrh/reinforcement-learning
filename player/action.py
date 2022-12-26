import numpy as np

from market.listing import Listing


# TODO: when we're ready for hardcoded agent
class Action:
    def __init__(self, player):
        self.player = player
        num_items = len(player.inventory.items)
        self.list_sell = [Listing(0, 0)] * num_items
        self.list_buy = [Listing(float('inf'), 0)] * num_items
        self.use_goods = [0] * num_items

    def list_sell_item(self, item, listing):
        self.list_sell[item] = listing

    def list_buy_item(self, item, listing):
        self.list_buy[item] = listing

    def use_good(self, item, count):
        self.use_goods[item] = count

    @classmethod
    def from_state(cls, player, arr):
        action = cls(player)
        num_items = len(player.inventory.items)

        # parse sell list
        sell = arr[0:2 * num_items]
        action.list_sell = [Listing.from_state(sell[i:i+2]) for i in range(0, len(sell), 2)]

        # parse buy list
        buy = arr[2 * num_items:4 * num_items]
        action.list_buy = [Listing.from_state(buy[i:i+2]) for i in range(0, len(buy), 2)]

        # parse use list
        action.use_goods = arr[4 * num_items:]

        return action
