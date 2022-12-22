from items.goods.apple import Apple
from items.investment import Investment


class AppleTree(Investment):
    DEFAULT_TRIGGER_RATE = 10

    def __init__(self, index, player, world, quantity):
        super().__init__(index, player, world, quantity, self.DEFAULT_TRIGGER_RATE)

    def trigger(self):
        print(f'triggering apple tree(s), quantity: {self.quantity}')
        super().trigger()
        # TODO: get index of apple class
        self.player.inventory.get_item(Apple).add(3 * self.quantity)
