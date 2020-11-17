from algorithms.tpminer.point_pruning import point_pruning
from mocks.Mini_database import *

def test_point_pruning():
	#Test on prefix with 1 ep
	expected_return = "[A+, B-, C+, D+]"
	print(expected_return)
	print(point_pruning(cs, prfx))

	if str(point_pruning(cs, prfx)) != expected_return:
		print("point_pruning Test 1 FAILED")
		return

	print("point_pruning Test Successful")

test_point_pruning()

