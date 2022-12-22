from items.base import Item


class Investment(Item):
    def __init__(self, index, player, world, quantity, trigger_rate):
        super().__init__(index, player, world, quantity)
        self.trigger_rate = trigger_rate
        self.last_trigger = 0

    def trigger(self):
        pass

    def tick(self):
        self.last_trigger += 1
        if self.last_trigger >= self.trigger_rate and self.quantity > 0:
            self.trigger()
            self.last_trigger = 0

    def add(self, quantity):
        self.last_trigger = int(self.last_trigger * self.quantity / (self.quantity + quantity))
        super().add(quantity)

    def as_state(self):
        return [self.quantity, self.last_trigger]
