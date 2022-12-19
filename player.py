from item import Good, Investment, Preference

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
    
class State:
    def __init__(self, market):
        self.market = market
        self.Inventory = Inventory()
    
class Action:
    def __init__(self):
        pass
