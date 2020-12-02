import testSuite as t
from models.job import Job
from exceptions import *


########################################
# useGenericPreprocessor
def Test_useGenericPreprocessor_ThrowExceptionIfUsedPropertyIsNone_NoneProperty():
    job = Job()

    m = ''
    isCatched = False
    try:
        job.useGenericPreprocessor()
    except ArgumentNotSetError as e:
        isCatched = True
        m += e.argument
    except:
        pass


    m = ('\'useGenericPreprocessor\' catched none properties: '
        + 'The following is not set[{}]'.format(m))
    t.test(isCatched, m)


def Test_useGenericPreprocessor_ThrowExceptionIfUsedPropertyIsNone_CorrectProperty():

    m = '\'useGenericPreprocessor\' correct properties no error'
    t.test(False, m)


########################################
# Run
def Test_run_RemovesPreviousResults():

    m = '\'run\' removes previous run results'
    t.test(False, m)


def Test_run_ReturnsResultsOfRun():

    m = '\'run\' returns result'
    t.test(False, m)


def Test_run_SavesResultsInResult():

    m = '\'run\' populate result'
    t.test(False, m)


print('********************')
print('Testing Job.py')
print()


Test_useGenericPreprocessor_ThrowExceptionIfUsedPropertyIsNone_NoneProperty()
Test_useGenericPreprocessor_ThrowExceptionIfUsedPropertyIsNone_CorrectProperty()

Test_run_RemovesPreviousResults()
Test_run_ReturnsResultsOfRun()
Test_run_SavesResultsInResult()
