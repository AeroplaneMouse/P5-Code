from algorithms.armada.MineIndexSet import GetFirstEndTime
from mocks import Patterns
from mocks import FStates
import testSuite as t


def one_patternTest():
    time = GetFirstEndTime(Patterns.D)
    m = 'Test 1-pattern. Return first state end time'
    t.test(time == FStates.F.End, m)


def two_patternTest():
    time = GetFirstEndTime(Patterns.E)
    m = 'Test 2-pattern. Return second state'
    t.test(time == FStates.G.End, m)


def three_patternTest():
    time = GetFirstEndTime(Patterns.C)
    m = 'Test 3-pattern. Return second state'
    t.test(time == FStates.G.End, m)


print('********************')
print('Testing GetFirstEndTime')
print()

one_patternTest()
two_patternTest()
three_patternTest()
