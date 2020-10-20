import pandas as pa
from models.FState import FState
from algorithms.armada.CreatePattern import CreatePattern


def GenerateStates():
    states = []

    states.append(FState(
        'A',
        7,
        22))

    states.append(FState(
        'B',
        8,
        15))
    states.append(FState(
        'C',
        10,
        22))

    return states

print('********************')
print('Testing CreatePattern')
print()


print('1 | Generating states')
states = GenerateStates()


print('2 | Testing generation of 1-Patterns')
patternA = CreatePattern(None, states[0])
print(patternA)
patternB = CreatePattern(patternA, states[1])
print(patternB)
patternC = CreatePattern(patternB, states[2])
print(patternC)

