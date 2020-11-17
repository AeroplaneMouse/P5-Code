from preprocessors.Preprocessor import GenericPreprocessor
from preprocessors import Support
from algorithms.armada import MineIndexSet
from algorithms.armada import Storage
from mocks import IndexSets
import pandas as pa
import testSuite


#####################################################################
# Setup
PATH = 'datasets/vent-minute-short.csv'
colOfInterest = [
    'Vent_HRVTempExhaustOut',
    'Vent_HRVTempOutdoorin',
    'Vent_HRVTempReturnIn',
    'Vent_HRVTempSupplyOut']


def getState(value, columnName):
    # Convert name to number
    columnName = colOfInterest.index(columnName)

    INTERVAL = 5
    # Compute distance to range start
    r = value % INTERVAL

    # Compute range start and end
    rangeStart = value - r
    rangeEnd = rangeStart + INTERVAL

    return '{}_{:.0f}->{:.0f}'.format(
        columnName,
        rangeStart,
        rangeEnd)

# Preprocessing
pre = GenericPreprocessor(PATH, ';', colOfInterest, getState)
mdb, skippedDays = pre.GenerateTemporalMdb()

# Generating and computing support for states
supportList = Support.GenerateStateSupportList(mdb)

# Setting support variables
minSupport = 0.7
maxGap = pa.to_timedelta('24:00:00')  # hh:mm:ss

mdb = Support.RemoveNonSupported(minSupport, supportList, mdb)

Storage.MDB = mdb
Storage.MinimumSupport = minSupport


#####################################################################
# Tests
def Test_ComputePotentialStems():
    # Setup
    a = IndexSets.A
    minSup = 0.7
    maxGap = pa.to_timedelta('24:00:00')

    stems = MineIndexSet.ComputePotentialStems(a, minSup, maxGap)


    return


print('********************')
print('Testing ComputePotentialStems')
print()

# Test_ComputePotentialStems()
