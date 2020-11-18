import pandas as pa
import testSuite as t
from preprocessors import Support
from algorithms.tpminer import tpminer
from preprocessors.Preprocessor import GenericPreprocessor


#####################################################
# Setup

PATH = 'datasets/vent-minute-short.csv'
colOfInterest = [
    'Vent_HRVTempExhaustOut',
    'Vent_HRVTempOutdoorin',
    'Vent_HRVTempReturnIn',
    'Vent_HRVTempSupplyOut']

# mdb = t.GenerateMdb()


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


def Test_TDBtoEndpoint():
    # Preprocessing
    pre = GenericPreprocessor(PATH, ';', colOfInterest, getState)
    mdb, skippedDays = pre.GenerateTemporalMdb()

    endpointSeqs = tpminer.TDBToEndpointSequenceList(mdb)

    for eSeq in endpointSeqs:
        for e in eSeq:
            print(e)
        print('#'*30)


print('********************')
print('Testing TDBasda sd.py')
print()

Test_TDBtoEndpoint()
