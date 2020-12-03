from time import perf_counter
import pandas as pa
from models.result import Result
from logging import Log, Severity
from exceptions import *
from preprocessors import Support
from preprocessors.Preprocessor import GenericPreprocessor


class Job:
    algorithm = None
    dataset = None
    getState = None
    columns = None
    results = None
    minSupport = None
    maxGap = None
    preprocessor = None

    def __init__(self, seperator=',', logger=None):
        self.seperator = seperator
        self.logger = logger

    def useGenericPreprocessor(self):
        # Check properties
        if (self.algorithm is None
                or self.dataset is None
                or self.getState is None):
            raise ArgumentNotSetError('', 'One or more required properties has not been set')

        self.preprocessor = GenericPreprocessor(
            self.dataset,
            self.seperator,
            self.columns,
            self.getState,
            self.logger)

    def run(self):
        if self.logger is not None:
            log = Log('Starting algorithm: {}'.format(self.algorithm.__name__), Severity.INFO)
            self.logger.log(log)

        t0 = perf_counter()
        mdb, skippedDays = self.preprocessor.GenerateTemporalMdb()
        supportList = Support.GenerateStateSupportList(mdb)
        preTime = perf_counter() - t0


        t0 = perf_counter()
        results = self.algorithm(mdb, supportList, self.logger, self.minSupport, self.maxGap)
        results.algorithmTime = perf_counter() - t0

        results.skippedDays = skippedDays
        results.dataset = self.dataset
        results.preprocessingTime = preTime

        self.results = results
        return self.results
