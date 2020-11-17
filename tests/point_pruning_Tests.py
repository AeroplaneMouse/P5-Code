from algorithms.tpminer.point_pruning import point_pruning
from mocks.Mini_database import *

def test_point_pruning():
	#Test on prefix with 1 ep
	expected_return = "[A+, B-, C+, D+]"
	expected_return2 = "[A+, C+, D+, D-]"

	if (
		str(point_pruning(cs, prfx)) != expected_return
		or str(point_pruning(cs, prfx2)) != expected_return2
	):
		print("point_pruning Test 1 FAILED")
		return

	#Test on prefix with 2 ep's
	expected_return = "[A+, B-, C+, D+, D-]"
	expected_return2 = "[A+, B+, B-, C+, D+, D-]"
	print(cs2)
	print(point_pruning(cs2, prfx3))

	if (
		str(point_pruning(cs, prfx3)) != expected_return
		or str(point_pruning(cs2, prfx3)) != expected_return2
	):
		print("point_pruning Test 2 FAILED")
		return

	print("All point_pruning Tests Successful")

test_point_pruning()

