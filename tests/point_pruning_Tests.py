from algorithms.tpminer.point_pruning import point_pruning
from mocks.Mini_database import *

def test_point_pruning():
	#Test on prefix with 1 ep
	expected_return = {a_finish, c_start, d_start}

	print(point_pruning(cs, prfx))
	print(expected_return)

	if (
		point_pruning(cs, prfx) != expected_return
	):
		print("point_pruning Test 1 FAILED")
		return

	#Test on prefix with 2 ep's

	print("All point_pruning Tests Successful")

test_point_pruning()

