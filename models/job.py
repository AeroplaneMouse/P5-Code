from time import perf_counter
import pandas as pa
from models.result import Result
from logging2 import Log, Severity
from exceptions import *
from preprocessors import Support
from preprocessors.Generic import GenericPreprocessor


class Job:
    algorithm = None
    dataset = None
    getState = None
    columns = None
    results = None
    minSupport = None
    maxGap = None
    preprocessor = None
    label = None

    def __init__(self, seperator=',', logger=None, label=""):
        self.seperator = seperator
        self.logger = logger
        self.label = label

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

    def __log(self, log):
        if self.logger is not None:
            self.logger.log(log)

    def run(self):
        # Check preprocessor
        if self.preprocessor == None:
            self.__log(Log('No preprocessor', Severity.ERROR))
            return Result(self.minSupport, self.maxGap, errors=['No preprocessor'])

        self.__log(Log('Starting algorithm: {}'.format(self.algorithm.__name__), Severity.INFO))

        t0 = perf_counter()
        mdb, skippedDays = self.preprocessor.GenerateTemporalMdb()
        preTime = perf_counter() - t0

        t0 = perf_counter()
        results = self.algorithm(mdb, self.logger, self.minSupport, self.maxGap)
        results.algorithmTime = perf_counter() - t0

        results.skippedDays = skippedDays
        results.dataset = self.dataset
        results.preprocessingTime = preTime
        results.job = self

        self.results = results
        return self.results
