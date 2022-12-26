import math

from items.good import Good
from models.dummy_policy import DummyPolicy
from market.market import Market
from player.action import Action
from player.player import Player


class World:
    def __init__(self, num_players=3, items=None):
        self.market = Market(num_players, items)
        self.players = [Player(i, self, items, DummyPolicy) for i in range(num_players)]

    def update_step(self):
        # Generate actions per player
        actions = []
        for i, player in enumerate(self.players):
            # TODO: how we generate observation(state) may change
            print(self.market.as_state())
            observation = self.market.as_state() + player.as_state()
            action_state = player.policy.act(observation)
            action = Action.from_state(player, action_state)
            actions.append(action)

        # update market listings with buy and sell listings
        for i, action in enumerate(actions):
            self.market.buy_listings[i] = action.list_buy
            self.market.sell_listings[i] = action.list_sell

        # resolve market and updates player inventory states as required
        for i in range(len(self.market.items)):
            # sort buy listings by buy price in descending order
            sorted_buy = list(filter(lambda x: x[1].price > 0 and x[1].quantity > 0,
                                     sorted([(j, lst[i]) for j, lst in enumerate(self.market.buy_listings)],
                                            key=lambda x: x[1].price,
                                            reverse=True)))

            # sort sell listings by offer price in ascending order
            sorted_sell = list(filter(lambda x: x[1].price > 0 and x[1].quantity > 0,
                                      sorted([(j, lst[i]) for j, lst in enumerate(self.market.sell_listings)],
                                             key=lambda x: x[1].price)))

            # continue resolving listings while spread difference
            # (difference between largest buy and smallest sell price) is non-negative
            while len(sorted_buy) > 0 and len(sorted_sell) > 0 and sorted_buy[0][1].price >= sorted_sell[0][1].price:
                # resolve listing
                buy_player_idx, curr_buy = sorted_buy[0][0], sorted_buy[0][1]
                sell_player_idx, curr_sell = sorted_sell[0][0], sorted_sell[0][1]

                buy_player = self.players[buy_player_idx]
                sell_player = self.players[sell_player_idx]

                bargain_price = (curr_buy.price + curr_sell.price) / 2
                buy_quantity = min(curr_buy.quantity, math.floor(buy_player.wallet / bargain_price))
                sell_quantity = min(curr_sell.quantity, sell_player.inventory.items[i].quantity)

                # check if transaction is valid
                if buy_quantity == 0:
                    # buyer cannot complete transaction, so remove their listing
                    sorted_buy.pop(0)
                elif sell_quantity == 0:
                    # seller cannot complete transaction, so remove their listing
                    sorted_sell.pop(0)
                else:
                    transaction_quantity = min(buy_quantity, sell_quantity)
                    transaction_price = bargain_price * transaction_quantity

                    # exchange money
                    buy_player.wallet -= transaction_price
                    sell_player.wallet += transaction_price

                    # exchange items
                    buy_player.inventory.items[i].add(transaction_quantity)
                    sell_player.inventory.items[i].remove(transaction_quantity)

                    # update listings
                    curr_buy.quantity -= transaction_quantity
                    curr_sell.quantity -= transaction_quantity

                    if curr_buy.quantity == 0:
                        sorted_buy.pop(0)
                    if curr_sell.quantity == 0:
                        sorted_sell.pop(0)

        # resolve use goods per player
        for player in self.players:
            player_action = actions[player.idx]
            use_goods = player_action.use_goods
            print("before: ", player.inventory.items)
            for i, item in enumerate(player.inventory.items):
                if isinstance(item, Good):
                    use_quantity = use_goods[i]
                    item.use(use_quantity)

            player.tick()
            print("player condition: ", player.condition.get_condition())
            print("after: ", player.inventory.items)

    def reset(self):
        pass
