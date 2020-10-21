from preprocessors.Vent import VentPreprocessor
from preprocessors.FindSupport import GenerateStateSupportList
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
    # Preprocessing
    vent = VentPreprocessor('datasets/vent-minute-short.csv', ';')
    mdb = vent.GenerateTemporalMdb()

    # Generating and computing support for states
    supportList = GenerateStateSupportList(mdb)

    # Clear the database of states not meeting the minimum support
    minSupport = 0.7

    for s in supportList:
        print(s)

    # minSup = 0.7
    # cs = RemoveLowSup(minSup, supList, cs)
    # mdb = SplitDataframe(cs)

    # # print(supList)
    # #Run Armada
    # Armada(mdb, supList).Run(minSup)

    # print(cs)

if __name__ == '__main__':
    Main()
