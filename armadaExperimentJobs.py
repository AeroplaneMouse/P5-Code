import pandas as pa
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



def getAllArmadaExperiments(logger):
    # 6 sequence jobs
    jobs_seq_6 = [
        min_5_seq_6,
        min_4_seq_6,
        min_3_seq_6,
        min_2_seq_6,
        min_1_seq_6
    ]
    for job in jobs_seq_6:
        job.algorithm = armada
        job.dataset = 'datasets/Vent-minute-6.csv'
        job.getState = vent_getState
        job.columns = vent_columns
        job.maxGap = pa.to_timedelta('24:00:00')
        job.logger = logger
        job.useGenericPreprocessor()

    return jobs_seq_6
