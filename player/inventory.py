from ..item import Good, Investment

class Inventory:
    def __init__(self, items):
        # TODO: items will store an Items object with properties like quantity in place of a singular count
        self.items = [Good() if x.type == "good" else Investment() for x in range(len(items))]

    def add_good(self, item, count):
        self.items[item] += count
    
    def remove_good(self, item, count):
        self.items[item] -= min(self.items[item], count)

    def as_state(self):
        pass
