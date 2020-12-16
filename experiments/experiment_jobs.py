import pandas as pa
from logging2 import FileLogger, Severity
from methods import *
from models.job import Job
from preprocessors.columns import vent_columns


min_5_seq_6 = Job(label='min_5_seq_6')
min_5_seq_6.minSupport = 0.05
min_5_seq_6.dataset = 'datasets/Vent-minute-6.csv'

min_4_seq_6 = Job(label='min_4_seq_6')
min_4_seq_6.minSupport = 0.04
min_4_seq_6.dataset = 'datasets/Vent-minute-6.csv'

min_3_seq_6 = Job(label='min_3_seq_6')
min_3_seq_6.minSupport = 0.03
min_3_seq_6.dataset = 'datasets/Vent-minute-6.csv'

min_2_seq_6 = Job(label='min_2_seq_6')
min_2_seq_6.minSupport = 0.02
min_2_seq_6.dataset = 'datasets/Vent-minute-6.csv'

min_1_seq_6 = Job(label='min_1_seq_6')
min_1_seq_6.minSupport = 0.01
min_1_seq_6.dataset = 'datasets/Vent-minute-6.csv'



min_5_seq_12 = Job(label='min_5_seq_12')
min_5_seq_12.dataset = 'datasets/Vent-minute-12.csv'
min_5_seq_12.minSupport = 0.05

min_5_seq_9 = Job(label='min_5_seq_9')
min_5_seq_9.dataset = 'datasets/Vent-minute-9.csv'
min_5_seq_9.minSupport = 0.05

min_5_seq_6 = Job(label='min_5_seq_6')
min_5_seq_6.dataset = 'datasets/Vent-minute-6.csv'
min_5_seq_6.minSupport = 0.05

min_5_seq_3 = Job(label='min_5_seq_3')
min_5_seq_3.dataset = 'datasets/Vent-minute-3.csv'
min_5_seq_3.minSupport = 0.05


def initializeJobs(algorithm, logger=None):
    allJobs = []

    # allJobs.append(min_5_seq_12)
    # allJobs.append(min_5_seq_9)
    # allJobs.append(min_5_seq_6)
    # allJobs.append(min_5_seq_3)

    # allJobs.append(min_5_seq_6)
    # allJobs.append(min_4_seq_6)
    # allJobs.append(min_3_seq_6)
    allJobs.append(min_2_seq_6)
    # allJobs.append(min_1_seq_6)

    for job in allJobs:
        job.algorithm = algorithm
        job.getState = vent_getState
        job.columns = vent_columns
        job.maxGap = pa.to_timedelta('24:00:00')

        # Create independent file logger
        # fLog = FileLogger(Severity.INFO, job.label+'.log')
        # fLog.INSERT_TIMESTAMP = True

        # Combine independent filelogger with global logger
        # mLog = MultiLogger([logger, fLog])
        job.logger = logger

        # if logger is None:
        # else:
        #     job.logger = logger

        job.useGenericPreprocessor()


    return allJobs
