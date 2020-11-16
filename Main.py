from preprocessors.Vent import VentPreprocessor
from preprocessors import Support
from algorithms.armada.Armada import Armada
from algorithms.tpminer import tpminer
import pandas as pa
import helper

PATH = 'datasets/vent-minute.csv'


def Main():
    # Preprocessing
    vent = VentPreprocessor(PATH, ';')
    mdb, skippedDays = vent.GenerateTemporalMdb(interval=5)

    # Generating and computing support for states
    supportList = Support.GenerateStateSupportList(mdb)

    # Clear the database of states not meeting the minimum support
    minSupport = 0.6
    maxGap = pa.to_timedelta('24:00:00')  # hh:mm:ss
 
    # TPMiner Call
    
 
    # Armada Call
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)
    frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)
    patterns = Armada(mdb, frequentStates, minSupport, maxGap)

    # Count the number of different patterns
    count = helper.CountNPatterns(patterns)

    # Print last 10 patterns
    helper.PrintNPatterns(10, patterns)
    helper.PrintResults(minSupport, maxGap, patterns, skippedDays, PATH)

    helper.PrintPatternCount(count)


if __name__ == '__main__':
    Main()
