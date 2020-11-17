from preprocessors.Preprocessor import GenericPreprocessor
from preprocessors import Support
from algorithms.armada.Armada import Armada
from algorithms.tpminer import tpminer
import pandas as pa
import helper


PATH = 'datasets/vent-minute.csv'
colOfInterest = [
    'Vent_HRVTempExhaustOut',
    'Vent_HRVTempOutdoorin',
    'Vent_HRVTempReturnIn',
    'Vent_HRVTempSupplyOut']


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


def Main():
    # Preprocessing
    pre = GenericPreprocessor(PATH, ';', colOfInterest, getState)
    mdb, skippedDays = pre.GenerateTemporalMdb()

    # Generating and computing support for states
    supportList = Support.GenerateStateSupportList(mdb)

    # Set support variables
    minSupport = 0.6
    maxGap = pa.to_timedelta('24:00:00')  # hh:mm:ss

    # TPMiner Call


    # Armada Call
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)
    frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)
    patterns = Armada(mdb, frequentStates, minSupport, maxGap)

    # Print last 10 patterns
    helper.PrintNPatterns(10, patterns)
    helper.PrintResults(minSupport, maxGap, patterns, skippedDays, frequentStates, PATH)

    # Display the number of different patterns
    count = helper.CountNPatterns(patterns)
    helper.PrintPatternCount(count)


if __name__ == '__main__':
    Main()
