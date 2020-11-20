from mocks.Mini_database import *
from algorithms.tpminer.db_construct import db_construct

def test_db_construct():
	#tests with 3 equivalent cs's
	cs = [a_s, c_s, a_f, c_f, d_s, d_f]
	cs2 = [a_s, c_s, a_f, c_f, d_s, d_f]
	cs3 = [a_s, c_s, a_f, c_f, d_s, d_f]
	cs_list = [cs, cs2, cs3]
		#one-pattern
	prfx = [a_s]
	db = DB(prfx)
	db.ES = cs_list
	result = db_construct(db, prfx).ES
	expected_result = [[c_s, a_f, d_s],[c_s, a_f, d_s],[c_s, a_f, d_s]]

	if result != expected_result:
		print("construct_db Test #1 FAILED")
		return

		#two-pattern of corresponding ep's
	prfx = [a_s, a_f]
	result = db_construct(db, prfx).ES
	expected_result = [[d_s],[d_s],[d_s]]

	if result != expected_result:
		print("construct_db Test #2 FAILED")
		return

	print("construct_db tests successful")

	

test_db_construct()
