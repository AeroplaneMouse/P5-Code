from preprocessors.Vent import VentPreprocessor
from preprocessors import Support
from algorithms.armada.Armada import Armada
from algorithms.armada.Armada import Armada_Deprecated


def Main():
    # Preprocessing
    vent = VentPreprocessor('datasets/vent-minute-shorter.csv', ';')
    mdb = vent.GenerateTemporalMdb()

    # Generating and computing support for states
    supportList = Support.GenerateStateSupportList(mdb)

    # Clear the database of states not meeting the minimum support
    minSupport = 0.3
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)

    frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)
    
    Armada(mdb, frequentStates, minSupport)
    
    # #Run Armada
    #Armada_Deprecated(mdb, supportList).Run(minSupport)

    # print(cs)

if __name__ == '__main__':
    Main()
