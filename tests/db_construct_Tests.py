from mocks.Mini_database import *
from algorithms.tpminer.db_construct import *

def test_db_construct():
	temp = db_construct(db, a_p)
	print(temp)

test_db_construct()
