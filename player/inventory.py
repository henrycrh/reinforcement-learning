class Inventory:
    def __init__(self, player, world, items):
        self.items = [item(i, player, world, 0) for i, item in enumerate(items)]
        self.lookup = {item.__name__: i for i, item in enumerate(items)}

    def get_item(self, target_class):
        return self.items[self.lookup[target_class.__name__]]

    def get_index(self, target_class):
        return self.lookup[target_class.__name__]

    def as_state(self):
        pass
