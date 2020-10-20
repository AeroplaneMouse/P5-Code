from mocks import FStates
from algorithms.armada.CreatePattern import CreatePattern


def OnePattern():
    print('Testing generation of 1-Patterns')

    patternA = CreatePattern(None, FStates.A)
    print(patternA)

    patternB = CreatePattern(patternA, FStates.B)
    print(patternB)

    patternC = CreatePattern(patternB, FStates.C)
    print(patternC)


print('********************')
print('Testing CreatePattern')
print()

OnePattern()
