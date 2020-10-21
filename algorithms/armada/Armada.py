# from algorithms.armada.MineIndexSet import MineIndexSet
# from algorithms.armada.CreatePattern import CreatePattern
# from algorithms.armada.CreateIndexSet import CreateIndexSet
# from models.FState import FState
from algorithms.armada import Storage


class Armada:
    def __init__(self, mdb, states):
        # Initialize storage with db
        Storage.MDB = mdb  # List if cs
        self.SupStates = states

    def Run(self, minSup):
        # Clear states
        Storage.MinSup = minSup
        self.States = GetStatesFor(minSup, self.SupStates)

        # for state in self.States:
        #     s = state.StateName

            # Create pattern

            # Create indexSet

            # Mine indexSet
        


# Remove states that does not meet min support
def GetStatesFor(minSup, supStates):
    states = []
    for s in supStates:
        if s.Support >= minSup:
            states.append(s.StateName)
    return states
