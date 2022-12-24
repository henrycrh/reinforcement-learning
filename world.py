from models.dummy_policy import DummyPolicy
from market.market import Market
from player.action import Action
from player.player import Player


class World:
    def __init__(self, num_players=3, items=None):
        if items is None:
            items = []
        self.market = Market(num_players, items)
        self.players = [Player(i, self, items, DummyPolicy) for i in range(num_players)]

    def update_step(self):
        # Generate actions per player
        actions = []
        for player in self.players:
            # TODO: how we geenrate observation(state) may change
            observation = self.market.as_state() + player.as_state()
            action = player.policy.act(observation)
            actions.append(Action.from_state(player, action))

        # update market listings with buy and sell listings

        # resolve market and updates player inventory states as required
        # order of largest spread difference and move down until spread difference is negative

        # resolve use goods per player

        for player in self.players:
            print(player.inventory.items)
            for item in player.inventory.items:
                item.tick()

    def reset(self):
        pass
