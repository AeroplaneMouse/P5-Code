import pandas as pa
import testSuite as t
from mocks import FStates
from mocks import Patterns
from mocks import IndexSets
from preprocessors import Support
from algorithms.armada import Storage
from algorithms.armada import MineIndexSet


#####################################################################
# Setup

#####################################################################
# Tests

def Test_ExtractStateName_ReturnExpectedLength():
    p = Patterns.A

    states = MineIndexSet.ExtractStateNames(p)
    expected_states = [FStates.D]

    m = 'ExtractStateName: Return expected length'
    t.test(len(states) == len(expected_states), m)


def Test_ExtractStateName_ReturnExpectetStates():
    p = Patterns.C

    states = MineIndexSet.ExtractStateNames(p)
    expected_states = ['F', 'G', 'H']

    result = True
    for i in range(0, 3):
        if states[i] != expected_states[i]:
            result = False
            break
    m = 'ExtractStateName: Return list of state names'
    t.test(result, m)


print('********************')
print('Testing ComputePotentialStems')
print()


# Test_ComputePotentialStems()
Test_ExtractStateName_ReturnExpectedLength()
Test_ExtractStateName_ReturnExpectetStates()
