from item import Good, Investment, Preference

class Market:
    def __init__(self, num_players, items):
        self.items = items
        self.buy_listings = [[Listing(0, 0) for x in range (len(items))] for x in range(num_players)]
        self.sell_listings = [[Listing(float('inf'), 0) for x in range (len(items))] for x in range(num_players)]
        
class Listing:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity