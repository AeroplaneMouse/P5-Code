from preprocessors.Vent import VentPreprocessor
from preprocessors import Support
from algorithms.armada.MineIndexSet import MineIndexSet, ComputePotentialStems
from algorithms.armada import Storage
from mocks import IndexSets
import pandas as pa


# Preprocessing
vent = VentPreprocessor('datasets/vent-minute-short.csv', ';')
mdb = vent.GenerateTemporalMdb()

# Generating and computing support for states
supportList = Support.GenerateStateSupportList(mdb)

# Clear the database of states not meeting the minimum support
minSupport = 0.7
mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)

Storage.MDB = mdb


print('********************')
print('Testing ComputePotentialStems')
print()


stems = ComputePotentialStems(indexSet=IndexSets.A, frequentStates=None, minSup=0.7)

print()
print('New stems:')
for s in stems:
    print(s)
