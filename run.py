from world import World

world = World()
for i in range(100):
    print("Starting", i)
    world.update_step()
    print("Ending", i)