from items.good import Good
from player.preference import Preference


class Apple(Good):
    def __init__(self, index, player, world, quantity):
        # TODO: possibly random preference
        super().__init__(index, player, world, quantity, Preference(self, 10, 10))
