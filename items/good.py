from items.base import Item


# TODO: each good might need a default steepness and QoL amount
# TODO: also each good needs basic condition metrics
class Good(Item):
    def __init__(self, index, player, world, quantity, preference):
        super().__init__(index, player, world, quantity)
        self.preference = preference

    # TODO: return amount used?
    def use(self, quantity):
        use_quantity = super().remove(quantity)
        for i in range(use_quantity):
            self.player.qol += self.preference.get()

        self.preference.last_use = 0
        return use_quantity

    def tick(self):
        super().tick()
        self.preference.last_use += 1

    def as_state(self):
        return [self.quantity] + self.preference.as_state()
