class Player:
    def __init__(self, market):
        self.state = State(market)
        self.weights = Weights()
        self.preferences = [Preference()] * 100 
        
    def get_action(self):
        return Action()
    
class Weights:
    def __init__(self):
        pass
    
class Inventory:
    def __init__(self):
        pass
    
class Market:
    def __init__(self, properties):
        pass
    
class State:
    def __init__(self, market):
        self.market = market
        self.Inventory = Inventory()
    
class World:
    def __init__(self, num_players = 3, properties = []):
        self.market = Market(properties)
    
    def update_step(self):
        print("Hello")
    
class Action:
    def __init__(self):
        pass

class Item:
    def __init__(self):
        pass
    
class Preference:
    def __init__(self, item):
        self.item = item

