from algorithms.armada import Storage
from algorithms.armada.CreateIndexSet import CreateIndexSet, printPatterns
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada.MineIndexSet import MineIndexSet


def Armada(mdb, frequentStates, minSupport):
    # Initialize
    Storage.MDB = mdb
    Storage.MinimumSupport = minSupport

    # Run the algorithm
    for s in frequentStates:
        p = CreatePattern(None, s)
        p_idx = CreateIndexSet(s, p, Storage.MDB)
        MineIndexSet(p, p_idx)

    printPatterns()
    return "Some fucking OP patterns... perhaps"


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
        
