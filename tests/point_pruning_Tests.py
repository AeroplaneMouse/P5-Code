from algorithms.tpminer.point_pruning import point_pruning
from mocks.Mini_database import *

def test_point_pruning():
	
	#test with prefix of length 1
	FE = {a_f, b_f, c_s, c_f, d_s, d_f}
	expected_return = {a_f, c_s, d_s}
	prfx = [a_s]

	if (
		point_pruning(FE, prfx) != expected_return
	):
		print("point_pruning Test 1 FAILED")
		return

	#Test on prefix with length 1
	FE = {a_s, a_f, b_f, c_s, c_f, d_s, d_f}
	expected_return = {a_s, a_f, c_s, c_f, d_s}
	prfx = [a_s, c_s]

	if (
		point_pruning(FE, prfx) != expected_return
	):
		print("point_pruning Test 2 FAILED")
		return

	print("All point_pruning Tests Successful")

test_point_pruning()

