from preprocessors.Load import LoadPreprocessor
from preprocessors import Support, loadData
from preprocessors.Preprocessor import GenericPreprocessor
from algorithms.armada.Armada import Armada
import pandas as pa
import helper


def getState(value, columnName):
    if (value == '1' or value == 1):
        return 'ON'
    else:
        return None


# PATH = 'datasets/Load-minute.csv'
PATH = 'datasets/Load-minute-short.csv'

colOfInterest = loadData.goodColumns

pre = GenericPreprocessor(PATH, ',', colOfInterest, getState)
mdb, skippedDays = pre.GenerateTemporalMdb()

supportList = Support.GenerateStateSupportList(mdb)

# Clear the database of states not meeting the minimum support
minSupport = 0.7
maxGap = pa.to_timedelta('24:00:00')  # hh:mm:ss
mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)

frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)

patterns = Armada(mdb, frequentStates, minSupport, maxGap)

# Count the number of different patterns
count = helper.CountNPatterns(patterns)

# Print last 10 patterns
helper.PrintNPatterns(n=10, patterns=patterns)

helper.PrintResults(minSupport, maxGap, patterns, skippedDays, PATH)

# Print number of different patterns
helper.PrintPatternCount(count)
