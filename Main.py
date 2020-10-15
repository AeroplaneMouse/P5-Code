from preprocessors.vent import VentPreprocessor
from findSupport import MakeStateSupportList, ComputeSupport
from algorithms.armada.Armada import Armada

import numpy as np

def Main():
    # Create preprocessor
    vent = VentPreprocessor()
    vent.InitializeDataFrame('datasets/vent-minute-short.csv', ';')

    cs = vent.GenerateTemporalDataFrame()
    supList = MakeStateSupportList(cs)
    ComputeSupport(cs, supList)

    Armada(cs, supList).Run(0.7)


if __name__ == '__main__':
    Main()
