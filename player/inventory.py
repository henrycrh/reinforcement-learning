class Inventory:
    def __init__(self, items):
        self.items = [0 for x in range(len(items))]

    def add_good(self, item, count):
        self.items[item] += count
    
    def remove_good(self, item, count):
        self.items[item] -= min(self.items[item], count)
