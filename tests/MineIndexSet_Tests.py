import pandas as pa
import testSuite as t
from mocks import FStates
from mocks import Patterns
from mocks import IndexSets
from preprocessors import Support
from algorithms.armada import Storage
from algorithms.armada import MineIndexSet


#####################################################################
# GetFirstEndTime
def one_patternTest():
    time = MineIndexSet.GetFirstEndTime(Patterns.D)
    e_time = str(FStates.F.End)[11:]

    m = 'Test 1-pattern. Return first state end time'
    t.test(time == e_time, m)


def two_patternTest():
    time = MineIndexSet.GetFirstEndTime(Patterns.E)
    e_time = str(FStates.G.End)[11:]

    m = 'Test 2-pattern. Return second state'
    t.test(time == e_time, m)


def three_patternTest():
    time = MineIndexSet.GetFirstEndTime(Patterns.C)
    e_time = str(FStates.G.End)[11:]

    m = 'Test 3-pattern. Return second state'
    t.test(time == e_time, m)


#####################################################################
# ExtractStateNames
def Test_ExtractStateNames_ReturnExpectedLength():
    p = Patterns.A

    states = MineIndexSet.ExtractStateNames(p)
    expected_states = [FStates.D]

    m = 'Return expected length'
    t.test(len(states) == len(expected_states), m)


def Test_ExtractStateNames_ReturnExpectetStates():
    p = Patterns.C

    states = MineIndexSet.ExtractStateNames(p)
    expected_states = ['F', 'G', 'H']

    result = True
    for i in range(0, 3):
        if states[i] != expected_states[i]:
            result = False
            break
    m = 'Return list of state names'
    t.test(result, m)


print('********************')
print('Testing MineIndexSet.py')
print()

print()
print('ExtractStateNames:')
Test_ExtractStateNames_ReturnExpectedLength()
Test_ExtractStateNames_ReturnExpectetStates()

print()
print('GetFirstEndTime:')
one_patternTest()
two_patternTest()
three_patternTest()
