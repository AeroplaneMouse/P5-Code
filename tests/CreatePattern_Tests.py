import numpy as np
import testSuite as t
from mocks import FStates
from algorithms.armada.CreatePattern import CreatePattern

A = FStates.A
B = FStates.B
C = FStates.C
D = FStates.D
E = FStates.E


def Test_GenerateOnePatterns():
    patternA = CreatePattern(None, A)
    patternB = CreatePattern(None, B)
    patternC = CreatePattern(None, C)

    testA = np.array([[None, A], [A, '=']])
    testB = np.array([[None, B], [B, '=']])
    testC = np.array([[None, C], [C, '=']])

    result = (np.array_equal(patternA, testA) and np.array_equal(patternB, testB) and np.array_equal(patternC, testC))
    t.test(result, 'Generate 1-patterns')


def Test_GenerateTwoPatterns():
    patternA = CreatePattern(None, A)
    patternB = CreatePattern(None, B)

    patternAB = CreatePattern(patternA, B)
    patternAC = CreatePattern(patternA, C)
    patternBC = CreatePattern(patternB, C)

    testAB = np.array([[None, A, B], [A, '=', 'c'], [B, '*', '=']])
    testAC = np.array([[None, A, C], [A, '=', 'f'], [C, '*', '=']])
    testBC = np.array([[None, B, C], [B, '=', 'o'], [C, '*', '=']])

    result = (np.array_equal(patternAB, testAB) and np.array_equal(patternAC, testAC) and np.array_equal(patternBC, testBC))
    t.test(result, 'Generate 2-patterns')


def Test_GenerateThreePatterns():
    patternA = CreatePattern(None, A)
    patternAB = CreatePattern(patternA, B)
    patternABC = CreatePattern(patternAB, C)

    testABC = np.array([
        [None, A, B, C],
        [A, '=', 'c', 'f'],
        [B, '*', '=', 'o'],
        [C, '*', '*', '=']])

    t.test(np.array_equal(patternABC, testABC), 'Generate 3-patterns')


def Test_PandaTime():
    patternD = CreatePattern(None, D)
    patternDE = CreatePattern(patternD, E)
    testDE = np.array([[None, D, E], [D, '=', 's'], [E, '*', '=']])

    t.test(np.array_equal(patternDE, testDE), 'Pattern comparison with panda time')


print('********************')
print('Testing CreatePattern.py')
print()

Test_GenerateOnePatterns()
Test_GenerateTwoPatterns()
Test_GenerateThreePatterns()
Test_PandaTime()
