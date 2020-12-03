from logging import *
from models.result import Result
from algorithms.armada.Armada import Armada
from preprocessors import Support, columns as col

########################################
# Vent
def vent_getState(value, columnName):
    # Convert name to number
    columnName = col.vent_columns.index(columnName)

    INTERVAL = 5
    # Compute distance to range start
    r = value % INTERVAL

    # Compute range start and end
    rangeStart = value - r
    rangeEnd = rangeStart + INTERVAL

    return '{}_{:.0f}->{:.0f}'.format(
        columnName,
        rangeStart,
        rangeEnd)


########################################
# Load
def load_getState(value, columnName):
    if value == '1' or value == 1:
        return '{}_{}'.format(columnName, value)
    else:
        return None


########################################
# ARMADA
def armada(mdb, supportList, logger, minSupport, maxGap):
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)
    frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)

    log = Log('Frequent states removed', Severity.INFO)
    logger.log(log)

    patterns = Armada(mdb, frequentStates, minSupport, maxGap, logger)

    return Result(minSupport, maxGap, patterns, frequentStates)

