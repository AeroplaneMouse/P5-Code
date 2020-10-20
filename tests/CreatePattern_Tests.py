from mocks import FStates
from algorithms.armada.CreatePattern import CreatePattern

print('********************')
print('Testing CreatePattern')
print()

# States can be located in mocks.FStates

print('2 | Testing generation of 1-Patterns')
patternA = CreatePattern(None, FStates.A)
print(patternA)

patternB = CreatePattern(patternA, FStates.B)
print(patternB)

patternC = CreatePattern(patternB, FStates.C)
print(patternC)
