from preprocessors.Vent import VentPreprocessor
from preprocessors import Support
from algorithms.armada.Armada import Armada


def Main():
    # Preprocessing
    vent = VentPreprocessor('datasets/vent-minute-short.csv', ';')
    mdb = vent.GenerateTemporalMdb()

    # Generating and computing support for states
    supportList = Support.GenerateStateSupportList(mdb)

    # Clear the database of states not meeting the minimum support
    minSupport = 0.7
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)

    print(mdb)

    # #Run Armada
    # Armada(mdb, supList).Run(minSup)

    # print(cs)

if __name__ == '__main__':
    Main()
