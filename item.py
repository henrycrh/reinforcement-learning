class Item:
    def __init__(self, name):
        self.name = name
        
class Good(Item):
    def __init__(self, name):
        super().__init__(name)
        
class Investment(Item):
    def __init__(self, name):
        super().__init__(name)
        
class PreferenceCurve:
    def __init__(self, amount, steepness):
        self.amount = amount
        self.steepness = steepness
        
    def get(self):
        return self.amount
    
class Preference:
    def __init__(self, item):
        self.item = item

