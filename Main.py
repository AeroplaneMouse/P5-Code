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
    maxGap = pa.to_timedelta('04:00:00')  # hh:mm:ss
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)

    print(mdb)
    import pdb; pdb.set_trace()  # breakpoint c6b86b0d //

    frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)

    patterns = Armada(mdb, frequentStates, minSupport, maxGap)

    # Print last 10 patterns
    print('Last 10 patterns:')
    i = len(patterns) - 9
    for p in patterns[-10:]:
        print(i)
        print(p)
        print()
        i += 1
    print('########################')
    print('# Minimum support: {:>5}'.format(minSupport))
    print('# Patterns found: {:>6}'.format(len(patterns)))


if __name__ == '__main__':
    Main()
