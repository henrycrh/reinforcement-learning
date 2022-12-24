from player.condition import Condition
from player.inventory import Inventory


class Player:
    def __init__(self, idx, world, items, policy_cls):
        self.idx = idx
        self.qol = 0
        self.condition = Condition()
        self.wallet = 0
        self.inventory = Inventory(self, world, items)
        self.policy = policy_cls(self)
        self.world = world

    def __repr__(self):
        return f'''Player(idx={self.idx},
                          qol={self.qol},
                          wall={self.wallet},
                          item_count={sum([x.quantity for x in self.inventory.items])})'''

    def as_state(self):
        pass
