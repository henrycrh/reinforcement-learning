def from_state(arr):
    return Listing(arr[0], arr[1])


class Listing:
    def __init__(self, price, quantity):
        # price per item
        self.price = price
        self.quantity = quantity

    def as_state(self):
        return [self.price, self.quantity]

    @classmethod
    def from_state(cls, arr):
        return cls(arr[0], arr[1])
