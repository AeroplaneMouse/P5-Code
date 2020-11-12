from algorithms.armada.FindRelation import FindRelation
import mocks.FStates as states

def TestFindRelation():
	if (
		FindRelation(states.A, states.B) != 'c' 
		or FindRelation(states.A, states.C) != 'f'
		or FindRelation(states.B, states.C) != 'o'
		or FindRelation(states.B, states.A) != 'X'
	):
		print("FindRelation_Tests failed")
		return
	else:
		print("FindRelation_Tests Succesful")
		

TestFindRelation()