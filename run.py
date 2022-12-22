from world import World
from item import ImmutableItem, Apple, AppleTree


temp = [Apple, AppleTree]

items = [ ImmutableItem(i, x.__name__, x) for i, x in enumerate(temp)]
print(items)
world = World(num_players = 3, items = items)


world.players[0].inventory.by_description("AppleTree").add(5)
for i in range(21):
    print("----------------Starting {}-----------------".format(i))
    world.update_step()
    if i==2:
        world.players[1].inventory.by_description("AppleTree").add(1)
    print("----------------Ending {}-----------------".format(i))