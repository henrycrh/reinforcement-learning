import copy

class BaseItem:
    def __init__(self, index, description):
        self.index = index
        self.description = description
     
    def __repr__(self):
        return "Item(index={}, description={})".format(self.index, self.description)
    
class ImmutableItem(BaseItem):
    def __init__(self, index, description, item):
        super().__init__(index, description)
        self.item = item
        
    def get_item(self, **kwargs):
        return self.item(self.index, self.description, **kwargs)

class MutableItem(BaseItem):

    def __init__(self, index, description, quantity, player, world):
        super().__init__(index, description)
        self.quantity = quantity
        self.player = player
        self.world = world
        
    def __repr__(self):
        return "Item(index={}, description={}, quantity={})".format(self.index, self.description, self.quantity)
        
    def use(self, quantity):
        self.quantity -= quantity
        
    def add(self, quantity):
        self.quantity += quantity
        
    def tick(self):
        pass
    
        
class Good(MutableItem):
    def __init__(self, index, description, quantity, player, world, preference):
        super().__init__(index, description, quantity, player, world)
        self.preference = preference
        
    def use(self, quantity):
        super().use(quantity)
        for i in range(quantity):
            self.player.qol += self.preference.get()
            self.preference.last_use = 0
        
    def tick(self):
        super().tick()
        self.preference.last_use += 1
        
    def as_state(self):
        return tuple(self.quantity) + self.preference.as_state()
        
class Investment(MutableItem):
    def __init__(self, index, description, quantity, player, world, trigger_rate):
        super().__init__(index, description, quantity, player, world)
        self.last_trigger = 0
        self.trigger_rate = trigger_rate
        
    def trigger(self):
        print("triggered " + self.description)
    
    def tick(self):
        self.last_trigger += 1
        if self.last_trigger >= self.trigger_rate and self.quantity > 0:
            self.trigger()
            self.last_trigger = 0  
            
    def add(self, quantity):
        self.last_trigger = int(self.last_trigger * self.quantity / (self.quantity + quantity))
        super().add(quantity)
            
    def as_state(self):
        return tuple(self.last_trigger)
    
class Apple(Good):
    def __init__(self, index, description, quantity, player, world):
        super().__init__(index, description, quantity, player, world, Preference(self, 10, 10))
        
class AppleTree(Investment):
    def __init__(self, index, description, quantity, player, world):
        super().__init__(index, description, quantity, player, world, 5)
        
    def trigger(self):
        self.player.inventory.by_description("Apple").add(self.quantity)
    
class Preference:
    def __init__(self, item, amount, steepness):
        self.item = item
        self.last_use = 0
        self.amount = amount
        self.steepness = steepness
        
    def get(self):
        return self.amount
    
    def as_state(self):
        return tuple(self.amount, self.last_use)
    

