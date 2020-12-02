import pandas as pa
from models.result import Result
from logging import Log, Severity
from exceptions import *
from preprocessors import Support
from preprocessors.Preprocessor import GenericPreprocessor


class Job:
    def __init__(self, seperator=',', logger=None):
        self.algorithm = None
        self.dataset = None
        self.getState = None
        self.seperator = seperator
        self.logger = logger
        self.columns = []
        self.results = None
        self.minSupport = 0.5
        self.maxGap = pa.to_timedelta('24:00:00')

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

        mdb, skippedDays = self.preprocessor.GenerateTemporalMdb()
        supportList = Support.GenerateStateSupportList(mdb)

        results = self.algorithm(mdb, supportList, self.logger, self.minSupport, self.maxGap)

        results.skippedDays = skippedDays
        results.path = self.dataset

        self.results = results
        return self.results
