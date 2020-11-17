from mocks.Mini_database import *
from algorithms.tpminer.db_construct import db_construct

def test_db_construct():
	temp = db_construct(db, a_p)
	print(temp.ES)

test_db_construct()
