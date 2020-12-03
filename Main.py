import sys
import pandas as pa
from models.job import Job
from models.result import Result
from methods import *
from logging import *
from preprocessors import Support, columns as col
from algorithms.tpminer import tpminer
from algorithms.tpminer.tpminer_main import tpminer_main
from algorithms.armada.Armada import Armada
from preprocessors.Preprocessor import GenericPreprocessor
from armadaExperimentJobs import getAllArmadaExperiments


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


def tpminer_stu(mdb, supportList, logger, minSupport, maxGap):
    patternSets = tpminer_main(mdb, minSupport, logger)

    # Convert set to list
    patterns = []
    for p in patternSets:
        patterns.append(p)

    return Result(minSupport, maxGap, patterns, [])


def armadaSetup(logger):
    job = Job(logger=logger)
    job.algorithm = armada
    job.seperator = ','
    job.dataset = 'datasets/Vent-minute.csv'
    job.columns = col.vent_columns
    job.getState = vent_getState
    job.minSupport = 0.5
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job


def tpminerSetup(logger):
    job = Job(logger=logger)
    job.algorithm = tpminer_stu
    job.seperator = ','
    job.dataset = 'datasets/Vent-minute-short.csv'
    job.columns = col.vent_columns
    job.getState = vent_getState
    job.minSupport = 0.5
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job


def runExperiments(logger):
    jobs = getAllArmadaExperiments(logger)
    results = []

    for job in jobs:
        result = job.run()
        results.append(result)
        result.print()

    # with open('result.log', 'w') as f:



def Main():
    # Logger setup
    logger = PrintLogger(Severity.INFO)
    log = Log('Start', Severity.NOTICE)
    logger.log(log)

    # job = processArguments(sys.argv)
    # job.logger = logger

    # runExperiments(logger)
    # return

    # Setup
    arJob = armadaSetup(logger)
    # tpJob = tpminerSetup(logger)

    # Run jobs
    arResults = arJob.run()
    # tpResults = tpJob.run()

    # View results
    arResults.print()
    # tpResults.print()



if __name__ == '__main__':
    Main()
