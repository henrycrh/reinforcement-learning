from ..market.listing import Listing


class Action:
    def __init__(self, items):
        self.list_sell = [Listing(0, 0)] * len(items)
        self.list_buy = [Listing(float('inf'), 0)] * len(items)
        self.use_goods = [0] * len(items)

    def list_sell_item(self, item, listing):
        self.list_sell[item] = listing

    def list_buy_item(self, item, listing):
        self.list_buy[item] = listing

    def use_good(self, item, count):
        self.use_goods[item] = count

    def from_state(self):
        pass
