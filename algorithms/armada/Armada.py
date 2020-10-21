# from algorithms.armada.MineIndexSet import MineIndexSet
# from algorithms.armada.CreatePattern import CreatePattern
# from algorithms.armada.CreateIndexSet import CreateIndexSet
# from models.FState import FState
from algorithms.armada import Storage
from algorithms.armada.CreateIndexSet import CreateFirstIndexSet


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
        

        ### Create pattern tests
        """
        state = FState(
            state='0_20->25',
            start=pa.to_datetime('2013-07-01 04:01:14'),
            end=pa.to_datetime('2013-07-01 13:08:17'))
        p = CreatePattern(None, state)
        """

        visited_states = []
        for i in range(0, len(Storage.MDB)):
            for j in range(0, len(Storage.MDB[i])):
                id = CreateFirstIndexSet(Storage.MDB[i].iloc[j], visited_states)

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
