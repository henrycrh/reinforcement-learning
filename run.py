from world import World
from items.goods.apple import Apple
from items.investments.apple_tree import AppleTree

# Add new items
items = [Apple, AppleTree]

print(items)
world = World(num_players=3, items=items)


world.players[0].inventory.get_item(AppleTree).add(5)
for i in range(21):
    print("----------------Starting {}-----------------".format(i))
    world.update_step()
    if i == 2:
        world.players[1].inventory.get_item(AppleTree).add(1)
    print("----------------Ending {}-----------------".format(i))