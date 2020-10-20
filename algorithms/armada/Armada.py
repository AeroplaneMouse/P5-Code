from algorithms.armada.MineIndexSet import MineIndexSet
from algorithms.armada.CreatePattern import CreatePattern
from models.FState import FState
from mocks import Patterns, IndexSets


class Armada:
    def __init__(self, cs, states):
        self.CS = cs
        self.SupStates = states

    def Run(self, minSup):
        # Clear states
        self.States = []
        self.States = GetStatesFor(minSup, self.SupStates)

        # for state in self.States:
        #     s = state.StateName

            # Create pattern

            # Create indexSet

            # Mine indexSet

        ### Create pattern tests
        state = FState(
            state='0_20->25',
            start='2013-07-01 04:01:14',
            end='2013-07-01 13:08:17')
        p = CreatePattern(None, state)

        print(p)

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
