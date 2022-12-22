from items.items import Items
from preference import Preference
from inventory import Inventory
from condition import Condition


class Player:
    def __init__(self):
        self.qol = 100
        self.condition = Condition()
        self.wallet = 0

        # TODO: Create a preference for each product
        # TODO: amount and steepness need to be supplied in a different manner
        self.preferences = [Preference(i, 10, 10) for i in range(len(Items.GOODS.value))]

        # TODO: assign preferences and player to items
        self.inventory = Inventory(self.preferences)

    def as_state(self):
        pass
