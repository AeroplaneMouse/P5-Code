from preprocessors.vent import VentPreprocessor, SplitDataframe
from findSupport import MakeStateSupportList, ComputeSupport
from algorithms.armada.Armada import Armada


# Check if a state name is in suplist
def Contains(state, supList):
    for supState in supList:
        if supState.StateName == state:
            return True

    return False


def RemoveLowSup(minSup, supList, cs):
        # Clear supList for states below minSup
    for i in reversed(range(0, len(supList))):
        if supList[i].Support < minSup:
            del supList[i]

    # Clear cs for states not in supList
    for i in reversed(range(0, len(cs))):
        singleCS = cs.iloc[i]

        if not Contains(singleCS.State, supList):
            cs = cs.drop(i)

    return cs


def Main():
    # Create preprocessor
    vent = VentPreprocessor()
    vent.InitializeDataFrame('datasets/vent-minute-short.csv', ';')

    # Create CS and compute support
    cs = vent.GenerateTemporalDataFrame()
    supList = MakeStateSupportList(cs)
    ComputeSupport(cs, supList)

    minSup = 0.7
    cs = RemoveLowSup(minSup, supList, cs)
    mdb = SplitDataframe(cs)

    # print(supList)
    #Run Armada
    Armada(mdb, supList).Run(minSup)

    # print(cs)

if __name__ == '__main__':
    Main()
