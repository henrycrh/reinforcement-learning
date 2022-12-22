from base import Item


# TODO: each good might need a default steepness and QoL amount
# TODO: also each good needs basic condition metrics
class Good(Item):
    def __init__(self, quantity, player, preference):
        super().__init__(quantity, player)
        self.preference = preference

    def use(self, quantity):
        super().remove(quantity)
        for i in range(quantity):
            self.player.qol += self.preference.get()
            self.preference.last_use = 0

    def tick(self):
        super().tick()
        self.preference.last_use += 1

    def as_state(self):
        return [self.quantity] + self.preference.as_state()
