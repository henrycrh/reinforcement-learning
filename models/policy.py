class Policy:
    def __init__(self, player):
        self.player = player

    def act(self, observation):
        pass

    # TODO: temporary for now, maybe we choose different formulation for policy update
    def update(self, rewards, obs, action):
        pass
