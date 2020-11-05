from preprocessors.Load import LoadPreprocessor
from preprocessors import Support
from algorithms.armada.Armada import Armada
import pandas as pa

PATH = '../Datasets/Load-minute.csv'


load = LoadPreprocessor(PATH, ',')
mdb, skippedDays = load.GenerateTemporalMdb()

supportList = Support.GenerateStateSupportList(mdb)

# Clear the database of states not meeting the minimum support
minSupport = 0.01
maxGap = pa.to_timedelta('24:00:00')  # hh:mm:ss
mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)

frequentStates = Support.ExtractFrequentStates(minSupport, supportList, mdb)

patterns = Armada(mdb, frequentStates, minSupport, maxGap)

# Count the number of different patterns
count = {}
for p in patterns:
    pSize = len(p[0][1:])

    if pSize not in count:
        count[pSize] = 1
    else:
        count[pSize] += 1

# Print last 10 patterns
print('Last 10 patterns:')
i = len(patterns) - 9
for p in patterns[-10:]:
    print(i)
    print(p)
    print()
    i += 1

print('########################################')
print('# Minimum support: {:>21}'.format(minSupport))
print('# Maximum gap: {:>25}'.format(str(maxGap)))
print('# Patterns found: {:>22}'.format(len(patterns)))
print('# Skipped days: {:>24}'.format(len(skippedDays)))

# Print number of different patterns
print('#')
for key in count:
    print('# {:>2}-patterns: {:>25}'.format(
        key,
        count[key]))
