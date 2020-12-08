import sys
import pandas as pa
from models.job import Job
from models.result import Result
from methods import *
from logging2 import *
from preprocessors import Support, columns as col
from algorithms.tpminer import tpminer
from algorithms.tpminer.tpminer_main import tpminer_main
from algorithms.armada.Armada import Armada
from preprocessors.Generic import GenericPreprocessor
from experiments import xp
import pdb, traceback, sys

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


def armadaVentSetup(logger):
    job = Job(logger=logger)
    job.algorithm = armada
    job.seperator = ','
    job.dataset = 'datasets/Vent-minute-short.csv'
    job.columns = col.vent_columns
    job.getState = vent_getState
    job.minSupport = 0.7
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job


def testSetup(logger):
    job = Job(logger=logger)
    job.algorithm = tpminer_stu
    job.seperator = ','
    job.dataset = 'datasets/Vent-minute.csv'
    job.columns = col.vent_columns[:-1]
    job.getState = vent_getState
    job.minSupport = 0.7
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job


def tpminerVentSetup(logger):
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

    

def Main():
    # Logger setup
    logger = PrintLogger(Severity.INFO)
    # logger = FileLogger(Severity.INFO, 'test.log')
    logger.INSERT_TIMESTAMP = True
    log = Log('Start', Severity.NOTICE)
    logger.log(log)

    # job = processArguments(sys.argv)
    # job.logger = logger

    if len(sys.argv) > 1 and (sys.argv[1] == '-e' or sys.argv == '--experiments'):
        xp.run(logger)
    elif len(sys.argv) == 3:        
        if(sys.argv[1] == 'armada'):
            if(sys.argv[2] == 'vent'):
                #ARMADA VENT
                arJob = armadaVentSetup(logger)
                arResults = arJob.run()
                arResults.print(logger)
                
            elif(sys.argv[2] == 'weathercrash'):
                #ARMADA WEATHERCRASH
                pass
            else:
                print('These are not the datasets you are looking for.')
        
        elif(sys.argv[1] == 'tpminer'):
            if(sys.argv[2] == 'vent'):
                #TPMINER VENT
                tpJob = tpminerVentSetup(logger)
                tpResults = tpJob.run()
                tpResults.print()
                
            elif(sys.argv[2] == 'weathercrash'):
                #TPMINER WEATHERCRASH
                pass
                
            else:
                print('These are not the datasets you are looking for.')
            
        else:
            print('Dr. WrongArg or: The Dataset Which Never Was.')
                      
    else:
        print('Invalid Arguments.')


if __name__ == '__main__':
    try:
        Main()
    except:
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)
