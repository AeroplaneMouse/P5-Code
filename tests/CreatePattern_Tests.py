import pandas as pa
from models.FState import FState
from algorithms.armada.CreatePattern import CreatePattern


def GenerateStates():
    states = []

    states.append(FState(
        'A',
        pa.to_datetime('2013-07-01 04:01:14'),
        pa.to_datetime('2013-07-01 13:08:17')))

    states.append(FState(
        'B',
        pa.to_datetime('2013-07-01 04:01:14'),
        pa.to_datetime('2013-07-01 14:57:17')))

    return states

print('********************')
print('Testing CreatePattern')
print()


print('1 | Generating states')
states = GenerateStates()


print('2 | Testing generation of 1-Patterns')
patternA = CreatePattern(None, states[0])


print(states)
