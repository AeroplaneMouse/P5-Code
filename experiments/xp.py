import time
import _thread
# import threading
from models.job import Job
from experiments import armada
from logging import FileLogger, MultiLogger, Log, Severity


def startWorkerThreads(jobs, rLock, logger, results):
    N_THREADS = len(jobs)
    locks = [_thread.allocate_lock() for i in range(N_THREADS)]
    threads = []

    for i in range(N_THREADS):
        t = _thread.start_new_thread(helper, (
            logger,
            i,
            locks[i],
            rLock,
            jobs[i],
            results))
        threads.append(t)

    return threads, locks


def shitMultithreading(jobs, logger):
    rLock = _thread.allocate_lock()
    results = []

    threads, locks = startWorkerThreads(jobs, rLock, logger, results)

    # Waiting on threads to start
    started = False
    while not started:
        time.sleep(0.5)
        count = 0
        for l in locks:
            if l.locked():
                count += 1

        # Exit when all threads has started
        started = count == len(locks)

    # Waiting for threads to exit
    while started:
        time.sleep(1)
        count = 0
        for l in locks:
            if l.locked():
                count += 1

        # Exit when all threads has exited
        started = count == len(locks)

    return results


def helper(logger, id, lock, rLock, job, results):
    with lock:
        logger.log(Log('Starting thread-'+str(id), Severity.INFO))

        result = job.run()

        # Save results
        with rLock:
            results.append(result)

        logger.log(Log('Exiting thread-'+str(id), Severity.INFO))



def run(logger):
    MULTITHREAD = False
    fLog = FileLogger(Severity.NOTICE, 'experiment_results.log')
    fLog.INSERT_TIMESTAMP = True
    mLog = MultiLogger([fLog, logger])


    if MULTITHREAD:
        jobs = armada.initializeJobs()
        results = shitMultithreading(jobs, logger)

        for result in results:
            result.print(mLog)
    else:
        jobs = armada.initializeJobs(mLog)

        results = []
        for job in jobs:
            res = job.run()
            results.append(res)
            res.print(fLog)


    logger.log(Log('Exiting Thread-Main', Severity.INFO))
