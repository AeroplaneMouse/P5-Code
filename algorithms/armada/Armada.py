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

    n = len(frequentStates)
    i = 1
    # Run the algorithm
    for s in frequentStates:
        # Create and save pattern
        p = CreatePattern(None, s)
        Storage.Patterns.append(p)
        p_idx = CreateIndexSet(s, p, Storage.MDB)
        MineIndexSet(p, p_idx)
        print('[INFO] ARMADA {:0.1f}%'.format((i/n)*100))
        i += 1

    return Storage.Patterns
