from base import Item


class Investment(Item):
    def __init__(self, quantity, player, trigger_rate):
        super().__init__(quantity, player)
        self.trigger_rate = trigger_rate
        self.last_trigger = 0

    def trigger(self):
        # print("triggered " + self.description)
        pass

    def tick(self):
        self.last_trigger += 1
        if self.last_trigger >= self.trigger_rate:
            self.trigger()
            self.last_trigger = 0

    def add(self, quantity):
        self.last_trigger = int(self.last_trigger * self.quantity / (self.quantity + quantity))
        super().add(quantity)

    def as_state(self):
        return [self.quantity, self.last_trigger]
