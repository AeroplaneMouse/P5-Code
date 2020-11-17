from algorithms.armada import Storage
from algorithms.armada.CreateIndexSet import CreateIndexSet
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada.MineIndexSet import MineIndexSet

import threading


class t (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        return


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

    return Storage.Patterns
