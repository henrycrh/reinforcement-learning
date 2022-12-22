from items.base import ItemBase
from items.good import Good


class AppleBase(ItemBase):
    def mutable_copy(self):
        return Apple(0, None, None)


class Apple(Good):
    def __init__(self, quantity, player, preference):
        super().__init__(quantity, player, preference)
