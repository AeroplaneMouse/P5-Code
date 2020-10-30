from preprocessors.Vent import VentPreprocessor
from preprocessors import Support
from algorithms.armada.Armada import Armada
import pandas as pa


def Main():
    # Preprocessing
    vent = VentPreprocessor('datasets/vent-minute.csv', ';')
    mdb, skippedDays = vent.GenerateTemporalMdb(interval=5)

    # Generating and computing support for states
    supportList = Support.GenerateStateSupportList(mdb)

    # Clear the database of states not meeting the minimum support
    minSupport = 0.01
    maxGap = pa.to_timedelta('24:00:00')  # hh:mm:ss
    mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)

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
    print('# Minimum support: {:>21}'.format(minSupport))
    print('# Maximum gap: {:>25}'.format(str(maxGap)))
    print('# Patterns found: {:>22}'.format(len(patterns)))
    print('# Skipped days: {:>24}'.format(len(skippedDays)))


if __name__ == '__main__':
    Main()
