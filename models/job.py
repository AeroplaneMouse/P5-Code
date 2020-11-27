from preprocessors.Preprocessor import GenericPreprocessor
from exceptions import *


class Job:
    def __init__(self, seperator=',', logger=None):
        self.algorithm = None
        self.dataset = None
        self.seperator = seperator
        self.logger = logger
        self.columns = []
        self.getState = None
        self.results = None

    def useGenericPreprocessor(self):
        # raise


        self.preprocessor = GenericPreprocessor(
            self.dataset,
            self.seperator,
            self.columns,
            self.getState,
            self.logger)

    def run():
        pass
