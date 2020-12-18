import pandas as pa
from methods import *
from logging2 import *
from models.job import Job
from models.result import Result
from preprocessors import columns as col
from preprocessors.Generic import GenericPreprocessor
from preprocessors.WeatherCrash import WeatherCrashPreprocessor
from experiments import xp
import pdb, traceback, sys


def armadaVentSetup(logger):
    job = Job(logger=logger, label='Armada main vent')
    job.algorithm = armada
    job.seperator = ','
    job.dataset = 'datasets/Vent-minute-short.csv'
    job.columns = col.vent_columns
    job.getState = vent_getState
    job.minSupport = 0.5
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job

def armadaWeatherSetup(logger):
    job = Job(logger=logger, label='Armada main weather-crash')
    job.algorithm = armada
    job.minSupport = 0.2
    job.maxGap = pa.to_timedelta('24:00:00')
    job.dataset = 'datasets/Weather-Crash.csv'
    preprocessor = WeatherCrashPreprocessor(
        'datasets/weather.csv',
        'datasets/Motor_Vehicle_Collisions_-_Crashes.csv',
        logger)
    job.preprocessor = preprocessor

    return job


def testSetup(logger):
    job = Job(logger=logger)
    job.algorithm = tpminer
    job.seperator = ','
    job.dataset = 'datasets/Vent-minute.csv'
    job.columns = col.vent_columns[:-1]
    job.getState = vent_getState
    job.minSupport = 0.1
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job


def tpminerVentSetup(logger):
    job = Job(logger=logger, label='TPMiner main vent')
    job.algorithm = tpminer
    job.seperator = ','
    job.dataset = 'datasets/Vent-minute-12.csv'
    job.columns = col.vent_columns
    job.getState = vent_getState
    job.minSupport = 0.1
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job

def tpminerLoadSetup(logger):
    job = Job(logger=logger, label='TPMiner load')
    job.algorithm = tpminer
    job.seperator = ','
    job.dataset = 'datasets/Load-minute-12.csv'
    job.columns = col.load_columns
    job.getState = load_getState
    job.minSupport = 0.5
    job.maxGap = pa.to_timedelta('24:00:00')

    job.useGenericPreprocessor()

    return job

def tpminerWeatherSetup(logger):
    job = Job(logger=logger, label='TPMiner weather-crash')
    job.algorithm = tpminer
    job.minSupport = 0.5
    job.maxGap = pa.to_timedelta('24:00:00')
    job.dataset = 'datasets/Weather-Crash.csv'
    preprocessor = WeatherCrashPreprocessor(
        'datasets/weather.csv',
        'datasets/Motor_Vehicle_Collisions_-_Crashes.csv',
        logger)
    job.preprocessor = preprocessor

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
                arResults.savePatterns('ARMADA_vent_Patterns.txt')

            elif(sys.argv[2] == 'weathercrash'):
                #ARMADA WEATHERCRASH
                arJob = armadaWeatherSetup(logger)
                arResults = arJob.run()
                arResults.print(logger)
                arResults.savePatterns('ARMADA_weather-crash_patterns.txt')
                pass
            else:
                print('These are not the datasets you are looking for.')

        elif(sys.argv[1] == 'tpminer'):
            if(sys.argv[2] == 'vent'):
                #TPMINER VENT
                tpJob = tpminerVentSetup(logger)
                tpResults = tpJob.run()
                tpResults.print(logger)
                tpResults.savePatterns('TP_vent_Patterns.txt')

            elif(sys.argv[2] == 'test'):
                #TPMINER VENT\
                tpJob = testSetup(logger)
                tpResults = tpJob.run()
                tpResults.print(logger)
                tpResults.savePatterns('TP_vent_TestPatterns.txt')

            elif sys.argv[2] == 'load':
                tpJob = tpminerLoadSetup(logger)
                tpResults = tpJob.run()
                tpResults.print(logger)
                tpResults.savePatterns('TP_load_TestPatterns.txt')

            elif(sys.argv[2] == 'weathercrash'):
                tpJob = tpminerWeatherSetup(logger)
                tpResults = tpJob.run()
                tpResults.print(logger)
                tpResults.savePatterns('TP_Weather-Crash_Patterns.txt')

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
