import testSuite as t
from preprocessors.Preprocessor import GenericPreprocessor

CSV_PATH = 'tests/TestSet.csv'
COLUMNS = ['Test1', 'Test2', 'Test3', 'Test4']
EXPECTED_CS_LENGTH = 9
EXPECTED_SKIPPED = 3 + 9 + 9


def getState(value, columnName):
    if (value == '1' or value == 1):
        return '{}_{}'.format(columnName, value)
    else:
        return None


def Test_ReturnCorrectNumberOfClients():
    pre = GenericPreprocessor(CSV_PATH, ',', COLUMNS, getState)
    mdb, skippedDays = pre.GenerateTemporalMdb()

    output = len(mdb)

    m = 'Return correct number of clients: Got[{}] expected[{}]'.format(
        output,
        EXPECTED_CS_LENGTH)
    t.test(output == EXPECTED_CS_LENGTH, m)


def Test_SkipEmptyDays():
    pre = GenericPreprocessor(CSV_PATH, ',', COLUMNS, getState)
    mdb, skippedDays = pre.GenerateTemporalMdb()
    output = len(skippedDays)

    m = 'Skipped empty days: [{} | {}]'.format(
        output,
        EXPECTED_SKIPPED)

    t.test(output == EXPECTED_SKIPPED, m)


print('********************')
print('Testing Generic preprocessor.py')
print()

Test_ReturnCorrectNumberOfClients()

Test_SkipEmptyDays()
