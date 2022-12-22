from item import Good, Investment, Preference

class Market:
    def __init__(self, num_players, items):
        self.items = items
        
        # listings[player_idx][item_idx]
        self.buy_listings = [[Listing(0, 0) for x in range (len(items))] for x in range(num_players)]
        self.sell_listings = [[Listing(float('inf'), 0) for x in range (len(items))] for x in range(num_players)]

    def as_state(self):
        pass
        
class Listing:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def as_state(self):
        pass
