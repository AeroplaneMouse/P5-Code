from algorithms.tpminer.count_support import count_support
from tpmmodels.DB import DB
from mocks.Mini_database import *
from copy import copy


def test_count_support():
	pattern = [a_s, a_f]
	cs = [c_f, d_f, b_f]
	db = DB(pattern)
	db.ES =[cs, copy(cs), copy(cs), copy(cs), [c_f, a_f, b_f]]

	FE = count_support(db, 1)

	print(len(FE))

test_count_support()