class BaseItem:
    def __init__(self, index, description):
        self.index = index
        self.description = description
     
class ImmutableItem(BaseItem):
    pass

class MutableItem(BaseItem):

    def __init__(self, index, description, quantity, player, world):
        super().__init__(index, description)
        self.quantity
        self.player = player
        self.world = world
        
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
            self.player.QoL += self.preference.get()
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
    
    def tick(self, player, world):
        self.last_trigger += 1
        if self.last_trigger >= self.trigger_rate:
            self.trigger()
            self.last_trigger = 0  
            
    def add(self, quantity):
        self.last_trigger = int(self.last_trigger * self.quantity / (self.quantity + quantity))
        super().add(quantity)
            
    def as_state(self):
        return tuple(self.last_trigger)
    
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
    

