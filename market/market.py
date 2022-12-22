from market.listing import Listing


class Market:
    def __init__(self, num_players, items):
        self.items = items
        self.buy_listings = [[Listing(0, 0)] * len(self.items)] * num_players
        self.sell_listings = [[Listing(float('inf'), 0)] * len(self.items)] * num_players

    def as_state(self):
        pass
