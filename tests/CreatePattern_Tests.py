from mocks import FStates
from algorithms.armada.CreatePattern import CreatePattern
import numpy as np


def TestCreatePattern():
	A = FStates.A
	B = FStates.B
	C = FStates.C

	print('Testing generation of 1-Patterns')

	patternA = CreatePattern(None, A)
	patternB = CreatePattern(None, B)
	patternC = CreatePattern(None, C)

	testA = np.array([[None,A],[A,'=']])
	testB = np.array([[None,B],[B,'=']])
	testC = np.array([[None,C],[C,'=']])
	if np.array_equal(patternA, testA) and np.array_equal(patternB, testB) and np.array_equal(patternC, testC):
		print("    Success")

	print('Testing generation of 2-Patterns')

	patternAB = CreatePattern(patternA, B)
	patternAC = CreatePattern(patternA, C)
	patternBC = CreatePattern(patternB, C)

	testAB = np.array([[None,A,B],[A,'=','c'],[B,'*','=']])
	testAC = np.array([[None,A,C],[A,'=','f'],[C,'*','=']])
	testBC = np.array([[None,B,C],[B,'=','o'],[C,'*','=']])

	if np.array_equal(patternAB, testAB) and np.array_equal(patternAC, testAC) and np.array_equal(patternBC, testBC):
		print("    Success")

	print('Testing generation of 3-Patterns')

	patternABC = CreatePattern(patternAB, C)

	testABC = np.array([[None, A, B, C],[A, '=', 'c', 'f'],[B, '*', '=', 'o'],[C, '*', '*', '=']])
	if(np.array_equal(patternABC, testABC)):
		print("    Success")


print('********************')
print('Testing CreatePattern')
print()

TestCreatePattern()
