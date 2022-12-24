from models.policy import Policy


class DummyPolicy(Policy):
    def __init__(self, player):
        super().__init__(player)

    def act(self, observation):
        print(observation)
        return [0] * (5 * len(self.player.inventory.items))
