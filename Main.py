import sys
import resultPrinting
import pandas as pa
from models.job import Job
from methods import *
from logging import *
from preprocessors import Support
from algorithms.tpminer import tpminer
from algorithms.armada.Armada import Armada
from preprocessors.Preprocessor import GenericPreprocessor
from preprocessors.loadData import goodColumns as LOAD_colOfInterest


PATH = 'datasets/vent-minute.csv'
PATH_LOAD = 'datasets/Load-minute.csv'

def processArguemnts(args):
    job = Job()

    # No arguments given. Use default settings
    if len(args) == 1:
        job.algorithm = None
        job.getState = None
        job.dataset = 'datasets/vent-minute.csv'
        job.columns = [
            'Vent_HRVTempExhaustOut',
            'Vent_HRVTempOutdoorin',
            'Vent_HRVTempReturnIn',
            'Vent_HRVTempSupplyOut']
        job.seperator = ';'
        job.minSupport = 0.5


    else:
        for arg in args:
            print(arg)

    return job


def armada(mdb, supportList, logger, minSupport, maxGap):
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)
    frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)

    log = Log('Frequent states removed', Severity.INFO)
    logger.log(log)

    patterns = Armada(mdb, frequentStates, minSupport, maxGap, logger)


def Main():
    # Starting the logger
    logger = PrintLogger(Severity.INFO)
    log = Log('Start', Severity.NOTICE)
    logger.log(log)

    # The number of arguments
    # len(sys.argv)
    # fileName = sys.argv[0] # File name
    # firstArgument = sys.argv[1] # First argument

    # job = processArguments(sys.argv)
    # job.logger = logger

    job = Job(logger=logger)

    # Settings
    job.algorithm = armada
    job.seperator = ';'
    job.dataset = 'datasets/vent-minute.csv'
    job.columns = vent_columns
    job.getState = vent_getState
    job.minSupport = 0.5
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    patterns = job.run()

    resultPrinting.PrintResults(
        job.minSupport,
        job.maxGap,
        patterns,
        [], [],
        job.dataset)

    # Display the number of different patterns
    count = resultPrinting.CountNPatterns(patterns)
    resultPrinting.PrintPatternCount(count)

    return
    # Vent preprocessing
    pre = GenericPreprocessor(PATH, ';', colOfInterest,
        getState, logger)
    # Load preprocessor
    # pre = GenericPreprocessor(PATH_LOAD, ',', LOAD_colOfInterest,
        # LOAD_getState, logger)

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

    log = Log('Frequent states removed', Severity.INFO)
    logger.log(log)

    patterns = Armada(mdb, frequentStates, minSupport, maxGap, logger)

    # Print last 10 patterns
    resultPrinting.PrintNPatterns(10, patterns)
    resultPrinting.PrintResults(minSupport, maxGap, patterns, skippedDays, frequentStates, PATH)

    # Display the number of different patterns
    count = resultPrinting.CountNPatterns(patterns)
    resultPrinting.PrintPatternCount(count)


if __name__ == '__main__':
    Main()
