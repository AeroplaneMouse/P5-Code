import pandas as pa
import numpy as np
from preprocessors.vent import VentPreprocessor

def Main():
    # Create preprocessor
    vent = VentPreprocessor()
    vent.CreateDataFrame('datasets/vent-minute-short.csv', ';')

    temporalVent = vent.GetTemporalDataFrame()


if __name__ == '__main__':
    Main()
