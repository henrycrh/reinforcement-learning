import os
from world import World
from items.goods.apple import Apple
from items.investments.apple_tree import AppleTree

class UI:
    def __init__(self, player, world):
        self.player = player
        self.world = world
            
    def get_action(self):
        action_result = []
        state = StartState(self, action_result)
        while not isinstance(state, EndState):
            state = state.get_action()
        return action_result
        
class State:
    def __init__(self, ui, action_result):
        self.ui = ui
        self.action_result = action_result
        self.headers = []
        self.rows = []
        self.actions = ["Back", "Finish"]
        
    def get_action(self):
        self.display_table()
        for i in range(10):
            try:
                cmd, args = self.get_action_input()
                print(cmd, args)
                return getattr(self, cmd)(*args)
            except Exception as e:
                print("Failed to process input:" + str(e))
    
            
    def display_table(self):
        os.system("cls")
        headers = ["Index"] + self.headers
        rows = [[i + 1] + x for i, x in enumerate(self.rows)]
        cols = len(headers)
        max_rowlengths = [ max([len(str(row[i])) for row in [headers] + rows]) for i in range(cols)]
        table_width = sum(max_rowlengths) + 3*cols + 1
        print("-"*table_width)
        for row in [headers] + rows:
            print("|" + "|".join([" " + str(x) + " "*(1 + max_rowlengths[i] - len(str(x))) for i, x in enumerate(row)]) + "|")
            print("-"*table_width)
    
    def get_action_input(self):
        vals = input("Choose Action: | {} | \n".format(" | ".join(["(" + action[0] + ")" + action[1:] for action in self.actions]))).split()
        return next((x.lower() for x in self.actions if x.lower().startswith(vals[0].lower())), None), vals[1:]
        
    def back(self, *args):
        return self
    
    def finish(self, *args):
        return EndState(self.ui, self.action_result)
    
    
class StartState(State):
    def __init__(self, ui, action_result):
        super().__init__(ui, action_result)
        self.actions = ["View"] + self.actions
        self.headers = ["Action"]
        self.rows = [["Market (Buy Listings)"], 
                     ["Market (Sell Listings)"], 
                     ["Inventory"]
                     ]
    
    def display_table(self):
        print("Player Number " + str(self.ui.player.idx))
        print("Main Menu")
        super().display_table()
        print("Quality of Life: " + str(self.ui.player.qol))
        
    def view(self, idx, *args):
        if idx == '1':
            return BuyMarketState(self.ui, self.action_result)
        if idx == '2':
            return SellMarketState(self.ui, self.action_result)
        if idx == '3':
            return InventoryState(self.ui, self.action_result)
        return self
    
class BuyMarketState(State):
    def back(self, *args):
        return StartState(self.ui, self.action_result)
        
class SellMarketState(State):
    def back(self, *args):
        return StartState(self.ui, self.action_result)
        
class InventoryState(State):
    def back(self, *args):
        return StartState(self.ui, self.action_result)
        
    
class EndState(State):
    pass
        

if __name__ == "__main__":
    items = [Apple, AppleTree]        
    world = World(num_players=3, items=items)
    ui = UI(world.players[0], world)
    print(ui.get_action())