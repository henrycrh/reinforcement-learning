from items.base import ItemBase
from items.investment import Investment
from items.items import Items


class AppleTreeBase(ItemBase):
    def mutable_copy(self):
        pass


class AppleTree(Investment):
    DEFAULT_TRIGGER_RATE = 100

    def __init__(self, quantity, player, trigger_rate=DEFAULT_TRIGGER_RATE):
        super().__init__(quantity, player, trigger_rate)

    def trigger(self):
        print(f'triggering apple tree(s), quantity: {self.quantity}')
        super().trigger()
        self.player.inventory.add_item(Items.APPLE.value, 3 * self.quantity)
