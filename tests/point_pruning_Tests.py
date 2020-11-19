from algorithms.tpminer.point_pruning import point_pruning
from mocks.Mini_database import *

def test_point_pruning():
	
	#test with prefix of length 1
	FE = {a_finish, b_finish, c_start, c_finish, d_start, d_finish}
	expected_return = {a_finish, c_start, d_start}
	prfx = [a_start]

	if (
		point_pruning(FE, prfx) != expected_return
	):
		print("point_pruning Test 1 FAILED")
		return

	#Test on prefix with length 1
	FE = {a_start, a_finish, b_finish, c_start, c_finish, d_start, d_finish}
	expected_return = {a_start, a_finish, c_start, c_finish, d_start}
	prfx = [a_start, c_start]

	if (
		point_pruning(FE, prfx) != expected_return
	):
		print("point_pruning Test 2 FAILED")
		return

	print("All point_pruning Tests Successful")

test_point_pruning()

