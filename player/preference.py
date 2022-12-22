class Preference:
    def __init__(self, item, amount, steepness):
        self.item = item
        self.last_use = 0
        self.amount = amount
        self.steepness = steepness

    def get(self):
        return self.amount

    def tick(self):
        # TODO: possibly?
        pass

    def as_state(self):
        return [self.amount, self.last_use]
