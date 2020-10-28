from algorithms.armada import Storage
from algorithms.armada.CreateIndexSet import CreateIndexSet
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada.MineIndexSet import MineIndexSet


def Armada(mdb, frequentStates, minSupport, maxGap):
    # Initialize
    Storage.MDB = mdb
    Storage.MinimumSupport = minSupport
    Storage.MaximumGap = maxGap
    Storage.Patterns = []

    # Run the algorithm
    for s in frequentStates:
        # Create and save pattern
        p = CreatePattern(None, s)
        Storage.Patterns.append(p)

        p_idx = CreateIndexSet(s, p, Storage.MDB)
        MineIndexSet(p, p_idx)

    # return "Some fucking OP patterns... perhaps"
    return Storage.Patterns


class Armada_Deprecated:
    def __init__(self, mdb, states):
        # Initialize storage with db
        Storage.MDB = mdb  # List if cs
        self.SupStates = states

    def Run(self, minSup):
        # for state in self.States:

        for i in range(0, len(Storage.MDB)):
            for j in range(0, len(Storage.MDB[i])):
                id = CreateIndexSet(Storage.MDB[i].iloc[j], None, Storage.MDB)
