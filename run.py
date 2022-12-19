from classes import Player, Weights, Inventory, Market, State, World, Action, Item, Preference


world = World()
for i in range(100):
    print("Starting", i)
    world.update_step()
    print("Ending", i)