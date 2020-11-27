import helper
import pandas as pa
from logging import *
from preprocessors import Support
from algorithms.tpminer import tpminer
from algorithms.armada.Armada import Armada
from preprocessors.Preprocessor import GenericPreprocessor
from preprocessors.loadData import goodColumns as LOAD_colOfInterest


PATH = 'datasets/vent-minute.csv'
PATH_LOAD = 'datasets/Load-minute.csv'
PATH_ABSENS = 'datasets/Absens_P5.csv'
colOfInterest = [
    'Vent_HRVTempExhaustOut',
    'Vent_HRVTempOutdoorin',
    'Vent_HRVTempReturnIn',
    'Vent_HRVTempSupplyOut']
ABSENS_cols = ['Andreas','Daniel','Lasse','Lisa','Rasmus','Slamal']

def getState(value, columnName):
    # Convert name to number
    columnName = colOfInterest.index(columnName)

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


def LOAD_getState(value, columnName):
    if value == '1' or value == 1:
        return '{}_{}'.format(columnName, value)
    else:
        return None


def absens_getState(value, columnName):
    output = columnName + '_'

    if (value == '✔️'):
        output += 'Here'
    elif (value == '❌'):
        output += 'Despawned'
    else:
        value = int(value)
        if (value <= 10):
            output += 'BitLate'
        elif (value <= 30):
            output += 'MediumLate'
        elif (value <= 90):
            output += 'MuchLate'

    return output


def weeklyClient(day):

    pass


def Main():
    logger = PrintLogger(Severity.NOTICE)
    log = Log('Start', Severity.NOTICE)
    logger.log(log)

    # Vent preprocessing
    # pre = GenericPreprocessor(PATH, ';', colOfInterest,
    #     getState, logger)
    # Load preprocessor
    # pre = GenericPreprocessor(PATH_LOAD, ',', LOAD_colOfInterest,
        # LOAD_getState, logger)
    # Absens
    pre = GenericPreprocessor(PATH_ABSENS, ',', ABSENS_cols,
        absens_getState, logger)

    pre.__getClientSequenceData__ = weeklyClient

    mdb, skippedDays = pre.GenerateTemporalMdb()

    # Generating and computing support for states
    supportList = Support.GenerateStateSupportList(mdb)

    # Set support variables
    minSupport = 0.2
    maxGap = pa.to_timedelta('24:00:00')  # hh:mm:ss

    # TPMiner Call


    # Armada Call
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)
    frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)

    log = Log('Frequent states removed', Severity.INFO)
    logger.log(log)

    patterns = Armada(mdb, frequentStates, minSupport, maxGap, logger)

    # Print last 10 patterns
    helper.PrintNPatterns(18, patterns)
    helper.PrintResults(minSupport, maxGap, patterns, skippedDays, frequentStates, PATH)

    # Display the number of different patterns
    count = helper.CountNPatterns(patterns)
    helper.PrintPatternCount(count)


if __name__ == '__main__':
    Main()
