import sys
from preprocessors.vent import VentPreprocessor
from findSupport import MakeStateSupportList, ComputeSupport
from algorithms.armada.Armada import Armada


def Main(mainPath):
    # Create preprocessor
    path = mainPath + 'datasets/vent-minute-short.csv'
    vent = VentPreprocessor()
    vent.InitializeDataFrame(path, ';')

    # Create CS and compute support
    cs = vent.GenerateTemporalDataFrame()
    supList = MakeStateSupportList(cs)
    ComputeSupport(cs, supList)

    # Run Armada
    Armada(cs, supList).Run(0.7)



if __name__ == '__main__':
    # Change \ to /
    path = sys.argv[0].replace('\\', '/')
    # Remove Main.py
    path = path[:-7]
    Main(path)
