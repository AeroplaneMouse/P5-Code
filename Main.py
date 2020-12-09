import pandas as pa
from methods import *
from logging2 import *
from models.job import Job
from models.result import Result
from preprocessors import columns as col
from preprocessors.Generic import GenericPreprocessor
from experiments import xp
import pdb, traceback, sys


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
    job.algorithm = tpminer
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
    job.algorithm = tpminer
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
