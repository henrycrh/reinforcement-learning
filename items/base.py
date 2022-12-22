class Item:
    def __init__(self, index, player, world, quantity):
        self.index = index
        self.player = player
        self.world = world
        self.quantity = quantity

    def __repr__(self):
        return f'{self.__class__.__name__}(index={self.index}, quantity={self.quantity})'

    def remove(self, quantity):
        self.quantity -= min(self.quantity, quantity)

    def add(self, quantity):
        self.quantity += quantity

    def tick(self):
        pass
