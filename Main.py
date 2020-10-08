import pandas as pa
import numpy as np
from preprocessors.vent import VentPreprocessor
from findSupport import MakeStateSupportList, FindSupport

def Main():
    # Create preprocessor
    vent = VentPreprocessor()
    vent.CreateDataFrame('datasets/vent-minute-short.csv', ';')

    temporalVent = vent.GetTemporalDataFrame()
    list = MakeStateSupportList(temporalVent)

    FindSupport(temporalVent, list)

    for l in list:
        print(l)

if __name__ == '__main__':
    Main()
