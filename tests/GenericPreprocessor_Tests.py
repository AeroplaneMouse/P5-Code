import pandas as pa
import testSuite as t
from logging2 import *
from preprocessors.Generic import GenericPreprocessor

CSV_PATH = 'tests/TestSet.csv'
COLUMNS = ['Test1', 'Test2', 'Test3', 'Test4']
EXPECTED_CS_LENGTH = 9
EXPECTED_SKIPPED = 3 + 9 + 9

logger = PrintLogger(Severity.ERROR)

def getState(value, columnName):
    if (value == '1' or value == 1):
        return columnName + '_1'
    else:
        return None


def Test_ReturnCorrectNumberOfClients():
    pre = GenericPreprocessor(CSV_PATH, ',', COLUMNS, getState, logger)
    mdb, skippedDays = pre.GenerateTemporalMdb()

    output = len(mdb)

    m = 'Return correct number of clients: Got[{}] expected[{}]'.format(
        output,
        EXPECTED_CS_LENGTH)
    t.test(output == EXPECTED_CS_LENGTH, m)


def Test_SkipEmptyDays():
    pre = GenericPreprocessor(CSV_PATH, ',', COLUMNS, getState, logger)
    mdb, skippedDays = pre.GenerateTemporalMdb()
    output = len(skippedDays)

    m = 'Skipped empty days: [{} | {}]'.format(
        output,
        EXPECTED_SKIPPED)

    t.test(output == EXPECTED_SKIPPED, m)


def Test_singleDayClientSequence_returns_correct_amount_of_data():
    pre = GenericPreprocessor(CSV_PATH, ',', COLUMNS, getState, logger)
    mdb, skippedDays = pre.GenerateTemporalMdb()

    data = mdb[0]
    expected = {
        'ClientID': 0,
        'State': 'Test1_1',
        'Start': pa.to_datetime('2013-07-01 00:07:00'),
        'End': pa.to_datetime('2013-07-01 00:30:00')}


    # Compare output with expected
    result = True
    for col in data.columns:
        if (data.at[0, col] != expected[col]):
            result = False
            break

    t.test(result, 'Default singleDayClientSequence return correct data')


print('********************')
print('Testing Generic preprocessor.py')
print()

Test_ReturnCorrectNumberOfClients()
Test_SkipEmptyDays()
Test_singleDayClientSequence_returns_correct_amount_of_data()
