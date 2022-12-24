from enum import Enum, auto


class State(Enum):
    ALIVE = auto()
    DEAD = auto()


class Condition:
    def __init__(self):
        self.food = 100

    def tick(self):
        if self.get_condition() is not State.DEAD:
            self.food -= 10

    def get_condition(self):
        if self.food <= 0:
            return State.DEAD

        return State.ALIVE
