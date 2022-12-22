import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

class Inventory:
    def __init__(self, player, world, items):
       self.items = [item.get_item(player=player, world=world, quantity=0) for item in items]

    def add_good(self, idx, count):
        self.items[idx].add(count)
    
    def remove_good(self, idx, count):
        self.items[idx].remove(count)

    def by_description(self, description):
        return next((x for x in self.items if x.description.lower() == description.lower()), None)

    def as_state(self):
        pass
