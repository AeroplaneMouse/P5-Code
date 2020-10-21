from algorithms.armada.CreateIndexSet import CreateFirstIndexSet
from algorithms.armada.MineIndexSet import MineIndexSet
from algorithms.armada.CreatePattern import CreatePattern
from models.FState import FState
import pandas as pa


class Armada:
    def __init__(self, cs, states):
        self.CS = cs
        self.SupStates = states

    def Run(self, minSup):
        # Clear states
        self.States = GetStatesFor(minSup, self.SupStates)

        # for state in self.States:
        #     s = state.StateName

            # Create pattern

            # Create indexSet

            # Mine indexSet
        

        ### Create pattern tests
        state = FState(
            state='0_20->25',
            start=pa.to_datetime('2013-07-01 04:01:14'),
            end=pa.to_datetime('2013-07-01 13:08:17'))
        p = CreatePattern(None, state)

        visited_states = []
        for i in range(0, len(self.CS)):
            print()
            
            if self.CS.iloc[i].State not in visited_states:
                visited_states.append(self.CS.iloc[i].State)
                print("Index table for " + self.CS.iloc[i].State)
                CreateFirstIndexSet(self.CS.iloc[i], self.CS)

        

        #print(self.CS)
        

        ### MineIndexSet tests
        # idx = IndexSets.A
        # MineIndexSet(
        #     pattern=None,
        #     indexSet=idx,
        #     frequentStates=self.States,
        #     cs=self.CS)

        # MineIndexSet(None, IndexSets.A)
        # MineIndexSet(pattern, indexSet)


# Remove states that does not meet min support
def GetStatesFor(minSup, supStates):
    states = []
    for s in supStates:
        if s.Support >= minSup:
            states.append(s.StateName)
    return states
