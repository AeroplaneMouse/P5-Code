import pandas as pa
from logging import FileLogger, Severity
from methods import *
from models.job import Job
from preprocessors.columns import vent_columns


min_5_seq_6 = Job(label='min_5_seq_6')
min_5_seq_6.minSupport = 0.05

min_4_seq_6 = Job(label='min_4_seq_6')
min_4_seq_6.minSupport = 0.04

min_3_seq_6 = Job(label='min_3_seq_6')
min_3_seq_6.minSupport = 0.03

min_2_seq_6 = Job(label='min_2_seq_6')
min_2_seq_6.minSupport = 0.02

min_1_seq_6 = Job(label='min_1_seq_6')
min_1_seq_6.minSupport = 0.01



min_5_seq_12 = Job(label='min_5_seq_12')
min_5_seq_12.dataset = 'datasets/Vent-minute-12.csv'

min_5_seq_9 = Job(label='min_5_seq_9')
min_5_seq_9.dataset = 'datasets/Vent-minute-9.csv'

min_5_seq_6 = Job(label='min_5_seq_6')
min_5_seq_6.dataset = 'datasets/Vent-minute-6.csv'

min_5_seq_3 = Job(label='min_5_seq_3')
min_5_seq_3.dataset = 'datasets/Vent-minute-3.csv'


def initializeJobs(logger=None):
    allJobs = []

    # 5_min support jobs
    jobs_min_5 = [
        min_5_seq_12,
        min_5_seq_9,
        min_5_seq_6,
        min_5_seq_3
    ]
    for job in jobs_min_5:
        job.minSupport = 0.05
        allJobs.append(job)

    # 6_sequence jobs
    jobs_seq_6 = [
        min_5_seq_6,
        min_4_seq_6,
        min_3_seq_6,
        min_2_seq_6,
        min_1_seq_6
    ]
    for job in jobs_seq_6:
        job.dataset = 'datasets/Vent-minute-6.csv'
        allJobs.append(job)


    for job in allJobs:
        job.algorithm = armada
        job.getState = vent_getState
        job.columns = vent_columns
        job.maxGap = pa.to_timedelta('24:00:00')

        if logger is None:
            fLog = FileLogger(Severity.INFO, job.label+'.log')
            fLog.INSERT_TIMESTAMP = True
            job.logger = fLog
        else:
            job.logger = logger

        job.useGenericPreprocessor()


    return allJobs
