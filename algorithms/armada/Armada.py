from logging2 import *
from algorithms.armada import Storage
from algorithms.armada.MineIndexSet import MineIndexSet
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada.CreateIndexSet import CreateIndexSet

def Armada(mdb, frequentStates, minSupport, maxGap, logger):
    # Initialize
    Storage.MDB = mdb
    Storage.MinimumSupport = minSupport
    Storage.MaximumGap = maxGap
    Storage.Patterns = []
    Storage.Logger = logger

    log = Log('ARMADA start', Severity.NOTICE)
    logger.log(log)

    # Run the algorithm
    i = 1
    n = len(frequentStates)
    logger.log(ProgressLog('ARMADA: '))
    for s in frequentStates:
        # Create and save pattern
        p = CreatePattern(None, s)
        Storage.Patterns.append(p)
        p_idx = CreateIndexSet(s, p, Storage.MDB)
        MineIndexSet(p, p_idx)

        # Logging
        m = 'ARMADA {:0.1f}%'.format((i/n))
        logger.log(ProgressLog('ARMADA: ', progress=(i/n)))

        i += 1

    log = Log('ARMADA finished', Severity.NOTICE)

    return Storage.Patterns
