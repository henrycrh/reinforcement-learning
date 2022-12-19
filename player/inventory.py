class Inventory:
    def __init__(self, items):
        # TODO: items will store an Items object with properties like quantity in place of a singular count
        self.items = [0 for x in range(len(items))]

    def add_good(self, item, count):
        self.items[item] += count
    
    def remove_good(self, item, count):
        self.items[item] -= min(self.items[item], count)

    def as_state(self):
        pass