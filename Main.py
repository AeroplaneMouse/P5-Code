from preprocessors.vent import VentPreprocessor
from findSupport import MakeStateSupportList, ComputeSupport
from algorithms.armada.Armada import Armada


def Main():
    # Create preprocessor
    vent = VentPreprocessor()
    vent.InitializeDataFrame('datasets/vent-minute-short.csv', ';')

    # Create CS and compute support
    cs = vent.GenerateTemporalDataFrame()
    supList = MakeStateSupportList(cs)
    ComputeSupport(cs, supList)

    # Run Armada
    Armada(cs, supList).Run(0.7)


if __name__ == '__main__':
    Main()
