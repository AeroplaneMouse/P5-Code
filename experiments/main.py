# import thread
# import threading
from models.job import Job
from experiments import armada
from logging import FileLogger, MultiLogger, Log, Severity


def run(logger):
    fLog = FileLogger(Severity.NOTICE, 'experiments.log')
    fLog.INSERT_TIMESTAMP = True
    mLog = MultiLogger([fLog, logger])

    jobs = armada.initializeJobs(mLog)
    results = []

    for job in jobs:
        result = job.run()
        results.append(result)
        result.print(mLog)

    # saveResults(results)

# def helper(list):

