from items.items import Items


class Inventory:
    def __init__(self, preferences):
        # TODO: Need to prepare items on instantiation with preferences and players
        self.items = [x.mutable_copy() for x in Items.GOODS.value] + [x.mutable_copy() for x in Items.INVESTMENTS.value]

    def add_item(self, item, count):
        self.items[item].add(count)

    def remove_item(self, item, count):
        self.items[item].remove(min(self.items[item], count))

    def as_state(self):
        pass
