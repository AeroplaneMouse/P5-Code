import sys
import pandas as pa
from models.job import Job
from models.result import Result
from methods import *
from logging import *
from preprocessors import Support, columns as col
from algorithms.tpminer import tpminer
from algorithms.armada.Armada import Armada
from preprocessors.Preprocessor import GenericPreprocessor


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

    return Result(minSupport, maxGap, patterns, frequentStates)


def setup(logger):
    job = Job(logger=logger)
    job.algorithm = armada
    job.seperator = ';'
    job.dataset = 'datasets/vent-minute.csv'
    job.columns = col.vent_columns
    job.getState = vent_getState
    job.minSupport = 0.5
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job


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

    # Setup
    job = setup(logger)

    # Run
    results = job.run()

    # View results
    results.print()



if __name__ == '__main__':
    Main()
