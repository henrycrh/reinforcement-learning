# class BaseItem:
#     def __init__(self, index, description):
#         self.index = index
#         self.description = description


# class ImmutableItem(BaseItem):
#     pass

class ItemBase:
    def __init__(self):
        self.index = index
    def mutable_copy(self):
        pass


class Item:
    def __init__(self, quantity, player):
        self.quantity = quantity
        self.player = player

    def remove(self, quantity):
        self.quantity -= quantity

    def add(self, quantity):
        self.quantity += quantity

    def set_owner(self, owner):
        self.player = owner

    def tick(self):
        pass
