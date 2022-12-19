from ..market import Listing


class Action:
    def __init__(self, items):
        self.list_sell = [Listing(0, 0) for x in range(len(items))]
        self.list_buy = [Listing(0, 0) for x in range(len(items))]
        self.use_goods = [0 for x in range(len(items))]

    def list_sell_item(self, item, listing):
        self.list_sell[item] = listing

    def list_buy_item(self, item, listing):
        self.list_buy[item] = listing

    def use_good(self, item, count):
        self.use_goods[item] = count
